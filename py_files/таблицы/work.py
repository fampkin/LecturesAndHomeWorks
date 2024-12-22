from tables.modules.csv_module import load_table as load_table_csv, save_table as save_table_csv
from tables.modules.pickle_module import load_table as load_table_pkl, save_table as save_table_pkl
from tables.operations.table_operations import Table


class Tests():   
    def test_load_csv(self):
        data = load_table_csv("py_files/таблицы/data/test.csv", auto=True)
        self.test_table = Table(data["headers"], data["rows"], data.get("column_types", None))
        self.test_table.print_table()
        input("Нажмите enter для продолжения...")
        print(self.test_table.get_values(3))
        input("Нажмите enter для продолжения...")
        first, second = self.test_table.split(2)
        second.print_table()
        input("Нажмите enter для продолжения...")
        print(self.test_table.get_column_types(by_number=False))
        input("Нажмите enter для продолжения...")
        second.concat(first)
        second.print_table()
        input("Нажмите enter для продолжения...")
    def test_save_csv(self):
        save_table_csv(self.test_table, 'babaka')
        input("Нажмите enter для продолжения...")
    def test_load_pkl(self):
        data = load_table_pkl("py_files/таблицы/data/data.pkl", auto=True)
        self.test_table = Table(data["headers"], data["rows"], data.get("column_types", None))
        self.test_table.print_table()
        input("Нажмите enter для продолжения...")
        print(self.test_table.get_values(3))
        input("Нажмите enter для продолжения...")
        first, second = self.test_table.split(2)
        second.print_table()
        input("Нажмите enter для продолжения...")
        print(self.test_table.get_column_types(by_number=False))
        input("Нажмите enter для продолжения...")
        second.concat(first)
        second.print_table()
        input("Нажмите enter для продолжения...")
    def test_save_pkl(self):
        save_table_pkl(self.test_table, 'babaka2')
        input("Нажмите enter для продолжения...")


if __name__ == '__main__':
    tests = Tests()
    tests.test_load_csv()
    tests.test_save_csv()
    tests.test_load_pkl()
    tests.test_save_pkl()

