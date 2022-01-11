import re
from typing import Optional, Union, Any
from df_engine.core import Context, Actor


# interactive mode
def run_interactive_mode(actor):
    ctx = {}
    while True:
        in_request = input("type your answer: ")
        _, ctx = turn_handler(in_request, ctx, actor)
