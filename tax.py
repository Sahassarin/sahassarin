def calculate_tax(income):
    tax_list = []
    brackets = []

    if income >= 5000000:
        brackets.append(("        0 -   150,000", 0))

        tax_list.append((300000.00 - 150000.00) * 0.05)
        brackets.append(("  150,000 -   300,000", tax_list[0]))

        tax_list.append((500000.00 - 300000.00) * 0.1)
        brackets.append(("  300,000 -   500,000", tax_list[1]))

        tax_list.append((750000.00 - 500000.00) * 0.15)
        brackets.append(("  500,000 -   750,000", tax_list[2]))

        tax_list.append((1000000.00 - 750000.00) * 0.2)
        brackets.append(("  750,000 - 1,000,000", tax_list[3]))

        tax_list.append((2000000.00 - 1000000.00) * 0.25)
        brackets.append(("1,000,000 - 2,000,000", tax_list[4]))

        tax_list.append((5000000.00 - 2000000.00) * 0.3)
        brackets.append(("2,000,000 - 5,000,000", tax_list[5]))

        tax_list.append((income - 5000000) * 0.35)
        brackets.append(("5,000,000 +          ", tax_list[6]))

    elif income >= 2000000:
        brackets.append(("        0 -   150,000", 0))

        tax_list.append((300000.00 - 150000.00) * 0.05)
        brackets.append(("  150,000 -   300,000", tax_list[0]))

        tax_list.append((500000.00 - 300000.00) * 0.1)
        brackets.append(("  300,000 -   500,000", tax_list[1]))

        tax_list.append((750000.00 - 500000.00) * 0.15)
        brackets.append(("  500,000 -   750,000", tax_list[2]))

        tax_list.append((1000000.00 - 750000.00) * 0.2)
        brackets.append(("  750,000 - 1,000,000", tax_list[3]))

        tax_list.append((2000000.00 - 1000000.00) * 0.25)
        brackets.append(("1,000,000 - 2,000,000", tax_list[4]))

        tax_list.append((income - 2000000.00) * 0.3)
        brackets.append(("2,000,000 - 5,000,000", tax_list[5]))

    elif income >= 1000000:
        brackets.append(("        0 -   150,000", 0))

        tax_list.append((300000.00 - 150000.00) * 0.05)
        brackets.append(("  150,000 -   300,000", tax_list[0]))

        tax_list.append((500000.00 - 300000.00) * 0.1)
        brackets.append(("  300,000 -   500,000", tax_list[1]))

        tax_list.append((750000.00 - 500000.00) * 0.15)
        brackets.append(("  500,000 -   750,000", tax_list[2]))

        tax_list.append((1000000.00 - 750000.00) * 0.2)
        brackets.append(("  750,000 - 1,000,000", tax_list[3]))

        tax_list.append((income - 1000000.00) * 0.25)
        brackets.append(("1,000,000 - 2,000,000", tax_list[4]))

    elif income >= 750000:
        brackets.append(("        0 -   150,000", 0))

        tax_list.append((300000.00 - 150000.00) * 0.05)
        brackets.append(("  150,000 -   300,000", tax_list[0]))

        tax_list.append((500000.00 - 300000.00) * 0.1)
        brackets.append(("  300,000 -   500,000", tax_list[1]))

        tax_list.append((750000.00 - 500000.00) * 0.15)
        brackets.append(("  500,000 -   750,000", tax_list[2]))

        tax_list.append((income - 750000.00) * 0.2)
        brackets.append(("  750,000 - 1,000,000", tax_list[3]))

    elif income >= 500000:
        brackets.append(("        0 -   150,000", 0))

        tax_list.append((300000.00 - 150000.00) * 0.05)
        brackets.append(("  150,000 -   300,000", tax_list[0]))

        tax_list.append((500000.00 - 300000.00) * 0.1)
        brackets.append(("  300,000 -   500,000", tax_list[1]))

        tax_list.append((income - 500000.00) * 0.15)
        brackets.append(("  500,000 -   750,000", tax_list[2]))

    elif income >= 300000:
        brackets.append(("        0 -   150,000", 0))

        tax_list.append((300000.00 - 150000.00) * 0.05)
        brackets.append(("  150,000 -   300,000", tax_list[0]))

        tax_list.append((income - 300000.00) * 0.1)
        brackets.append(("  300,000 -   500,000", tax_list[1]))

    elif income >= 150000:
        brackets.append(("        0 -   150,000", 0))

        tax_list.append((income - 150000.00) * 0.05)
        brackets.append(("  150,000 -   300,000", tax_list[0]))

    else:
        brackets.append(("0 - 150,000", 0))

    total_tax = sum(tax_list)
    final_income = income - total_tax
    effective_rate = (total_tax / income) * 100 if income > 0 else 0

    return brackets, total_tax, final_income, effective_rate

income = float(input("กรอกเงินได้สุทธิ: "))

brackets, total_tax, final_income, effective_rate = calculate_tax(income)

print("\n       รายละเอียดภาษี\n")
for label, tax in brackets:
    print(f"{label}: {tax} บาท")

print("\n    ภาษีรวม ", total_tax, "บาท")
print("    รายได้หลังหักภาษี ", final_income, "บาท")
print(f"    Effective Tax Rate = {effective_rate:.2f}%")