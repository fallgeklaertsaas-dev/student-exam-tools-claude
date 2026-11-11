from fractions import Fraction
import copy
import io
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from contextlib import redirect_stderr, redirect_stdout

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from student_exam_tools.toolkit import (MAX_INPUT, cardinality, complex_roots, complex_svg, er_mermaid, fraction_svg,
                                      main, quadratic_analysis, quadratic_svg, read_text, xml_outline)


def model(ab=(0, "many"), ba=(1, 1)):
    return {"entities": ["Student", "Enrollment"], "relationships": [{
        "a": "Student", "b": "Enrollment", "label": "has",
        "a_to_b": dict(zip(("min", "max"), ab)), "b_to_a": dict(zip(("min", "max"), ba))}]}


class Fractions(unittest.TestCase):
    def test_shading_matches_numerator(self):
        ns = {"s": "http://www.w3.org/2000/svg"}
        for n, d in [(0, 4), (3, 4), (11, 12), (7, 4), (120, 24)]:
            root = ET.fromstring(fraction_svg(n, d))
            shaded = [x for x in root.findall(".//s:rect", ns) if x.attrib.get("fill") == "#245ca6"]
            self.assertEqual(len(shaded), n)
            self.assertIn(str(Fraction(n, d)), fraction_svg(n, d))

    def test_equal_width_parts(self):
        root = ET.fromstring(fraction_svg(7, 4))
        widths = [x.attrib["width"] for x in root.iter() if x.attrib.get("stroke") == "#172b4d"]
        self.assertEqual(set(widths), {"165.000"})
        self.assertEqual(len(widths), 8)

    def test_reject_invalid(self):
        for n, d in [(1, 0), (-1, 4), (1, 25), (6, 1), (True, 2), (1.5, 2)]:
            with self.subTest(n=n, d=d), self.assertRaises(ValueError):
                fraction_svg(n, d)

    def test_accessible_localized_svg(self):
        for lang, title in [("en", "Fraction model"), ("de", "Bruchmodell")]:
            content = fraction_svg(3, 4, lang)
            self.assertIn(title, content)
            self.assertIn('aria-labelledby="title desc"', content)
            ET.fromstring(content)


class Quadratics(unittest.TestCase):
    def test_exact_known_case(self):
        result = quadratic_analysis(1, -4, 3)
        self.assertEqual(result["real_roots"], [1.0, 3.0])
        self.assertEqual(result["vertex"], [2.0, -1.0])

    def test_double_root(self):
        self.assertEqual(quadratic_analysis(1, -2, 1)["real_roots"], [1.0])

    def test_decimal_double_root(self):
        result = quadratic_analysis(0.1, 0.6, 0.9)
        self.assertEqual(result['discriminant'], 0)
        self.assertEqual(result['real_roots'], [-3.0])
        self.assertEqual(result['vertex'], [-3.0, 0.0])

    def test_underflow_rejected_not_false_double_root(self):
        with self.assertRaises(ValueError):
            quadratic_analysis(1, 1e-308, 0)

    def test_no_real_root(self):
        self.assertEqual(quadratic_analysis(1, 0, 1)["real_roots"], [])

    def test_zero_constant(self):
        self.assertEqual(quadratic_analysis(1, 0, 0)["real_roots"], [0.0])
        self.assertEqual(quadratic_analysis(-1, 2, 0)["real_roots"], [0.0, 2.0])

    def test_reject_bad_coefficients(self):
        for a, b, c in [(0, 1, 2), (1e-10, 0, 0), (1, float('nan'), 0), (1, 0, float('inf')), (1e7, 0, 0)]:
            with self.subTest(a=a, b=b, c=c), self.assertRaises(ValueError):
                quadratic_analysis(a, b, c)

    def test_random_root_residual_and_vieta(self):
        rng = random.Random(17)
        for _ in range(150):
            a = rng.choice([-3, -1, 1, 2, 4])
            r1, r2 = rng.uniform(-8, 8), rng.uniform(-8, 8)
            b, c = -a * (r1 + r2), a * r1 * r2
            result = quadratic_analysis(a, b, c)
            self.assertEqual(len(result['real_roots']), 2)
            for r in result['real_roots']:
                self.assertAlmostEqual((a * r + b) * r + c, 0, places=8)
            self.assertAlmostEqual(sum(result['real_roots']), -b / a, places=8)
            self.assertAlmostEqual(math.prod(result['real_roots']), c / a, places=8)

    def test_stable_small_root(self):
        result = quadratic_analysis(1, 1e6, 1)
        self.assertAlmostEqual(result['real_roots'][1], -1e-6, places=15)

    def test_svg_valid_and_localized(self):
        for lang in ("en", "de"):
            result = quadratic_svg(1, -4, 3, -2, 6, lang)
            ET.fromstring(result)
            self.assertNotIn('nan', result.lower())
            self.assertIn('polyline', result)

    def test_invalid_window(self):
        for low, high in [(1, 1), (2, 1), (0, float('inf')), (0, 1e-8), (-1e7, 2)]:
            with self.subTest(low=low, high=high), self.assertRaises(ValueError):
                quadratic_svg(1, 0, 0, low, high)


class ComplexRoots(unittest.TestCase):
    def test_cubes(self):
        result = complex_roots(0, 8, 3)
        self.assertEqual(len(result['roots']), 3)
        for x,y in result['roots']:
            self.assertLess(abs(complex(x,y)**3-8j), 1e-12)

    def test_degrees_and_residuals(self):
        for degree in range(1,13):
            result = complex_roots(-3, 4, degree)
            self.assertEqual(len(result['roots']), degree)
            for x,y in result['roots']:
                self.assertLess(abs(complex(x,y)**degree-complex(-3,4)), 1e-10)

    def test_zero_multiplicity(self):
        result = complex_roots(0,0,3)
        self.assertEqual(result['roots'], [[0.,0.]])
        self.assertEqual(result['multiplicity_if_zero'], 3)

    def test_small_roots_use_readable_scale(self):
        ns = {'s':'http://www.w3.org/2000/svg'}
        source = ET.fromstring(complex_svg(.000001,0,2))
        roots = [e for e in source.findall('.//s:circle',ns) if e.attrib.get('r') == '5']
        self.assertEqual(len(roots),2)
        self.assertGreater(abs(float(roots[0].attrib['cx'])-float(roots[1].attrib['cx'])),200)

    def test_bad_inputs(self):
        for real,imag,degree in [(0,8,0),(0,8,13),(float('inf'),0,3),(0,1e7,3),(0,8,True)]:
            with self.assertRaises(ValueError):
                complex_roots(real,imag,degree)

    def test_localized_valid_svg(self):
        for lang in ('en','de'):
            source = complex_svg(0,8,3,lang)
            ET.fromstring(source)
            self.assertIn('Re',source)
            self.assertIn('Im',source)

    def test_cli(self):
        with redirect_stdout(io.StringIO()) as out:
            self.assertEqual(main(['complex-roots','0','8','3','--analysis']),0)
        self.assertEqual(len(json.loads(out.getvalue())['roots']),3)


class ER(unittest.TestCase):
    def test_directional_contract(self):
        self.assertIn('Student ||..o{ Enrollment : "has"', er_mermaid(model()))

    def test_all_sixteen_endpoint_combinations(self):
        counts = [(0, 1), (1, 1), (0, "many"), (1, "many")]
        left = ["|o", "||", "}o", "}|"]
        right = ["o|", "||", "o{", "|{"]
        for i, ab in enumerate(counts):
            for j, ba in enumerate(counts):
                self.assertIn(f'Student {left[j]}..{right[i]} Enrollment', er_mermaid(model(ab, ba)))

    def test_no_invention_for_minimum_two(self):
        with self.assertRaises(ValueError):
            er_mermaid(model((2, "many")))

    def test_unknown_entity(self):
        item = model()
        item['relationships'][0]['b'] = 'Missing'
        with self.assertRaises(ValueError):
            er_mermaid(item)

    def test_duplicate_entity(self):
        item = model()
        item['entities'].append('Student')
        with self.assertRaises(ValueError):
            er_mermaid(item)

    def test_reject_diagram_injection(self):
        for label in ['x"\nclick Student "https://example.com"', '<script>', '%%{init: {}}%%']:
            item = model()
            item['relationships'][0]['label'] = label
            with self.assertRaises(ValueError):
                er_mermaid(item)

    def test_reserved_mermaid_identifiers(self):
        for name in ('erDiagram', 'ERDIAGRAM', 'direction', 'classDef'):
            with self.assertRaises(ValueError):
                er_mermaid({'entities':[name],'relationships':[]})

    def test_directive_like_label(self):
        for label in ('direction LR', 'indirection LR', 'direction LRate'):
            item = model()
            item['relationships'][0]['label'] = label
            with self.assertRaises(ValueError):
                er_mermaid(item)

    def test_unicode_plain_label(self):
        item = model()
        item['relationships'][0]['label'] = 'besitzt Einschreibungen'
        self.assertIn('besitzt Einschreibungen', er_mermaid(item))

    def test_bad_shapes(self):
        for item in [None, [], {}, {"entities": "x", "relationships": []},
                     {"entities": ["A"], "relationships": {}}, {"entities": ["A B"], "relationships": []}]:
            with self.subTest(item=item), self.assertRaises(ValueError):
                er_mermaid(item)

    def test_bad_cardinalities(self):
        for value in [None, [], {"min": True, "max": 1}, {"min": 0, "max": True},
                      {"min": 0, "max": 1.0}, {"min": 0, "max": []}, {"min": -1, "max": "many"}, {"min": 0, "max": 2}]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                cardinality(value)

    def test_valid_empty_relationships(self):
        self.assertEqual(er_mermaid({"entities": ["A"], "relationships": []}), 'erDiagram\n    A\n')


class XML(unittest.TestCase):
    def test_namespaces_and_attributes(self):
        output = xml_outline('<course xmlns="urn:study"><topic id="t1">Algebra</topic></course>')
        self.assertIn('{urn:study}course', output)
        self.assertIn('  {urn:study}topic [@id]', output)
        self.assertNotIn('t1', output)
        self.assertNotIn('Algebra', output)

    def test_malformed(self):
        with self.assertRaises(ET.ParseError):
            xml_outline('<a><b></a>')

    def test_dtd_and_entities_rejected(self):
        for text in ['<!DOCTYPE a SYSTEM "file:///etc/passwd"><a/>',
                     '<!DOCTYPE a [<!ENTITY x "hello">]><a>&x;</a>']:
            with self.assertRaises(ValueError):
                xml_outline(text)

    def test_conservative_declaration_tokens_in_cdata(self):
        for text in ['<a><![CDATA[<!DOCTYPE test>]]></a>', '<!-- <!DOCTYPE test> --><a/>']:
            with self.assertRaises(ValueError):
                xml_outline(text)

    def test_depth_limit(self):
        with self.assertRaises(ValueError):
            xml_outline('<a>' * 33 + '</a>' * 33)

    def test_node_limit(self):
        with self.assertRaises(ValueError):
            xml_outline('<a>' + '<b/>' * 2001 + '</a>')

    def test_size_limit(self):
        with self.assertRaises(ValueError):
            xml_outline('<a>' + 'x' * MAX_INPUT + '</a>')

    def test_localized(self):
        self.assertIn('XML-Struktur', xml_outline('<a/>', 'de'))


class CLI(unittest.TestCase):
    def test_stdout_svg(self):
        output = io.StringIO()
        with redirect_stdout(output):
            code = main(['fraction', '3', '4', '--lang', 'de'])
        self.assertEqual(code, 0)
        ET.fromstring(output.getvalue())

    def test_existing_file_protected(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'student.svg'
            target.write_text('original')
            with redirect_stderr(io.StringIO()):
                code = main(['fraction', '3', '4', '--output', str(target)])
            self.assertEqual(code, 2)
            self.assertEqual(target.read_text(), 'original')

    def test_bad_input_exit(self):
        with redirect_stderr(io.StringIO()) as output:
            self.assertEqual(main(['fraction', '1', '0', '--lang', 'de']), 2)
        self.assertIn('Fehler', output.getvalue())

    def test_er_and_xml_paths_with_spaces(self):
        with tempfile.TemporaryDirectory() as folder:
            for command, content in [('er', json.dumps(model())), ('xml', '<a><b/></a>')]:
                target = Path(folder) / 'input file.txt'
                target.write_text(content)
                with redirect_stdout(io.StringIO()) as output:
                    code = main([command, str(target)])
                self.assertEqual(code, 0)
                self.assertTrue(output.getvalue())

    def test_negative_scientific_literals(self):
        for arguments in [
            ['quadratic','1','-1e-5','-1','--analysis'],
            ['quadratic','1','0','-1','--xmin','-1e3'],
            ['complex-roots','-1e-5','8','3','--analysis']
        ]:
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(main(arguments),0)
            self.assertTrue(output.getvalue())

    def test_missing_file(self):
        with redirect_stderr(io.StringIO()):
            self.assertEqual(main(['xml', '/no/such/file.xml']), 2)

    def test_file_size_bound(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'large.xml'
            target.write_bytes(b'x' * (MAX_INPUT + 1))
            with self.assertRaises(ValueError):
                read_text(str(target))

    def test_standalone_bundle_without_repo(self):
        with tempfile.TemporaryDirectory() as folder:
            for locale in ('en', 'de'):
                script = ROOT / f'skills/student-exam-{locale}/scripts/study_tools.py'
                result = subprocess.run([sys.executable, str(script), 'fraction', '3', '4', '--lang', locale],
                                        cwd=folder, capture_output=True, text=True, check=True)
                ET.fromstring(result.stdout)


class MathFixtures(unittest.TestCase):
    def test_complex_roots_by_original_equation(self):
        roots = [complex(math.sqrt(3), 1), complex(-math.sqrt(3), 1), complex(0, -2)]
        self.assertEqual(len(set(roots)), 3)
        for root in roots:
            self.assertLess(abs(root ** 3 - 8j), 1e-12)

    def test_half_plane_against_distances(self):
        for x in range(-5, 6):
            for y in range(-5, 6):
                z = complex(x, y)
                self.assertEqual(abs(z - 1j) < abs(z + 1), y > -x)

    def test_matrix_eigenpairs(self):
        for eigenvalue, vector in [(3, (1, 1)), (1, (1, -1))]:
            x, y = vector
            self.assertEqual((2*x+y, x+2*y), (eigenvalue*x, eigenvalue*y))

    def test_fraction_sum(self):
        self.assertEqual(Fraction(3, 4) + Fraction(1, 6), Fraction(11, 12))


if __name__ == '__main__':
    unittest.main()
