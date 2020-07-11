from django.shortcuts import render
from python_graphql_client import GraphqlClient
import requests

client = GraphqlClient(endpoint="https://integracion-rick-morty-api.herokuapp.com/graphql")
# Requests for APi rick and Morty

def episodes(term):
    query = """
                query episodeQuery($name: String) {
                  episodes(filter: {name: $name}) {
                    info {
                      count
                    }
                    results {
                      name
                      episode
                    }
                  }
                }
            """
    variables = {"name": term}
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    if('errors' in data.keys()):
        episodes = None
    else:
        episodes = data['data']['episodes']['results']
    return episodes

def lugares(term):
    query = """
                    query episodeQuery($name: String) {
                      locations(filter: {name: $name}) {
                        info {
                          count
                        }
                        results {
                          name
                          id
                        }
                      }
                    }
                """
    variables = {"name": term}
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    if('errors' in data.keys()):
        lugares = None
    else:
        lugares = data['data']['locations']['results']
    return lugares

def caracteres(term):
    query = """
                        query episodeQuery($name: String) {
                          characters(filter: {name: $name}) {
                            info {
                              count
                            }
                            results {
                              name
                              id
                            }
                          }
                        }
                    """
    variables = {"name": term}
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    if('errors' in data.keys()):
        caracteres = None
    else:
        caracteres = data['data']['characters']['results']
    return caracteres

# Create your views here.

def home(request):
    query = """
        query {
          episodes {
            info {
              count
            }
            results {
              name
              id
              air_date
              episode
            }
          }
        }
    """

    # Synchronous request
    data = client.execute(query=query)
    episodes = data['data']['episodes']['results']
    contexto = {'episodios': episodes}
    return render(request, "Episodios.html", contexto)

def episode_view(request, code):
    print(code)
    query = """
            query episodeQuery($episode: String) {
              episodes(filter: {episode: $episode}) {
                info {
                  count
                }
                results {
                  name
                  id
                  air_date
                  episode
                  characters {
                    name
                    id
                  }
                }
              }
            }
        """
    variables = {"episode": code}
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    print(data['data']['episodes']['results'])
    contexto = {'episodio': data['data']['episodes']['results'][0]}
    return render(request, "UnEpisodio.html", contexto)

def character_view(request, id_character):
    query = """
                query characterQuery($id: ID!) {
                  character(id: $id) {
                    id
                    name
                    image
                    status
                    species
                    type
                    gender
                    location {
                      name
                      id
                    }
                    origin {
                      id
                      name
                      residents {
                        id
                        name
                      }
                    } 
                    episode {
                      name
                      episode
                    }
                  }
                }
            """
    variables = {"id": id_character}
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    print(data)
    contexto = {'caracter': data['data']['character']}
    return render(request, "UnCaracter.html", contexto)

def location_view(request, id_lugar):
    query = """
                    query characterQuery($id: ID!) {
                      location(id: $id) {
                        name
                        id
                        dimension
                        residents {
                          name
                          id
                        }
                        type
                      }
                    }
                """
    variables = {"id": id_lugar}
    # Synchronous request
    data = client.execute(query=query, variables=variables)
    print(data)
    contexto = {'lugar': data['data']['location']}
    return render(request, "UnLugar.html", contexto)

def searchBar(request):
    term = request.GET.get('term')
    episodesMatch = episodes(term)
    locationsMatch = lugares(term)
    charactersMatch = caracteres(term)
    contexto = {'episodios': episodesMatch, 'term': term, 'lugares': locationsMatch, 'caracteres': charactersMatch}
    return render(request, "Search.html", contexto)