from worker import Worker
from exepct import Except
from datetime import datetime
from datetime import timedelta
from math import floor

class Vacation(Worker,Except):
    def __init__(self, name, lastname, id, cod, job, salary, adm_date, due_date, from_date, holid_day, previous_day, calc_salar_tax=0, perc_soc_sec=0.04, perc_lph=0.005, bon_tax=0.01, bonus_day=15):
        super().__init__(name, lastname, id, cod, job, salary, adm_date)
        self.due_date = due_date
        self.from_date = from_date
        self.holid_day = holid_day
        self.previous_day = previous_day
        self.calc_salar_tax = calc_salar_tax
        self.perc_soc_sec = perc_soc_sec
        self.bon_tax = bon_tax
        self.bonus_day = bonus_day
        self.daily_salary = self.salary/30
        self.perc_lph = perc_lph
        self.mensaje = ''
        self.inf_total_days = []
        self.pay_total_day = []
        self.dic_taxes = {}
        self.base_week=0
        
    #calculating number of years for vacation bonus    
    def dif_year(self):
        dif_date = floor(((self.due_date - self.adm_date).days)/360)
        anual_special_bonus = dif_date
        ad_bonus_day = dif_date - 1 
        if anual_special_bonus>=30: 
            anual_special_bonus = 30
        if ad_bonus_day>=30:
            ad_bonus_day = 30
        self.inf_total_days = [(self.bonus_day, round(self.bonus_day*self.daily_salary,2)), (ad_bonus_day, round(ad_bonus_day*self.daily_salary,2)), (self.bonus_day, round(self.bonus_day*self.daily_salary,2)), 
                               (anual_special_bonus, round(anual_special_bonus*self.daily_salary,2)), (self.holid_day, round(self.holid_day*self.daily_salary,2))]
      


    
    # calculating vacation days
    def vacation_day(self):
        self.dif_year() 
        if self.inf_total_days[1][0] != None:
            ad_day= self.inf_total_days[2][0] + self.inf_total_days[1][0] + self.holid_day - self.previous_day -1
            # print(ad_day)    
            if ad_day <= 30:
                return ad_day
            else:
                return 30
            
    # getting last day of vacation and monday days
    def endue_date_vacation(self):
        add_d=self.vacation_day()
        
        if add_d != None:            
            count = 1
            date_tour = self.from_date
            monday_day = 0
            week_day = 0

            while count <= add_d:     

                if datetime.weekday(date_tour)!=5 and datetime.weekday(date_tour)!=6:
                    if datetime.weekday(date_tour)==0:
                        monday_day += 1
                    date_tour= date_tour + timedelta(days=1) 
                    count+=1
                else:
                    week_day += 1
                    date_tour= date_tour + timedelta(days=1) 

                until_date = date_tour
            self.inf_total_days.extend([(week_day, round(week_day*self.daily_salary,2)), (self.previous_day, round(self.previous_day*-self.daily_salary,2)), monday_day]) 
            self.social_security()
            self.lph()
            self.bonus_tax()

            return(until_date)
        
        else:

            return Except.show_exception("Trabajador no aplica para vaciones aun")
        
    # calculating total days to pay
    def total_days_pay(self):
        total_day_pay = 0
        total_pay = 0
        for i in range(len(self.inf_total_days)-1):
            total_day_pay += self.inf_total_days[i][0] 
            total_pay += self.inf_total_days[i][1] 

        self.pay_total_day = (total_day_pay,round(total_pay,2))
        return self.pay_total_day
    


    # calculating taxes

    def social_security(self):
        self.base_week=(self.daily_salary*360)/52
        pay_ss = round(self.perc_soc_sec*self.base_week*self.inf_total_days[-1],2)
        self.dic_taxes["s_sec"]= pay_ss
        

    def lph(self):
        pay_lph = round(self.dic_taxes["s_sec"]/8,2)
        self.dic_taxes["tax_lph"]= pay_lph


    def bonus_tax(self):
  
        pay_bt = round((self.inf_total_days[2][1] + self.inf_total_days[3][1])*self.bon_tax,2)
        # print(f"{pay_bt}")
        self.dic_taxes["tax_bon"]= pay_bt

    def taxes_total(self):
        tax_tot = 0
        for values in self.dic_taxes.values():
            tax_tot += values 
        return round(tax_tot,2)
    
    def total_cancel_employ(self):
        total = self.pay_total_day[1] - self.taxes_total()
        return total








