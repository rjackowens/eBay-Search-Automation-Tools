# Prompts User to Enter Search Term, Min/Max Price, and Condition

# def enter_selection():
#     search_term = input ("\nEnter Search Term: ")
#     min_price = input("Enter Minimum Price: ") # Enter %00 to hard code no min price
#     max_price = input("Enter Maximum Price: ") # Enter %00 to hard code no max price
    
#     print ("\n1 = New \n2 = Used \n3 = For Parts or Not Working") # Displays category selections
#     condition = input("\nSelect Condition: ")
#     if condition == "1":
#         condition = "1000"
#     elif condition == "2":
#         condition = "3000"
#     elif condition == "3":
#         condition = "7000"
#     else:
#         print ("You did not select a valid category")

# if __name__ == "__main__":
#     enter_selection()

#######


def get_search_term():
    search_term = input ("\nEnter Search Term: ")
    return search_term

def get_min_price():
    min_price = input("Enter Minimum Price: ") # Enter %00 to hard code no min price
    return min_price

def get_max_price():
    max_price = input("Enter Maximum Price: ") # Enter %00 to hard code no max price
    return max_price

def get_condition():
    print ("\n1 = New \n2 = Used \n3 = For Parts or Not Working") # Displays category selections
    item_condition = input("\nSelect Condition: ")
    if item_condition == "1":
        item_condition = "1000"
        return item_condition
    elif item_condition == "2":
        item_condition = "3000"
        return item_condition
    elif item_condition == "3":
        item_condition = "7000"
        return item_condition
    else:
        print ("You did not select a valid category")
        
#get_condition()


# def f(x):
#     return {
#         "1000": 1,
#         "3000": 2,
#         "7000": 3,
#     }[x]
    
    