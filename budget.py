# printing warning
print('This is an estimator for your monthly bills!')
# amount you bring home and how much you spend
weekly = int(input('How much money you make a week after taxes: '))
food = int(input('How much do you spend on groceries a week: '))
power = int(input('How much is your average monthly power bill: '))
water = int(input('How much is your monthly water bill: '))
cable = int(input('How much is your TV, internet, and home phone bill: '))
phone = int(input('how much is your Cell Phone bill: '))
# monthly bill print out
weekly = int(weekly * 4)
food = int(food * 4)

print('Monthly Average Bills')

print('Take home pay: ', weekly)
print('How much you pay for groceries: ', food)
print('How much you pay for power: ', power)
print('How much you pay for water: ', water)
print('How much you pay for TV and Internet: ', cable)
print('How much you pay for your cell phone: ', phone)

print('Left over money for the month: ', weekly - (food + power + water + cable + phone))

weekly = int(weekly * 12)
food = int(food * 12)
