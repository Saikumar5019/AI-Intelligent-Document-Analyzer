CLASSIFY_PROMPT = """
Classify the document.

Categories:

1. Invoice
2. Contract
3. Resume
4. Medical Report
5. Bank Statement
6. Others

Document:

{text}

Return only category.
"""