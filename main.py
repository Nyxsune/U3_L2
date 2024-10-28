"""
Connor Cox
U3 Lab 2
Factorials
"""

def for_factorial(num):
  factorial = num
  for i in range(1, num):
    factorial *= (num-i)

  return factorial

def while_factorial(num):
  factorial = num
  while num <= 4 and num > 0:
    num -= 1
    if num > 0:
      factorial *= num

  return factorial

def recursion_factorial(num):
  if num == 0:
    factorial = num + 1
    return factorial

  factorial = recursion_factorial(num-1)
  factorial *= num

  return factorial
  

def main():
  number = 1000
  factorial1 = for_factorial(number)
  factorial2 = while_factorial(number)
  factorial3 = recursion_factorial(number)
  print(f"This is the For Loop example of {number}!: {factorial1}\n")
  print(f"This is the While Loop example of {number}!: {factorial2}\n")
  print(f"This is the Recursion example of {number}!: {factorial3}\n")

if __name__ == "__main__":
  main()