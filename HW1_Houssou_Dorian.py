



# Question 1

# to get input for four values
def user_input():
    values = []
    for i in range(4):
        value = float(input(f"Please provide value {i+1}: "))
        values.append(value)
    return values

# to calculate descriptive statistics
def descriptive_statistics(values):
    maximum = max(values)
    minimum = min(values)
    total_sum = sum(values)
    value_range = maximum - minimum
    return maximum, minimum, total_sum, value_range

# to answer Question 1
def question_1():
    print("Analyzing Descriptive Statistics Of Four Values")
    values = user_input()
    maximum, minimum, total_sum, value_range = descriptive_statistics(values)
    print("Maximum value:", maximum)
    print("Minimum value:", minimum)
    print("Total sum of values:", total_sum)
    print("Range of values:", value_range)

# Question 2

# to get input for hours worked and pay rate

def hours_and_rate():
    hours_worked = int(input("Please enter the number of hours worked last week: "))
    pay_rate = float(input("Please enter the pay rate per hour: $"))
    return hours_worked, pay_rate

# to calculate weekly wage
def weekly_pay(hours_worked, pay_rate):
    if hours_worked <= 45:
        regular_pay = hours_worked * pay_rate
        print("No overtime; gross pay = ${:.2f}".format(regular_pay))
    else:
        regular_pay = 45 * pay_rate
        overtime_hours = hours_worked - 45
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        total_pay = regular_pay + overtime_pay
        print(f"{overtime_hours} hours overtime; gross pay = ${total_pay:.2f}")

# to answer Question 2
def question_2():
    print("Calculating Weekly Wage")
    hours_worked, pay_rate = hours_and_rate()
    weekly_pay(hours_worked, pay_rate)

# Question 3
 
#to determine eligibility for voting
def check_voting_eligibility(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

#to answer Question 3

def question_3():
    print("Verifying Voter Eligibility")
    age = int(input("Please enter your age: "))
    check_voting_eligibility(age)


question_1()
question_2()
question_3()
