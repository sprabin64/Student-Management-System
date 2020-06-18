
import re
# Create your tests here.

with open('C:/Users/USER/Google Drive/Desktop/FYP/Program/extract.txt') as file:
    fin = file.read()
    try:
        FirstName= re.search('First Name(.*?)Last Name', fin).group(1)
        Last_name = re.search('Last Name(.*?)Gender', fin).group(1)
        Gender = re.search('Gender(.*?)Address', fin).group(1)
        Address = re.search('Address(.*?)Email', fin).group(1)
        Email = re.search('Email(.*?)End', fin).group(1)
    except:
        print("Match not found")

    '''print(Name)
    print(Address)
    print(Phone_Number)
    print(Email)'''

    file.close()