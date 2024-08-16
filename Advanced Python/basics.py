# a=[1,2,3,4,5]
# b=[]

# for i in range(5):
#     print(a[i]*a[i])
#     b.append(a[i]*a[i])
    
# b=[element**2 for element in a]
# print(b)

# b=[i**2 if i%2==0 else i**3 for i in range(1,100)]
# print(b)


# b = lambda a: [x / 2 for x in a]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = b(a)
# print(result)

# import pandas as pd

# n = int(input("Enter the number of inputs: "))

# # Initializing lists
# list_variable = []
# odd_even_list = []

# Collecting inputs from the user
# for i in range(n):
#     list_variable.append(int(input(f"Enter the variable {i+1}: ")))

# # Lambda function to determine if the number is odd or even
# list_x = lambda x: 'even' if x % 2 == 0 else 'odd'

# # Creating the list of odd/even classifications
# for num in list_variable:
#     odd_even_list.append({num: list_x(num)})

# # Output the result
# print(pd.DataFrame(odd_even_list))

'''
1. Take N from user
2. create a list of length N asking number from user (ask numbers and put it in a list
3. create another list of N asking number from user(2nd list created with first list))
4. using map figuter out which from both list add up to 10 concat the 2 numbers and dispyay the list

'''

# def check(x,y):
#     if int(x)+int(y) == 10:
#         return f'{x}{y}'
    
# list_a=[]
# list_b=[]
# n=int(input('Number of inputs'))
# print('for list a')
# list_a=[int(input('')) for _ in range(n)]
# print('for list b')
# list_b=[int(input('')) for _ in range(n)]

# mapped=list(map(check,list_a,list_b))

# print(mapped)


# list_first=['apple','ball','bat','car','cheese','sage']

# list_second=list(filter(lambda x: len(x)>4,list_first))
# print(list_second)

from functools import reduce

# list_of_numbers=[1,2,3,4,5,6,7,8]
# output=reduce(lambda x,y:x*y,list_of_numbers)
# print(output)

n=int(input('Number of inputs'))

def square_and_add_4(x):
    return int(x)**2+4

number_list=[int(input('')) for _ in range(n)]
transition_list_1 =list(map(square_and_add_4,number_list))
transition_list_2=list(filter(lambda x:x%5==0,transition_list_1))
transition_list_3=list(reduce(lambda x,y: x+y,transition_list_2))
print(transition_list_2)
print(transition_list_3)
print(transition_list_1)