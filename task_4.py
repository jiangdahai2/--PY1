import json

INPUT_FILE = "input.csv"

"""
filename - файл куда надо записывать
headers - список заголовков
rows список списков с данными
delimiter - разделитель между значениями, по умолчанию ","
new_line - разделитель строк, по умолчанию "\n".
"""

def csv_to_list_dict(file_name, divider=',', new_line='\n') -> list[dict]:
    with open(file_name) as input_file:
        lines = input_file.read().split(new_line)
    headers = lines[0].split(divider)
    rows = [lines[i].split(divider) for i in range(1, len(lines) - 1)]
    data = []

    for row in rows:
        data.append({headers[i]: row[i] for i in range(0, len(headers))})
    return data

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))



