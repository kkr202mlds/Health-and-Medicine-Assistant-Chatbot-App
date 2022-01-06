import re
import logging
from df_engine.core import Actor, Context



HEALMED_COMPILED_PATTERN = re.compile(
    r"(health|Health|medicine|Medicine|mental health|Mental health|diet|Diet|clinical|Clinical|physical examination|^Physical examination.*)",
    re.IGNORECASE,
)


logger = logging.getLogger(__name__)



def health_medicine_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return bool(HEALMED_COMPILED_PATTERN.search(request))



def another_health_medicine_condition(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    request = ctx.last_request
    return bool("other" in request or ctx.misc.get("yes_intent"))

