import re
from typing import Optional, Union, Any
from df_engine.core import Context, Actor
from data.Arabic.appointment_    import appointment
from data.Arabic.doctor_         import doctor
from data.Arabic.health_         import health
from data.Arabic.medicine_       import medicine
from data.Arabic.diet_           import diet
from data.Arabic.mental_health_  import mental_health




def arabic_transform(ctx: Context, actor: Actor, *args, **kwargs) -> Any:
    request = ctx.last_request
    request = request.lower()
    if re.search(r'\bميعاد\b|\bدكتور', request, re.IGNORECASE):
        if re.search(r'\bميعاد\b|\bدكتور', request, re.IGNORECASE)[0] == 'ميعاد':
            return appointment(request)
        else:
            return doctor(request)
    elif re.search(r'\bصحة\b|\b^طب$', request, re.IGNORECASE):
        if re.search(r'\bصحة\b|\b^طب$', request, re.IGNORECASE)[0] == 'صحة':
            return health(request)
        else:
            return medicine(request)
    elif re.search(r'\bحمية\b|\bالصحة_العقلية', request, re.IGNORECASE):
        if re.search(r'\bحمية\b|\bالصحة_العقلية', request, re.IGNORECASE)[0] == 'حمية':
            return diet(request)
        else:
            return mental_health(request)
    elif re.search(r'\bاطباء|اطباء قلب|اطباء الجهاز الهضمى|طبيب اسنان|اخصائى انف واذن وحنجرة|الطبيب المعالج', request, re.IGNORECASE):
        return  """موافق! لدي حجز موعد مع {} دكتور لك سيدي""".format(re.search(r'\bاطباء|اطباء قلب|اطباء الجهاز الهضمى|طبيب اسنان|اخصائى انف واذن وحنجرة|الطبيب المعالج', request, re.IGNORECASE)[0])
    return "'1بالتأكيد سيدي ، شكرا لزيارتك ولكن يمكنك الذهاب إلى خدمات أخرى إذا لزم الأمر يمكنك كتابة 'مرحبًا"









