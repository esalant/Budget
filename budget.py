# printing warning
print('This is an estimator for your monthly bills!')
# amount you bring home and how much you spend
weekly = float(input('How much money you make a week after taxes: '))
food = float(input('How much do you spend on groceries a week: '))
power = float(input('How much is your average monthly power bill: '))
water = float(input('How much is your monthly water bill: '))
cable = float(input('How much is your TV, Internet, and Home Phone bill: '))
phone = float(input('how much is your Cell Phone bill: '))
# monthly bill print out

print('Monthly Average Bills')

print('Take home pay: ', weekly * 4)
print('How much you pay for groceries: ', food * 4)
print('How much you pay for power: ', power)
print('How much you pay for water: ', water)
print('How much you pay for TV, Internet, and Home Phone: ', cable)
print('How much you pay for your cell phone: ', phone)

print('Left over money for the month: ', (weekly * 4) - ((food * 4) + power + water + cable + phone))

print('Total for the year: ')
weekly = round(weekly * 52, 2)
food = round(food * 52, 2)
power = round(power * 52, 2)
water = round(water * 12, 2)
cable = round(cable * 12, 2)
phone = round(phone * 12, 2)

print('Take home pay: ', weekly)
print('How much you pay for groceries: ', food)
print('How much you pay for power: ', power)
print('How much you pay for water: ', water)
print('How much you pay for TV and Internet: ', cable)
print('How much you pay for your cell phone: ', phone)

print('Left over money for the year: ', weekly - food - power - water - cable - phone)
