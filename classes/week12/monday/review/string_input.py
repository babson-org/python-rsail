lines = []
print("Enter text (blank line to finish):")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = " ".join(lines)
print("\nYou entered:")
print(text)

text = """
This is line 1
This is line 2
This is line 3
"""
print(text)

text = (
"This is line a " 
"This is line b " 
"This is line c " 
)
print(text)

test = "This is line x " + \
       "This is line y " + \
       "This is line z "

print(test)