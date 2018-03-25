## 2. Parsing the File ##

weather_data = []
file = open("la_weather.csv","r")
contents = file.read()
split_row = contents.split('\n')
for row in split_row:
    splited = row.split(",")
    weather_data.append(splited)
    

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for item in weather_data:
    value = item[1]
    weather.append(value)

## 4. Counting the Items in a List ##

count = 0
for item in weather:
    count+=1

## 5. Removing the Header ##

new_weather = weather[1:366]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for weather in weather_types:
    content =  weather in new_weather
    weather_type_found.append(content)