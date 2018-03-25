## 1. Opening Files ##

f = open("crime_rates.csv", "r")
content = f.read()
print(content)

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()
print(data)

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)

## 5. Practice - Loops ##

ten_rows = rows[0:10]

for rows in ten_rows:
    print(rows)

## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 7. Practice - Splitting Elements in a List ##

final_data = []
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_list = row.split(',')
    final_data.append(split_list)
print(final_data[0:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list = []
first_elements = five_elements[0][0]
cities_list.append(first_elements)
second_element = five_elements[1][0]
cities_list.append(second_element)
third_element = five_elements[2][0]
cities_list.append(third_element)
fourth_element = five_elements[3][0]
cities_list.append(fourth_element)
fifth_element = five_elements[4][0]
cities_list.append(fifth_element)

## 9. Looping Through a List of Lists ##

cities_list = []

for row in final_data:
   data = row[0]
   cities_list.append(data)

## 10. Challenge ##

int_crime_rates = []

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    singlerow = row.split(',')
    firstletter = singlerow[1]
    intfirstletter = int(firstletter)
    
    int_crime_rates.append(intfirstletter)
