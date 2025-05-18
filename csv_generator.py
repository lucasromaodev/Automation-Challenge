import csv

def generate_csv(data):
    with open('invoices.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['ID', 'DueDate', 'InvoiceNo', 'InvoiceDate', 'CompanyName', 'TotalDue']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            csv_row = {
                'ID': row.get('ID', ''),
                'DueDate': row.get('Due Date', ''),
                'InvoiceNo': row.get('Invoice Number', ''),
                'InvoiceDate': row.get('Invoice Date', ''),
                'CompanyName': row.get('Company Name', ''),
                'TotalDue': row.get('Total Due', '')
            }
            writer.writerow(csv_row)
