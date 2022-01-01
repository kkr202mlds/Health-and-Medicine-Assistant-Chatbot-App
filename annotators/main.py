from df_engine.core import Context
from .basic import binary_intent

def annotate(ctx: Context):
    # TODO: add your own annotators
    ctx = binary_intent(ctx)
    # add annotation in context
    return ctx
