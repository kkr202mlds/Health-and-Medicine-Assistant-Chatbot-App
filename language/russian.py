import re
from typing import Optional, Union, Any
from df_engine.core import Context, Actor
from data.Dutch.appointment_    import appointment
from data.Dutch.doctor_         import doctor
from data.Dutch.health_         import health
from data.Dutch.medicine_       import medicine
from data.Dutch.diet_           import diet
from data.Dutch.mental_health_  import mental_health




def russian_transform(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request
    request = request.lower()
    if re.search(r'\bназначение\b|\bврач', request, re.IGNORECASE):
        if re.search(r'\bназначение\b|\bврач', request, re.IGNORECASE)[0] == 'назначение':
            return appointment(request)
        else:
            return doctor(request)
    elif re.search(r'\bздоровье\b|\bлекарство', request, re.IGNORECASE):
        if re.search(r'\bздоровье\b|\bлекарство', request, re.IGNORECASE)[0] == 'здоровье':
            return health(request)
        else:
            return medicine(request)
    elif re.search(r'\bдиета\b|\bпсихическое_здоровье', request, re.IGNORECASE):
        if re.search(r'\bдиета\b|\bпсихическое_здоровье', request, re.IGNORECASE)[0] == 'диета':
            return diet(request)
        else:
            return mental_health(request)
    elif re.search(r'\b|Врачи|Кардиологи|Гастроэнтерологи|Дантист|ЛОР-специалист|Гинеколог', request, re.IGNORECASE):
        return  """В ПОРЯДКЕ! Я записал вас на прием к {} врачу, сэр.""".format(re.search(r'\b|Врачи|Кардиологи|Гастроэнтерологи|Дантист|ЛОР-специалист|Гинеколог', request, re.IGNORECASE)[0])
    return "Конечно, сэр, я благодарю за ваш визит, но вы можете воспользоваться другими услугами, если это необходимо, вы можете напечатать 'привет'"







