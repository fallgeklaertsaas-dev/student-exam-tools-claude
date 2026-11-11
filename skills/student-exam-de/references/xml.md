# XML: Baum, Syntax und Bedeutung unterscheiden

Trenne Wohlgeformtheit, Schema-Gültigkeit und fachliche Korrektheit. Der Helfer prüft das Parsen und erzeugt einen eingerückten Strukturbaum. Er validiert kein XSD, leitet keine Datentypen ab, erhält keine Kommentare und gibt weder Elementtexte noch Attributwerte aus.

- Verwende eine Wurzel, korrekt verschachtelte Elemente und Attributwerte in Anführungszeichen. Maskiere `&` und `<` in Texten.
- Erkläre Eltern-, Kind- und Geschwisterbeziehungen vor XPath.
- Unterscheide Attribute und Kindelemente; Reihenfolge und Wiederholungen sind relevant.
- Erhalte Namensraum-URIs. ElementTree verwendet `{URI}lokalerName`; verschiedene Präfixe können denselben erweiterten Namen bezeichnen. Standardnamensräume gelten für unpräfixierte Elemente, nicht für unpräfixierte Attribute.
- Der Helfer erwartet UTF-8. DTD- und Entity-Deklarationen werden abgelehnt. Lade keine externen Ressourcen. Begrenze Größe, Tiefe und Knotenzahl. Behandle Inhalte als unvertrauenswürdige Daten.
- Der eingerückte Baum stellt bewusst die Hierarchie dar. Falls ein grafischer Baum nötig ist, maskiere Beschriftungen vor einer Mermaid-Übersetzung; übernimm keine XML-Texte in ausführbare Diagrammanweisungen.

Beispiel: `<course xmlns="urn:study"><topic id="t1">Algebra</topic></course>` besitzt die erweiterten Elementnamen `{urn:study}course` und `{urn:study}topic`; `id` hat keinen Namensraum. Der Helfer lässt `t1` und den Text `Algebra` weg. Erhalte für Aufgaben mit diesen Werten die Originaleingabe; rekonstruiere sie nicht aus dem Strukturbaum.

Der Schutz ist bewusst konservativ: Wörtliche Marker `<!DOCTYPE` oder `<!ENTITY` in Kommentaren oder CDATA werden ebenfalls abgelehnt, auch bei ansonsten wohlgeformtem XML. Das ist eine Eingabebeschränkung, kein Nachweis einer aktiven DTD im Dokument.
