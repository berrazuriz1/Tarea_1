from django.shortcuts import render
from django.http import HttpResponse
import requests

# Requests for APi rick and Morty

def episodes(term):
    episodesMatch = requests.get('https://rickandmortyapi.com/api/episode/?name=' + term).json()
    if('error' in episodesMatch):
        episodes = None
    else:
        episodes = episodesMatch['results']
    return episodes

def lugares(term):
    locationsMatch = requests.get('https://rickandmortyapi.com/api/location/?name=' + term).json()
    if('error' in locationsMatch):
        lugares = None
    else:
        lugares = locationsMatch['results']
    return lugares

def caracteres(term):
    charactersMatch = requests.get('https://rickandmortyapi.com/api/character/?name=' + term).json()
    if('error' in charactersMatch):
        caracteres = None
    else:
        caracteres = charactersMatch['results']
    return caracteres

# Create your views here.

def home(request):
    r = requests.get("https://rickandmortyapi.com/api/episode").json()
    episodios = r['results']
    for page in range(1,r['info']['pages']+1):
        episodios += (requests.get(r['info']['next']).json()['results'])
    contexto = {'episodios': episodios, 'tipo': 'episodios'}
    return render(request, 'Episodios.html', contexto)

def episode_view(request, id_episodio):
    r = requests.get("https://rickandmortyapi.com/api/episode/" + str(id_episodio)).json()
    characters = []
    for characther in r["characters"]:
        characters.append(requests.get(characther).json())
    r['characters'] = characters
    contexto = {'episodio': r}
    return render(request, "UnEpisodio.html", contexto)

def character_view(request, id_character):
    r = requests.get("https://rickandmortyapi.com/api/character/" + str(id_character)).json()
    episodes= []
    for episode in r["episode"]:
        episodes.append(requests.get(episode).json())
    r['episode'] = episodes
    if (not r['origin']['name'] == 'unknown'):
        r['origin'] = requests.get(r['location']['url']).json()
    if (not r['location']['name'] == 'unknown'):
        r['location'] = requests.get(r['location']['url']).json()
    contexto = {'caracter': r}
    return render(request, "UnCaracter.html", contexto)

def location_view(request, id_lugar):
    r = requests.get("https://rickandmortyapi.com/api/location/" + str(id_lugar)).json()
    characters = []
    for characther in r["residents"]:
        characters.append(requests.get(characther).json())
    r['residents'] = characters
    contexto = {'lugar': r}
    return render(request, "UnLugar.html", contexto)

def searchBar(request):
    term = request.GET.get('term')
    episodesMatch = episodes(term)
    locationsMatch = lugares(term)
    charactersMatch = caracteres(term)
    contexto = {'episodios': episodesMatch, 'term': term, 'lugares': locationsMatch, 'caracteres': charactersMatch}
    return render(request, "Search.html", contexto)