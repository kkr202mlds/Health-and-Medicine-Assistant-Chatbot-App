import random

from df_engine.core import Actor, Context
import random
import re
from df_engine.core import Actor, Context


HEALMED_LIST = [
("Health refers to the extent of a person’s physical, mental, and social well-being. \
 This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not \
 just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. \
 The quality of the social environment in turn can affect a person’s physical and mental health, \
 underscoring the importance of social factors for these twin aspects of our overall well-being.", "health"), 
("Medicine is the social institution that seeks both to prevent, diagnose, and treat illness and \
 to promote health as just defined. Dissatisfaction with the medical establishment has been growing. \
 Part of this dissatisfaction stems from soaring health-care costs and \
 what many perceive as insensitive stinginess by the health insurance industry, \
 as the 2009 battle over health-care reform illustrated. Some of the dissatisfaction also reflects a growing view that the social \
 and even spiritual realms of human existence play a key role in health and illness. \
 This view has fueled renewed interest in alternative medicine. We return later to these many issues for the social institution of medicine.", "medicine"),
]



def health_medicine_response(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    fact, topic = random.sample(HEALMED_LIST, 1)[0]
    return f"{fact}"
