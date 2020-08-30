tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

for i in range(4):
    for j in tableData:
        if len(j[i])>leng:
            leng=len(j[i])           

for i in range(4):
    for j in tableData:
        print(j[i].rjust(leng," "),end=" ")
    print()