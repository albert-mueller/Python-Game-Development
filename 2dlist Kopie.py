import sys
s=[[5,10,15],[1,2,3],[100,300,500]]
print(s)
print(len(s))
print(len(s[0]))
print(s[2][0])
print(s[0][2])
matrix=[]
rows=int(input("Enter the amount of rows:"))
columns=int(input("Enter the amount of columns:"))
for i in range(rows):
    rows_list=[]
    for j in range(columns):
        element=int(input("Enter the element:"))
        rows_list.append(element)
    matrix.append(rows_list)
print(matrix)