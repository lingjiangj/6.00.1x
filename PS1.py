# Problem 1

sum = 0
for letter in s:
  if letter =="a" or letter =="e" or letter =="i" or letter =="o" or letter=="u":
    sum += 1
    
print("Number of vowels: ",sum)


# Problem 2

total = 0
for i in range(len(s)-2):
  if s[i:i+3] =="bob":
    total +=1

print("Number of times bob occurs is: ",total)


#Problem 3

beststr = ""
currentstr = ""
prevletter = "z"

for i in s:
    if i >= prevletter:
        currentstr += i
    else:
        currentstr = i
    if len(currentstr) > len(beststr):
        beststr = currentstr
    prevletter = i

print("Longest substring in alphabetical order is: "+beststr)
