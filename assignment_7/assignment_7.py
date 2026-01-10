'''
Problem 1: The "Price Tagger"
The Challenge: You are given a list of product prices. You need to write a function that takes this list and a "Discount Percentage." Inside the function, use a list comprehension to create a new list where each price is reduced by that percentage.

prices = [100, 250, 400, 50]
'''
# Solution_1.0:
prices = [100, 250, 400, 50]

def price_tagger(price, discount_percentage):
    return[round((price[i] - ((price[i]*discount_percentage)/100)), 2) for i in range(len(price))]

print(price_tagger(prices, 10))

#solution_1.1:
def price_tager1(price, discount_percentage):
    return[round((i - (i*discount_percentage)/100), 2) for i in price]
    
print(price_tager1(prices, 20))

'''
Problem 2: The "Short Word" Filter
The Challenge: You have a list of words. Some are long, some are short.Create a Lambda function that checks if a word has more than 3 letters (returns True or False).
Use a List Comprehension and that Lambda to create a new list containing only the "Long Words."

words = ["hi", "python", "is", "cool", "code", "a"]
'''
# solution_2.0:
words = ["hi", "python", "is", "cool", "code", "a"]

# letter_check= lambda w: ["True" if len(i)>3 else "Flase" for i in w]

check_letter = lambda words: [len(w) > 3 for w in words]
long_words = lambda words: [w for w in words if len(w) >3]

print(check_letter(words))
print(long_words(words))

# solution 2.1:

letter_check = lambda w: len(w) >3
words_long = lambda words: [w for w in words if letter_check(w)]

print(words_long(words))
