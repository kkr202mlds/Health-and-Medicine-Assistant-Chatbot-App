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
- Test Output:- 
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
- Created the transformer
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
