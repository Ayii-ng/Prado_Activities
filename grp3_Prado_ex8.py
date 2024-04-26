# Python program find difference between each number in the array and the average of all numbers
def average_Difference(number):
    list_numbers= [int(x) for x in number.split()]
    average = sum(list_numbers) / len(list_numbers)
    print(average)

    difference = [num - average for num in list_numbers]
    print(difference)

number = input("enter a list of number: ")
average_Difference(number)

# Python program to convert a string in an array
def string_array(string):
    return list(string)

userInput = input("Enter full name: ")
result = string_array(userInput)
print(result)

# Python program to split an array in two and store even numbers in one array and odd numbers in the other.
def split_even_odd(numbers):
  
  even_numbers = []
  odd_numbers = []
  for num in numbers:
    if num % 2 == 0:
      even_numbers.append(num)
    else:
      odd_numbers.append(num)
  return even_numbers, odd_numbers


numbers = [1, 2, 3, 4, 5]
even_numbers, odd_numbers = split_even_odd(numbers)
print("Even numbers:", even_numbers) 
print("Odd numbers:", odd_numbers, "\n")

# Perform insertion sort on an array:
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(array)
print(sorted_array, "\n")
