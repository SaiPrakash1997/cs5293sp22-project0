import sqlite3


class incidentDataBase:
    sql_drop_table_query = "drop table if exists 'incidents';"
    sql_create_table_query = "create table incidents ( incident_time TEXT, incident_number TEXT, incident_location TEXT, incident_nature TEXT, incident_ORI TEXT);"
    sql_insert_into_table_query = "insert into incidents(incident_time, incident_number, incident_location, incident_nature, incident_ORI) values(?, ?, ?, ?, ?);"
    sql_count_nature_of_incident_query = "select count(incident_nature) as number, incident_nature from incidents group by incident_nature order by incident_number desc, incident_nature asc;"

    def __init__(self):
        self.databaseName = 'normanpd.db'

    def createdb(self):
        try:
            con = sqlite3.connect(self.databaseName)
        except (sqlite3.Error, RuntimeError) as exception:
            print("Error Message while establishing a connection:", exception.args)
        return con

    def populatedb(self, dataList):
        try:
            con = sqlite3.connect(self.databaseName)
        except (sqlite3.Error, RuntimeError) as exception:
            print("Error Message while establishing a connection:", exception.args)
        print("Connected to database......")
        con.execute(self.sql_drop_table_query)
        con.execute(self.sql_create_table_query)
        cursorObj = con.cursor()
        count = 0
        for i in range(0, (len(dataList)-1), 1):
            cursorObj.execute(self.sql_insert_into_table_query, (dataList[i][0], dataList[i][1], dataList[i][2], dataList[i][3], dataList[i][4]))
            count += 1
        print("Total number of rows inserted:", count)
        con.commit()
        cursorObj.close()
        con.close()

    def status(self):
        try:
            con = sqlite3.connect(self.databaseName)
        except sqlite3.Error as exception:
            print("Error Message while establishing a connection:", exception.args)
        print("Connected to database......")
        cursorObjToFetchIncidents = con.cursor()
        cursorObjToFetchIncidents.execute(self.sql_count_nature_of_incident_query)
        dataFetchedFromDatabase = cursorObjToFetchIncidents.fetchall()
        print("Incident\t", "Count")
        for data in dataFetchedFromDatabase:
            print(data[1], "|", data[0])
        cursorObjToFetchIncidents.close()
        con.close()
        return dataFetchedFromDatabase






