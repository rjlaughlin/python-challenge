# Dependencies
import csv
import os

file_directory = os.path.dirname(__file__) #Find directory of script. Reference 1 in README file.
# Files to load and output
file_to_load = os.path.join(file_directory,"Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join(file_directory,"analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')
    # Skip the header row
    header = next(reader)

    # Track the total and net change

    # Process each row of data
    for row in reader:

        # Setting initial criteria for first row of data
        if total_months == 0:
            amount = int(row[1])

        # Setting incremental criteria for data beyond first row
        else:
            net_change = int(row[1]) - amount
            amount = int(row[1])
            net_change_list.append((row[0],net_change))

        # Incrementing total_months and total_net variables
        total_months += 1
        total_net += int(row[1])

# Calculate the greatest increase in profits (month and amount)
max_value = (max([i[1] for i in net_change_list]))
greatest_increase_index = [i[1] for i in net_change_list].index(max_value)
greatest_increase_month = net_change_list[greatest_increase_index][0]

# Calculate the greatest decrease in losses (month and amount)

min_value = (min([i[1] for i in net_change_list]))
greatest_decrease_index = [i[1] for i in net_change_list].index(min_value)
greatest_decrease_month = net_change_list[greatest_decrease_index][0]

# Generate the output text variables and combine to one summary
average_change = f'Average Change: ${round(sum([i[1] for i in net_change_list])/(total_months-1),2)}'

total_months = 'Total Months: ' + str(total_months)

total = 'Total: $' + str(total_net)

greatest_increase = 'Greatest Increase in Profits: ' + greatest_increase_month +' ($' + str(max_value) +')'

greatest_decrease = 'Greatest Decrease in Profits: ' + greatest_decrease_month +' ($' + str(min_value) +')'

output = f'''Financial Analysis 
----------------------------
{total_months} 
{total} 
{average_change}
{greatest_increase}
{greatest_decrease}'''

# Print the output
print('\n' + output + '\n')

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
