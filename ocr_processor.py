import pytesseract
import os
from PIL import Image
import re

# Caminho para a instalação do Tesseract (ajuste se necessário)
tesseract_path = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = os.path.join(tesseract_path, "tesseract.exe")

# Caminho para a pasta tessdata
os.environ["TESSDATA_PREFIX"] = os.path.join(tesseract_path, "tessdata")

def extract_invoice_data(invoice_files):
    extracted_data = []

    for invoice in invoice_files:
        file_path = invoice['file']
        print(f"[INFO] Processando fatura: {file_path}")

        try:
            text = pytesseract.image_to_string(Image.open(file_path))
        except Exception as e:
            print(f"[ERRO] Falha ao processar OCR da imagem {file_path}: {e}")
            continue

        print(f"[DEBUG] Texto OCR extraído de {file_path}:\n{text}\n{'-'*40}")

        # Quebra o texto em linhas
        lines = text.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]

        # Company Name: Primeira linha com letras e possívelmente "LLC", "Inc", etc.
        company_name = ""
        for line in lines[:3]:  # Tenta nas primeiras linhas
            if re.search(r'[A-Za-z]{2,}', line):
                company_name = line
                break

        if not company_name:
            print(f"[ERRO] Não encontrou Company Name em {file_path}")

        # Invoice Number - busca por "Invoice #xxxx" ou variações
        invoice_number_match = re.search(r'Invoice\s*(?:Number)?\s*[#:]*\s*([A-Za-z0-9\-]+)', text, re.I)
        invoice_number = invoice_number_match.group(1).strip() if invoice_number_match else ""

        if not invoice_number:
            print(f"[ERRO] Não encontrou Invoice Number em {file_path}")

        # Invoice Date - formato tipo "2019-06-03", "03/06/2019", etc.
        invoice_date_match = re.search(r'\b(\d{4}[-/]\d{2}[-/]\d{2})\b', text)
        invoice_date = invoice_date_match.group(1).strip() if invoice_date_match else ""

        if not invoice_date:
            print(f"[ERRO] Não encontrou Invoice Date em {file_path}")

        # Total Due - valor após "Total", ignorando "Subtotal" e "Sales Tax"
        total_due = ""
        total_lines = [line for line in lines if re.search(r'\bTotal\b', line, re.I)]
        for line in total_lines:
            if re.search(r'\bSubtotal\b', line, re.I) or re.search(r'\bSales\s*Tax\b', line, re.I):
                continue
            match = re.search(r'Total\s*[:\-]?\s*\€?\$?\s*([0-9.,]+)', line, re.I)
            if match:
                total_due = match.group(1).strip()
                break

        if not total_due:
            print(f"[ERRO] Não encontrou Total Due em {file_path}")

        extracted_data.append({
            'Invoice Number': invoice_number,
            'Invoice Date': invoice_date,
            'Company Name': company_name,
            'Total Due': total_due,
            'File Name': file_path
        })

    return extracted_data
