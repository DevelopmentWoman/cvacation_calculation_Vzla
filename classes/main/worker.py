from datetime import date
from datetime import datetime

class Worker():
    def __init__(self, name, lastname, id, cod, job, salary, adm_date ):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.cod = cod
        self.job = job
        self.salary = salary
        self.adm_date = adm_date


    
    def integral_salary(self):
        sal = (self.salary/30)+ self.vacation_rate() +self.profit_rate()
        return sal
    
    
    def vacation_rate(self,  bonus_day=15):
        sal = (self.salary/30*bonus_day)/360
        return sal

    def profit_rate(self, profit_day=120):
        sal = (self.salary/30*profit_day)/360
        return sal
    
    





# cl = Worker("Yelitza", "Suniaga", "15891543", 105.4, datetime.strptime('2007-07-15', '%Y-%m-%d'))
# v1=cl.dif_year()
# print(v1)

# cla = Worker("Yelitza", "Suniaga", "15891543",503,"coordinador de sistemas", 105.4, datetime.strptime('2022-12-15', '%Y-%m-%d'), datetime.strptime('2023-10-15', '%Y-%m-%d'),15,120)
# v1=cla.dif_year()
# print(v1)