import pandas as pd

#  ########################################################################
#  READ IN DATA AND PULL OUT NEEDED INFORNATION
#  ########################################################################

try:
    cwd_list = os.listdir()

    file_names = []
    for x in cwd_list:
        if '.csv' in x:
            file_names.append(x)
    
    if len(file_names) == 0: 
        raise Exception("No .csv files in directory")

    if len(file_names) > 1:
        raise Exception("Too many .csv files in directory")
        
    file = file_names[0]
        
    data = pd.read_csv(file, skip_blank_lines=True, dtype=str, keep_default_na=False)
     
except Exception as error:
    print(f'Somthing went wrong: {error}')

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
#  FUNCTIONS
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
     
    total_coffees = 0.0

    for name, quantity in coffees.items():
          if name in milk_list:
              total_coffees += quantity

    return total_coffees

# Coffees for vending machine    
def bean_coffee():
    milk_list = ['BEAN COFFEE MACHINE']
     
    total_coffees = 0.0

    for name, quantity in coffees.items():
          if name in milk_list:
              total_coffees += quantity
    
    return total_coffees

# Fresh made coffees
def lavazza_coffee():
    milk_list = ['LAVAZZA AMERICANO W/MILK 3',
                 'LAVAZZA ICED COFFEE 350ML',
                 'LAVAZZA ICED COFFEE 250ML',
                 'LAVAZZA AMERI W/MILK 250ML',
                 'LAVAZZA ESPRESSO',
                 'LAVAZZA AMERICANO 250ML',
                 'LAVAZZA CAPPUCCINO 250ML',
                 'LAVAZZA CAPPUCCINO 350ML',
                 'LAVAZZA AMERICANO 350ML',
                 ]
     
    total_coffees = 0.0

    for name, quantity in coffees.items():
          if name in milk_list:
              total_coffees += quantity

    return total_coffees

#  ########################################################################
#  USER INTERFACE
#  ########################################################################