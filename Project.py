import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def can_be_int(string):
    try:
        int(string)
    except ValueError:
        return False # return False if error occurs (can't be converted to int)
    else:
        return True # return True if conversion to int works

clear_terminal()        # clear terminal as it starts
list = []
reset_keyword = "reset" # keyword used to reset program
sort_keyword = "sort"   # keyword used to sort the current list
list.clear()

while True:
    item = input("Enter a string/integer to add to the list: ") # store input in "item"
    
    if item == reset_keyword:
        clear_terminal()
        list.clear()
  
    if item == sort_keyword:
        clear_terminal()
        list.sort(key=lambda value: (    # sorts integers and strings seperatly since normal sort() can't do both at the same time
            isinstance(value, str),      # check if it is a string
            value.lower() if isinstance(value, str) else value
        ))
        print("Sorted list: ", list)
        print(f"Enter **{reset_keyword}** to start over")

    else:    
        clear_terminal()
        if can_be_int(item):            # if item can be converted to int
            item = int(item)            # convert to integer
        if item != reset_keyword:       # stops the reset command to be added to the list
            list.append(item)           # add input stored in "item" to the list
        print("Current list: ", list)
        print(f"Enter **{reset_keyword}** to start over")
        print(f"Enter **{sort_keyword}** to sort")



