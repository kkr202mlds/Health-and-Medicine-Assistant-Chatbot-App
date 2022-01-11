import re
import logging
from typing import Optional, Union

from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
import df_engine.conditions as cnd
import scenario.condition
from  scenario.condition import healmed_request



logger = logging.getLogger(__name__)

# First of all, to create a dialog agent, we need to create a dialog script.
# Below, `plot` is the dialog script.
# A dialog script is a flow dictionary that can contain multiple plot .
# Plot are needed in order to divide a dialog into sub-dialogs and process them separately.
# For example, the separation can be tied to the topic of the dialog.
# In our example, there is one flow called greeting_flow.

# Inside each flow, we can describe a sub-dialog.
# Here we can also use keyword `LOCAL`, which we have considered in other examples.

# Flow describes a sub-dialog using linked nodes, each node has the keywords `RESPONSE` and `TRANSITIONS`.

# `RESPONSE` - contains the response that the dialog agent will return when transitioning to this node.
# `TRANSITIONS` - describes transitions from the current node to other nodes.
# `TRANSITIONS` are described in pairs:
#      - the node to which the agent will perform the transition
#      - the condition under which to make the transition
plot = {
    "greeting_flow": {
        "start_node": {  # This is an initial node, it doesn't need an `RESPONSE`
            RESPONSE: "",
            TRANSITIONS: {"node1": cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE)}, 
        },
        "node1": {
            RESPONSE: "Hi I'm Health and medicine Chatbot Assitant, how may help you?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental health|Mental health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: healmed_request,
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental health|Mental health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: healmed_request,
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental health|Mental health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE)},
        },
        "node4": {
            RESPONSE: healmed_request,
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental_health|Mental_health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE)},
        },
        "node5": {
            RESPONSE: "Welcome Sir/Mam",
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental health|Mental health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE),
                         "node6": cnd.regexp(r"\bNo|no|NO|Nothing|nothing", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "bye", TRANSITIONS: {"node1": cnd.exact_match("Hi")}},
        "fallback_node": {  # We get to this node if an error occurred while the agent was running
            RESPONSE: "Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'",
            TRANSITIONS: {"node1": cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE)},
        },
    }
}

# An actor is an object that processes user input replicas and returns responses
# To create the actor, you need to pass the script of the dialogue `plot`
# And pass the initial node `start_label`
# and the node to which the actor will go in case of an error `fallback_label`
# If `fallback_label` is not set, then its value becomes equal to `start_label` by default
actor = Actor(plot, start_label=("greeting_flow", "start_node"), fallback_label=("greeting_flow", "fallback_node"))


