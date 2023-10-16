from worker import Worker
from exepct import Except
from datetime import datetime
from datetime import timedelta
from math import floor

class Vacation(Worker,Except):
    def __init__(self, name, lastname, id, cod, job, salary, adm_date, due_date, from_date, holid_day, bonus_day=15):
        super().__init__(name, lastname, id, cod, job, salary, adm_date)
        self.due_date = due_date
        self.from_date = from_date
        self.holid_day = holid_day
        self.bonus_day = bonus_day
        self.ad_bonus_day = 0
        self.week_day = 0
        self.mensaje = ''
        
    def dif_year(self):
        dif_date = floor(((self.due_date - self.adm_date).days)/365)
        self.ad_bonus_day = dif_date
        if dif_date == 0:
            # self.mensaje="Trabajador no aplica para vaciones aun"
            return
        return dif_date

    def add_day(self):
        
        dif_y = self.dif_year()        
        if dif_y != None:
            ad_day= self.bonus_day + dif_y + self.holid_day - 1
            if ad_day <= 30:
                return ad_day
            else:
                return 30
            
    
    def endue_date_vacation(self):
        add_d=self.add_day()
        
        if add_d != None:
            
            count = 1
            date_tour = self.from_date
            monday_day = 0
            while count <= add_d:
                
                if datetime.weekday(date_tour)!=5 and datetime.weekday(date_tour)!=6:
                    if datetime.weekday(date_tour)==0:
                        monday_day += 1
                    date_tour= date_tour + timedelta(days=1) 
                    count+=1
                else:
                    self.week_day += 1
                    date_tour= date_tour + timedelta(days=1) 
            print(self.week_day)
            return(date_tour, monday_day)
        else:
            return Except.show_exception("Trabajador no aplica para vaciones aun")
    


cl = Vacation("Yelitza", "Suniaga", "15891543","505","Coord", 105.4, datetime.strptime('2022-07-15', '%Y-%m-%d'), datetime.strptime('2023-10-15', '%Y-%m-%d'), datetime.strptime('2023-10-18', '%Y-%m-%d'), 2)
v1=cl.endue_date_vacation()
print(v1)

if cl.mensaje=='':
    print(cl.mensaje)