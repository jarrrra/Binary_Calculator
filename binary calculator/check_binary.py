from operations import operations
from text_manipulation import text_filter, text_split

def check_ANDs(numbers):
    current_number = 0
    current_operation = 0
    
    ops = text_filter(numbers, ["AND"])
    numbers = text_split(numbers, ['AND'])
    
    for n in range(len(numbers)):
        numbers[n] = check_plus_minus(numbers[n])
        if numbers[n] == 'invalid!':
            return numbers[n]
        
    while current_number < len(numbers):
        if current_operation >= len(ops):
            break
           
        result, current_number = operations(ops[current_operation], numbers, current_number)
        if result == 'invalid!':
            numbers[current_number] = 'invalid!'
            break
               
        numbers[current_number] = str(result)
        current_operation += 1

    return numbers[current_number]
    
def check_plus_minus(numbers):

    current_number = 0
    current_operation = 0
    
    ops = text_filter(numbers, ['+', '-'])
    numbers = text_split(numbers, ['+', '-'])

    for n in range(len(numbers)):
        numbers[n] = check_multi_division(numbers[n])
        if numbers[n] == 'invalid!':
            return numbers[n]
        
    while current_number < len(numbers):
        if current_operation >= len(ops):
            break
        
        result, current_number = operations(ops[current_operation], numbers, current_number)
        if result == 'invalid!':
            numbers[current_number] = 'invalid!'
            break
            
        numbers[current_number] = str(result)
        current_operation += 1
    
    return numbers[current_number]

def check_multi_division(numbers):

    current_number = 0
    current_operation = 0
    
    ops = text_filter(numbers, ['*', '/'])
    numbers = text_split(numbers, ['*', '/'])

    numbers = check_NOTs(numbers)
    if numbers == 'invalid!':
        return numbers
    
    while current_number < len(numbers):
        if current_operation >= len(ops):
            break
        
        result, current_number = operations(ops[current_operation], numbers, current_number)
        if result == 'invalid!':
            numbers[current_number] = 'invalid!'
            break
            
        numbers[current_number] = str(result)
        current_operation += 1

    return numbers[current_number]


def check_NOTs(numbers):
    
    for n in range(len(numbers)):
        if '~' in numbers[n]:
            if not all(char in '01' for char in numbers[n][1:].strip()):
                return 'invalid!'
            numbers[n] = operations('~', [numbers[n][1:].strip()], 0)
        elif 'NOT' in numbers[n]:
            if not all(char in '01' for char in numbers[n][3:].strip()):
                return 'invalid!'
            numbers[n] = operations('~', [numbers[n][3:].strip()], 0)
        else:
            if not all(char in '01' for char in numbers[n].strip()):
                return 'invalid!'
            
        if numbers[n] == 'invalid!':
            return numbers[n]

    return numbers