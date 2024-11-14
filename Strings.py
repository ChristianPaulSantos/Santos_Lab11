words = []
length = []

for i in range(10):
    wordinput = input("Enter words: ")
    words.append(wordinput)
    if any(char.isdigit() for char in wordinput):
        print("Invalid input, Please try again!")

lengthinput = int(input("Enter a number for the length: "))
for words in words:
    if len(words) == lengthinput:
        length.append(words)
    else:
        continue
print(length)