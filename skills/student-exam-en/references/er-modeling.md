# ER modeling: derive constraints before drawing

1. Extract entities, candidate keys, attributes and relationship verbs from the supplied task.
2. Quote or paraphrase the supporting requirement for every minimum/maximum; label unstated constraints as unknown.
3. For ONE A ask how many B instances are allowed; then reverse the question.
4. Select the notation used in the course (Chen, min–max, crow's foot). Explain a translation; do not silently change notation.
5. Ask one targeted question in hint mode. Never infer mandatory participation merely from a plural noun.

## Precise binary example

One student has zero or many enrollments. Each enrollment belongs to exactly one student. Use `a=Student`, `b=Enrollment`, `a_to_b={min:0,max:"many"}`, `b_to_a={min:1,max:1}`. This produces `Student ||..o{ Enrollment : "has"`.

The symbols beside B count B instances per A; the symbols beside A count A instances per B. `..` denotes non-identifying relationships in Mermaid, not optional participation. The helper deliberately emits only non-identifying relationships. Do not infer keys or weak entities from this line.

| Count | Left endpoint | Right endpoint |
| --- | --- | --- |
| exactly one | `||` | `||` |
| zero or one | `|o` | `o|` |
| one or many | `}|` | `|{` |
| zero or many | `}o` | `o{` |

The helper supports binary relationships with minima 0 or 1 and maxima 1 or many. A requirement such as “at least two tracks per CD” cannot be expressed exactly with these symbols: preserve (2,n) as text or use the course's min–max/Chen notation. Do not silently reduce it to (1,n). In a min–max model, explain which entity's participation a pair constrains; notation conventions differ.

For ISA, state total/partial and disjoint/overlapping only if given. For ternary relationships, do not replace them with three binary edges without proving equivalence. Conceptual ER and relational schemas are separate artifacts; map M:N relationships to junction tables only when requested.
