#เขียน function ชื่อ convert_currency()
#ที่ทำหน้าที่ในการแปลงสกุล
#THB <-> USD กำหนดให้ 1 USD = 33 THB
#ทั้งนี้ให้ function ดังกล่าว รับข้อมูล จำนวนเงินที่ต้องการแปลง และสกุลเงินปลายทาง
#ตัวอย่างวิธีการเรียกใช้
#convert_currency(100,"USD")
#convert_currency(100,"THB")

#ตัวอย่างหน้าจอ
#100 THB = 3.33 USD
#100 USD = 3300.0 THB

def convert_currency(value, currency):
    if currency == "USD":
        print(f"{value} THB = {value / 33.0} USD")
    else:
        print(f"{value} USD = {value * 33.0} THB")
        print()
    
convert_currency(100,"USD")
convert_currency(100,"THB")

def convert_currency(value, currency):
    result = 0
    if currency == "USD":
        result = value / 33.0
        print(f"{value} THB = {result} USD")
    else:
        result = value * 33.0
        print(f"{value} USD = {result} THB")
        print()
    
convert_currency(100,"USD")
convert_currency(100,"THB")