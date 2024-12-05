from csv_module import load_table, save_table
from pickle_module import load_table as ld_tb, save_table as sv_tb
from ops import Table
from datetime import datetime


data = load_table("py_files/test.csv")
table_1 = Table(data["headers"], data["rows"])
table_1.print_table()
table_1.set_column_types({"id": int, "Name": str, "Age": float, "Gender": str, "Date": datetime}, by_number=False)
print(table_1.get_column_types(by_number=True))