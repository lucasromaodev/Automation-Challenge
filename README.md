# 🧾 RPA Challenge - Automação de Extração de Faturas com OCR

Este projeto automatiza o processo de extração de dados de faturas disponíveis no site [RPA Challenge - OCR](https://rpachallengeocr.azurewebsites.net/) utilizando **Selenium**, **OCR com Tesseract**, e geração/envio de arquivo **CSV**.

---

## 🚀 Funcionalidades

1. Acessa automaticamente o site do desafio.
2. Obtém as faturas com vencimento atual ou anterior.
3. Baixa os arquivos de imagem (JPG) das faturas.
4. Executa OCR para extrair dados relevantes:
   - Invoice Number
   - Invoice Date
   - Company Name
   - Total Due
5. Gera um CSV com os dados extraídos.
6. Faz upload do CSV de volta ao site.
7. Limpa arquivos JPG temporários após execução.

---

## 🧰 Requisitos

- Python 3.8+
- Google Chrome + ChromeDriver compatível
- Tesseract OCR instalado

### Instalação das bibliotecas

```bash
pip install selenium pillow pytesseract
```

---

## 🗂 Estrutura do Projeto

```bash
.
├── main.py                 # Script principal de execução
├── browser.py             # Inicialização e navegação no site
├── invoice_downloader.py  # Download de faturas via Selenium
├── ocr_processor.py       # Extração de texto com OCR (Tesseract)
├── csv_generator.py       # Geração do arquivo CSV
├── upload_csv.py          # Upload do CSV no site
├── cleanup.py             # Limpeza de arquivos temporários .jpg
├── utils.py               # Função para filtrar faturas vencidas (não incluído)
└── invoices.csv           # CSV gerado (output)
```

---

## ⚙️ Como Executar

1. **Configure o caminho do Tesseract** (em `ocr_processor.py`):

```python
tesseract_path = r"C:\Program Files\Tesseract-OCR"
```

2. **Execute o script principal:**

```bash
python main.py
```

---

## 📤 Exemplo de Saída do CSV

```csv
ID,DueDate,InvoiceNo,InvoiceDate,CompanyName,TotalDue
1077,2023-07-04,INV-001,2023-06-01,Example Inc,185.50
```

---

## 📌 Observações

- O código considera que as faturas estejam em até **3 páginas**.
- Os arquivos `.jpg` são apagados ao final da execução.
- A função `get_due_invoices(driver)` está em `utils.py`, necessário para funcionamento completo.

---

## 👨‍💻 Autor

Desenvolvido como exercício prático de automação com foco em OCR e web scraping usando Python.

---
