from datetime import datetime


class Table:
    def __init__(self, headers, rows, column_types=None):
        self.headers = headers
        self.rows = rows
        if column_types is None:
            self.column_types = {col: str for col in range(len(headers))}
        else:
            self.column_types = column_types

    def __call__(self, *args, **kwargs):
        return {"headers": self.headers, "rows": self.rows, "column_types": self.column_types}

    def print_table(self):
        print("\t".join(self.headers))
        for row in self.rows:
            print("\t".join(map(str, row)))

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        try:
            if stop:
                selected_rows = self.rows[start - 1:stop]
            else:
                selected_rows = self.rows[start - 1:start]
            if copy_table:
                return Table(self.headers, [row[:] for row in selected_rows])
            else:
                return Table(self.headers, selected_rows)
        except TypeError:
            print("Введено неправильное значение")

    def get_rows_by_index(self, *values, copy_table=False):
        try:
            if not values:
                raise ValueError("Неправильный ввод данных")
            selected_rows = [row for row in self.rows if row[0] in values]
            if copy_table:
                return Table(self.headers, [row[:] for row in selected_rows])
            else:
                return Table(self.headers, selected_rows)
        except ValueError as e:
            print(e)

    def set_column_types(self, types_dict, by_number=True):
        try:
            for col, col_type in types_dict.items():
                if by_number:
                    index = col - 1
                else:
                    index = self.headers.index(col)
                self.column_types[index] = col_type
        except AttributeError:
            print("Нужен словарь")

    def get_column_types(self, by_number=True):
        if by_number:
            return {i + 1: self.column_types[i] for i in range(len(self.headers))}
        else:
            return {self.headers[i]: self.column_types[i] for i in range(len(self.headers))}

    def get_values(self, column=0):
        try:
            if isinstance(column, int):
                index = column - 1
            else:
                index = self.headers.index(column)
            col_type = self.column_types[index]
            if col_type == datetime:
                return [datetime.strptime(row[index], "%d-%m-%Y").date() for row in self.rows]
            return [col_type(row[index]) for row in self.rows]
        except ValueError:
            print("Нужно ввести целое число")
        except KeyError:
            print("Запрашиваемый столбец отсутсвует")

    def get_value(self, column=0):
        try:
            if isinstance(column, int):
                index = column - 1
            else:
                index = self.headers.index(column)
            col_type = self.column_types[index]
            if col_type == datetime:
                return [datetime.strptime(row[index], "%d-%m-%Y").date() for row in self.rows][0]
            return [col_type(row[index]) for row in self.rows][0]
        except KeyError:
            print("Запрашиваемый столбец отсутсвует")

    def set_values(self, values, column=0):
        try:
            if isinstance(column, int):
                index = column - 1
            else:
                index = self.headers.index(column)
            col_type = self.column_types[index]
            for i, value in enumerate(values):
                self.rows[i][index] = col_type(value)
        except IndexError:
            raise IndexError("Некорректный ввод значений")

    def set_value(self, value, column=0):
        try:
            if isinstance(column, int):
                index = column - 1
            else:
                index = self.headers.index(column)
            col_type = self.column_types[index]
            self.rows[0][index] = col_type(value)
        except IndexError:
            print("Некорректный ввод значений")

    def concat(self, new_table):
        if self.headers != new_table.headers:
            raise ValueError("Заголовки таблиц не совпадают")
        self.rows.extend(new_table.rows)

    def split(self, row_number):
        if row_number - 1 < 0 or row_number - 1 > len(self.rows):
            raise IndexError("Номер строки за пределами таблицы")
        return Table(self.headers, self.rows[:row_number]), Table(self.headers, self.rows[row_number:])
