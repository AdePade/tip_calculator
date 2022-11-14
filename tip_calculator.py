
def tip_calulator():
    # this is the code to ask for inputs
    price = float(input('How much does your meal cost?: '))
    num_of_friends = int(input('How many friends are you splitting the bill with?: '))
    tip = int(input('What percent are you tipping today?: '))

    # This function coverts the input into the correct data type and then calculates the tip and tax 
    # then divids the result by the number of people splitting the bill
    def cal_tip():
        # coverts the price input into a float with 2 decimal points
        cost_of_food = float("{:.2f}".format(price))
        # this calulates the tax by multiplying the price input by .10 or 10%
        tax = (cost_of_food * 0.10)
        # this adds the tax to the price input
        add_tax = (cost_of_food + tax)
        tip_total = (cost_of_food * (tip / 100))
        # this adds the total of the price + tax to the tip
        total_bill = (add_tax + tip_total)
        # this splts the bill by the num_of_friends input by diving the total_bill by the num_of_friends
        bill_split = (total_bill / num_of_friends)

        # This then prints out the two final totals
        total_bill = (f'Total bill: ${total_bill}')
        bill_split = (f'Each person should pay ${bill_split}')

        print(total_bill)
        print(bill_split)

        # this functon is a while loop that loops through the function and ask user if they would like to calulate another tip
        # If yes then it run the function aain if no the it ask again

        ask_again = input('Would you like to enter another tip? ')
            # ask_again = "yes" or "no"
        while ask_again == "yes":
            tip_calulator()
        if ask_again == "no":
            print("Thank you for dinning with us today!!!")





    cal_tip()

tip_calulator()

