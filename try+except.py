def deposit(balance, amount):
    if amount < 0:
        raise ValueError("เกิดข้อผิดพลาด:จำนวนเงินฝากต้องมากกว่า0")
    return balance + amount

balance = 1000
try:
    print(f"ยอดเงินเรื่มต้น {balance} บาท")
    amount = float(input("กรอกจำนวนเงินที่ต้องการจะฝาก: "))
    balance = deposit(balance, amount)
    print("\nฝากเงินสำเร็จ")
    print(f"ยอดเงินคงเหลือ: {balance} บาท")
    print("สิ้นสุดรายการฝากเงิน")

except ValueError as e:
    print(f"เอ็งไม่พิมพิ์ตัวเลขละน้อง {e}")