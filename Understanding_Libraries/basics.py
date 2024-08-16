import pandas as pd


# dictionary_variable={
#     'Students':['Ram','Shyam','Hari'],
#     'Marks':[100,10,30]
# }
# dictionary_variable['Hello']=['h1','h2','h3']
# data_frame_variable=pd.DataFrame(dictionary_variable)
# print(data_frame_variable.drop(columns=['Marks']))

# This code snippet allows a user to input a number of questions and their answers, then stores them
# in a DataFrame using pandas in Python. Here's a breakdown of what the code does:
n=int(input("Enter how many questions you want to add"))
question=[]
answer=[]
for i in range(0,n):
    question.append(input("Enter a question"))
    answer.append(input("Enter the answer for the question"))
list_dict=dict(zip(question,answer))
print(list_dict)
data_frame = pd.DataFrame(list_dict.items(),columns=['question','answer'])
print(data_frame)
# lookup=data_frame.loc[data_frame['question'].str.lower()=='what is the capital city of nepal?']
# print(data_frame)
# print(lookup)
# This code snippet is creating a DataFrame from a dictionary named `dictionary_variable`, then
# exporting that DataFrame to a CSV file named 'Data.csv' without including the index. After that, it
# reads the 'Data.csv' file back into a new DataFrame named `new_data` and prints the contents of the
# new DataFrame.
# data_frame=pd.DataFrame(dictionary_variable)
# data_frame.to_csv('Data.csv',index=False)

new_data=pd.read_csv('Data.csv')
print(new_data.iloc[2])