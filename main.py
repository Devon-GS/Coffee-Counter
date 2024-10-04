import pandas as pd

data = pd.read_csv('1 - Resource/coffee.csv', skip_blank_lines=True, dtype=str, keep_default_na=False)

# Extract columns and strip white space
coffee_extract = data.iloc[:, [1, 6]].values.tolist()

coffee_extracted_list = []
coffee_extracted_list_names = []

for x in coffee_extract:
    name = x[0].strip()
    quantity = x[1].strip()
    if name != 'Stock Description':
        if name != '':
            coffee_extracted_list.append([name, quantity])
            coffee_extracted_list_names.append(name)

# Remove duplicate
coffee_names_filtered = list(set(coffee_extracted_list_names))

# Create dic and add totals 
coffees = {}

for x in coffee_names_filtered:
    if x !='':
        coffees[x] = 0
    
for x in coffee_extracted_list:
        coffees[x[0]] += float(x[1])

#  ########################################################################

# Coffees that use milk
def milk():
     milk_list = ['LAVAZZA AMERICANO W/MILK 3',
                  'LAVAZZA ICED COFFEE 350ML',
                  'LAVAZZA ICED COFFEE 250ML',
                  'BEAN COFFEE MACHINE',
                  'LAVAZZA AMERI W/MILK 250ML',
                  'HOT CHOCOLATE 350ML',
                  'LAVAZZA CAPPUCCINO 250ML',
                  'LAVAZZA CAPPUCCINO 350ML',
                  ]
     
for x in coffees:
     print(x)
          







'''
'ROOIBOS TEA 250ML'
'LAVAZZA AMERICANO W/MILK 3'
'LAVAZZA ICED COFFEE 350ML'
'BEAN COFFEE MACHINE'
'LAVAZZA AMERI W/MILK 250ML'
'HOT CHOCOLATE 350ML'
'LAVAZZA ESPRESSO'
'LAVAZZA AMERICANO 250ML'
'LAVAZZA CAPPUCCINO 250ML'
'LAVAZZA CAPPUCCINO 350ML'
'LAVAZZA AMERICANO 350ML'
'''