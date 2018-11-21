To RUN:
`python3 pricefinder.py`
input filename
input gift card price

find the highest item under the gift card cost

take the lowest and binary search the remainder of the list for the largest match under the remainder of wallet cost

take that number and binary search everything less than it for the largest number that is below its remainder

you should now have two items that make an amount equal to the best pair in the set.


big O time for this should be O(log(n)) for the actual search since it just runs a binary search over and over on subsets of the list.
whole program is O(n) since we have to read in the prices to begin with (it's in another function to at least simulate an API call out to get a premade object)


Extra:
At the moment this isn't arbitarily extendable, but to get three items instead of two you could attach a second check for a trio by the following:

find the best pair as before, let's say they are a (hi) and b (lo)

check your set for an item c that costs less than the remainder of the prices of a and b together

if no such item exists then move a to a-1

check again

