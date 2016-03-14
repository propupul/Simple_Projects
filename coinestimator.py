__author__ = "Propupul"

# Coin Estimator by weight
# Weighs coins pennies, nickels, dimes, and quarters
# Outputs how many coins of each you have and how many wrappers you need
# also allows you to chose between grams or pounds.
# Number of coins is rounded to the nearest whole number.

def main():
    print("Welcome!")
    lb_or_g = input("Would you like to enter the info in lbs or grams? [g/lb]: ")
    if lb_or_g == 'g':
        coins_gram()
    else:
        coins_lb()
    


def coins_gram():
    penny_weight = 2.500
    nickel_weight = 5.000
    dime_weight = 2.268
    quarter_weight = 5.670

    penny = 1
    nickel = 5
    dime = 10
    quarter = 25
    

    weight_penny = float(input("How much do pennies weight? "))
    weight_nickel = float(input("How much do nickels weight? "))
    weight_dime = float(input("How much do dimes weight? "))
    weight_quarter = float(input("How much do quarters weight? "))

    coins_penny = weight_penny / penny_weight
    coins_nickel = weight_nickel / nickel_weight
    coins_dime = weight_dime / dime_weight
    coins_quarter = weight_quarter / quarter_weight

    wrap_penny = round(coins_penny / 50)
    wrap_nickel = round(coins_nickel / 40)
    wrap_dime = round(coins_dime / 50)
    wrap_quarter = round(coins_quarter / 40)
    print("you have", round(coins_penny),"pennies and need", wrap_penny, "wrappers")
    print("you have", round(coins_nickel), "nickels and need", wrap_nickel, "wrappers")
    print("you have", round(coins_dime),"dimes and need", wrap_dime, "wrappers")
    print("you have", round(coins_quarter), "quarters and need", wrap_quarter, "wrappers")
    
    penny_total = round(coins_penny) * penny
    nickel_total = round(coins_nickel) * nickel
    dime_total = round(coins_dime) * dime
    quarter_total = round(coins_quarter) * quarter
    cent_total = penny_total + nickel_total + dime_total + quarter_total
    dollar_total = cent_total / 100
    print("You have a total of " + "$" + (str(dollar_total)))
    return(dollar_total)


    
def coins_lb():
    penny_weight_lb = 0.00551156
    nickel_weight_lb = 0.0110231
    dime_weight_lb = 0.0050000841
    quarter_weight_lb = 0.01250021

    penny = 1
    nickel = 5
    dime = 10
    quarter = 25
    

    weight_penny = float(input("How much do pennies weight? "))
    weight_nickel = float(input("How much do nickels weight? "))
    weight_dime = float(input("How much do dimes weight? "))
    weight_quarter = float(input("How much do quarters weight? "))

    coins_penny = weight_penny / penny_weight_lb
    coins_nickel = weight_nickel / nickel_weight_lb
    coins_dime = weight_dime / dime_weight_lb
    coins_quarter = weight_quarter / quarter_weight_lb

    wrap_penny = round(coins_penny / 50)
    wrap_nickel = round(coins_nickel / 40)
    wrap_dime = round(coins_dime / 50)
    wrap_quarter = round(coins_quarter / 40)
    print("you have", round(coins_penny),"pennies and need", wrap_penny, "wrappers")
    print("you have", round(coins_nickel), "nickels and need", wrap_nickel, "wrappers")
    print("you have", round(coins_dime),"dimes and need", wrap_dime, "wrappers")
    print("you have", round(coins_quarter), "quarters and need", wrap_quarter, "wrappers")
    
    penny_total = round(coins_penny) * penny
    nickel_total = round(coins_nickel) * nickel
    dime_total = round(coins_dime) * dime
    quarter_total = round(coins_quarter) * quarter
    cent_total = penny_total + nickel_total + dime_total + quarter_total
    dollar_total = cent_total / 100
    print("You have a total of " + "$" + (str(dollar_total)))
    return(dollar_total)
    


    
main()
