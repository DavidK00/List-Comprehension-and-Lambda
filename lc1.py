x = [i for i in range(10)]
print(x)

#adding an expression -square of each number
squares = [i**2 for i in range(10)]
print(squares)

#multiply each element by 3
list1 = [3,4,5]
multiplied = [item * 3 for item in list1]
print(multiplied)

#word manipulation
listofwords = ['this', 'is', 'a', 'list', 'of', 'words']
modified_list = [i[0] for i in listofwords]
print(modified_list)

list1 = ['A', 'B', 'C']
list2 = [i.lower() for i in list1]
print(list2)

#adding an if condition
#all even numbers from range 0-4 squared
new_range = [i * i for i in range(5) if i%2 == 0]
print(new_range)

string = 'Hello 12345 World'
numbers = [i for i in string if i.isdigit()]
words = [x for x in string if x.isalpha()]
print(numbers)
print(words)

#using a file
infile = open('test.txt','r')
result = [i.rstrip('\n') for i in infile if 'line3' in i]
print(result)


#usiong functions
def double(x):
    return x* 2

#for even numbers only
print(double(10))
mynumbers = [double(x) for x in range(10) if x%2 == 0]
print(mynumbers)

#you can add more than one arguement
result = [x+y for x in [10,30,50] for y in [20,40,60]]

print(result)