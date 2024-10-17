import csv
import matplotlib.pyplot as plt

# Open and read the CSV file
with open('my data.csv', 'r') as file:
    reader = csv.reader(file)

    # Convert the reader object to a list
    data = list(reader)

    # Check if data is empty
    if not data:
        print("The CSV file is empty.")
        exit()

    # First row is the header
    header = data[0]
    rows = data[1:]  # All the other rows

    # Filter and sort the rows based on the year
    filtered_rows = []
    for row in rows:
        try:
            year = int(row[1])  # Attempt to convert year to an integer
            filtered_rows.append(row)  # Append the valid row to filtered_rows
        except ValueError:
            print(f"Skipping row due to invalid year: {row[1]}")  # Print the problematic value

    # Sort the valid rows based on the year
    filtered_rows.sort(key=lambda x: int(x[1]))

    # Separate names and years into two lists
    names = [row[0] for row in filtered_rows]  # Extract names from each row
    years = [int(row[1]) for row in filtered_rows]  # Extract years and convert to integers

# Visualize using a bar chart
plt.bar(names, years, color='skyblue')

# Add labels and title
plt.xlabel('Names')
plt.ylabel('Years')
plt.title('Sorted Years by Name')

# Show the plot
plt.show()
