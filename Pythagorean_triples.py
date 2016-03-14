__author__ = "Propupul"

# A program that allows the user to input the sides of any triangle
# Returns whether triangle is Pythagorean triple or not
# Order of integers does not matter
# Program will pick the largest as the hypotenuse

def main():
        keep_going = 'y'
        while keep_going == 'y':
                print("Pythagoream theorem - a**2 + b**2 = c**2")
                print("-----------------------------------------------------------------------")
                enter1 = int(input("Enter the side - hint the hypotenuse is the largest side: "))
                enter2 = int(input("Enter the side - hint the hypotenuse is the largest side: "))
                enter3 = int(input("Enter the side - hint the hypotenuse is the largest side: "))
                ptriplets(enter1, enter2, enter3)
                keep_going = input("Would you like to do another? [y/n]: ")
                if keep_going == 'n':
                        print("ok see ya!")



def ptriplets(a, b, c):
        ''' Enter positive integers '''

        if a > c:
                a,b,c = a,c,b
                if c < a or c < b:
                    a,b,c = c,b,a
                a = a**2
                b = b**2
                a_b = a + b
                c = c**2
                if a_b == c:
                        print("This is a Pythagoran triple",a_b ,"==", c)
                else:
                        print("This is not a Pythagorean triple",a_b ,"!=", c)

        elif b > c:
                c,b = b,c
                a = a**2
                b = b**2
                a_b = a + b
                c = c**2
                if a_b == c:
                        print("This is a Pythagoran triple", a_b, "==", c)
                else:
                        print("This is not a Pythagorean triple",a_b ,"!=", c)
                        

                       
                
                
        else:
                a = a**2
                b = b**2
                a_b = a + b
                c = c**2
                if a_b == c:
                        print("This is a Pythagoran triple: ",a_b ,"==", c)
                else:
                        print("This is not a Pythagorean triple",a_b ,"!=", c)

        
    
    

main()
