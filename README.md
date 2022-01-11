## ml_s_kill_hack_2.0

## Description

**dff_health_&_medicine_skill** 
## Quickstart

```bash
pip install -r requirements.txt
```
Run interactive mode
```bash
python run_interactive.py
```
Run tests
```bash
python run_test.py
```
## Task
Week 3

- Latest Test Output:- 
- - run_test() result:-
```
2022-01-11 07:22:31,652-           root:104:        turn_handler():INFO - in_request=Hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
2022-01-11 07:22:31,659-           root:104:        turn_handler():INFO - in_request=I want to book a appointment? ->
 OK! I have book a appointment of Doctor for health checkup for you Sir
2022-01-11 07:22:31,667-           root:104:        turn_handler():INFO - in_request=Physicians ->
 OK! I have book a appointment of physicians Doctor for you Sir
2022-01-11 07:22:31,675-           root:104:        turn_handler():INFO - in_request=Thanks ->
 Welcome Sir/Mam
2022-01-11 07:22:31,689-           root:104:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'
2022-01-11 07:22:31,703-           root:104:        turn_handler():INFO - in_request=Hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
2022-01-11 07:22:31,726-           root:104:        turn_handler():INFO - in_request=What is health? ->
 Health refers to the extent of a person’s physical, mental, and social well-being. This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. The quality of the social environment in turn can affect a person’s physical and mental health, underscoring the importance of social factors for these twin aspects of our overall well-being.
2022-01-11 07:22:31,747-           root:104:        turn_handler():INFO - in_request=What is medicine ->
 Medicine is the social institution that seeks both to prevent, diagnose, and treat illness and to promote health as just defined. Dissatisfaction with the medical establishment has been growing.Part of this dissatisfaction stems from soaring health-care costs and what many perceive as insensitive stinginess by the health insurance industry, as the 2009 battle over health-care reform illustrated. Some of the dissatisfaction also reflects a growing view that the social and even spiritual realms of human existence play a key role in health and illness. This view has fueled renewed interestin alternative medicine. We return later to these many issues for the social institution of medicine.
2022-01-11 07:22:31,785-           root:104:        turn_handler():INFO - in_request=what is mental_health? ->
 Mental health refers to cognitive, behavioral, and emotional well-being. It is all about how people think, feel, and behave. People sometimes use the term “mental health” to mean the absence of a mental disorder. Mental health can affect daily living, relationships, and physical health.Mental health as a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community.
2022-01-11 07:22:31,809-           root:104:        turn_handler():INFO - in_request=how  can are change my diet? ->
 Diet is the sum of food consumed by a person or other organism. The word diet often implies the use of specific intake of nutrition for health or weight-management reasons (with the two often being related). Although humans are omnivores, each culture and each person holds some food preferences or some food taboos. This may be due to personal tastes or ethical reasons. Individual dietary choices may be more or less healthy.Diet includes a variety of plant-based and animal-based foods that provide nutrients tothe body. Such nutrients provide the body with energy and keep it running. Nutrients help build and strengthenbones, muscles, and tendons and also regulate body processes (i.e., blood pressure). Water is essential for growth, reproduction and good health. Macronutrients are consumed in relatively large quantities and include proteins, carbohydrates, and fats and fatty acids. Micronutrients – vitamins and minerals – are consumed in relatively smaller quantities, but are essential to body processes.
2022-01-11 07:22:31,826-           root:104:        turn_handler():INFO - in_request=what a doctor ->
 There is a many doctor like following:
- Physicians
- Cardiologists
- Gastroenterologists
- Dentist
- ENT specialist
- Gynaecologist
Please write type of doctor according above way
2022-01-11 07:22:31,852-           root:104:        turn_handler():INFO - in_request=Ok ->
 Welcome Sir/Mam
2022-01-11 07:22:31,888-           root:104:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'
<-- Test Successful -->
```

- - run_interactive_mode(actor) result:-
```
type your answer: hey
2022-01-11 07:23:17,806-           root:104:        turn_handler():INFO - in_request=hey ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
type your answer: I want an appointment of doctor
2022-01-11 07:23:43,606-           root:104:        turn_handler():INFO - in_request=I want an appointment of doctor ->
 OK! I have book a appointment of Doctor for health checkup for you Sir
type your answer: which doctor
2022-01-11 07:23:52,099-           root:104:        turn_handler():INFO - in_request=which doctor ->
 There is a many doctor like following:
- Physicians
- Cardiologists
- Gastroenterologists
- Dentist
- ENT specialist
- Gynaecologist
Please write type of doctor according above way
type your answer: Physicians
2022-01-11 07:24:06,826-           root:104:        turn_handler():INFO - in_request=Physicians ->
 OK! I have book a appointment of physicians Doctor for you Sir
type your answer: thanks
2022-01-11 07:24:42,226-           root:104:        turn_handler():INFO - in_request=thanks ->
 Welcome Sir/Mam
type your answer: ok
2022-01-11 07:24:46,841-           root:104:        turn_handler():INFO - in_request=ok ->
 Welcome Sir/Mam
type your answer: bye
2022-01-11 07:24:50,353-           root:104:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'
type your answer: hi
2022-01-11 07:24:53,475-           root:104:        turn_handler():INFO - in_request=hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
type your answer: what is health
2022-01-11 07:24:59,789-           root:104:        turn_handler():INFO - in_request=what is health ->
 Health refers to the extent of a person’s physical, mental, and social well-being. This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. The quality of the social environment in turn can affect a person’s physical and mental health, underscoring the importance of social factors for these twin aspects of our overall well-being.
type your answer: and medicine
2022-01-11 07:25:06,234-           root:104:        turn_handler():INFO - in_request=and medicine ->
 Medicine is the social institution that seeks both to prevent, diagnose, and treat illness and to promote health as just defined. Dissatisfaction with the medical establishment has been growing.Part of this dissatisfaction stems from soaring health-care costs and what many perceive as insensitive stinginess by the health insurance industry, as the 2009 battle over health-care reform illustrated. Some of the dissatisfaction also reflects a growing view that the social and even spiritual realms of human existence play a key role in health and illness. This view has fueled renewed interestin alternative medicine. We return later to these many issues for the social institution of medicine.
type your answer: how can I change my diet plan
2022-01-11 07:25:19,024-           root:104:        turn_handler():INFO - in_request=how can I change my diet plan ->
 Diet is the sum of food consumed by a person or other organism. The word diet often implies the use of specific intake of nutrition for health or weight-management reasons (with the two often being related). Although humans are omnivores, each culture and each person holds some food preferences or some food taboos. This may be due to personal tastes or ethical reasons. Individual dietary choices may be more or less healthy.Diet includes a variety of plant-based and animal-based foods that provide nutrients tothe body. Such nutrients provide the body with energy and keep it running. Nutrients help build and strengthenbones, muscles, and tendons and also regulate body processes (i.e., blood pressure). Water is essential for growth, reproduction and good health. Macronutrients are consumed in relatively large quantities and include proteins, carbohydrates, and fats and fatty acids. Micronutrients – vitamins and minerals – are consumed in relatively smaller quantities, but are essential to body processes.
type your answer: I issue of mental_Health
2022-01-11 07:25:35,124-           root:104:        turn_handler():INFO - in_request=I issue of mental_Health ->
 Mental health refers to cognitive, behavioral, and emotional well-being. It is all about how people think, feel, and behave. People sometimes use the term “mental health” to mean the absence of a mental disorder. Mental health can affect daily living, relationships, and physical health.Mental health as a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community.
type your answer: good
2022-01-11 07:26:07,348-           root:104:        turn_handler():INFO - in_request=good ->
 Welcome Sir/Mam
```


- Old Test Output:-
```
type your answer: Hi
2022-01-11 05:32:56,958-           root:104:        turn_handler():INFO - in_request=Hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
type your answer: than
2022-01-11 05:33:03,035-           root:104:        turn_handler():INFO - in_request=than ->
 Sorry due to technical reason this request can't be proceed but your can go other service if needed you can type 'hi'
type your answer: hi
2022-01-11 05:33:07,904-           root:104:        turn_handler():INFO - in_request=hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
type your answer: APPOINTMENT
2022-01-11 05:33:16,764-           root:104:        turn_handler():INFO - in_request=APPOINTMENT ->
 OK! I have book a appointment of Doctor for health checkup for you Sir
type your answer: THANKS
2022-01-11 05:33:21,760-           root:104:        turn_handler():INFO - in_request=THANKS ->
 Welcome Sir/Mam
type your answer: YES
2022-01-11 05:33:30,146-           root:104:        turn_handler():INFO - in_request=YES ->
 Sorry due to technical reason this request can't be proceed but your can go other service if needed you can type 'hi'
```

## Resources
#TODO: TODO:
- Modify the Health and Medicine Chatbot Assitant with help of skill hackathon Project.

WIP:
- At this point my main goal is generating better health and medicine chatbot environment and their plot , response and condition functions in order to add different functionality for the dialogs. The assistant first needs to understand similarity and difference between test output and interactive output.
Creating this scenarios to implement them in the chatbot project.

Done:
- Modify the Health and Medicine Chatbot Assitant
- Modify plot
- Modify condition
- Make the transformer of Health and Medicine Chatbot Assitant
- Modify the response

## Support links
- [Examples of Other projects for SocialBot](https://github.com/emora-chat/emora_stdm_zoo)
- [Basic Examples from Dialog Flow Engine (main package of DFF)](https://github.com/deepmipt/dialog_flow_engine) + examples in repo
- [Advance examples with ML annotators from Dialog Flow SDK](https://github.com/deepmipt/dialog_flow_sdk)
- [Hard Examples for distributed  ML annotators](https://github.com/deepmipt/dream/tree/commonb/skills) + look at dirs:
  - dff_short_story_skill
  - dff_grounding_skill
  - dff_program_y
  - dff_program_y_dangerous
  - dff_program_y_wide
  - dff_template_skill
  - dff_coronavirus_skill
  - dff_funfact_skill
  - dff_book_skill
  - dff_weather_skill
