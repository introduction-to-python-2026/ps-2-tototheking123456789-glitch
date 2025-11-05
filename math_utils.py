num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))


def find_max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
maxnum = find_max_number(num1, num2, num3)

print(maxnum)

def find_mean(num1, num2, num3):
    return (num1 + num2 + num3) / 3
mean = find_mean(num1, num2, num3)
print(mean)

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    std = (((num1 - mean) ** 2 + (num2 - mean) ** 2 + (num3 - mean) ** 2) / 3) ** 0.5
    return mean, std

mean, std = find_mean_std(num1, num2, num3)
