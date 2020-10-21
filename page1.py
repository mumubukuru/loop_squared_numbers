"""Prints numbers between 1 - 100. The numbers will be printed alongside their squared value.
The app will stop once the value is 200 or more has reached. It will ask to input number between 1-100 """

count=0

for i in range(1,100):
    sq = i*i
    print(i, ' ', sq)
    if sq>200:
        break

while count<2:
    print("Enter number between 1-100: ")
    val = int(input())
    while val <100:
        sq = val*val
        print(val, ' ', sq)
        if sq>200:
            break
        val+=1
    else:
        print("Please enter number 1-100: or press 2 to exit")
        count = int(input())