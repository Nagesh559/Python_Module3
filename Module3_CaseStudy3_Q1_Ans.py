import re
class CustomerNotAllowedException():
    pass

class Customer():
    title=""
    firstname=""
    lastname=""
    isblacklisted=0
    custList = []
    def __init__(self):
        customerdata=open('C:/Temp/Python/FairDealCustomerData.csv', 'r')
        # custList = []
        for data in customerdata:
            data = data.rstrip('\n')
            lastname = data.split(',')[0]
            firstname = data.split('.')[0]
            firstname = firstname.split(',')[0]
            title = data.split(',')[1]
            title = title.split('.')[0]
            isblacklisted = data.split(',')[2]
            self.custList.append(title.strip()+firstname+lastname+" "+isblacklisted)

        customerdata.close()
        # l = [self.custList.index(i) for i in self.custList if 'Mr Allen Allen' in i]
        # print l

    def CreateOrder(self,custName):
        try:
            # custName = raw_input('Enter a customer name:')
            l = [self.custList.index(i) for i in self.custList if self.custName in i]
            print l
            # if bool(re.search('1',self.custList[l]))==True:
            #     raise CustomerNotAllowedException

        except CustomerNotAllowedException:
            pass

        else:
            pass

obj=Customer()
# obj.CreateOrder('Miss Heikkinen Heikkinen')