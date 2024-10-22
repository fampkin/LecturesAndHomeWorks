
class Calculator():
    def __init__(self, number_dict, operation_dict, words_parasites):
        self.number_dict = number_dict
        self.operation_dict = operation_dict
        self.words_parasites = words_parasites

    def prepare_expression(self, expression):
        expression = expression.split()
        while "на" in expression or "скобка" in expression or "в" in expression:
            if "на" in expression:
                del expression[expression.index("на")]
            if "скобка" in expression:
                del expression[expression.index("скобка")]
            else:
                del expression[expression.index("в")]

        intermediate_res = str()
        for word in expression:
            if word in self.number_dict.keys():
                intermediate_res += self.number_dict[word]
            else:
                intermediate_res += self.operation_dict[word]
        return intermediate_res
    
    def calc(self, expression):
        intermediate_res = self.prepare_expression(expression=expression)
        intermediate_res = str(eval(intermediate_res))
        self.print_result_in_phrase(intermediate_res=intermediate_res)

    def print_result_in_phrase(self, intermediate_res):
        res = str()
        if intermediate_res not in self.number_dict.values():
            if len(intermediate_res) == 2:
                doz = intermediate_res[0] + "0"
                for key, value in self.number_dict.items():
                    if doz == value:
                        res += key + " "
                        intermediate_res = intermediate_res[-1]
            if len(intermediate_res) == 1:
                uni = intermediate_res[0]
                for key, value in self.number_dict.items():
                    if uni == value:
                        res += key
        else:
            for key, value in self.number_dict.items():
                if intermediate_res == value:
                    res += key
        
        print(res)

number_dict = {
        "ноль": "0",
        "один": "1",
        "два": "2",
        "три": "3",
        "четыре": "4",
        "пять": "5",
        "шесть": "6",
        "семь": "7",
        "восемь": "8",
        "девять": "9",
        "десять": "10",
        "одиннадцать": "11",
        "двенадцать": "12",
        "тринадцать": "13",
        "четырнадцать": "14",
        "пятнадцать": "15",
        "шестнадцать": "16",
        "семнадцать": "17",
        "восемнадцать": "18",
        "девятнадцать": "19",
        "двадцать": "20",
        "тридцать": "30",
        "сорок": "40",
        "пятьдесят": "50",
        "шестьдесят": "60",
        "семьдесят": "70",
        "восемьдесят": "80",
        "девяносто": "90",
    }
operation_dict = {
    "плюс": "+",
    "умножить": "*",
    "минус": "-",
    "открывается": "(",
    "закрывается": ")",
    "степени": "**"
}
words_parasites = ['на', 'в', 'скобка']
calculator = Calculator(number_dict,operation_dict, words_parasites)
calculator.calc("скобка открывается два минус один скобка закрывается в степени два умножить на три")