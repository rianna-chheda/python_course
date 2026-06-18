#while loop - use when we dont know the iteration (count), we only go with a condition 
#while only runs when the condition is true
#if a variable is created inside a loop, it exists only in the loop (same for function, condition, etc.)
#break is used to break a certain loop
#for loop -> for varibale in sequence (list, dictionary):
# syntax -> while condition: 

num=1
while num<=5:
    print(num)
    num=num+1
print(num)
print(num)
print()
print("FOR LOOP")
groc=["milk", "veggies", "fruits", "eggs"]
for i in groc: 
    print(i)

# for loop syntax -> for variable in sequence (list/dictionary) or range :
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num}/{i}={num/i}")
    
# nested loop -> loop inside a loop
print("NESTED LOOPS")
for i in range(1,4):
    for j in range(1,4):
        print(j)

    print("\n")

print("NESTED LIST")
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(mat[0][0])
print(mat[0][1])