def filter_strings_by_prefix(strings, prefix):
    """
    Возвращает список строк, которые начинаются с заданной подстроки.
    
    Args:
        strings (list): Список строк для фильтрации
        prefix (str): Подстрока, с которой должны начинаться строки
        
    Returns:
        list: Список отфильтрованных строк
    """
    return [s for s in strings if s.startswith(prefix)]

def sum_squares_of_odds(numbers):
    """
    Возвращает сумму квадратов всех нечетных чисел в списке.
    
    Args:
        numbers (list): Список чисел
        
    Returns:
        int/float: Сумма квадратов нечетных чисел
    """
    return sum(x * x for x in numbers if x % 2 != 0)

# Примеры использования:
if __name__ == "__main__":
    # Пример для filter_strings_by_prefix
    strings = ["apple", "banana", "apricot", "orange", "appetizer"]
    prefix = "ap"
    print(f"Строки, начинающиеся с '{prefix}': {filter_strings_by_prefix(strings, prefix)}")
    # Вывод: ['apple', 'apricot', 'appetizer']

    # Пример для sum_squares_of_odds
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Сумма квадратов нечетных чисел: {sum_squares_of_odds(numbers)}")
    # Вывод: 165 (1² + 3² + 5² + 7² + 9² = 1 + 9 + 25 + 49 + 81 = 165) 