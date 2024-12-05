import csv
from datetime import datetime


def difine_types(headers, rows):
    column_types = {}
    for i, val in enumerate(rows[0]):
        a = str
        try:
            if float(val):
                a = float(val)
                if a == int(a):
                    a = int
                else:
                    a = float
        except ValueError:
            test = val
            if test.count("-") == 2:
                a = datetime
            else:
                a = str
        column_types[headers[i]] = a
    return column_types


def load_table(*files, auto=False):
    complex_data = {}
    for file in files:
        try:
            with open(file, 'r', encoding="utf-8") as csvfile:
                csvreader = csv.reader(csvfile)
                data = [row for row in csvreader]
            if not data:
                raise ValueError("Файл пустой")
            headers = data[0]
            rows = data[1:]
            if not complex_data:
                complex_data = {"headers": headers, "rows": rows}
                if auto:
                    column_types = difine_types(headers, rows)
            else:
                complex_data["rows"].extend(rows)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file} не найден.")
    if auto:
        complex_data["column_types"] = column_types
    return complex_data


def save_table(table, file, max_rows=None):
    if "headers" not in table or "rows" not in table:
        raise ValueError("Таблица некорректна.")
    if max_rows is None:
        max_rows = len(table["rows"])
    for i, start in enumerate(range(0, len(table["rows"]), max_rows)):
        part_of_file = f"{file}_p_{i + 1}.csv"
        with open(part_of_file, "w", encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(table["headers"])
            writer.writerow(table["rows"][start:start + max_rows])