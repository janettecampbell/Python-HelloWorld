import locale

house_price = 1000000
has_good_credit = True

if has_good_credit:
    percent_down = 10
else:
    percent_down = 20

down_payment = house_price * (percent_down/100)
locale.setlocale(locale.LC_ALL, "en_US")
down_payment_formatted = locale.currency(down_payment, symbol=True, grouping=True, international=False)

print(f"Your down payment is {percent_down}%. Which comes to {down_payment_formatted}.")
