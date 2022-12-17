with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

# // is integer division operator

class Monkey:
    def __init__(self, starting_items = None, operation = None, modulo = None, true_throw = None, false_throw = None, worry_result = None) -> None:
        self.starting_items = starting_items
        self.operation = operation                   
        self.modulo = modulo
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.worry_result = worry_result            # worry result will be // by 3 after every operation


    
        