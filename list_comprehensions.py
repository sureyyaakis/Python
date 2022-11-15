
## List Comprehensions
myList = [1,2,3,4,5]
[2*item for item in myList]


### List comprehensions with filters
myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
filteredList
filteredList = [item for item in myList if item % 10 < 3]
print(filteredList)


### List comprehensions with functions
myString = 'My name is Ryan Mitchell. I live in Boston'
myString.split('.')
myString.split()

 
def cleanWord(word):
    return word.replace('.', '').lower()

[cleanWord(word) for word in myString.split()]
[cleanWord(word) for word in myString.split() if len(cleanWord(word)) < 3]


### Nested list comprehensions
[[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')]
