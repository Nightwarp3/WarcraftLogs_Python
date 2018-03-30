import sqlalchemy as sql

def SetUpEngine(username, password):
    engine = sql.create_engine('mysql+mysqlconnector://' + username + ':' + password + '@localhost/warcraftlogs')
    return engine

def DefineCharTable():
    metadata = sql.MetaData()
    table = sql.Table('character', metadata,
                      sql.Column('CharacterName', sql.String(45)),
                      sql.Column('CharacterID', sql.Integer(), primary_key=True),
                      sql.Column('Class-Spec', sql.String(45)),
                      sql.Column('item_level', sql.Integer()),
                      sql.Column('report_date', sql.Date())
                      )
    return table


def DefineReportsTable():
    metadata = sql.MetaData()
    reports_table = sql.Table('log_reports', metadata,
                              sql.Column('log_id', sql.String(20), primary_key=True),
                              sql.Column('owner', sql.String(45)),
                              sql.Column('zone_id', sql.Integer),
                              sql.Column('log_title', sql.String(45)),
                              sql.Column('log_end_time', sql.String(45))
                              )
    return reports_table

def SelectLogTime(log, engine):
    table = DefineReportsTable()
    select = sql.select([table.c.log_end_time]).where(table.c.log_id == log)

    conn = engine.connect()
    rows = conn.execute(select)
    result_row = rows.first()
    result = result_row[0]
    conn.close()
    return result

def Insert(table, list_dict, engine):
    conn = engine.connect()
    result = conn.execute(table.insert(), list_dict)

    if(result != ""):
        print("Insert Successful!")
        conn.close()
    else:
        print("Insert Unsuccessful")
        conn.close()

