import tempfile
import PyPDF2
import re


class extractDataFromFile:
    def __init__(self):
        self.fp = tempfile.TemporaryFile()

    def extractincidents(self, data):
        dataList = []
        self.fp.write(data)
        # Set the curser of the file back to the begining
        self.fp.seek(0)
        # Read the PDF
        pdfReader = PyPDF2.pdf.PdfFileReader(self.fp)
        pageCount = pdfReader.getNumPages()
        print("Page Count:", pageCount)

        for i in range(0, pageCount, 1):
            print("Process started for the page:", i)
            page = pdfReader.getPage(i).extractText()
            if i == 0:
                page = page.replace("NORMAN POLICE DEPARTMENT", "")
                page = page.replace("Daily Incident Summary (Public)", "")
                page = page.replace("Date / Time", "")
                page = page.replace("Incident", "")
                page = page.replace("Number", "")
                page = page.replace("Location", "")
                page = page.replace("Nature", "")
                page = page.replace("Incident", "")
                page = page.replace("ORI", "")
                page = page.strip()
                print("After applying strip method for 1st page:", page)
            if i != 0:
                page = page.strip()
            page = page.replace("14005", "14005;")
            page = page.replace("EMSSTAT", "EMSSTAT;")
            page = page.replace("OK0140200", "OK0140200;")
            page = page.replace("14009", "14009;")
            print("Data after applying replace methods for", i, "page:", page)
            tempDataList = page.split(';\n')
            print("tempDataList for", i, ":", tempDataList)
            for data in tempDataList:
                if data != '' or data != "" or not data:
                    tempData = data.split("\n")
                    print("tempData in if method:", tempData)
                    if tempData[-1] == '14005;':
                        tempData[-1] = '14005'
                    elif tempData[-1] == 'EMSSTAT;':
                        tempData[-1] = 'EMSSTAT'
                    elif tempData[-1] == 'OK0140200;':
                        tempData[-1] = 'OK0140200'
                    elif tempData[-1] == '14009;':
                        tempData[-1] = '14009'
                    print("tempData in if after replacing last element in list to remove semicolon:", tempData)

                    if len(tempData) > 5:
                        print("Entered to trim the list:", tempData)
                        print("Value at index 2:", tempData[2])
                        print("Value at index 3:", tempData[3])
                        str1 = tempData[2] + tempData[3]
                        print("Value in str1:", str1)
                        tempData[2] = str1
                        del tempData[3]
                        print("List after deletion:", tempData)

                    if len(tempData) == 3:
                        strDate = tempData[0]
                        print("Date value:", strDate)
                        check = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", strDate)
                        print("Check Value:", check)
                        if check != '' or check != 0 or check is not None and tempData[3] == '14005' or tempData[3] == 'EMSSTAT' or tempData[3] == 'OK0140200' or tempData[3] == '14009':
                            tempData.insert(2, 'Null')
                            tempData.insert(3, 'Null')
                    print("tempData Value before adding to the final list:", tempData)
                    dataList.append(tempData)
        print("Final List:", dataList)
        print("Length of final dataList:", len(dataList))
        return dataList
