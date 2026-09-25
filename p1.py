text = input()
lower_text = text.lower()

rev = ""
for  ch in lower_text:
    rev = ch + rev

if lower_text == rev:
    print("Yes")
else:
    print("No")