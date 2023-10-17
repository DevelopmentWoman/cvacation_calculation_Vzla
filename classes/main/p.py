from holiday import Vacation
from difference_in_vacation import Diference_Vacation as df
from datetime import  datetime
clase = Vacation("Yelitza", "Suniaga", "15891543","505","Coord", 163.43, datetime.strptime('2011-04-5', '%Y-%m-%d'), datetime.strptime('2023-4-5', '%Y-%m-%d'), datetime.strptime('2023-8-16', '%Y-%m-%d'),0, 0)
v1=clase.endue_date_vacation()
print(v1)

cla1 = df("Yelitza", "Suniaga", "15891543","505","Coord", 163.43, datetime.strptime('2011-04-5', '%Y-%m-%d'), datetime.strptime('2023-4-5', '%Y-%m-%d'), datetime.strptime('2023-8-16', '%Y-%m-%d'),0, 0)

print(cla1.pay_taxes())