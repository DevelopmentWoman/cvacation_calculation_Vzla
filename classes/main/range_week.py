from datetime import datetime as dt, timedelta  

# getting date ranges intermediate between 2 dates

def calculation_range_week(ini_date, last_date):
    dat =[ini_date]
    days = [15,30,31]
    
    while  ini_date<=last_date:
        
        if  ini_date.day in days:

            if ini_date.day == 31: 
                ini_date= ini_date + timedelta(days=1)
                dat.append(ini_date)
                continue
                

            dat.append(ini_date)
            seg_date= ini_date + timedelta(days=1)
            if seg_date.day == 31:
                ini_date= ini_date + timedelta(days=1)
                continue
            else:
                dat.append(seg_date)
        ini_date = ini_date + timedelta(days=1)
    
    dat.append(last_date)
    return calculation_day_and_moday(dat)


# calculating number of days and number of Mondays in a range of dates
def calculation_day_and_moday(list_date):
    count = len(list_date)
    i=0
    data_result={}
    count_sem = 0


    while i <= count-1:
        date1 = list_date[i]
        date2 = list_date[i+1]
        x = date1
        y = date2
        count_mond = 0
        date_result =  (date2.day-date1.day) + 1
        while x<=y:
            if dt.weekday(x) == 0:
                count_mond+=1
            x = x + timedelta(days=1)
        count_sem+=1
        data_result[f"sem{count_sem}"] = [date1,date2,date_result,count_mond]
        i+=2
    return data_result



            




# print(calculation_range_week(dt.strptime('2023-08-16', '%Y-%m-%d'), dt.strptime('2023-09-20', '%Y-%m-%d')))