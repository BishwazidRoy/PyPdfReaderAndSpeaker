import pyttsx3
import PyPDF2

book=open('romantic.pdf', 'rb')
pdfR=PyPDF2.PdfFileReader(book)
pages=pdfR.numPages
print(pages)

friend=pyttsx3.init()
for num in range(6,pages):
    page=pdfR.getPage(num)
    text=page.extractText()
    friend.say(text)
    friend.runAndWait()