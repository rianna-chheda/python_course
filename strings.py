name=input("Type your full name: ")
print("In uppercase:", name.upper())
print("In titlecase:", name.title())
print()

sentence=input("Type a sentence: ")
print("Count of 'a' in the sentence:", sentence.count('a'))
print()

n1="Rianna"
a1=16
c1="Mumbai"
print(f"My name is {n1}, I am {a1} years old and I live in {c1}")
print(f"Next year I will be {a1 + 1}")
print()

word=input("Enter a word: ")
print("Replacement of all vowels (a,e,i,o,u):", word.replace('a',"*").replace('e','*').replace('i',"*").replace('o',"*").replace('u',"*"))