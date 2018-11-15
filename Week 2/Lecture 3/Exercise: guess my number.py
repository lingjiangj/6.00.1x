# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low+high)//2
while True:
  print("Is your secret number",ans,"?",end="")
  guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
  if guess =="l":
    low = ans
    ans = (low+high)//2
   elif guess =="h":
    high = ans
    ans = (low+high)//2
   elif guess =="c":
    print("Game over. Your secret number was:",ans)
    break
   else:
    print("I did not understand your input.")
  
