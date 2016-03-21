__author__ = "Propupul"



# Change calculator
# Input change and prints the amount of quarters, dimes, nickles, and pennis

def main():
    
    keep_going = 'y'
    while keep_going == 'y':
        how_much = float(input("How much is the product? "))
        money = float(input("Enter customer money: "))
        computing = money - how_much
        calculator(computing)
        keep_going = input("Do you want to do another? [y/n]: ")

def calculator(change):
    Quarter = .25
    Dime = .10
    Nickel = .05
    Penny = .01

    
    quarter_change = change // Quarter
    quarter_remainder = change % Quarter
    quarter_multiply = (quarter_change * Quarter)
    if quarter_change == 1.0:
        print("You need",int(quarter_change), "quarter")
    else:
        print("You need",int(quarter_change), "quarters")


    
    dime_change = quarter_remainder // Dime
    dime_remainder = quarter_remainder % Dime
    dime_multiply = dime_change * Dime
    if dime_change == 1.0:
        print("you need", int(dime_change),"dime")
    else:
        print("you need", int(dime_change),"dimes")

    
    nickel_change = dime_remainder // Nickel
    nickel_remainder = dime_remainder % Nickel
    nickel_multiply = nickel_change * Nickel
    if nickel_change == 1.0:
        print("You need", int(nickel_change),"nickel")
    else:
        print("You need", int(nickel_change),"nickels")

    add_all = quarter_multiply + dime_multiply + nickel_multiply
    difference = change - add_all
    difference = "%.2f" % difference
    
    
    if difference == 0.01:
        print("You need",difference,"penny")
    else:
        print("You need", difference,"Pennies")
    
    
    

main()
    
