## 1. Overview ##

file = open("movie_metadata.csv",'r')
content = file.read()
firstsplit = content.split('\n')
movie_data = []
for item in firstsplit:
    splititem = item.split(',')
    movie_data.append(splititem)
print(movie_data[0:4])

## 3. Writing Our Own Functions ##

movie_names = []
def movies(list_name):
    for item in list_name:
        movie_names.append(item[0])
    return movie_names

first_movies = movies(movie_data)
print(first_movies[0:4])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if(input_lst[6] == 'USA'):
        return True
    else:
        return False
wonder_woman_usa = is_usa(wonder_woman)  

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
def index_equals_str(list_name,list_index,string_name):
    if list_name[list_index] == string_name:
        return True
    else:
        return False
wonder_woman_in_color = index_equals_str(wonder_woman,2,'Color')