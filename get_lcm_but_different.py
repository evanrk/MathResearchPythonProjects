first_num = int(input("enter the number on the left: ")) # gets the number on the left of the equals
second_num = int(input("enter the number on the right: ")) # gets the number in the mod
b = int(input("enter the b: ")) # gets the constant

while True:
    if b % first_num == 0: # checks to see if the number on the left divides b
        print(f"the number is {b//first_num}") # returns the divided number if true
        break
    else:
        b += second_num # if not it adds the number in the mode one time