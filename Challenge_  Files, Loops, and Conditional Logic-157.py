## 3. Read the File Into a String ##

file = open("dq_unisex_names.csv","r")
names = file.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()

names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##


f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')

nested_list = []
for single in names_list:
    singlelist = single.split(',')
    nested_list.append(singlelist)
print(nested_list[0:5])

## 6. Convert Numerical Values ##


numerical_list = []

for singlelist in nested_list:
    a = singlelist[0]
    b = singlelist[1]
    con_b = float(b)
    c = [a,con_b]
    numerical_list.append(c)
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = []
greater = 0
for names in numerical_list:
    if (names[1] >= 1000):
        greater = names[0]
        thousand_or_greater.append(greater)
print(thousand_or_greater[0:5])
    