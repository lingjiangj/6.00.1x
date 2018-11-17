# Problem 1

monIntRate = annualInterestRate/12
remainBal = balance

for i in range(12):
    
    minPayment = round(remainBal * monthlyPaymentRate,2)
    unpaidBal = remainBal - minPayment
    interest = round(unpaidBal * monIntRate,2)
    remainBal = unpaidBal + interest
    
    print("Month",i+1,"Remaining balance:",round(remainBal,2))  #for testing

print("Remaining balance:",round(remainBal,2))  #result



# Problem 2

remainBal = balance
monIntRate = annualInterestRate/12
lowestpay = 0

while remainBal >= 0:
    remainBal = balance
    lowestpay += 10
    for i in range(12):
        unpaidBal = remainBal - lowestpay
        interest = round(unpaidBal * monIntRate,2)
        remainBal = unpaidBal + interest
    
print("Lowest Payment:",round(lowestpay,2))


#Problem 3

remainBal = balance
monIntRate = annualInterestRate/12
lowerbound = balance /12
upperbound = (balance*(1+monIntRate)**12)/12

while True:
    remainBal = balance
    lowestpay = (lowerbound+upperbound)/2
    for i in range(12):
        unpaidBal = remainBal - lowestpay
        interest = round(unpaidBal * monIntRate,2)
        remainBal = unpaidBal + interest
    
    if remainBal > 0.001:
        lowerbound = lowestpay
    elif remainBal < -0.001:
        upperbound = lowestpay
    else:
        break
        
print("Lowest Payment:",round(lowestpay,2))
