# Open The File
file = open("colors.txt", "r")

# Input To Define The Color
inp = str(input('Color: '))

# Loop For Each Line In The File
for line in file:
    a, b = line.split(",")
    b = b.replace('\n', '')
    if b.lower() == inp.lower():
        print(f"{b}: #{a}")
    elif "#" + a == inp or a == inp:
        print(f"{b}: #{a}")

# Close The File
file.close()
