import re
from typing import Optional, Union, Any
from df_engine.core import Context, Actor
from data.Dutch.appointment_    import appointment
from data.Dutch.doctor_         import doctor
from data.Dutch.health_         import health
from data.Dutch.medicine_       import medicine
from data.Dutch.diet_           import diet
from data.Dutch.mental_health_  import mental_health




def dutch_transform(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request
    request = request.lower()
    if re.search(r'\bafspraak\b|\barts$', request, re.IGNORECASE):
        if re.search(r'\bafspraak\b|\barts', request, re.IGNORECASE)[0] == 'afspraak':
            return appointment(request)
        else:
            return doctor(request)
    elif re.search(r'\bgezondheid\b|\bgeneeskunde', request, re.IGNORECASE):
        if re.search(r'\bgezondheid\b|\bgeneeskunde', request, re.IGNORECASE)[0] == 'gezondheid':
            return health(request)
        else:
            return medicine(request)
    elif re.search(r'\beetpatroon\b|\bmentale_gezondheid', request, re.IGNORECASE):
        if re.search(r'\beetpatroon\b|\bmentale_gezondheid', request, re.IGNORECASE)[0] == 'eetpatroon':
            return diet(request)
        else:
            return mental_health(request)
    elif re.search(r'\bArtsen|Cardiologen|Gastro-enterologen|Tandarts|KNO-arts|Gynaecoloog', request, re.IGNORECASE):
        return  """OKE! Ik heb een afspraak gemaakt met {} Dokter voor u meneer""".format(re.search(r'\bArtsen|Cardiologen|Gastro-enterologen|Tandarts|KNO-arts|Gynaecoloog', request, re.IGNORECASE)[0])
    return "Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen"






