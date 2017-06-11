from decimal import Decimal

coins = [1, .50, 0.20, .10, .05, .02, .01]
amountList = []
coinCount = [20, 3, 2, 12, 6, 23, 10]

available_items = {
    'coke': .73,
    'biscuits': 1.15,
    'apple': .43
}

def give_change(amount):
    change = []
    index = 0
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount and coinCount[index] > 0:
            amount -= coin
            change.append(float(coin))
        index = index + 1
    #steal some change
    change = change[ : -1]
    return change

def give_item_and_change(item, amount):
    if item not in available_items:
        amount -= amount
        return None, amount, "that item isn't available - and I'm keepig the money!"

    cost = available_items[item]

    if amount < cost:
        amount -= amount
        return None, amount, "not enough money - and now it's mine!"

    change_to_return = amount - cost
    coins = give_change(change_to_return)
    return item, coins, "here's your change but I've kept a little for myself!"


if __name__ == '__main__':
    while True:
        item = raw_input('choose item: %s' % available_items)
        amount = 0
        amountList = input('enter amount in pounds separated by commas:')
        for eachCoin in amountList:
            amount = amount + eachCoin
        print give_item_and_change(item, amount)