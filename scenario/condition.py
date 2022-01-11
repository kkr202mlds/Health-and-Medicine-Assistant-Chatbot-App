from typing import Optional, Union, Any
from df_engine.core import Context, Actor
from data.appointment_    import appointment
from data.doctor_         import doctor
from data.health_         import health
from data.medicine_       import medicine
from data.diet_           import diet
from data.mental_health_  import mental_health


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
    elif re.search(r'\b|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist', request, re.IGNORECASE):
        return  """OK! I have book a appointment of {} Doctor for you Sir""".format(request)
    return "Sure Sir, I thanks for your visit that but your can go other services if needed you can type 'hi'"
