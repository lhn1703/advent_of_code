import parse
import math

with open('input.txt', 'r') as input_file:
    input_text = input_file.read()#.splitlines()

# // is integer division operator

class Monkey:
    def __init__(
        self, 
        starting_items = None, 
        operation = None, 
        modulo = None, 
        true_throw = None, 
        false_throw = None, 
        worry_value = None, 
        inspection_count = 0
        ) -> None:

        self.starting_items = starting_items
        self.operation = operation                   
        self.modulo = modulo
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.worry_value = worry_value            # worry value will be // by 3 after every operation
        self.inspection_count = inspection_count

    def inspect_item(self):
        if len(self.starting_items) == 0:           # do nothing if no items to throw
            return
        self.inspection_count += 1
        item = self.starting_items.pop(0)        
        x, op, y = self.operation.split()

        if x == 'old':
            x = item
        if y == 'old':
            y = item

        x, y = int(x), int(y)
        # don't use eval() since it is highly unsafe
        if op == '+':
            worry = x + y
        elif op == '*':
            worry = x * y
        # worry = worry // 3                      # integer division
        self.worry_value = worry

    def inspect_item_shortcut(self, lcm):
        if len(self.starting_items) == 0:           # do nothing if no items to throw
            return
        self.inspection_count += 1
        item = self.starting_items.pop(0)        
        x, op, y = self.operation.split()

        if x == 'old':
            x = item
        if y == 'old':
            y = item

        x, y = int(x), int(y)
        x = x % lcm                       # modulo to decrease runtime
        y = y % lcm
        # don't use eval() since it is highly unsafe
        if op == '+':
            worry = x + y
        elif op == '*':
            worry = x * y
        # worry = worry // 3                      # integer division
        self.worry_value = worry

    def relief(self):
        self.worry_value = self.worry_value // 3
    
    def throw_item(self):
        if self.worry_value % self.modulo == 0:
            return self.true_throw, self.worry_value
        else:
            return self.false_throw, self.worry_value

    def catch_item(self, item):
        self.starting_items.append(item)


monkey_list = []
current_monkey = None 

monkey_parse_list = parse.findall('''Monkey {}:
  Starting items: {}
  Operation: new = {}
  Test: divisible by {}
    If true: throw to monkey {}
    If false: throw to monkey {}''', input_text)

for monkey_parse in monkey_parse_list:
    # print(monkey_parse)

    monkey_index = int(monkey_parse[0])
    starting_items = monkey_parse[1].split(', ')
    operation = monkey_parse[2]
    modulo = int(monkey_parse[3])
    true_throw = int(monkey_parse[4])
    false_throw = int(monkey_parse[5])

    monkey = Monkey(starting_items, operation, modulo, true_throw, false_throw)
    monkey_list.append(monkey)

for rounds in range(20):
    for i in range(len(monkey_list)):
        monkey = monkey_list[i]
        while monkey.starting_items != []:
            monkey.inspect_item()
            monkey.relief()
            target_monkey, item = monkey.throw_item()
            monkey_list[target_monkey].catch_item(item)

inspection_list = []
for i in range(len(monkey_list)):
    monkey = monkey_list[i]
    inspection_list.append(monkey.inspection_count)
    # print('monkey:', i, 'inspected:', monkey.inspection_count)

inspection_list = sorted(inspection_list)
answer = inspection_list[-1] * inspection_list[-2]
print('part1:', answer)




monkey_list = []
modulo_list = []
current_monkey = None 

monkey_parse_list = parse.findall('''Monkey {}:
  Starting items: {}
  Operation: new = {}
  Test: divisible by {}
    If true: throw to monkey {}
    If false: throw to monkey {}''', input_text)

for monkey_parse in monkey_parse_list:
    # print(monkey_parse)

    monkey_index = int(monkey_parse[0])
    starting_items = monkey_parse[1].split(', ')
    operation = monkey_parse[2]
    modulo = int(monkey_parse[3])
    true_throw = int(monkey_parse[4])
    false_throw = int(monkey_parse[5])

    modulo_list.append(modulo)
    monkey = Monkey(starting_items, operation, modulo, true_throw, false_throw)
    monkey_list.append(monkey)

lcm = math.lcm(*modulo_list)

for rounds in range(10000):
    for i in range(len(monkey_list)):
        monkey = monkey_list[i]
        while monkey.starting_items != []:
            monkey.inspect_item_shortcut(lcm)
            target_monkey, item = monkey.throw_item()
            monkey_list[target_monkey].catch_item(item)

inspection_list = []
for i in range(len(monkey_list)):
    monkey = monkey_list[i]
    inspection_list.append(monkey.inspection_count)
    # print('monkey:', i, 'inspected:', monkey.inspection_count)

inspection_list = sorted(inspection_list)
answer = inspection_list[-1] * inspection_list[-2]
print('part2:', answer)

