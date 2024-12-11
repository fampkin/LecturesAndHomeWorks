import pickle
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
            with open(file, 'rb') as f:
                table = pickle.load(f)
            if not complex_data:
                complex_data = table
                if auto:
                    column_types = difine_types(table("headers"), table("rows"))
            else:
                complex_data["rows"].extend(table["rows"])
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file} не найден.")
    if auto:
        complex_data["column_types"] = column_types
    return complex_data


def save_table(table, file, max_rows=None):
    if "headers" not in table or "rows" not in table:
        raise ValueError("Таблица некорректна")
    if max_rows is None:
        max_rows = len(table["rows"])
    for i, start in enumerate(range(0, len(table["rows"]), max_rows)):
        part_of_file = f"{file}_p_{i + 1}.pkl"
        with open(part_of_file, 'wb') as f:
            pickle.dump({"headers": table["headers"], "rows": table["rows"][start:start+max_rows]}, f)