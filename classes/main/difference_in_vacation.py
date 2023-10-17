import range_week as rw
from holiday import Vacation
from datetime import datetime

class Diference_Vacation(Vacation):

    def __init__(self, name, lastname, id, cod, job, salary, adm_date, due_date, from_date, holid_day, previous_day, calc_salar_tax=0, perc_soc_sec=0.04, perc_lph=0.005, bon_tax=0.01, bonus_day=15):

        super().__init__(name, lastname, id, cod, job, salary, adm_date, due_date, from_date, holid_day, previous_day, calc_salar_tax, perc_soc_sec, perc_lph, bon_tax, bonus_day)

    def pay_taxes(self):
        result = rw.calculation_range_week(self.from_date, self.endue_date_vacation())
        for value in result.values():
            # value.append(6)
            if self.calc_salar_tax !=0:
                ss_tax = round(value[3]*self.perc_soc_sec*self.calc_salar_tax,2)                
            else:
                ss_tax =round(value[3]*self.perc_soc_sec*self.base_week,2)
                print(ss_tax)


cla1 = Diference_Vacation("Yelitza", "Suniaga", "15891543","505","Coord", 163.43, datetime.strptime('2011-04-5', '%Y-%m-%d'), datetime.strptime('2023-4-5', '%Y-%m-%d'), datetime.strptime('2023-8-16', '%Y-%m-%d'),0, 0)

cla1.pay_taxes()






