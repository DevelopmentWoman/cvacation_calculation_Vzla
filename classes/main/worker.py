from datetime import date
from datetime import datetime
from math import floor
class Worker():
    def __init__(self, name, lastname, id, cod, job, salary, adm_date, actual_date=datetime.today(), bonus_day=15, profit_day=120):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.cod = cod
        self.job = job
        self.salary = salary
        self.adm_date = adm_date
        self.actual_date = actual_date
        self.bonus_day = bonus_day
        self.profit_day= profit_day


    
    def integral_salary(self):
        sal = (self.salary/30)+ self.vacation_rate() +self.profit_rate()
        return sal
    

    def dif_year(self):
        dif_date = floor(((self.actual_date - self.adm_date).days)/365)

        # dif_date = (self.actual_date.day - self.adm_date.day)
        return dif_date


    
    def vacation_rate(self):
        sal = (self.salary/30*self.bonus_day)/360
        return sal

    def profit_rate(self):
        sal = (self.salary/30*self.profit_day)/360
        return sal
    
    # def integral_bonus(self):





# cl = Worker("Yelitza", "Suniaga", "15891543", 105.4, datetime.strptime('2007-07-15', '%Y-%m-%d'))
# v1=cl.dif_year()
# print(v1)

cla = Worker("Yelitza", "Suniaga", "15891543",503,"coordinador de sistemas", 105.4, datetime.strptime('2022-12-15', '%Y-%m-%d'), datetime.strptime('2023-10-15', '%Y-%m-%d'),15,120)
v1=cla.dif_year()
print(v1)