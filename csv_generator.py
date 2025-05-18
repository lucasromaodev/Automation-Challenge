import csv

def generate_csv(data):
    with open('invoices.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['#', 'ID', 'Due Date', 'Invoice Number', 'Invoice Date', 'Company Name', 'Total Due']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for index, row in enumerate(data, start=1):
            # Cria um dicionário filtrado para o CSV
            csv_row = {
                '#': index,
                'ID': row.get('ID', ''),
                'Due Date': row.get('Due Date', ''),
                'Invoice Number': row.get('Invoice Number', ''),
                'Invoice Date': row.get('Invoice Date', ''),
                'Company Name': row.get('Company Name', ''),
                'Total Due': row.get('Total Due', '')
            }
            writer.writerow(csv_row)
