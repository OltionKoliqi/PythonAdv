fruits = ["apple", "banana", "cherry"]

print(fruits)

#create a tuple
words = ("spam", "eggs", "sausages")
print(words[1])

person = ('Oltion', 13,"Programming")

name, age, proffesion = person

print(name, "'s", "proffesion is",proffesion, "and he is",age,"years old.")


#Creating a disctionary

my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value 3"

}

contact_info = {
    "Blerta": "444-333405",
    "Drini": "3339-3333"
}

#Create a variable called kreative's phone and use [] we can specify witch key we want to acces

kreative_phone = contact_info ["Blerta"]

print(kreative_phone)
print(contact_info)

contact_info ["Drini"] = "0294-48575"

print(contact_info)

#we want to add another friend to contact_info

contact_info ["Eros"] = "9384-117348"

print(contact_info)

#Delete a contact info

del contact_info ["Blerta"]
print(contact_info)

keys = contact_info.keys()

print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)











































