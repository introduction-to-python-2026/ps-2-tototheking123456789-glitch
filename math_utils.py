def find_max_number(num1, num2, num3):
    return max(num1, num2, num3)


def find_mean(num1, num2, num3):
    return (num1 + num2 + num3) / 3


def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    return (((num1 - mean) ** 2 + (num2 - mean) ** 2 + (num3 - mean) ** 2) / 3) ** 0.5


# --- main program ---
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))

print("The maximum number is:", find_max_number(num1, num2, num3))
print("The mean is:", find_mean(num1, num2, num3))
print("The standard deviation is:", find_mean_std(num1, num2, num3))
