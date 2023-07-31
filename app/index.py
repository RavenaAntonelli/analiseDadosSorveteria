import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Lista para armazenar os registros do CSV
    data = []

    # Lendo o arquivo CSV
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Escrevendo no arquivo JSON
    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    csv_file_path = "arquivosCSV/portfolio_ofertas - portfolio_ofertas.csv"
    json_file_path = "arquivosJson/portfolio_ofertas.json"
    csv_file_path2 = "arquivosCSV/dados_clientes - dados_clientes.csv"
    json_file_path2 = "arquivosJson/dado_clientes.json"
    csv_file_path3 = "arquivosCSV/eventos_ofertas - eventos_ofertas.csv"
    json_file_path3 = "arquivosJson/eventos_ofertas.json"
    csv_to_json(csv_file_path, json_file_path)
    csv_to_json(csv_file_path2, json_file_path2)
    csv_to_json(csv_file_path3, json_file_path3)