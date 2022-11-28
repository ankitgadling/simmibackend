from .models import CustomSessions
from datetime import datetime,timedelta


def create_session(key,value,expiry_date):
    try:
        session = CustomSessions.objects.get(key=str(key))
        session.delete()
        session = CustomSessions.objects.create(key=str(key),value=str(value),created_date=datetime.now(),expiry_date=expiry_date)
        return True
    except CustomSessions.DoesNotExist:
        session = CustomSessions.objects.create(key=str(key),value=str(value),created_date=datetime.now(),expiry_date=expiry_date)
        return True
    
def get_session_by_key(key):
    try:
        session = CustomSessions.objects.get(key=key)
        if session.created_date < session.expiry_date:
            return session.value
        else:
            session.delete()
            return None
    except CustomSessions.DoesNotExist:
        return None


def delete_session_by_key(key):
    try:
        session = CustomSessions.objects.get(key=key)
        session.delete()
    except CustomSessions.DoesNotExist:
        pass
    
    
    
def indian_currency_format(ruppes):
    final_ruppes = ""
    count = 0
    if ruppes < 1000:
        return str(ruppes)
    elif ruppes > 999 and ruppes < 9999:
        for i in str(ruppes):
            if count == 1:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes
    elif ruppes > 9999 and ruppes < 99999:
        for i in str(ruppes):
            if count == 2:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes
    else:
        for i in str(ruppes):
            if count == 1 or count == 3:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes    
