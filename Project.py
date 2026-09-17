import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

clear_terminal() # clear terminal as it starts
list = []
list.clear()
while True:
    clear_terminal()
    item = input("Enter a word/number to add to the list: ") # store input in "item"
    
    if item == "reset":
        clear_terminal()
        list.clear()
        
  
    elif item == "done":
        clear_terminal()
        list.sort()
        print("Sorted list: ", list)

    else:    
        clear_terminal()
        list.append(item) # add input stored in "item" to the list
        print("Current list: ", list)
        print("Enter **reset** to start over")
        print("Enter **done** to finish")
        
        
    
