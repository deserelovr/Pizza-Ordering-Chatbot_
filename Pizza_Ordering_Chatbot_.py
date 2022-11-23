print('Hello, my name is Alex your virtual assistant. I will help you order a pizza!')
print('I am going to ask you a few questions. After typing and answer, press enter.')
print('\n')
userName = input('\nEnter your name: ')
while (len(userName) ==0):
    userName = input("Please enter your name: ")
if userName.lower() == "jasmine bumbray":
    print('\nMy creator, ' + userName +  ", Pleasure to serve you!")
else:
    print("\nHello, " + userName + ", Nice to meet you!")
size = input('\nWhat size do you want? Enter small, medium, or large: ')
while size.lower() != 'small' and size.lower() != "medium" and size.lower() != "large":
    size = input("Invalid value. Please enter small, medium, or large:  ")

flavor = input('\nEnter the flavor of pizza: ')
crustType = input('\n What type of crust do you want: ')
quantity = input('\nHow many of these do you want to order? Enter a numeric value: ')
while not quantity.isdigit():
    quantity = input('\nValue not recognized. Please enter a numeric value:  ')
quantity = int(quantity)
method = input('\nIs this carry our or delivery:')
while method.lower() !="delivery" and method.lower() != "carry out" and method.lower() !="carryout":
    method = input("\Invalid value. Please enter delivery or carry out:  ")

salesTax = 1.1
pizzaCost = 14.99
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99

if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
total = (pizzaCost * quantity) * salesTax + deliveryFee
print('\n---------------')
print('Thank you,', userName, ', for your order')
print('your', quantity, size, flavor, 'pizza with', crustType, 'crust costs', '${:,.2f}'.format(total) + '.')
if total >= 50:
    print("\nCongraduations, you're been awarded a $10 off coupon for your next order!")
else:
    print("\nOrders over $50 with receive a free $10 off coupon!")
print('-------------------')