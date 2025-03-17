def to_bin(num):
    if num//2 == 0:
        return str(num%2)
    
    return to_bin(num//2) + str(num%2)
    
def to_bin_negative(num):
    if num < 0:
        return str(1) + to_bin(num*-1)
    else:
        return str(0) + to_bin(num)

def to_dec(num):
    digits = [int(d) for d in str(num)]
    return sum(d * 2**(len(digits) - 1 - enum) for enum, d in enumerate(digits))
        
def to_dec_negative(num):
    digits=[int(d) for d in str(num)]
    return (-1 if digits[0] == 1 else 1) * sum(d * 2**(len(digits) - 1 - enum) for enum, d in enumerate(digits[1:]))

def main():
    print("Enter a number and the type of number through space.",
          "\n\nExample:",
          "\n\n101110 2",
          "\n  or",
          "\n34 10",
          "\n\n(2 for binary number, 10 for decimal, add minus before (-2/-10) if it\'s negative):")
    
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
    
    if num_type == -10:
            return to_bin_negative(num)
    
    print("Something went wrong. Try again.")
    return main()


answer = main()
print("After conversion, your number is: ", answer)
