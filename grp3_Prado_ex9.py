# 1.Display numbers from -10 to -1 using for loop
# 2. Use else block to display a message “Done” after successful execution of for loop

while True:
    for num in range(-10,0):
        print(num)
    else:
        print("Done")
    break

# 3.Write a program to display all prime numbers within a range
# 4.Use a loop to display elements from a given list present at odd index positions
print("Prime Numbers: ")

for i in range(100):
    if (i % 2 != 0):
        print(f" - {i}")

# 5. Display numbers from a list using loop
# a. The number must be divisible by five
# b. If the number is greater than 150, then skip it and move to the next number
# c. If the number is greater than 500, then stop the l
# numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
print("Numbers Divisible by 5: ")
for number in numbers:
    if (number % 5 == 0):
        if (number < 500):
            if(number != 150):
                print(f" - {number}")
