import aspose.words as aw

# Create a new empty document A
docA = aw.Document()

# Inisialize a DocumentBuilder
builder = aw.DocumentBuilder(docA)

# Insert text to the document A start
builder.move_to_document_start()
builder.write("First Hello World paragraph")

# Open an existing document B
docB = aw.Document(f"D:\doc-docx\out.docx")

# Add document B to the and of document A, preserving document B formatting
docA.append_document(docB, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)

# Save the output as PDF
docA.save(f"D:\doc-docx\output_AB.pdf")