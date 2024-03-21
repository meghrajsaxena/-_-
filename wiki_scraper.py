import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headers = []

for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    text = header.text.strip()
    level = header.name
    headers.append((text, level))

# Create PDF
pdf = FPDF()
pdf.add_page()

# Set font for header text
pdf.set_font("Arial", size=12)

# Add headers to PDF
for text, level in headers:
    if level == "h1":
        pdf.set_font("Arial", style="B", size=16)
    elif level == "h2":
        pdf.set_font("Arial", style="B", size=14)
    elif level == "h3":
        pdf.set_font("Arial", style="B", size=12)
    elif level == "h4":
        pdf.set_font("Arial", style="B", size=10)
    elif level == "h5":
        pdf.set_font("Arial", style="B", size=8)
    elif level == "h6":
        pdf.set_font("Arial", style="B", size=6)
    pdf.cell(200, 10, txt=text, ln=True, align="L")

# Save PDF file
pdf.output("wikipedia_headers.pdf")
