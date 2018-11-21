import csv, math


#find the biggest value equal to or less than the goal value between the start and end indexes for a given array.
def binarySearch(arr, bottomIndex, topIndex, goal):

    while(bottomIndex <= topIndex):
        i = int(math.floor((bottomIndex + topIndex) / 2))
        if(arr[i]["price"] < goal):
            bottomIndex = i + 1
        elif(arr[i]["price"] > goal):
            topIndex = i - 1
        else:
            return i
    if(topIndex == len(arr) -1 ):
        return i
    elif(i > 0):
        return i -1
    else:
        return -1 

def readPrices(filename):
    prices = []
    if(not filename):
        filename = "prices.txt" #fallback for empty string for personal testing purposes
    with open(filename, 'r') as file:
        pricesReader = csv.reader(file)
        for row in pricesReader:
            price = {}
            price["item"]= row[0]
            price["price"] = int(row[1])
            prices.append(price)
    return prices

def main():
    prices = readPrices(input("enter the filename of your price sheet "))
    goal = int(input("enter the value of your gift card "))
    #topValue is the highest index worth looking at i.e. the one closest to the goal without going over
    topValue = binarySearch(prices, 0, len(prices) - 1, goal)
    lower = prices[0] #startwith the lower value as if you can't find anything that matches with it without going over yo ucan't find anything
    upperIndex = binarySearch(prices, 0, topValue, goal-lower["price"]) #find the value closest to the remainder without going over
    if(upperIndex == -1):
        print("Not possible")
    else:
        upper = prices[upperIndex]
        lowerIndex = binarySearch(prices, 0, upperIndex, goal-upper["price"]) #see if you can find a better value for lower
        lower = prices[lowerIndex] # this will either just be the same as lower in worst case, or something better
        if(lower != upper):  
            print(lower)
            print(upper)
        else:
            print("Not possible")
    

main()