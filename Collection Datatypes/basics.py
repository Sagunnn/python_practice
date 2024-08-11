'''
List 
    -List is collection datatype that is capable of holding more than 1 variable
    -It is very similar to Array but has 1 fundamental Difference
    _It  is heterogeneous for  these you can put in any type of ValueError
    -It is denoted by '[]' brackets
    -Each value has index or location associated
'''
# list_var=[1,2,3,4,5,6,7,8]
# print((list_var),type(list_var),list_var[0])

# for i in range(0,len(list_var)):
#     print(list_var[i])

# print('--'*25)

# for list_element in list_var:
#     print(list_element)

# print('--'*25)

# for list_index,list_element in enumerate(list_var):
#     print(list_index,list_element)

# # Task 1: Loop over each element of this list and show only even number  
# list_element=[1,2,3,4,5,6,7,8,9,10]
# print('--'*25)
# def even_num(list_element):
#     for num in list_element:
#         if num%2==0:
#             print(f"{num} is an even number")
            
# even_num(list_element)

# list_var_3=[]

# # Static
# list_var_3=[1]
# # Dynamic
# list_var_3.append(4)
# print(list_var_3)    

# list_var_4=[]

# for i in range(1,10):
#     list_var_4.append(i)
    
# print(list_var_4)

print('--'*30)

# Task 2: Create a list name Even_list that should contain all the  even numbers from 1-100:

# Even_list = []

# for i in range(1,101):
#     if i % 2 == 0:
#         Even_list.append(i)
        
# print('---'*30)
# #slicing in list
# print(Even_list[1:3])

# list_var_6=[2,3,4,5,6,7,8,9,10,11]
# print(list_var_6)
# list_var_6.pop(3)
# print(list_var_6)

# Task 3: Create a list of numbers from 1-100 using append, then remove all the odd numbers from that list
# list=[]
# for i in range(1,101):
#     list.append(i)
# print(list)
# print('---'*30)
# for i in range(len(list) - 1, -1,-1):
#     if list[i] % 2 != 0:
#         list.pop(i)
# print(list)

# list_keys=['apple', 'android','chrome','chase']
# list_values=['1','2','3','4']
# list_dict=dict(zip(list_keys,list_values))
# print(list_dict.keys(),list_dict.values())

# Task create quiz questions answer dictionary usng zip function and 2 list!!

# list_questions = [
#     "What is the capital of France?",
#     "Who wrote the play 'Romeo and Juliet'?",
#     "What is the largest planet in our solar system?",
#     "In what year did the Titanic sink?",
#     "Which element has the chemical symbol 'O'?",
#     "What is the fastest land animal?",
#     "Who painted the Mona Lisa?",
#     "What is the smallest country in the world?",
#     "How many continents are there on Earth?",
#     "What is the longest river in the world?",
#     "Which language has the most native speakers?",
#     "What year did World War II end?"]

# list_answer=[
#     "Paris",  # What is the capital of France?
#     "William Shakespeare",  # Who wrote the play 'Romeo and Juliet'?
#     "Jupiter",  # What is the largest planet in our solar system?
#     "1912",  # In what year did the Titanic sink?
#     "Oxygen",  # Which element has the chemical symbol 'O'?
#     "Cheetah",  # What is the fastest land animal?
#     "Leonardo da Vinci",  # Who painted the Mona Lisa?
#     "Vatican City",  # What is the smallest country in the world?
#     "Seven",  # How many continents are there on Earth?
#     "Nile",  # What is the longest river in the world?
#     "Mandarin Chinese",  # Which language has the most native speakers?
#     "1945"]

# list_dict=dict(zip(list_questions, list_answer))
# print(list_dict)

list_questions=[]
list_answer=[]
continue_loop="y"

while(continue_loop.lower()=="y"):
    list_questions.append(input('Enter Question'))
    list_answer.append(input('Enter Answer'))
    continue_loop=input('Do you want to Continue Y/N?')

list_dict=dict(zip(list_questions,list_answer))
print(list_dict)
    
    





