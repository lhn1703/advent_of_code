with open('test.txt', 'r') as input_file:
    input_text = input_file.read().splitlines()

class Monkey:
    def __init__(self, starting_items = None, operation = None, result = None, modulo = None, true_throw = None, false_throw = None) -> None:
        self.starting_items = starting_items
        self.operation = operation
        self.result = result
        self.modulo = modulo
        self.true_throw = true_throw
        self.false_throw = false_throw
        