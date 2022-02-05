import re
from typing import Optional, Union, Any
from df_engine.core import Context, Actor
from data.English.appointment_    import appointment
from data.English.doctor_         import doctor
from data.English.health_         import health
from data.English.medicine_       import medicine
from data.English.diet_           import diet
from data.English.mental_health_  import mental_health


def healmed_request(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request
    request = request.lower()
    if re.search(r'\bappointment\b|\bdoctor', request, re.IGNORECASE):
        if re.search(r'\bappointment\b|\bdoctor', request, re.IGNORECASE)[0] == 'appointment':
            return appointment(request)
        else:
            return doctor(request)
    elif re.search(r'\bhealth\b|\bmedicine', request, re.IGNORECASE):
        if re.search(r'\bhealth\b|\bmedicine', request, re.IGNORECASE)[0] == 'health':
            return health(request)
        else:
            return medicine(request)
    elif re.search(r'\bdiet\b|\bmental_health', request, re.IGNORECASE):
        if re.search(r'\bdiet\b|\bmental_health', request, re.IGNORECASE)[0] == 'diet':
            return diet(request)
        else:
            return mental_health(request)
    elif re.search(r'\bPhysicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist', request, re.IGNORECASE):
        return  """OK! I have book a appointment of {} Doctor for you Sir""".format(re.search(r'\bPhysicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist', request, re.IGNORECASE)[0])
    return "Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'"