text = input()
lower_text = text.lower()
rev = lower_text[::-1]

if text == lower_text:
    print("Yes")
else:
    print("No")