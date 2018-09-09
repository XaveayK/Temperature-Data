'''--------------------------------------------------------
                       Xavier Kidston
-----------------------------------------------------------
Purpose of this is to read temperatures and average them and other things'''



MONTH_LIST = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]



'''
Function: To open and put into a list the temperatures
Parameters: File_name - the name of the file with the months and temps
Returns: temp_dict - A dictionary of temps keyd to the month
'''
def build_temp_dict(file_name):
    
    #Establishes variables to use in later loops
    temp_dict = {}
    list_temp_nums = []
    temp_nums = []
    temperature = []
    temps_list = []
    a_list = []
    
    #Tries to open the file, if it can't prints that it cant
    try:
        temps = open(file_name)
        temps_list = temps.read().splitlines()
        
    except:
        print("The file", file_name, "does not exist or can't be read.")
        return
    
    #Creates a list of lists, each list contains the month, split from the string of
    #the numbers
    for i in range(len(temps_list)):
        a_list = temps_list[i].split(":")
        temperature.append(a_list)
    
    #splits all of the numbers, and turns them into integers
    for item in temperature:
        temp_nums = []
        list_temp_nums = []
        temp_nums = item[1].split(",")
        for temp in temp_nums:
            list_temp_nums.append(int(temp))
        temp_dict[item[0]] = list_temp_nums
    
    return temp_dict
        
        

'''
Function: To get all temperatures with no replication 
Parameters: month - a string of the month
            temp data - the dictionary of temps keyd to months
Returns: new_set - all the temperatures but only displays each one once
'''
def month_temp(month, temp_data):
    
    #Just sets the data 
    key = temp_data[month]
    new_set = set(key)
    
    return new_set



'''
Function: To get the average temperature of the month 
Parameters: Temp_data - dict of temp data
Returns: common - a set of common temperatures
'''
def common_degrees(temp_data):
    
    #Establishes variables
    counter = 0
    temp_list = []
    common = []
    data = []
    
    #Makes a list of all the temperatures
    for i in range(0, len(MONTH_LIST)):
        temps = temp_data[MONTH_LIST[i]]
        for item in temps:
            temp_list.append(item)
    
    #Puts the list into a set, and resets the variable temp_list
    All_temps = set(temp_list)
    temp_list = []
    
    #puts the above set into a list as to make it indexable.
    for items in All_temps:
        temp_list.append(items)
    
    #Makes a list of each month with only their unique temperatures, and then sets
    #it back to a list
    for month in MONTH_LIST:
        data.append(list(set(temp_data[month])))
        
    #checks how many months the item occurs in, if it is greater than 11 (12)
    #appends the list to include them
    for item in temp_list:
        counter = 0
        for lists in data:
            if item in lists:
                counter += 1
                if counter > 11:
                    common.append(item)
    
    #This just creates only one copy of each unique common temp
    common = set(common)
      
    return common



'''
Function: To get the degrees that only occur in that month
Parameters: Month - the string of the month
            temp_data - the temperature data in a dict
Returns: The set of temperatures that only occured in this month
'''
def rare_degrees(month, temp_data):
    
    #Establishes variables
    counter = 0
    rare = []
    data = []
    
    temp_list = list(set(temp_data[month]))
    
    #Makes a list within a list of each month of data
    for month in MONTH_LIST:
        data.append(list(set(temp_data[month])))
        
    #checks how many months the item occurs in, if it is equal to 1, appends them
    for item in temp_list:
        counter = 0
        for lists in data:
            if item in lists:
                counter += 1
        if counter == 1:
            rare.append(item)
    
    #This just makes it look the same as the output it wants
    rare = set(rare)
      
    return rare    



'''
Function: To get the lowest and highest degree of each month
Parameters: Temp_data - the temperature data
Returns: data_dict - a dictionary that gets min and max temps
'''
def degree_limits(temp_data):
    
    #Establishes variables for later use
    data_dict = {}
    data = ()
    minimum = 0
    maximum = 0
    
    #For each month in the year, it gets the min and max temps, puts that in a tuple, and then puts
    #that into a dictionary with the month
    for month in MONTH_LIST:
        data = ()
        minimum = min(temp_data[month])
        maximum = max(temp_data[month])
        data = minimum, maximum
        data_dict[month] = data
    
    return data_dict



'''
Function: Combines the Q2 base functions to come to work together
Parameters: None
Returns: None
'''
def test_Q2():
    
    #runs through all the helper functions
    temp_dict = build_temp_dict("yearly_temperature.txt")
    month = month_temp('February', temp_dict)
    common = common_degrees(temp_dict)
    rare = rare_degrees('December', temp_dict)
    limits = degree_limits(temp_dict)
    
    #Runs through all the prints
    print("Building the dictionary of temperature data: temps...")
    print()
    print("month_temp('February', temp_dict):", month)
    print("common_degrees(temp_dict):", common)
    print("rare_degrees('December', temp_dict):", rare)
    print("degree_limits(temp_dict):")
    
    #Runs through the loop to print out each month, and then the tuple
    for item in limits:
        print(item + ":", end = ' ')
        print(limits[item])