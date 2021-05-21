#!/usr/bin/env python
# coding: utf-8



import requests 
import json
from bs4 import BeautifulSoup as bs
import re
import csv



url_bulbapedia="https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_National_Pokédex_number"

response_bulba=requests.get(url_bulbapedia)
soup = bs(response_bulba.text, 'html.parser')

names=[]

list_pkmn= soup.findAll("a",{"title":re.compile('.(Pokémon)')})

for x in list_pkmn:
    poke_name=x.text
    names.append(poke_name.lower())
    

final_names= list(dict.fromkeys(names))



pokemon_list=[]
pokemon_details=[]
def webIterate():
    for i in final_names:
        try:
            url2="https://pokeapi.co/api/v2/pokemon/{}".format(i)
            response=requests.get(url2)
            data=response.text
            parsed=json.loads(data)
            id=parsed["id"]
            name=parsed["name"]
            height=parsed["height"]
            weight=parsed["weight"]
            base=parsed["base_experience"]
            pokemon_list.append(['{},{}'.format(name,id)])
            pokemon_details.append(['{},{},{},{},{}'.format(name,id,height,weight,base)])
        except:
            pass
webIterate()





row_list = pokemon_list
with open('pokemon_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

row_details=pokemon_details
with open('pokemon_details.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_details)





