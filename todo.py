to_do_list = ["Code", "Eat", "Sleep"]
selection = ''

while selection != "4":
    selection = input("\nPlease select a number: \n\
    1. View list \n\
    2. Add to list \n\
    3. Remove from list \n\
    4. Quit\n")

    if selection == "1":
        print(f"\nHere's your to-do list:\n")
        for item in to_do_list:
            print(item)
        input("Press enter to continue...\n")

    if selection == "2":
        item_to_be_added = input("\nWhat would you like to add to the list?\n") 
        to_do_list.append(item_to_be_added)
        print(f"\nItem was added to list: {item_to_be_added}\n")
        input("Press enter to continue...")

    if selection == "3":
        print(f"\nHere's your to-do list:\n")
        count = 1
        for item in to_do_list:
            print(f"{count}. {item}")
            count += 1
        item_to_be_removed = input("Which item do you want to remove?")
        to_do_list.pop(int(item_to_be_removed) - 1)
        input("Item removed. Press enter to continue...")

# next steps: add for entries outside of 1-4 so an error/print 'selection out of range'
# make append changes permit?
