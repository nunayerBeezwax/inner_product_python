from time import sleep

origElemRow = float(input('How many elements do the vectors have?: '))
origElemColumn = origElemRow

lstRow = []
lstColumn = []

while (True):
    lstRow.append(float(input('Row vector element please: ')))
    origElemRow -= 1
    if origElemRow = 0:
        break

while (True):
    lstColumn.append(float(input('Column vector element please: ')))
    origElemColumn -= 1
    if origElemColumn = 0:
        break

product = [a*b for a,b in zip(lstRow,lstColumn)]
innerproduct = sum(product)
print(product)
print('The inner product of those vectors is ', innerproduct)

sleep(30)

    
    
    
