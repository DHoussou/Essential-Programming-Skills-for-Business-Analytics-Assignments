# Q1. (25pts) Write a program that uses a for loop to print out the numbers 1 to 10.
print("Question 1:")
for i in range(1, 11):
    print(i)

# Q2. (25pts) Write a for loop to find the smallest number in a given list [3, 7, 1, 9, 4, 6, 8, 2, 5]
print("\nQuestion 2:")
numbers = [3, 7, 1, 9, 4, 6, 8, 2, 5]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("The smallest number is:", smallest)

# Q3. (25pts) Write a program that uses a while loop to print out the numbers from 1 to 10.
print("\nQuestion 3:")
num = 1
while num <= 10:
    print(num)
    num += 1

# Q4. (25pts) Write a while loop program that asks the user to enter a password, and keeps
# prompting the user to enter a password until they enter the correct password. The correct
# password is "abc123". Once the user enters the correct password, the program should print
# "Access granted" and exit
print("\nQuestion 4:")
password = input("Enter the password: ")
while password != "abc123":
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")
print("Access granted")
