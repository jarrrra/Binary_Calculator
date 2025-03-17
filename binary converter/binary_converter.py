#converter

def to_bin(num):
    if num//2 == 0:
        return str(num%2)
    
    return to_bin(num//2) + str(num%2)
    
def to_bin_negative(num):
    number = to_bin(num*-1).replace('1', '2').replace('0', '1').replace('2', '0')
    if number[-1] == '0':
        number = number[:-1] + '1'
    else:
        for n in range(len(number[:-1])):
            number[-n] = number[:-n] + '0' + number[-n+1:]
            if number[-n-1] == '0':
                number[-n-1] = number[:-n-1] + '1' + number[-n:]
                break
            
    return '1' + number

def to_dec(num):
    digits = [int(d) for d in str(num)]
    return sum(d * 2**(len(digits) - 1 - enum) for enum, d in enumerate(digits))
        
def to_dec_negative(num):
    digits=[int(d) for d in str(num)]
    return (-1 if digits[0] == 1 else 1) * 2**(len(digits)-1) + sum(d * 2**(len(digits) - 2 - enum) for enum, d in enumerate(digits[1:]))

def main():
    print("Enter a number and the type of number through space.",
          "\n\nExample:",
          "\n\n101110 2",
          "\n  or",
          "\n34 10",
          "\n\n(2 for binary number, 10 for decimal, add minus before (-2) if the binary number is negative):")
    
    while True:
        try:
            num, num_type = map(int, input().split())
        except:
            print("Something wrong with your answer. Try again.")
        else:
            break;
            
    if num_type == 2:
        if not any(x > 1 for x in map(int, str(num))):
            return to_dec(num)
    
    if num_type == -2:
        if not any(x > 1 for x in map(int, str(num))):
            return to_dec_negative(num)
    
    if num_type == 10:
        if num >= 0:
            return to_bin(num)
        if num < 0:
            return to_bin_negative(num)
    
    print("Something went wrong. Try again.")
    return main()


answer = main()
print("After conversion, your number is: ", answer)
