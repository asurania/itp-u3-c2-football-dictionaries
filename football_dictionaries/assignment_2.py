# Data
from football_dictionaries.squads_data import SQUADS_DATA

def players_by_position(squads_list):
    results = {}
    for player in squads_list:
        squad = {}
        squad['number']=player[0]
        squad['position']=player[1]
        squad['name']=player[2]
        squad['date_of_birth'] =player[3]
        squad['caps'] =player[4]
        squad['club']=player[5]
        squad['country']=player[6]
        squad['club_country']=player[7]
        squad['year']=player[8]
        position = player[1]
        results.setdefault(position,[])
        results[position].append (squad)
    return results
