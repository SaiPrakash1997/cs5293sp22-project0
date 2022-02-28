import sqlite3
from project0.extractIncidents import extractDataFromFile
from project0.incidentsDB import incidentDataBase


def test_extractsIncidents():
    localFileData = open('2022-01-01_daily_incident_summary.pdf', 'rb')
    print(localFileData)
    extractData = extractDataFromFile()
    dataList = extractData.extractincidents(localFileData.read())
    assert len(dataList) != 0
    assert len(dataList) == 262


def test_populatedDB():
    fetch_sql = "select count(*) from incidents; "
    localFileData = open('2022-01-01_daily_incident_summary.pdf', 'rb')
    extractData = extractDataFromFile()
    dataList = extractData.extractincidents(localFileData.read())
    incidentObj = incidentDataBase()
    incidentObj.populatedb(dataList)
    dbName = "normanpd.db"
    con = sqlite3.connect(dbName)
    sql_cursor = con.cursor()
    sql_cursor.execute(fetch_sql)
    result = sql_cursor.fetchall()
    print(result)
    assert result[0][0] == 261


def test_status():
    incidentObj = incidentDataBase()
    result = incidentObj.status()
    assert result != 0
    assert len(result) > 1


def test_createdb():
    incidentObj = incidentDataBase()
    con = incidentObj.createdb()
    assert con is not None





