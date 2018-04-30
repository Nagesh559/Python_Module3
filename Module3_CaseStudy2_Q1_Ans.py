import csv
bankData = open("C:\\Temp\\bank-data.csv", "r")
# Set up CSV reader and process the header
csvReader = csv.reader(bankData)
header = csvReader.next()
ageIndex = header.index("age")
jobIndex = header.index("job")
maritalIndex = header.index("marital")
yIndex = header.index("y")

# Make an empty list
customerList = []
jobList=['management','admin','entrepreneur','services','self-employed']
# Loop through the lines in the file and get each coordinate
for row in csvReader:
    age = row[ageIndex]
    job = row[jobIndex]
    # marital = row[maritalIndex]
    # y  = row[yIndex]
    customerList.append([age, job])

print customerList
# strjob=raw_input('Enter profession to check:')
# for itm in customerList:
#     if strjob == itm:
#         print itm
