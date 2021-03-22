price = [25.00, 105.09, 30.25, 850.35, 100.09, 88.25, 1008.25, 95.87, 303.25, 62.84]
for elem in price:
    elem_rub = int(elem)
    elem_penny = int(elem * 100 % 100)
    print(f'{elem_rub} руб {elem_penny:02d} коп')
price.sort()
print(price)
price_max_to_low = list(reversed(price))
print(price_max_to_low)
print(price_max_to_low[:4])