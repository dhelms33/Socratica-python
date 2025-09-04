#stopped 2:57
import json
#look at methods in module
dir(json)
#json.load() f for file, s from string
json_file = open("F:/data/movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()