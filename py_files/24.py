from collections import Counter, defaultdict, namedtuple, OrderedDict
from enum import Enum

def least_common_element(lst):
    counter = Counter(lst)
    return min(counter, key=counter.get)

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(least_common_element(lst))

def city_population(pairs):
    population_dict = defaultdict(int)
    for city, population in pairs:
        population_dict[city] += population
    return dict(population_dict)

pairs = [("Moscow", 10), ("New York", 8), ("Moscow", 5)]
print(city_population(pairs)) 
 
class Transport(Enum):
    CAR = 1
    BIKE = 2
    PLANE = 3

def max_speed(transport):
    speeds = {
        Transport.CAR: 200,
        Transport.BIKE: 50,
        Transport.PLANE: 900,
    }
    return speeds.get(transport, "Unknown transport")

print(max_speed(Transport.PLANE)) 

def unique_symbols(string):
    return frozenset(string)

string = "hello world"
print(unique_symbols(string))


Book = namedtuple('Book', ['title', 'author', 'year'])

def sort_books_by_year(books):
    return sorted(books, key=lambda book: book.year, reverse=True)

books = [
    Book("Book A", "Author A", 1999),
    Book("Book B", "Author B", 2005),
    Book("Book C", "Author C", 2010),
]
sorted_books = sort_books_by_year(books)
print(sorted_books)


def sorted_products(file_path):
    with open(file_path, 'r') as file:
        products = {}
        for line in file:
            name, price = line.strip().split(',')
            products[name] = float(price)
    sorted_products = OrderedDict(sorted(products.items(), key=lambda item: item[1]))
    return sorted_products

sorted_dict = sorted_products("py_files/24.txt")
print(sorted_dict)