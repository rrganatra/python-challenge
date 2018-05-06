import csv
import os

# choose 1 or 2
file_num = 1

file = os.path.join('budget_data_'+ str(file_num) +'.csv')

months = []
revenue = []

with open(file, newline="") as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first revenue entry
#set total revenue = 0 
greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_revenue = 0

#loop through revenue indices and compare # to find greatest inc and dec
#also add each revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_decrease:
        greatest_decrease = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

average_change = round(total_revenue/total_months, 2)

#sets path for output file
output_dest = os.path.join('pybank_output_' + str(file_num) + '.txt')

# opens the output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_decrease) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())