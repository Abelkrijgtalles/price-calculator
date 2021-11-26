import json

numberfile = "number.json"
numberfilestring = ""
numberfilelistitem = []
pricefile = "price.json"
pricefilestring = ""
pricefilelistitem = []
price = 0
pricelist = []

with open(numberfile) as numberfilenotstring:
    numberfilestring = str(numberfilenotstring.read())

numberfilejson = json.loads(numberfilestring)

with open(pricefile) as pricefilenotstring:
    pricefilestring = str(pricefilenotstring.read())

pricefilejson = json.loads(pricefilestring)

for item in numberfilejson:
    numberfilelistitem.append(item)

for item in pricefilejson:
    pricefilelistitem.append(item)

if not numberfilelistitem == pricefilelistitem:
    print("Error code: 1; You can't have the \"id's\" of the number- and pricefile not the same. For more info, go to the GitHub page: https://abelr.tk/pc")
else:
    print("Check passed; " + numberfile + " and " + pricefile + " have the same id's")
    inlist = 0
    for item in numberfilelistitem:
        numberfilejsonstring = numberfilejson[item]
        pricefilejsonstring = pricefilejson[item]
        priceforlist = (numberfilejsonstring) * (pricefilejsonstring)
        pricelist.append(priceforlist)
        inlist = inlist + 1
    for price in pricelist:
        price = price + (price)

print("The price is: " + str(price))