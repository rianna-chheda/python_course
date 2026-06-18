#function -> write it once and call it multiple times 
#syntax -> def func_name(parameter): 
print("TASK 1")
def square(n):
    print(f"{n} squared = {n*n}")

square(5)
square(12)
square(0)

print()
print("TASK 2")
def is_even(a):
    if a % 2 == 0:
        print(f"{a} is an even number")
    else: 
        print(f"{a} is an odd number")
for i in range (1,11):
    is_even(i)

print()
print("TASK 3")
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0 
    for letter in word:
        if letter in vowels:
            count = count+1
    print(f"{word} has {count} vowels")
    return count
word=str(input("Enter a word: "))
count_vowels(word)

print()
print("CHALLENGE")
def make_sandwich(bread, filling):
    print("YOUR SANDWICH ORDER")
    print(f"Bread used is {bread}")
    print(f"Filling using is {filling}")
    print()
make_sandwich("Wheat", "Cheese")
make_sandwich("Sour dough", "Tomato")
make_sandwich("Whole wheat", "Swiss cheese")