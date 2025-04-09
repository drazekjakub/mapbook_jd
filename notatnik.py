users:list = [
    {"name":"Jakub","location":"Warszawa","posts":2},
]
print(users)

def add_user(users_data:list)->None:

    new_name=input("podaj imię nowego znajomego: ")
    new_location=input("podaj miasto pochodzenia nowego znajomego: ")
    new_posts=int(input("podaj ilość postów nowego znajomego: "))
    users_data.append({"name":new_name,"location":new_location,"posts":new_posts})
add_user(users)


print(users)