import argparse
from dataclasses import dataclass
import sys

# Define a dataclass to represent options
@dataclass
class Options:
    name: str
    age: int

# Create an argparse parser
parser = argparse.ArgumentParser(description="Example script")

# Add arguments to the parser - именованные аргументы
parser.add_argument("--name", '-n',  nargs='?', type=str, help="Name of the person")
#nargs='?' - необязательный аргумент
parser.add_argument("--age", type=int, help="Age of the person")
parser.add_argument("--profession", "--p", type=str, default='Worker')
#ниже передаем значения позиционных аргумнтов
parser.add_argument ('addres', nargs='?', default='Москва, красноармейская ул')
parser.add_argument ('tel', nargs='?', default='111-111-11')

options, rest = parser.parse_known_args(sys.argv[1:]) #первый параметр не нужен - это название скрипта
arg_dict = vars(options)
print(arg_dict)
print('Неизвестные аргументы ', rest)
# Parse command-line arguments
args = parser.parse_args(['25', '1']) #установить значения по умолчанию для позиционных аргументов 'addres' и 'tel'
default_options = vars(args)
print("Default Options:", default_options)

# Convert the options object and the parsed arguments into dictionaries
options_dict = vars(Options(name="John Doe", age=30))


print("Options:", options_dict)

print(vars(args))

#запуск :  python examples.py --n Vasya --age 40
#python examples.py Москва 222-222-22  --n Vasya --age 40
