# รับข้อมูลชื่อจริง ("เป็นภาษา English")จากผู้ใช้
# นับจำนวนสระในช่องดังกล่าว

# ตัวอย่างหน้าจอ
# what is your name?: Boonchoo
# you have 4 vowels in your text.

name = input("what is your name?: ")
letters = list(name)
counter = 0

# ท่าที่ 1
for char in letters:
    if char == 'a' or char == 'A':
        counter = counter + 1

    if char == 'e' or char == 'E':
        counter = counter + 1

    if char == 'i' or char == 'I':
        counter = counter + 1

    if char == 'o' or char == 'O':
        counter = counter + 1

    if char == 'u' or char == 'U':
        counter = counter + 1

# ท่าที่ 2
a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')

vowels = a + e + i + o + u + A + E + I + O + U

print ("you have",counter, "vowels in your text.")
print ("you have",{vowels}, "vowels in your text.")