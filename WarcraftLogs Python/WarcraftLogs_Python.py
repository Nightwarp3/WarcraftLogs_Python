import datetime as dt
import LogsAPIRequests as la
import MySqlRequests as mydb

"""
#   http://docs.sqlalchemy.org/en/latest/core/tutorial.html
"""

def ReportData():
    report_id = input("Please enter the Report ID:\n")
    view = input("Please enter one of the following: damage-done|healing|damage-taken:\n")

    engine = mydb.SetUpEngine('admin', 'password1')

    log_end = mydb.SelectLogTime(report_id, engine)
    report_data = la.getReportData(view, report_id, log_end)
    converted_date = FormatUnixTime(log_end)
    
    char_list = list()
    for char in report_data['entries']:
        if('itemLevel' in char.keys()):
            char_list.append({ 'CharacterName': char['name'], 'CharacterID': char['guid'], 'Class-Spec': char['icon'], 'item_level': char['itemLevel'], 'report_date': converted_date })
        else:
            char_list.append({ 'CharacterName': char['name'], 'CharacterID': char['guid'], 'Class-Spec': char['icon'], 'item_level': 0, 'report_date': converted_date })

    character = mydb.DefineCharTable()
    mydb.Insert(character, char_list, engine)
    engine.dispose()
    print("Insert successful.")


def UsernameConsole():
    username = input("Warcraft Logs Username:")
    nightwarp_logs = la.getUsersReports(username)

    if (len(nightwarp_logs) == 0):
        print("getLogsByUsername has not returned any values. Please try again")
        input("Press enter to exit...")
        exit()
    answer = input("Should this be entered into the DB? (Y|N)")

    if (answer.lower() == "y"):
        db_credentials = DBCreds()
        parsed_logs = list()
        for log in nightwarp_logs:
            parsed_logs.append( {"log_id": log["id"], "owner": log["owner"], "zone_id": log["zone"], "log_title": log["title"], "log_end_time": log["end"] })
        
        engine = mydb.SetUpEngine(db_credentials[0], db_credentials[1])
        log_reports = mydb.DefineReportsTable()
        mydb.Insert(log_reports, parsed_logs, engine)
        engine.dispose()
        print("Insert successful.")


def DBCreds():
    dbuser = input("Please enter USERNAME for DB access:")
    dbpass = input("Please enter PASSWORD for DB access:")

    return [dbuser, dbpass]


def FormatUnixTime(timestamp):
    count = 0
    unixtime = ""
    for char in timestamp:
        if(count < len(timestamp) - 3):
            unixtime += char
            count += 1
    
    date = dt.datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d')
    return date


#if __name__ == '__main__':
#    run = True
#    while(run):
#        program = input("Please enter one of the following: InsertUserLogs, GetReportData, InsertGuildLogs, exit: \n")
#        if (program.lower() == "insertuserlogs"):
#            UsernameConsole()
#        elif(program.lower() == "getreportdata"):
#            ReportData()
#        elif(program.lower() == "insertguildlogs"):
#            print("Not implemented yet...")
#        elif(program.lower() == "exit"):
#            break;
#    print("Exiting Program...")
#    exit()
