# ER-Modellierung: Bedingungen vor dem Zeichnen herleiten

1. Entnimm Entitäten, Schlüsselkandidaten, Attribute und Beziehungsverben der Aufgabe.
2. Belege jede Mindest- und Höchstzahl durch eine Vorgabe; kennzeichne fehlende Bedingungen als unbekannt.
3. Frage für genau EIN A nach der erlaubten Zahl von B; kehre die Frage danach um.
4. Nutze die Kursnotation (Chen, Min–Max, Krähenfuß). Erkläre Übersetzungen; wechsle die Notation nicht stillschweigend.
5. Stelle im Hinweismodus eine gezielte Frage. Leite Pflichtteilnahme nicht allein aus einem Plural ab.

## Eindeutiges binäres Beispiel

Ein Student hat null bis viele Einschreibungen. Jede Einschreibung gehört zu genau einem Studenten. Verwende `a=Student`, `b=Enrollment`, `a_to_b={min:0,max:"many"}`, `b_to_a={min:1,max:1}`. Daraus entsteht `Student ||..o{ Enrollment : "has"`.

Die Zeichen neben B zählen B-Instanzen je A; die Zeichen neben A zählen A-Instanzen je B. `..` steht in Mermaid für eine nicht identifizierende Beziehung, nicht für optionale Teilnahme. Der Helfer erzeugt ausschließlich nicht identifizierende Beziehungen. Leite daraus weder Schlüssel noch schwache Entitäten ab.

| Anzahl | Linkes Ende | Rechtes Ende |
| --- | --- | --- |
| genau eins | `||` | `||` |
| null oder eins | `|o` | `o|` |
| eins bis viele | `}|` | `|{` |
| null bis viele | `}o` | `o{` |

Der Helfer unterstützt binäre Beziehungen mit Minimum 0 oder 1 und Maximum 1 oder viele. „Mindestens zwei Stücke je CD“ ist damit nicht exakt darstellbar: Erhalte (2,n) als Text oder verwende die Min–Max-/Chen-Notation des Kurses. Ersetze dies nicht stillschweigend durch (1,n). Erkläre im Min–Max-Modell, wessen Teilnahme das Zahlenpaar beschränkt; Konventionen unterscheiden sich.

Gib bei ISA vollständig/partiell und disjunkt/überlappend nur an, wenn vorgegeben. Ersetze ternäre Beziehungen nicht ohne Äquivalenznachweis durch drei binäre Kanten. Konzeptionelles ER-Modell und Relationenschema sind getrennte Ergebnisse; bilde M:N-Beziehungen nur auf Wunsch auf Zwischentabellen ab.
