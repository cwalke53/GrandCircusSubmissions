#create a 3 lists and fill them with student information
names = ["Charles", "Abe", "Jahaira","Ebrahaim"]
hometown = ["Detroit", "Atlanta", "Washington", "Dallas"]
favorite_food = ["Lobster", "Chicken", "Beef", "Seafood"]
#Prompt the user to ask about a particular student by number. Convert the input to an integer.
# Use the integer as the index for the lists. Print the student’s name.
print(len(names))

while True:
    user_input  = int(input("Using numbers, choose a student to learn more about: (1)Charles, (2)Abe, (3)Jahaira, (4)Ebrahaim: ")) - 1

    if user_input not in range(len(names)):
            print("invalid, please try again")
            continue

    print(f"Student choice: {names[user_input]}")

    #Ask the user which category to display: Hometown or Favorite food. Then display the relevant information.
    while True:
        category_choice = input("Choose a category. Enter hometown or favorite food: ").strip().lower()

        if category_choice == "hometown":
            print(f"Hometown: {hometown[user_input]}")
            break
        elif category_choice == "favorite food":
            print(f"Favorite_food: {favorite_food[user_input]}")
            break
        else:
            print("invalid entry")

    restart = input("would you like to learn about another student? (Yes or No): ").strip().lower()
    if restart == "yes":
        break
    elif restart == "no":
        print("Thanks for playing")
        break
    else:
        print("Invalid entry")




