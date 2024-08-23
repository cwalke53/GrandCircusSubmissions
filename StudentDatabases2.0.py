    #list 3 students
    #loop through the list and print name along with the index numvers
def list_names(students):
    for index, student in enumerate(students, start=1):
        print(index,student["name"])

def get_new_student():
    new_dictionary = {}
    name = input("Enter your name: ")
    hometown = input("Enter your hometown: ")
    favorite_food = input("Enter your favorite food: ")
    new_dictionary = dict(name=name, hometown=hometown, favorite_food=favorite_food)
    return new_dictionary


students = [
        {"name": "Charles", "hometown": "Detroit", "favorite food": "Chicken"},
        {"name": "Abe", "hometown": "Atlanta", "favorite food": "pizza"},
        {"name": "Jahaira", "hometown": "Houston", "favorite food": "shrimp"}
    ]
# print(list_names(students))

while True:
    user_input = input("Would you like to add, view, or quit?: ")
    if user_input == "view":
        list_names(students)
        pick_user = input("Which student would you like to learn more about? Enter a number 1-3: ")
        if pick_user == "1" or pick_user.lower() == "Charles":
            print(students[0]["name"])
        elif pick_user == "2" or pick_user.lower() == "Abe":
            print(students[1]["name"])
        elif pick_user == "3" or pick_user.lower() == "Jahaira":
            print(students[2]["name"])
        else:
            print("Invalid selection, try again")
            continue

        while True:
            category_choice = input("Choose a category. Enter hometown or favorite food: ").strip().lower()
            if category_choice == "hometown":
                print(f"Hometown: {students[int(pick_user)-1]["hometown"]}")
                break
            elif category_choice == "favorite food":
                print(f"Favorite food: {students[int(pick_user)-1]["favorite food"]}")
                break
            else:
                print("invalid entry")
    elif user_input == "add":
        print(get_new_student())


    elif user_input == "quit":
        print("Goodbye")
        break
    else:
        print("Try again")


    # elif user_input == "add":
        # get_new_student()


