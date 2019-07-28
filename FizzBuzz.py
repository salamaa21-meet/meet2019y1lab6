result=[]
n=int(input("Enter a random number"))
for count in range(1,n):
    if count%3==0:
        result.append("Fizz")
    elif count%5==0:
        result.append("Buzz")
    else:
        result.append(count)
print(result)
