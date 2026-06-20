import pandas as pd

data = {
    "Name": ["Priya", "Jasmine", "Ellie", "Caleb", "Tommy"],
    "Marks": [75, 85, 90, 83, 70]
}

df = pd.DataFrame(data)
print(f"These are the students' marks:\n{df}")

highest_marks = df["Marks"].max()
print("\nThe highest marks are ", highest_marks)

average_marks = df["Marks"].mean()
print("The average marks are ", average_marks)

print("\nStudents scoring more than 80 marks:")
print(df[df["Marks"] > 80])