def calculator_total(bill,tip_percent=10,tax_percent=5):
    tip=bill*(tip_percent/100)
    tax=bill*(tax_percent/100)
    return bill+tip+tax

amount=float(input("enter your amount:"))
total_amount=calculator_total(amount,tip_percent=15)
print(f"Total Amount to Pay:${total_amount:.2f}")
