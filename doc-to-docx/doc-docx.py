import aspose.words as aw

# # Create and save a simple document
# doc = aw.Document()
# builder = aw.DocumentBuilder(doc)
# builder.writeln("Hello Aspose.Words for Python via .NET")
#
# doc.save(f"D:\doc-docx\out.docx")


import aspose.words as aw


inp_name = input('Input name of file w/o ext. =')
doc = aw.Document(f"D:\doc-docx\{inp_name}.doc")
doc.save(f"D:\doc-docx\{inp_name}.docx")