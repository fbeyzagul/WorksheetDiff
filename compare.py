import collections
import pandas as pd
firstDF=pd.read_excel('BOM.xlsx')
firstNp=firstDF.to_numpy()

secondDF=pd.read_excel('Pick Place.xlsx')

import numpy  as np

if collections.Counter(firstDF) == collections.Counter(secondDF):  
    print("The lists 1 and 2 are the same")  
else:  
    print("The lists 1 and 2 are not the same")  
	


desCol=firstDF["Designator"]
rowArr=desCol.iloc[0].split(',')

desCol2=secondDF["Designator"]
rowArr=desCol2.iloc[0].split(',')

output=[]


for item in desCol2:
    isExist=False
    for  row in desCol.iloc:
        rowArr = str(row).split(',')
        for item2 in rowArr:

            if(item.strip()==item2.strip()):
                isExist=True
                break
        if(isExist):
            break
    if(not isExist):
        output.append(item)
        print(item, "not exist 1")

      
for row in desCol.iloc:
	rowArr = str(row).split(',')
	for item2 in desCol2:
		isExist=False
		for item in rowArr:
			if(item2==item):
				isExist=True
				break
		if(isExist):
				break
	if(not isExist):
         output.append(item)
         print(item, "not exist 2")

listToStr = '\n'.join([str(elem) for elem in output])
f = open("output2.txt","w")
f.write(listToStr)
f.close()
