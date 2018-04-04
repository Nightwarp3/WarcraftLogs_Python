import datetime as dt
import math
from WarcraftLogsPython import LogsAPIRequests as la, MySqlRequests as mydb

"""
#   http://docs.sqlalchemy.org/en/latest/core/tutorial.html
"""

def GetRankData(name, server, region):
    rankings_json = la.getCharacterRanking(name.lower(), server.lower(), region.lower())
    data_list = list()
    for fight in rankings_json:
        class_spec = mydb.GetClassSpec(fight['class'], fight['spec'])
        encounter = mydb.GetEncounter(fight['encounter'])
        date = FormatUnixTime(fight['startTime'])
        difficulty = EncounterDifficulty(fight['difficulty'])
        parse = math.ceil(fight['rank'] / fight['outOf'] * 100)

        data_list.append({ 'boss': encounter[0][0],
                          'zone': encounter[0][1],
                          'class': class_spec[0][0],
                          'spec': class_spec[0][1],
                          'rank': fight['rank'],
                          'parse': parse,
                          'dps': fight['total'],
                          'item_level': fight['itemLevel'],
                          'date': date
                          })
        return data_list


def FormatUnixTime(timestamp):
    count = 0
    unixtime = ""
    for char in timestamp:
        if(count < len(timestamp) - 3):
            unixtime += char
            count += 1
    
    date = dt.datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d')
    return date

def EncounterDifficulty(difficulty):
    if(difficulty == '1'):
        return 'LFR'
    elif(difficulty == '2'):
        return 'Unkown'
    elif(difficulty == '3'):
        return 'Normal'
    elif(difficulty == '4'):
        return 'Heroic'
    else:
        return 'Mythic'
