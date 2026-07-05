from PyPDF2 import PdfReader

def extract_text(pdf_path):
    """
    Reads a PDF file and returns the extracted text.
    """

    reader = PdfReader(pdf_path)

    print(f"\n📄 Reading PDF: {pdf_path}")
    print(f"📑 Total Pages: {len(reader.pages)}\n")

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text