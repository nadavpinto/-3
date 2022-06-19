#exercise3
#1
num=int(input("number "))
def recursia(num1):
  atseret=1
  if num1==0:
    return 1
  if num1==1:
    return atseret
  atseret=num1*atseret
  return num1*recursia(num1-1)
print(recursia(num))