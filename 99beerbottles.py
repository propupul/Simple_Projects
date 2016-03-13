__author__ = "Propupul"

# Prints every line to the song "99 bottles of beer on the wall"

list_of_num = []

for numbers in range(1,100):
	list_of_num.append(numbers)



def main():
        print("Lyrics to the song '99 bottles of beer on the wall'")
        input("press enter to continue: ")
        lyrics()

def lyrics():
        number_const = 99
        
        print("99 bottles of beer on the wall, 99 bottles of beer.")
        for bottles in list_of_num:
                
                minus = number_const - bottles
                if minus == 1:
                        print(minus,"bottle of beer on the wall,", minus, "bottle of beer")
                else:
                        print("Take one down and pass it around,", minus,", bottles of beer on the wall.")
                        print()
                        print(minus,"bottles of beer on the wall,", minus, "bottles of beer")
                
                
                
                


main() 
