#list syntax -> list_name = ["item1", "item2", "item3",...]
#printing the item of list -> list_name[items index]
#indexing of the item in a list starts FROM 0 

#dictionary syntax -> dictionary_name = {"key1": "value1", "key2": "value2",...}
print("task 1")
dictionary={
    "name":"Rianna",
    "class":10,
    "city":"Mumbai",
    "favourite_subject":"Biology",
    "favourite_food":"Pizza",
    "favourite_movie":"HSM"
}
print(f"My name is {dictionary['name']}")
print(f"I am in grade {dictionary['class']}")
print(f"I live in {dictionary['city']}")
print(f"My favourite subject is {dictionary['favourite_subject']}")
print(f"My favourite food is {dictionary['favourite_food']}")
print(f"My favourite movie is {dictionary['favourite_movie']}")
print()

#artithmetic operators
n1=20
n2=10
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(n1%n2)
print(n1**n2)

#comparision operators 
n3=20
n4=10
print(n1==n2)

#logical operators
n1=20
n2=10 
print(n1>n2 and n1!=n2)
print(n1>n2 or n1!=n2)
print(not(n1>n2 and n1!=n2))
