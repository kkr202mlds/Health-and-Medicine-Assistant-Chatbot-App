import re
from typing import Optional, Union, Any
from df_engine.core import Context, Actor
from typing import Optional, Union
from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
import df_engine.conditions as cnd
from scenario.main import actor
 


# interactive mode
def run_interactive_mode(actor):
    ctx = {}
    while True:
        in_request = input("type your answer: ")
        _, ctx = turn_handler(in_request, ctx, actor)
