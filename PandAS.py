import pandas as pd
database = pd.read_csv("D:/Користувачі/дз/НП пайтон/Dataset/student-mat.csv")
database.head()
x1=database.shape[0]
print(x1)

F=0
M=0
for i in database['sex']:
    if i == 'F':
        F+=1
    elif i == 'M':
        M=+1
print("NUMBER of female persons"+ F)
print("NUMBERR of male persons"+ M)


x22=int(database['age'].sum/x1)
print(x22)


#% paid
xxx=int(100 - (100/database['paid'].sum()*x1))
print(xxx)

print(database[["Walc","age"]].sort_values(by=["age"],ascending=False).head(30))