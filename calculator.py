def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b

if __name__ == "__main__":
    a = int(input("enter the num 1 :"))
    b = int(input("enter the num 2 :"))

    addition = add(a,b)
    print(addition)
    subtraction = sub(a,b)
    print(subtraction)
    multiply = mul(a,b)
    print(multiply)
    divide = div(a,b)
    print(divide)