income = float(input("กรอกเงินได้สุทธ: "))

tax_list = []

print("รายละเอียดภาษี\n")

if income >= 5000000:
    print("0 - 150,000: 0")

    tax_list.append((300000.00 - 150000.00) * 0.05)
    print("150,000 - 300,000: ", tax_list[0], "บาท")

    tax_list.append((500000.00 - 300000.00) * 0.1)
    print("300,000 - 500,000: ", tax_list[1], "บาท")

    tax_list.append((750000.00 - 500000.00) * 0.15)
    print("500,000 - 750,000: ", tax_list[2], "บาท")

    tax_list.append((1000000.00 - 750000.00) * 0.2)
    print("750,000 - 1,000,000: ", tax_list[3], "บาท")

    tax_list.append((2000000.00 - 1000000.00) * 0.25)
    print("1,000,000 - 2,000,000: ", tax_list[4], "บาท")

    tax_list.append((5000000.00 - 2000000.00) * 0.3)
    print("2,000,000 - 5,000,000: ", tax_list[5], "บาท")

    tax_list.append((income - 5000000) * 0.35)
    print("5,000,000+: ", tax_list[6], "บาท\n")

elif income >= 2000000:
    print("0 - 150,000: 0")

    tax_list.append((300000.00 - 150000.00) * 0.05)
    print("150,000 - 300,000: ", tax_list[0], "บาท")

    tax_list.append((500000.00 - 300000.00) * 0.1)
    print("300,000 - 500,000: ", tax_list[1], "บาท")

    tax_list.append((750000.00 - 500000.00) * 0.15)
    print("500,000 - 750,000: ", tax_list[2], "บาท")

    tax_list.append((1000000.00 - 750000.00) * 0.2)
    print("750,000 - 1,000,000: ", tax_list[3], "บาท")

    tax_list.append((2000000.00 - 1000000.00) * 0.25)
    print("1,000,000 - 2,000,000: ", tax_list[4], "บาท")

    tax_list.append((income - 2000000.00) * 0.3)
    print("2,000,000 - 5,000,000: ", tax_list[5], "บาท\n")

elif income >= 1000000:
    print("0 - 150,000: 0")

    tax_list.append((300000.00 - 150000.00) * 0.05)
    print("150,000 - 300,000: ", tax_list[0], "บาท")

    tax_list.append((500000.00 - 300000.00) * 0.1)
    print("300,000 - 500,000: ", tax_list[1], "บาท")

    tax_list.append((750000.00 - 500000.00) * 0.15)
    print("500,000 - 750,000: ", tax_list[2], "บาท")

    tax_list.append((1000000.00 - 750000.00) * 0.2)
    print("750,000 - 1,000,000: ", tax_list[3], "บาท")

    tax_list.append((income - 1000000.00) * 0.25)
    print("1,000,000 - 2,000,000: ", tax_list[4], "บาท\n")

elif income >= 750000:
    print("0 - 150,000: 0")

    tax_list.append((300000.00 - 150000.00) * 0.05)
    print("150,000 - 300,000: ", tax_list[0], "บาท")

    tax_list.append((500000.00 - 300000.00) * 0.1)
    print("300,000 - 500,000: ", tax_list[1], "บาท")

    tax_list.append((750000.00 - 500000.00) * 0.15)
    print("500,000 - 750,000: ", tax_list[2], "บาท")

    tax_list.append((income - 750000.00) * 0.2)
    print("750,000 - 1,000,000: ", tax_list[3], "บาท\n")

elif income >= 500000:
    print("0 - 150,000: 0")

    tax_list.append((300000.00 - 150000.00) * 0.05)
    print("150,000 - 300,000: ", tax_list[0], "บาท")

    tax_list.append((500000.00 - 300000.00) * 0.1)
    print("300,000 - 500,000: ", tax_list[1], "บาท")

    tax_list.append((income - 500000.00) * 0.15)
    print("500,000 - 750,000: ", tax_list[2], "บาท\n")

elif income >= 300000:
    print("0 - 150,000: 0")

    tax_list.append((300000.00 - 150000.00) * 0.05)
    print("150,000 - 300,000: ", tax_list[0], "บาท")

    tax_list.append((income - 300000.00) * 0.1)
    print("300,000 - 500,000: ", tax_list[1], "บาท\n")


elif income >= 150000:
    print("0 - 150,000: 0")

    tax_list.append((income - 150000.00) * 0.05)
    print("150,000 - 300,000: ", tax_list[0], "บาท\n")

total_tax = sum(tax_list)
final_income = income - total_tax
effective_rate = (total_tax / income) * 100
print("ภาษีรวม ", total_tax, "บาท")
print("รายได้หลังหักภาษี ", final_income, "บาท")
print(f"Effective Tax Rate = {effective_rate:.2f}%")