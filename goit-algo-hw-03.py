import datetime 
import random
from datetime import datetime

def get_days_from_today(date):
    try:
        datetime_object = datetime.strptime(date, "%d.%m.%Y")
        today= datetime.now()
        difference_days = datetime_object.toordinal() - today.toordinal()
        return (difference_days)          
    except ValueError:
        try:
            datetime_object = datetime.strptime(date, "%Y.%m.%d")
            today= datetime.now()
            difference_days = datetime_object.toordinal() - today.toordinal()
            return (difference_days)
        except ValueError:   
            return(f"{date} is wrong format of date")

def get_numbers_ticket(min, max=1, quantity=1):
    lottery_numbers = list()
    try:
        while len(lottery_numbers)<= quantity-1:
        
            num = random.randrange(min, max)
            if num not in lottery_numbers:
                lottery_numbers.append(num)
        lottery_numbers.sort()
    
        return(f"Ваші лотерейні числа: {lottery_numbers}")
    except TypeError:
        return( "Incorrect data entered")
    
