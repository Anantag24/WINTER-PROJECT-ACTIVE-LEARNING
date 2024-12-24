import csv

filename = 'data.csv'
data = [
    ["Name", "Age", "Score"],
    ["A", 24, 55],
    ["B", 22, 50],
    ["C", 21, 90],
    ["D", 26, 89],
    ["E", 25, 98]
]

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully.")

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"Rows with Score > 75:")
    for row in reader:
        if int(row[2]) > 75:
            print(row)