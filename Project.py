import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

clear_terminal() # clear terminal as it starts
list = []
string = False # To know if it needs to convert to integer/string (False = Number, True = String)
selected = False # If type has already been selected
list.clear()

#========================= select numbers or string =========================#
while True:
    type = input("Would you like to sort numbers or words/letters?\nType **numbers** or **words**\n")
    if type == "numbers":
        string = False
        break
    if type == "words":
        string = True
        break
    else:
        clear_terminal()
        print("==========Invalid input==========")
while True:
    #===========================================================================#
    item = input("Enter a word/number to add to the list: ") # store input in "item"
    
    if item == "reset":
        clear_terminal()
        list.clear()
  
    if item == "done":
        clear_terminal()
        list.sort()
        print("Sorted list: ", list)
        print("Enter **reset** to start over")

    else:    
        clear_terminal()
        if string == False:
            item = int(item) # convert to integer if not a string
        list.append(item) # add input stored in "item" to the list
        print("Current list: ", list)
        print("Enter **reset** to start over")
        print("Enter **done** to finish")
        
        
    
