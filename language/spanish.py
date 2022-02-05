import re
import logging
from typing import Optional, Union
from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
from typing import Optional, Union, Any
import df_engine.conditions as cnd
from scenario.condition import healmed_request
from data.Spanish.appointment_    import appointment
from data.Spanish.doctor_         import doctor
from data.Spanish.health_         import health
from data.Spanish.medicine_       import medicine
from data.Spanish.diet_           import diet
from data.Spanish.mental_health_  import mental_health


def spanish_transform(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request
    request = request.lower()
    if re.search(r'\bcita|Cita\b|\bmédica$|médico$', request, re.IGNORECASE):
        if re.search(r'\bcita|Cita\b|\bmédica$|médico$', request, re.IGNORECASE)[0] == 'cita':
            return appointment(request)
        else:
            return doctor(request)
    elif re.search(r'\bsanidad|Sanidad\b|\bmedicamento|Medicamento', request, re.IGNORECASE):
        if re.search(r'\bsanidad|Sanidad\b|\bmedicamento|Medicamento', request, re.IGNORECASE)[0] == 'sanidad':
            return health(request)
        else:
            return medicine(request)
    elif re.search(r'\bdieta|Dieta\b|\bsalud_mental|Salud_mental$', request, re.IGNORECASE):
        if re.search(r'\bdieta|Dieta\b|\bsalud_mental|Salud_mental$', request, re.IGNORECASE)[0] == 'dieta':
            return diet(request)
        else:
            return mental_health(request)
    elif re.search(r'\bMédicos|Médicas|Cardiólogos|Gastroenterólogos|Dentista|Otorrinolaringólogo|Ginecólogo', request, re.IGNORECASE):
        return  """OK! He reservado una cita con {} médico para usted, señor.""".format(re.search(r'\bMédicos|Médicas|Cardiólogos|Gastroenterólogos|Dentista|Otorrinolaringólogo|Ginecólogo', request, re.IGNORECASE)[0])
    return "Claro señor, gracias por su visita, pero puede ir a otros servicios si es necesario, puede escribir 'hola'"