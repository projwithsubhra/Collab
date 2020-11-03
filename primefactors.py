def primenumber(a):
    if a<1:
        return False
    x=True
    for i in range(2,(a//2)+1):
        if a%i==0:
            x=False
            break
    return x


def primefactors():
    x=checkinput(input("Enter an integer:"))
    for i in range(2,(x//2)+1):
        if x%i==0:
            if primenumber(i):
                print(i)
    if primenumber(x):
        print(x)

def checkinput(x):
    while True:
        try:
            x = int(x)
            break
        except ValueError:
            print("Not a valid integer!")
            x=input("Please enter a valid integer:")
    return x

primefactors()