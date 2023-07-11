#Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
'''format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"'''

def Date_Format(date):
    new_date = '' # There we create basic algorithm which delete symbol '/'
    for i in date:
        if i == '/':
            new_date += ''
        else:
            new_date += i
    result_date = ''
    result_date = new_date[-4] + new_date[-3] +new_date[-2] +new_date[-1] + new_date[2] +new_date[3] +new_date[0] +new_date[1] 
    print(result_date)





Date_Format("11/12/2019")
Date_Format("12/31/2019")
Date_Format("12/31/2019")