import re
import logging
from typing import Optional, Union
from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
from typing import Optional, Union, Any
import df_engine.conditions as cnd
from scenario.condition import healmed_request
from data.Greek.appointment_    import appointment
from data.Greek.doctor_         import doctor
from data.Greek.health_         import health
from data.Greek.medicine_       import medicine
from data.Greek.diet_           import diet
from data.Greek.mental_health_  import mental_health



def greek_transform(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request
    request = request.lower()
    if re.search(r'\bραντεβού|Ραντεβού\b|\bγιατρός$|Γιατρός$', request, re.IGNORECASE):
        if re.search(r'\bραντεβού|Ραντεβού\b|\bγιατρός$|Γιατρός$', request, re.IGNORECASE)[0] == 'ραντεβού':
            return appointment(request)
        else:
            return doctor(request)
    elif re.search(r'\bυγεία|Υγεία\b|\bφάρμακο|Φάρμακο|Ιατρική', request, re.IGNORECASE):
        if re.search(r'\bυγεία|Υγεία\b|\bφάρμακο|Φάρμακο|Ιατρική', request, re.IGNORECASE)[0] == 'υγεία':
            return health(request)
        else:
            return medicine(request)
    elif re.search(r'\bδιατροφή|Διατροφή|δίαιτα\b|\bψυχική_υγειονομικός$|Ψυχική_υγειονομικός$', request, re.IGNORECASE):
        if (re.search(r'\bδιατροφή|Διατροφή|δίαιτα\b|\bψυχική_υγειονομικός$|Ψυχική_υγειονομικός$', request, re.IGNORECASE)[0] == 'διατροφή') | (re.search(r'\bδιατροφή|Διατροφή|δίαιτα\b|\bψυχική_υγειονομικός$|Ψυχική_υγειονομικός$', request, re.IGNORECASE)[0] == 'δίαιτα'):
            return diet(request)
        
        else:
            return mental_health(request)
    elif re.search(r'\bΓιατροί$|Καρδιολόγοι|Γαστρεντερολόγοι|Οδοντίατρος|Ειδικός ΩΡΛ|Γυναικολόγος', request, re.IGNORECASE):
        return  """ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό {} για εσάς, κύριε""".format(re.search(r'\bΓιατροί$|Καρδιολόγοι|Γαστρεντερολόγοι|Οδοντίατρος|Ειδικός ΩΡΛ|Γυναικολόγος', request, re.IGNORECASE)[0])
    return "Claro señor, gracias por su visita, pero puede ir a otros servicios si es necesario, puede escribir 'hola'"