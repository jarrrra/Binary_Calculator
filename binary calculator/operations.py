def operations(op, nums, current_number):

    num1 = int(nums[current_number], 2)
    current_number += 1
    
    if op == 'NOT' or op == '~':
        bit_length = len(nums[current_number-1])
        bitmask = (1 << bit_length) - 1
        result = (~num1) & bitmask

        return bin(result)[2:]
    
    else:
        num2 = int(nums[current_number], 2)
            
        if op == 'AND':
            return bin(num1 & num2)[2:], current_number
        elif op == 'OR':
            return bin(num1 | num2)[2:], current_number
        elif op == 'XOR':
            return bin(num1 ^ num2)[2:], current_number
        elif op == '+':
            return bin(num1 + num2)[2:], current_number
        elif op == '-':
            return bin(num1 - num2)[2:], current_number
        elif op == '*':
            return bin(num1 * num2)[2:], current_number
        elif op == '/':
            if num2 == 0:
                return 'invalid!', current_number
            return bin(num1 // num2)[2:], current_number
        
    return 'invalid!', current_number
