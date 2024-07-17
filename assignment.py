import yt_dlp

# Enter the url for the download url = input("Enter video url: ")

ydl_opts = {}

with yt_dlp. YoutubeDL(ydl_opts) as ydl: ydl.download([url])

print("Video downloaded successfully!")
#code 2
from colorama import Fore print(Fore. RED + "hello world") print(Fore. BLUE + "hello world") print(Fore. GREEN + "hello world")

print(Fore. YELLOW + "CLCODING.COM")

print(Fore. CYAN + "THANK YOU")
#code 3
import barcode from barcode import Code128

def generate_barcode(data): code = Code128(data) code.save("barcode") print("Barcode generated.")

data = "1234-5678-9012" generate_barcode(data)
#code 4
import barcode from barcode import Code128

def generate_barcode(data): code = Code128(data) code.save("barcode") print("Barcode generated.")

data = "1234-5678-9012" generate_barcode(data)
#code 5
from faker import Faker

fake Faker()

print(fake.name())

print(fake.address())

print(fake.text())

print(fake.email())

print(fake.country())

print(fake.latitude(), fake.longitude())

print(fake.url())
#code 6
from textblob import TextBlob

def Convert(string):

li= list(string.split())

return li

str1 = input("Enter your word : ")

words=Convert(str1)

corrected_words = []

for i in words:

corrected_words.append(TextBlob(i))

print("Wrong words:", words)

print("Corrected Words are :")

for i in corrected_words:

print(i.correct(), end="")

#clcoding.com
#code7
from rembg import remove from PIL import Image

input_path = 'masai.jpg'

output_path = 'masai.png'

inp = Image.open(input_path)

output = remove(inp)

output.save(output_path)
#code 8
# pip install PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

writer = PdfFileWriter()

file = 'test_file.pdf'

reader = PdfFileReader(file)

for page in range(reader.numPages): writer.addPage (reader.getPage(page))

writer.encrypt('Password')

with open(f'test_file.pdf', 'wb') as file:

writer.write(file)

print('PDF encrypted')
