import logging
from typing import Optional, Union
from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
import df_engine.conditions as cnd
from scenario.main import actor
from scenario.response import turn_handler

# testing
testing_dialog = [
    ("Hi", "Hi I'm Health and medicine Chatbot Assitant, how may help you?"),  # start_node -> node1
    ("I want to book a appointment?","OK! I have book a appointment of Doctor for health checkup for you Sir"),
    ("I want a doctor", "There is a many doctor like following:\n- Physicians\n- Cardiologists\n- Gastroenterologists\n- Dentist\n- ENT specialist\n- Gynaecologist\nPlease write type of doctor according above way"),    
    ("I Really want a Physicians doctor", "OK! I have book a appointment of physicians Doctor for you Sir"),
    ("Urgently want a Gastroenterologists", "OK! I have book a appointment of urgently want a gastroenterologists Doctor for you Sir"),
    ("I have problem in my ear, Can book a ENT specialist", "OK! I have book a appointment of i have problem in my ear, can book a ent specialist Doctor for you Sir"),
    ("I want a Dentist for my teeth", "OK! I have book a appointment of dentist Doctor for you Sir"),
    ("I have heart problem, book a Cardiologists", "OK! I have book a appointment of cardiologists Doctor for you Sir").
    ("Thanks", "Welcome Sir/Mam"),  
    ("bye", "Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'"),
    ("Hi", "Hi I'm Health and medicine Chatbot Assitant, how may help you?"),
    ("What is health?", "Health refers to the extent of a person’s physical, mental, and social well-being. This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. The quality of the social environment in turn can affect a person’s physical and mental health, underscoring the importance of social factors for these twin aspects of our overall well-being."),  
    ("Define a medicine","Medicine is the social institution that seeks both to prevent, diagnose, and treat illness and to promote health as just defined. Dissatisfaction with the medical establishment has been growing.Part of this dissatisfaction stems from soaring health-care costs and what many perceive as insensitive stinginess by the health insurance industry, as the 2009 battle over health-care reform illustrated. Some of the dissatisfaction also reflects a growing view that the social and even spiritual realms of human existence play a key role in health and illness. This view has fueled renewed interestin alternative medicine. We return later to these many issues for the social institution of medicine."),        #
    ("what is mental_health?", "Mental health refers to cognitive, behavioral, and emotional well-being. It is all about how people think, feel, and behave. People sometimes use the term “mental health” to mean the absence of a mental disorder. Mental health can affect daily living, relationships, and physical health.Mental health as a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community."), 
    ("how  can are change my diet?", "Diet is the sum of food consumed by a person or other organism. The word diet often implies the use of specific intake of nutrition for health or weight-management reasons (with the two often being related). Although humans are omnivores, each culture and each person holds some food preferences or some food taboos. This may be due to personal tastes or ethical reasons. Individual dietary choices may be more or less healthy.Diet includes a variety of plant-based and animal-based foods that provide nutrients tothe body. Such nutrients provide the body with energy and keep it running. Nutrients help build and strengthenbones, muscles, and tendons and also regulate body processes (i.e., blood pressure). Water is essential for growth, reproduction and good health. Macronutrients are consumed in relatively large quantities and include proteins, carbohydrates, and fats and fatty acids. Micronutrients – vitamins and minerals – are consumed in relatively smaller quantities, but are essential to body processes."),  
    ("I want a doctor", "There is a many doctor like following:\n- Physicians\n- Cardiologists\n- Gastroenterologists\n- Dentist\n- ENT specialist\n- Gynaecologist\nPlease write type of doctor according above way"),    
    ("Thanks", "Welcome Sir/Mam"),
    ("Good Service", "Welcome Sir/Mam"),
    ("bye","Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'"),
]


def run_test():
    ctx = {}
    for in_request, true_out_response in testing_dialog:
        _, ctx = turn_handler(in_request, ctx, actor, true_out_response=true_out_response)


# interactive mode
def run_interactive_mode(actor):
    ctx = {}
    while True:
        in_request = input("type your answer: ")
        _, ctx = turn_handler(in_request, ctx, actor)


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s-%(name)15s:%(lineno)3s:%(funcName)20s():%(levelname)s - %(message)s", level=logging.INFO
    )
    run_test()
    print("<-- Test Successful -->")

