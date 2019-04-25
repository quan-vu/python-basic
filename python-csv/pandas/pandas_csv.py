# Reading CSV Files With pandas
import pandas


data = pandas.read_csv('employee.csv')
print(data)
#   firstname lastname department   birth_day
# 0      Quan       Vu         IT  1990-05-01
# 1    Quan 2       Vu         IT  1990-05-01
# 2      John    Smith         HR  1988-01-01


data = pandas.read_csv('employee.csv', index_col='firstname', parse_dates=['birth_day'])
print('\n')
print(data)
#           lastname department  birth_day
# firstname                               
# Quan            Vu         IT 1990-01-05
# Huy             Vu         IT 1990-01-06
# John         Smith         HR 1990-01-07


data = pandas.read_csv('employee.csv', 
        index_col='firstname', 
        parse_dates=['birth_day'], 
        header=0,
    )

# Rename columns
data.columns = ['Lastname','Department', 'Birth day']

# iterating the columns 
for col in data.columns: 
    print(col) 

# list(data) or 
list_columns = list(data.columns) 

# using sorted() method 
sorted(data)

# display  
data  

print('\n List of columns')
print(list_columns)
print('\n')
print(data)
