"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons. 

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json','r')   #bc the file starts with a [ it's a list and so school automatically is a list

schools = json.load(infile)

conference_schools = [372,108,107,130]

print(len(schools))

#for school in schools:  #schools is a list but school is a dictionary that represcenst everything in the dictionary. keys on the left, value on the right 
   # NCAAnum = (school['NCAA']['NAIA conference number football (IC2020)'])
    #for i in conference_schools:
       # if i == NCAAnum:
           # print(f'University: {school["instnm"]}')
           # print(f'Gradiation Rate for Women: {school["Graduation rate  women (DRVGR2020)"]}\n')


#############how bohdwani did it

for school in schools:
    school_conf_number = school['NCAA']['NAIA conference number football (IC2020)']
    if school_conf_number in conference_schools:
        grad_rate = school["Graduation rate  women (DRVGR2020)"]
        if grad_rate > 75:
            print(f'University Name: {school["instnm"]}')
            print(f'Gradiation Rate for Women: {grad_rate}%')
            print()
            print()


for school in schools:
    school_conf_number = school['NCAA']['NAIA conference number football (IC2020)']
    if school_conf_number in conference_schools:
        total_price = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        if total_price != None:
            if total_price > 50000:
                print(f'University Name: {school["instnm"]}')
                print(f'Total price for in-state students living off campus: ${total_price:.2f}\n')