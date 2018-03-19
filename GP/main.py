from item import Item
import math


def calculateAGV(items):
    x = 0
    y = 0
    for item in items:
        x += item
        y += 1
    return x / y


def getSimilarity2F(item1, item2, avgPrice, avgRate):
    f1i1 = item1.rate - avgRate
    f1i2 = item2.rate - avgRate

    f2i1 = item1.price - avgPrice
    f2i2 = item2.price - avgPrice

    numerator = 0
    denominator = 0

    numerator += f1i1 * f1i2
    numerator += f2i1 * f2i2

    denominator += math.sqrt(math.pow(f1i1, 2) + math.pow(f2i1, 2));
    denominator *= math.sqrt(math.pow(f1i2, 2) + math.pow(f2i2, 2));


    sim = (numerator / denominator) * 100
    if sim >= 99.99:
        sim = 100
    return sim


# def getAllSimilaritiesForOneItem(items, item, avgPrice, avgRate):
#     similarties = []
#     for i in items:
#         s = getSimilarity2F(i, item, avgPrice, avgRate)
#         similarties.append(s)
#     return similarties


def buildData(items):
    item1 = Item('1', 1, 3, 7, 800);
    items.append(item1)
    item1 = Item('1', 1, 3, 8, 1200);
    items.append(item1)
    item1 = Item('1', 1, 3, 8, 1000);
    items.append(item1)
    item1 = Item('1', 1, 3, 6, 400);
    items.append(item1)
    item1 = Item('1', 1, 3, 8, 20);
    items.append(item1)

    return items


if __name__ == '__main__':
    print("hello");
    items = []
items = []
prices = []
rates = []
matrix = [[]]

items = buildData(items)
for i in range(items.__len__()):
    prices.append(items.__getitem__(i).price)
    rates.append(items.__getitem__(i).rate)

priceAVG = calculateAGV(prices)
rateAVG = calculateAGV(rates)

print(priceAVG)
print(rateAVG)

sim = getSimilarity2F(items.__getitem__(1), items.__getitem__(4), priceAVG, priceAVG)
print(sim)
print("\n")

for ii in items:
    simis = []
    for i in items:
        sims = getSimilarity2F(ii, i, priceAVG, priceAVG)
        simis.append(sims)
    matrix.append(simis)

for m in matrix:
    print(m)
