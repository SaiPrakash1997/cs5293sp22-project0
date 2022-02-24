import argparse
from fetchIncidents import *
from extractIncidents import *
from incidentsDB import *


def main(url):

    fetchIncidentObj = dataFetchedFromURL()
    extractData = extractDataFromFile()
    dataList = extractData.extractincidents(fetchIncidentObj.fetchincidents(url))
    incidentDBObj = incidentDataBase()
    incidentDBObj.populatedb(dataList)
    dataFetchedFromDB = incidentDBObj.status()
    if dataFetchedFromDB is not None:
        print("Operation Successful")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="Incident summary url.")

    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
