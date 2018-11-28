from colorama import init, Fore

# Prompt User to Schedule Email Alert
schedule_choice = input(Fore.YELLOW + "Schedule Email Alert? Enter Y or N: " + Fore.GREEN)
print ("") # New Line

if schedule_choice.lower() == "yes" or schedule_choice.lower() == "y":
   print ("You selected Yes")
elif schedule_choice.lower() == "no" or schedule_choice.lower() == "n":
   print ("You selected No")
else:
   print ("You did not enter Y or N")

print ("") # New Line