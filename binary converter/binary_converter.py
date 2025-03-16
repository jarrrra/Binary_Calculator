def to_bin(num):
    if num//2 == 0:
        return str(num%2)
    
    return to_bin(num//2) + str(num%2)
    
    

def to_dec(num):
    digits = [int(d) for d in str(num)]
    return sum(d * 2**(len(digits) - 1 - enum) for enum, d in enumerate(digits))
        

def main():
    print("Enter a number and the type of number through space.",
          "\n\nExample:",
          "\n\n101110 2",
          "\n  or",
          "\n34 10",
          "\n\n(2 for binary number, 10 for decimal):")
    
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
    
    if num_type == 10:
        return to_bin(num)
    
    print("Something went wrong. Try again.")
    return main()


answer = main()
print("After conversion, your number is: ", answer)
