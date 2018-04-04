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

def DefineMappingTable():
    metadata = sql.MetaData()
    mapping_table = sql.Table('zone_mapping', metadata,
                              sql.Column('id', sql.Integer()),
                              sql.Column('zone_name', sql.String(45)),
                              sql.Column('parent_id', sql.Integer()),
                              sql.Column('parent_name', sql.String(45))
                              )
    return mapping_table

def DefineCharSpecTable():
    metadata = sql.MetaData()
    char_spec_table = sql.Table('class_spec_mapping', metadata,
                                sql.Column('id', sql.Integer()),
                                sql.Column('class_name', sql.String(45)),
                                sql.Column('spec', sql.String(45)),
                                sql.Column('class_id', sql.Integer()),
                                sql.Column('spec_id', sql.Integer())
                                )
    return char_spec_table

def SelectLogTime(log, engine):
    table = DefineReportsTable()
    select = sql.select([table.c.log_end_time]).where(table.c.log_id == log)

    conn = engine.connect()
    rows = conn.execute(select)
    result_row = rows.first()
    result = result_row[0]
    conn.close()
    return result

def GetEncounter(encounterID):
    table = DefineMappingTable()
    engine = SetUpEngine('admin', 'password1')
    select = sql.select([table.c.zone_name, table.c.parent_name]).where(table.c.id == encounterID)

    conn = engine.connect()
    rows = conn.execute(select)
    result_row = list()
    for row in rows:
        result_row.append(row)
    conn.close()
    return result_row

def GetClassSpec(classid, specid):
    table = DefineCharSpecTable()
    engine = SetUpEngine('admin', 'password1')
    select = sql.select([table.c.class_name, table.c.spec]).where(table.c.class_id == classid and table.c.spec_id == specid)

    conn = engine.connect()
    rows = conn.execute(select)
    result = list()
    for row in rows:
        result.append(row)
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


