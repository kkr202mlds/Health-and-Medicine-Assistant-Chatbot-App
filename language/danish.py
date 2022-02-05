import re
from typing import Optional, Union, Any
from df_engine.core import Context, Actor
from data.Danish.appointment_    import appointment
from data.Danish.doctor_         import doctor
from data.Danish.health_         import health
from data.Danish.medicine_       import medicine
from data.Danish.diet_           import diet
from data.Danish.mental_health_  import mental_health



def danish_transform(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request
    request = request.lower()
    if re.search(r'\budnævnelse\b|\blæge$', request, re.IGNORECASE):
        if re.search(r'\budnævnelse\b|\blæge', request, re.IGNORECASE)[0] == 'udnævnelse':
            return appointment(request)
        else:
            return doctor(request)
    elif re.search(r'\bsundhed\b|\bmedicin', request, re.IGNORECASE):
        if re.search(r'\bsundhed\b|\bmedicin', request, re.IGNORECASE)[0] == 'sundhed':
            return health(request)
        else:
            return medicine(request)
    elif re.search(r'\bdiæt\b|\bmental_sundhed', request, re.IGNORECASE):
        if re.search(r'\bdiæt\b|\bmental_sundhed', request, re.IGNORECASE)[0] == 'diæt':
            return diet(request)
        else:
            return mental_health(request)
    elif re.search(r'\bKardiologer|Gastroenterologer|Tandlæge|ØNH-specialist|Gynækolog', request, re.IGNORECASE):
        return  """OK! Jeg har booket en tid til {} læge til dig, hr""".format(re.search(r'\bKardiologer|Gastroenterologer|Tandlæge|ØNH-specialist|Gynækolog', request, re.IGNORECASE)[0])
    return "Selvfølgelig, Sir, jeg takker for dit besøg, men du kan gå til andre tjenester, hvis det er nødvendigt, du kan skrive 'hej'"








