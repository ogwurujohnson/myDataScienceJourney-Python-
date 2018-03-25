three_rows = ["Davido,749","Isaac,371","Gloria,828"]
final_list = []

for row in three_rows:
    particular_list = row.split(',')
    final_list.append(particular_list)
print(final_list)
print(final_list[0])
