campaign_data = open('C:\\Temp\\bank-data.csv','r')
i = 0;

joblist = set() # empty set to store list of jobs

for data in campaign_data:
    i += 1
    if i == 1 :     # 1st Line is header skip it.
        continue

data = data.rstrip('\n')

#print (" data is:" , data)
# Split the line on comma read the second word as it contains the job name

words = data.split(',')
joblist.add(words[1])

campaign_data.close()
print "List of Jobs Eligible For Campaign:", joblist
client_prof = raw_input('Enter client profession: ')
if (client_prof in joblist):
    print ( "Go Ahead!!! and Make Some Sales !!!! Client is eligible for Tele Calling" )
else:
    print("Skip this one *** Client Needs to be in one of these jobs", joblist)
