# Prompts User to Enter a Search Term, Min/Max Price, and Condition

def enter_selection():
    searchTerm = input ("\nEnter Search Term: ")
    minPrice = input("Enter Minimum Price: ") # Enter %00 to hard code no min price
    maxPrice = input("Enter Maximum Price: ") # Enter %00 to hard code no max price
    print ("\n1 = New \n2 = Used \n3 = For Parts or Not Working")

    condition = input("\nSelect Condition: ")
    if condition == "1":
        condition = "1000"
    elif condition == "2":
        condition = "3000"
    elif condition == "3":
        condition = "7000"
    else:
        print ("You did not select a valid category")

if __name__ == "__main__":
    enter_selection()