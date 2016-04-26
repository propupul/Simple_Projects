__author__ = "Propupul"

# Mean, Median, Mode
# Three functions that allow user to find mean, median, and mode
# Mean == Average
# Mode == Number that occurs the most
# Median == if numbers arranged numerically is the number in the middle


def main():
    number_list = num_list()
    average = mean(number_list)
    print("The average is", average)
    middle_num = median(number_list)
    median_one = len(middle_num) - len(middle_num)//2
    print("The median is: ", middle_num[median_one-1])
    mode_one, mode_two = mode(number_list)
    print("The number that apppears the most is:", mode_two, "and it appears", mode_one, "times")
    
    


def num_list():
    a_list = []
    while True:
        try:
            the_numbers = (int(input("Enter the numbers: ")))
            a_list.append(the_numbers)
        except:
            print(a_list)
            break
    return(a_list)


def mean(a_list):
    counter = 0
    for num in a_list:
        counter += num
    average = counter / len(a_list)
    return(average)


def median(a_list):

    another_list = []
    for num in a_list:
        if num < a_list[0]:
            another_list.insert(0, num)
        elif num > a_list[0]:
            another_list.append(num)
        elif num == a_list[0]:
            another_list.insert(-1, num)

    return(another_list)



def mode(a_list):
    b_list = []
    var = 0
    for nums in a_list:
        
        position = a_list[var]
        counts = a_list.count(position)
        var += 1
        b_list.append(counts)
        #print(b_list)
        maximus = max(b_list)
        #print(maximus)
        return(maximus, a_list[maximus-1])



main()
