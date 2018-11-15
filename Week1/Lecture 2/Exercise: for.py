# 1. Convert the following code into code that uses a for loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints "Goodbye!"

for i in range(2,12,2):
  print(i)
print("Goodbye!")


# 2. Convert the following code into code that uses a for loop.
# prints "Hello!"
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print("Hello!")
for i in range(10,0,-2):
  print(i)


# 3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.
# For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

sum = 0
for i in range(1,end+1):
  sum += i
print(sum)
