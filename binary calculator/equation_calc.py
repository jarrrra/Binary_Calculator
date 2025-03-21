from operations import operations
from text_manipulation import text_filter, text_split
from check_binary import check_ANDs
            

def equation_calculator(equation):

    try:
        operations_list = ["XOR", "OR", "="]
        current_number = 0
        current_operation = 0
        
        numbers = text_split(equation, operations_list)
        ops = text_filter(equation, operations_list)    
    
        print('\033[A' + equation, end='')
        if len(ops) == 0 or ops[-1] != '=':
            print('=', end='')
    
        if len(numbers) == 0 or (ops.count('=') > 0 and ops.index('=') != len(ops) - 1):
            return 'invalid!'
        
        breaking = False
        for num in numbers:
            if num in '~NOTAND*-+/':
                breaking = True
                break
            
        if breaking: return 'invalid!'
    
        for n in range(len(numbers)):
            numbers[n] = check_ANDs(numbers[n])
            if numbers[n] == 'invalid!':
               breaking = True
               break
           
        if breaking: return 'invalid!'           
    
        while current_number < len(numbers):
            if current_operation >= len(ops):
                break
            
            if ops[current_operation] == '=':
                break
                
            result, current_number = operations(ops[current_operation], numbers, current_number)
            if result == 'invalid!':
                numbers[current_number] = 'invalid!'
                break
                
            numbers[current_number] = str(result)
            current_operation += 1
            
            
        return numbers[current_number]
    
    except:
        return 'invalid!'