from docx import Document

# Create a new Word document and adding text to it
doc = Document()
doc.add_paragraph(text)

# Input the desired name of file the user wants to save the content in
fname = input("Enter the name you want the file to be named :")
doc.save(fname+".docx")

print("Text saved to '", fname+".docx'"," in the current folder.")
