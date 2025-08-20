number = int(input("Enter your number: "))
i=0;

while number != 1:
    i += 1
    if (number % 2) == 0:
        number /= 2
    else:
        number = (3 * number) + 1
    print(str(number))
else:
    print("steps = ", i)
