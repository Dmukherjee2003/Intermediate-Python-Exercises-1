count = 0
sum = 0
while count < 5:
    x = input("Enter a number: ")
    y = x.lstrip("-")
    if y.isdigit():
        x = int(x) 
        sum += x  
        count += 1
    else:
        print("Invalid Output. Please enter an int.")


