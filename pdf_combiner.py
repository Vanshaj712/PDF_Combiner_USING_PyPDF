import PyPDF2
# Dont forget to give the path for both

file1 = r''
file2 = r''

# Open the files that have to be merged one by one
pdf1 = open(file2, 'rb')
pdf2 = open(file1, 'rb')

# Read the files that you have opened
pdf1Reader = PyPDF2.PdfFileReader(pdf1)
pdf2Reader = PyPDF2.PdfFileReader(pdf2)

# Create a new PdfFileWriter object which represents a blank PDF document
writer = PyPDF2.PdfFileWriter()

# Loop through all the pagenumbers for the first document
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    writer.addPage(pageObj)

# Loop through all the pagenumbers for the second document
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    writer.addPage(pageObj)

# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open('MergedFiles.pdf', 'wb')
writer.write(pdfOutputFile)

# Close all the files - Created as well as opened
pdfOutputFile.close()
pdf1.close()
pdf2.close()