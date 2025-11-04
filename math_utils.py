def find_max_number(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return(num1)
  elif num2 > num1 and num2> num3:
    return(num2)
  elif num3 > num1 and num3 > num2:
    return(num3)
  elif num1 == num2:
    return(num1)
  elif num1 == num3:
    return(num1)
  return(num2)
num1 = int(input("enter a number"))
num2 = int(input("enter another number"))
num3 = int(input("enter a third number"))
find_max_number(num1, num2, num3)




def find_mean(num1, num2, num3):
  return((num1 + num2 + num3)/3)
    
num1 = int(input("enter a numbner"))
num2 = int(input("enter another number"))
num3 = int(input("enter a third number"))
find_mean(num1, num2, num3)










num1 = int(input("enter a numbner"))
num2 = int(input("enter another number"))
num3 = int(input("enter a third number"))


def find_mean(num1, num2, num3):
  return((num1 + num2 + num3)/3)
    

def find_mean_std(num1, num2, num3):
  mean = find_mean(num1, num2, num3)
  return((((num1-mean)**2 +(num2-mean)**2 + (num3-mean)**2)/3)**0.5) 


print(find_mean(num1, num2, num3))

print(find_mean_std(num1, num2, num3))




