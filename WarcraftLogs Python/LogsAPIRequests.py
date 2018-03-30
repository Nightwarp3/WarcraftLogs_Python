import json, requests

# Warcraft Logs Public API Key
# d61ae7109219494d4b032246eec72339
params = { 'api_key': 'd61ae7109219494d4b032246eec72339' }
base_url = 'https://www.warcraftlogs.com:443/v1'

def getLogRankingsByID(encounter_id):
    # Gathers the rankings by Encounter ID (found by calling getEncounterIDs())
    url = base_url + '/rankings/encounter/' + encounter_id
    response = requests.post(url, params=params)

    return response.json()

def getCharacterRanking(char_name, server_name, region):
    # Gathers the rankings for specified character
    url = base_url + '/rankings/character/' + char_name + '/' + server_name + '/' + region
    response = requests.post(url, params=params)

    return response.json()

def getEncounterIDs():
    # Gathers the Encounters and their associated IDs
    response = requests.post(base_url + '/zones', params=params)
    
    return response.json()

def getCharacterParses(char_name, server_name, region):
    # Gathers the parses for the specified character
    url = base_url + '/parses/character/' + char_name + '/' + server_name + '/' + region
    response = requests.post(url, params=params)

    return response.json()

def getGuildReports(guild_name, server_name, region):
    # Gathers the uploaded reports by Guild
    valid_guild = parseParameters(guild_name)
    url = base_url + '/reports/guild/' + valid_guild + '/' + server_name + '/' + region
    response = requests.post(url, params=params)

    return response.json()

def getUsersReports(user_name):
    url = base_url + '/reports/user/' + user_name
    response = requests.post(url, params=params)

    return response.json()

def parseParameters(param):
    parsed_value = param.replace(' ', '%20')
    return parsed_value

def getFightsbyReport(report_id):
    url = base_url + '/report/fights' + report_id
    response = requests.post(url, params=params)

    return response.json()

def getReportData(view, report_id, end):
    url = base_url + '/report/tables/' + view + '/' + report_id + '?end=' + end
    response = requests.post(url, params=params)

    return response.json()

def getZoneData():
    url = base_url + '/zones'
    response = requests.post(url, params=params)

    return response.json()