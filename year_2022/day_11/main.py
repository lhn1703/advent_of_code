import parse

with open('test.txt', 'r') as input_file:
    input_text = input_file.read()#.splitlines()

# // is integer division operator

class Monkey:
    def __init__(self, starting_items = None, operation = None, modulo = None, true_throw = None, false_throw = None, worry_result = None) -> None:
        self.starting_items = starting_items
        self.operation = operation                   
        self.modulo = modulo
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.worry_result = worry_result            # worry result will be // by 3 after every operation

    # def inspect(item):

monkeys = []
current_monkey = None 

test = parse.findall('''Monkey {}:
  Starting items: {}, {}
  Operation: new = {} * {}
  Test: divisible by {}
    If true: throw to monkey {}
    If false: throw to monkey {}\n''', input_text)

for i in test:
    print(i)

