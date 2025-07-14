from email import contentmanager
import os
import sys
import csv
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

except UnicodeDecodeError:
    # Find Problem Line
    with open(file, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            name = row[1]
            if name.strip() == 'DAIRYMAID NESTLÉ ROLO 90ML':
                line_number = reader.line_num
                line_data = row
                line_data[1] = 'DAIRYMAID NESTLE ROLO 90ML'
                new_line_data = ', '.join(line_data) + '\n'

    # Change Problem Line
    with open(file, 'r') as f:
        content = f.readlines()
    
    content[line_number - 1] = new_line_data

    # Write New Line To CSV File 
    with open(file, 'w') as f:
        f.writelines(content)

    print('UnicodeDecodeError, Re-encoding...')

    # Get Data Into Dataframe
    data = pd.read_csv(file, skip_blank_lines=True, dtype=str, keep_default_na=False)
     
except Exception as error:
    print(f'Somthing went wrong: {error}')
    os.system('pause')
    sys.exit(1)

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

# Coffees That Use Milk
def milk():
	coffee_list = ['BEAN COFFEE MACHINE',
                    'LAVAZZA AMERI W/MILK 250ML',
                    'LAVAZZA AMERICANO W/MILK 3',
                    'LAVAZZA CAPPUCCINO 250ML',
                    'LAVAZZA CAPPUCCINO 350ML',
                    'LAVAZZA HOT CHOCOLATE 350M',
                    'LAVAZZA ICED COFFEE 350ML',
                    'LAVAZZA ICED COFFEE 250ML',
                    'LAVAZZA MOCHACCINO 350ML',  
                    'ROOIBOS TEA 350ML',         
                    'ROOIBOS TEA 250ML',
                    'PANCAKE (FPG)'             
                    ]

	total_coffees = 0.0

	total_pancakes = 0.0
	
	for name, quantity in coffees.items():
		if name in coffee_list:
			if name == 'PANCAKE (FPG)':
				total_pancakes += quantity
			else:
				total_coffees += quantity

	return total_coffees, total_pancakes

# Coffees For Vending Machine    
def bean_coffee():
    coffee_list = ['BEAN COFFEE MACHINE']
     
    total_coffees = 0.0

    for name, quantity in coffees.items():
          if name in coffee_list:
              total_coffees += quantity
    
    return total_coffees

# Fresh Made Coffees
def lavazza_coffee():
    coffee_list = ['LAVAZZA AMERI W/MILK 250ML',
                    'LAVAZZA AMERICANO 250ML',
                    'LAVAZZA AMERICANO 350ML',
                    'LAVAZZA AMERICANO W/MILK 3',
                    'LAVAZZA CAPPUCCINO 250ML',
                    'LAVAZZA CAPPUCCINO 350ML',
                    'LAVAZZA ESPRESSO',
                    'LAVAZZA ICED COFFEE 350ML',
                    'LAVAZZA ICED COFFEE 250ML',
                    'LAVAZZA MOCHACCINO 350ML'
                    ]
     
    total_coffees = 0.0

    for name, quantity in coffees.items():
          if name in coffee_list:
              total_coffees += quantity

    return total_coffees

# All Coffees For Sugar Use
def coffee_sugar():
    coffee_list = ['BEAN COFFEE MACHINE',
                    'LAVAZZA AMERI W/MILK 250ML',
                    'LAVAZZA AMERICANO 250ML',
                    'LAVAZZA AMERICANO 350ML',
                    'LAVAZZA AMERICANO W/MILK 3',
                    'LAVAZZA CAPPUCCINO 250ML',
                    'LAVAZZA CAPPUCCINO 350ML',
                    'LAVAZZA ESPRESSO',
                    'LAVAZZA HOT CHOCOLATE 350M',
                    'LAVAZZA MOCHACCINO 350ML',
                    'LAVAZZA ICED COFFEE 350ML',
                    'LAVAZZA ICED COFFEE 250ML',
                    'ROOIBOS TEA 350ML',
                    'ROOIBOS TEA 350ML',
                 ]
     
    total_coffees = 0.0

    for name, quantity in coffees.items():
          if name in coffee_list:
              total_coffees += quantity

    return total_coffees
#  ########################################################################
#  USER INTERFACE
#  ########################################################################

while True:
    print()
    print('Push any other button to exit!')
    print('Data Loaded in please select one of the follwing options:')
    print('1 - Coffees that use milk')
    print('2 - Bean coffees')
    print('3 - Lavazza Coffee')
    print('4 - Total Coffee Sales For Sugar')

    user = input('Please select an option: ')

    if user == '1':
        print()
        print('***********************************')
        print(f'Coffees That Use Milk = {milk()[0]} and Pancakes Mande {milk()[1]}')
        print('***********************************')
    elif user == '2':
        print()
        print('***********************************')
        print(f'Bean Coffees = {bean_coffee()}')
        print('***********************************')
    elif user == '3':
        print()
        print('***********************************')
        print(f'Lavazza Coffees = {lavazza_coffee()}')
        print('***********************************')
    elif user == '4':
        print()
        print('***********************************')
        print(f'Total Coffees Sales For Sugar = {coffee_sugar()}')
        print('***********************************')
    else:
        print()
        print('Exiting Program...')
        break