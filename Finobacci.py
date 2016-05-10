__author__ = "Propupul"

# BeginnerProjects Reddit
# FIBONACCI Sequence


def main():
    number = int(input("Enter an integer: "))
    fino = finobacci(number)

    


def finobacci(num):
    a_list = list(range(num))
    f0 = 0
    f1 = 1
    f2 = 1
    print(f0)
    print(f1)
    print(f2)
    result = 0
    for number in a_list:
        
        adding = f1 + f2
        result = adding + f2
        f1 = adding
        f2 = result
        print(f1)
        print(f2)
        
            
        
        
        
            
            
        


main()
