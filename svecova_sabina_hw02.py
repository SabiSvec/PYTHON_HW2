

import json

data = []

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as file:
    for line in file:
        line = line.strip().split("\t")
        data.append(line)

header = data[0]
rows = data[1:]

title_idx = header.index('PRIMARYTITLE')
director_idx = header.index('DIRECTOR')
cast_idx = header.index('CAST')
genres_idx = header.index('GENRES')
year_idx = header.index('STARTYEAR')

film_list = []
 
for row in rows:
    title = row[title_idx]

    if row[director_idx] == "":
        director = []
    else:
        director = row[director_idx].split(', ')

    if row[cast_idx] == "":
        cast = []
    else:
        cast = row[cast_idx].split(', ')

    genres = row[genres_idx].split(',')

    decade = (int(row[year_idx]) // 10) * 10
    
    film = {
    "title": title,
    "directors": director,
    "cast": cast,
    "genres": genres,
    "decade": decade
    }

    film_list.append(film)

with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(film_list, file,ensure_ascii=False, indent=4)