import csv
import json

csv_file = 'test.json'
print(csv_file)


def make_json(csvFilePath, jsonFilePath):
    # create a dictionary

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        print(csvReader)
        jsonArray = []
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            print(rows)
            # exit()
            jsonArray.append(rows)
            print(jsonArray)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(jsonArray, indent=4))


# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'employees.csv'
jsonFilePath = r'employees.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)