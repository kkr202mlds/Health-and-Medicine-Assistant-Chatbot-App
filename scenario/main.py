import df_engine.conditions as cnd
from df_engine.core import Actor
from df_engine.core.keywords import LOCAL, RESPONSE, TRANSITIONS


import scenario.condition as loc_cnd
import scenario.response as rsp


plot = {
    "service": {
        LOCAL: {
            TRANSITIONS: {
                ("funfact", "random"): loc_cnd.health_medicine_condition,
            }
        },
        "start": {RESPONSE: "hi"},
        "fallback": {RESPONSE: "Sorry"},
    },
    "funfact": {
        "random": {
            RESPONSE: rsp.health_medicine_response,
            TRANSITIONS: {
                ("funfact", "random"): cnd.any([loc_cnd.health_medicine_condition, loc_cnd.another_health_medicine_condition])
            },
        },
    },
}


actor = Actor(plot, start_label=("service", "start"), fallback_label=("service", "fallback"))
