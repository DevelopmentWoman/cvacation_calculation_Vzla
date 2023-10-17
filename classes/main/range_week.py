from datetime import datetime as dt, timedelta  

def calculation_range_week(ini_date, last_date):
    dat =[ini_date]
    dat_conj = {}
    days = [15,30,31]
    
    while  ini_date<=last_date:
        # if  dt.weekday(ini_date) != 5 and dt.weekday(ini_date)!=6:
        
        if  ini_date.day in days:
            if ini_date in dat:
                ini_date = ini_date + timedelta(days=1)
                continue
            if ini_date.day == 31:
                date_30= ini_date + timedelta(days=-1)
                
                if date_30 in dat: dat.remove(date_30)
            dat.append(ini_date)
        ini_date = ini_date + timedelta(days=1)
    
    dat.append(last_date)
    return dat


print(calculation_range_week(dt.strptime('2023-10-15', '%Y-%m-%d'), dt.strptime('2023-11-04', '%Y-%m-%d')))