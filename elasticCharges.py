import pandas as pd
import matplotlib.pyplot as plt

# Purpose and Usage
print()
print("--This bush league script outputs a bush league graph of spend by day.")
print("--You'll need to supply a 2-column CSV with \"Date\" and \"Subtotal ($)\" column headers.")
print("--Dates should be in mm/dd/yy format.")
print()

# Prompt the user for the CSV file path
file_path = input("Please enter the path to your CSV file: ")

# Load the data from the provided CSV file path
data = pd.read_csv(file_path)

# Convert the 'Date' column to a datetime type for proper sorting and display
data['Date'] = pd.to_datetime(data['Date'], format = '%m/%d/%y')

# Sorting data by date in case it's not sorted in the CSV
data.sort_values('Date', inplace=True)

# Plotting the bar chart
plt.figure(figsize=(10, 6))  # Set the figure size as needed
bars = plt.bar(data['Date'].dt.strftime('%m/%d/%Y'), data['Subtotal ($)'], color='blue')  # Formatting the date display

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Subtotal ($)')
plt.title('Elastic Charges by Day')

# Annotate each bar with the respective data value
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

# Rotate date labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()

