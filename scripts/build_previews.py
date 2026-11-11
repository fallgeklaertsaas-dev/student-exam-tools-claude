"""Build honest GitHub previews from bundled examples (optional Pillow/Matplotlib/Inkscape/Graphviz).

These dependencies are for maintainers generating documentation images only.
They are not required for the installed skills or offline study helpers.
"""
from pathlib import Path
import shutil
import subprocess
import tempfile
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/images'
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
INK = '#16213a'
MUTED = '#51617a'
ACCENT = '#087f8c'


def font(size, bold=False, mono=False):
    name = 'DejaVuSansMono.ttf' if mono else ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')
    try:
        return ImageFont.truetype(str(FONT_DIR / name), size)
    except OSError:
        return ImageFont.truetype(name, size)


def fit(image, box):
    image = image.convert('RGB')
    image.thumbnail(box, Image.Resampling.LANCZOS)
    return image


def er_preview(lang, folder):
    # Same example relationships as enrollment.json; not a screenshot of Claude.
    words = ('Student', 'Enrollment', 'Course', 'has', 'receives') if lang == 'en' else (
        'Student', 'Einschreibung', 'Kurs', 'hat', 'erhält')
    student, enrollment, course, has, receives = words
    dot = f'''graph Study {{
      graph [bgcolor="white", rankdir=LR, pad=0.5, nodesep=1.0, ranksep=1.1, splines=polyline, dpi=180];
      node [shape=box, style="rounded,filled", fillcolor="#f1f6fc", color="#245ca6", fontname="DejaVu Sans", fontsize=18, margin="0.22,0.18"];
      edge [color="#51617a", fontname="DejaVu Sans", fontsize=13, labelfontsize=14, labeldistance=2.3, labelangle=25];
      Student [label="{student}"];
      Enrollment [label="{enrollment}"];
      Course [label="{course}"];
      {{rank=same; Student; Course;}}
      Student -- Enrollment [label="{has}", taillabel="1", headlabel="0..n"];
      Course -- Enrollment [label="{receives}", taillabel="1", headlabel="0..n"];
    }}'''
    dotfile = folder / f'er-{lang}.dot'
    dotfile.write_text(dot, encoding='utf-8')
    raw = folder / f'er-{lang}.png'
    subprocess.run(['dot', '-Tpng', str(dotfile), '-o', str(raw)], check=True)
    canvas = Image.new('RGB', (1200, 720), 'white')
    d = ImageDraw.Draw(canvas)
    d.text((44,32), 'ER: enrollment' if lang == 'en' else 'ER: Einschreibung', font=font(32,True), fill=INK)
    label = ('Explicit example assumptions • endpoint counts' if lang == 'en' else
             'Ausdrückliche Beispielannahmen • Anzahl am Beziehungsende')
    d.text((44,85),label,font=font(21),fill=MUTED)
    diagram = fit(Image.open(raw),(1110,420))
    canvas.paste(diagram,((1200-diagram.width)//2,138+(420-diagram.height)//2))
    notes = (['One enrollment belongs to exactly one student and one course.',
              'One student or course may have zero or many enrollments.',
              'Preview from example JSON. The tool exports Mermaid source.'] if lang == 'en' else
             ['Eine Einschreibung gehört genau einem Studenten und einem Kurs.',
              'Ein Student oder Kurs hat null bis viele Einschreibungen.',
              'Vorschau aus Beispiel-JSON. Das Werkzeug erzeugt Mermaid-Quelltext.'])
    for i,line in enumerate(notes):
        d.text((44,580+i*37),line,font=font(23 if i<2 else 20),fill=INK if i<2 else MUTED)
    canvas.save(OUT/f'er-{lang}.png',optimize=True)


def xml_preview(lang):
    canvas = Image.new('RGB',(1200,700),'white')
    d=ImageDraw.Draw(canvas)
    d.text((44,32),'XML: inspect the hierarchy' if lang=='en' else 'XML: Hierarchie verstehen',font=font(32,True),fill=INK)
    d.text((44,88),'Namespace-aware outline' if lang=='en' else 'Strukturbaum mit Namensräumen',font=font(23),fill=MUTED)
    content=(ROOT/f'examples/xml-{lang}.md').read_text().split('```text\n')[1].split('```')[0].strip('\n')
    d.rounded_rectangle((38,145,1162,545),radius=16,fill='#f4f7fb',outline='#dce3ed')
    for i,line in enumerate(content.splitlines()):
        d.text((68,175+i*42),line,font=font(21,mono=True),fill=INK)
    lines=(['Original tool output. Element text and attribute values are omitted.',
            'Well-formedness and XSD validity are different checks.'] if lang=='en' else
           ['Originalausgabe. Elementtexte und Attributwerte werden ausgelassen.',
            'Wohlgeformtheit und XSD-Gültigkeit sind unterschiedliche Prüfungen.'])
    for i,line in enumerate(lines):
        d.text((44,584+i*40),line,font=font(22),fill=MUTED)
    canvas.save(OUT/f'xml-{lang}.png',optimize=True)


def latex_preview(lang):
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    fig=Figure(figsize=(12,7),dpi=100,facecolor='white')
    FigureCanvasAgg(fig)
    fig.text(.04,.90,'Formula preview' if lang=='en' else 'Formelvorschau',fontsize=24,weight='bold',color=INK)
    formulas=[r'$\frac{3}{4}+\frac{1}{6}=\frac{9}{12}+\frac{2}{12}=\frac{11}{12}$',
              r'$x^2-4x+3=(x-1)(x-3)=(x-2)^2-1$',
              r'$z_k=2e^{i(\pi/6+2\pi k/3)},\quad k=0,1,2$']
    for y,formula in zip((.68,.47,.26),formulas):
        fig.text(.06,y,formula,fontsize=27,color=INK)
    fig.text(.04,.09,'Matplotlib MathText rendering; separate LaTeX worksheet sources included.' if lang=='en' else
             'Mit Matplotlib MathText gerendert; separate LaTeX-Arbeitsblattquellen enthalten.',fontsize=14,color=MUTED)
    fig.savefig(OUT/f'latex-{lang}.png',facecolor='white')


def overview(lang):
    canvas=Image.new('RGB',(1600,1120),'#f0f4f9')
    d=ImageDraw.Draw(canvas)
    d.rectangle((0,0,1600,260),fill='#111e36')
    d.text((64,42),'STUDENT EXAM TOOLS',font=font(48,True),fill='white')
    d.text((66,113),'for Claude  /  für Claude',font=font(26),fill='#9ee5e3')
    d.text((66,171),'Student-led. Built for learners.' if lang=='en' else
           'Studentisch entwickelt. Gemeinsam besser lernen.',font=font(29),fill='#e0e9f5')
    d.text((66,220),'EN + DE   •   Python   •   LaTeX   •   Mermaid   •   SVG',font=font(20),fill='#b8cbe5')
    names=[('fraction','Equal parts' if lang=='en' else 'Gleiche Teile'),
           ('quadratic','Functions' if lang=='en' else 'Funktionen'),
           ('complex','Complex plane' if lang=='en' else 'Komplexe Ebene'),
           ('er','ER relationships' if lang=='en' else 'ER-Beziehungen'),
           ('xml','XML hierarchy' if lang=='en' else 'XML-Hierarchie'),
           ('latex','Readable formulas' if lang=='en' else 'Lesbare Formeln')]
    for index,(stem,title) in enumerate(names):
        x=50+(index%3)*510; y=288+(index//3)*375
        d.rounded_rectangle((x,y,x+480,y+345),radius=18,fill='white',outline='#dce3ed',width=2)
        d.text((x+22,y+18),title,font=font(24,True),fill=INK)
        photo=fit(Image.open(OUT/f'{stem}-{lang}.png'),(444,265))
        canvas.paste(photo,(x+(480-photo.width)//2,y+65+(265-photo.height)//2))
    d.text((52,1052),'Real example outputs; ER preview drawn from the example model.' if lang=='en' else
           'Echte Beispielausgaben; ER-Vorschau aus dem Beispielmodell.',font=font(20),fill=MUTED)
    d.text((52,1083),'Independent community project • Not an Anthropic product' if lang=='en' else
           'Unabhängiges Community-Projekt • Kein Anthropic-Produkt',font=font(18),fill=MUTED)
    canvas.save(OUT/f'overview-{lang}.png',optimize=True)


def main():
    for binary in ('inkscape','dot'):
        if not shutil.which(binary):
            raise SystemExit(f'Optional preview dependency missing: {binary}')
    OUT.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        folder=Path(temporary)
        for lang in ('en','de'):
            for stem in ('fraction','quadratic','complex'):
                subprocess.run(['inkscape',str(ROOT/f'examples/{stem}-{lang}.svg'),
                                '--export-type=png',f'--export-filename={OUT/f"{stem}-{lang}.png"}',
                                '--export-width=1200'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
            er_preview(lang,folder)
            xml_preview(lang)
            latex_preview(lang)
            overview(lang)
    print('Built 14 bilingual PNG previews from repository examples.')


if __name__=='__main__':
    main()
