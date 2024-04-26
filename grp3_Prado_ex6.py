def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

print(f"the maximum number is {max_of_three(5, 10, 3)}")

def sum_of_list(lst):
    return sum(lst)

print(f"The sum of list {sum_of_list([1, 2, 3, 4, 5])}")

def reverse_string(string):
    return string[::-1]

print(reverse_string("Seventeen"))

def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

print(count_case("Say the Name"))

def distinct_elements(lst):
    return list(set(lst))

print(distinct_elements([1, 2, 2, 3, 4, 4, 5]))