from df_engine.core import Context
from .basic import binary_intent

def annotate(ctx: Context):
    # TODO: add your own annotators
    ctx = check_language(ctx)
    # add annotation in context
    ctx = previous_label(ctx)
    return ctx
