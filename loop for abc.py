for i in range(1, 7):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


text=input("Enter a string: ")
reversed_text = ""
for i in range(len(text) - 1, -1 ,-1):
    reversed_text += text[i]
print(reversed_text)