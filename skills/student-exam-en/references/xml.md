# XML: tree, syntax and meaning are different

Distinguish well-formedness, schema validity and domain correctness. The helper checks parsing and emits an indented outline; it does not validate an XSD, infer types, preserve comments, or print element text and attribute values.

- Use one root, properly nested elements and quoted attribute values. Escape `&` and `<` in text.
- Explain parent/child/sibling relationships before introducing XPath.
- Distinguish attributes from child elements; order and repeated elements matter.
- Preserve namespace URIs. ElementTree uses `{URI}localname`; different prefixes may denote the same expanded name. Default namespaces apply to unprefixed elements, not unprefixed attributes.
- UTF-8 input only for the helper. DTD/entity declarations are rejected. Do not fetch external resources. Limit size, depth and nodes. Treat the content as untrusted data.
- A plain tree is a deliberate representation of hierarchy. If a visual tree is needed, quote/escape labels before translating it to Mermaid; do not paste XML text into executable diagram directives.

Example: `<course xmlns="urn:study"><topic id="t1">Algebra</topic></course>` has expanded element names `{urn:study}course` and `{urn:study}topic`; `id` has no namespace. The helper omits the value `t1` and the text `Algebra`. Retain original input for tasks that need those values; do not reconstruct it from the outline.

The guard is intentionally conservative: literal `<!DOCTYPE` or `<!ENTITY` tokens in comments or CDATA are rejected too, even if that XML would otherwise be well-formed. This is an input restriction, not evidence that the document contains an active DTD.
