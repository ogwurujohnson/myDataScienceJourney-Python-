split_list = []
filename = input("Enter File name")
searchkeyword = input("Search Keyword")
file = open(filename,'r')
content = file.read()
split_content = content.split('\n')
for item in split_content:
    split_item = item.split(',')
    split_list.append(split_item)

if searchkeyword in split_list:
    print(searchkeyword+"found")
