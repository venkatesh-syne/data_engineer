import csv


# Open the CSV file for reading
with open('employees.csv', mode='r') as file:
    reader = csv.reader(file)
    # print(reader)
    print(type(reader))
    next(reader)  # Skipping Unnecessary Rows

    # Iterate through each row in the CSV
    for row in reader:
        print(type(row))
        print(f"{row[0]}, {row[2]},{row[3]}")