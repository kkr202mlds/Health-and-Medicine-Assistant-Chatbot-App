# Week 1

TODO:
- I have created the clone the DFF repo (link will appear later today) and run the code
- I have to modify the skills codebase to get acquainted with development w the framework
- I have try to set up the meeting and to plan the development of the Health and Medicine skill in chatbot 

WIP:
- At this point my main goal is to understand the code and how to execute different ideas in the code and to implement them later in code.


Done:
- I have created the clone the DFF repo (link will appear later today) and run the code
- I have try to modify the skills codebase to get acquainted with development w the framework
- - 20 minutes meeting with Oleg Serikov, 23.12.2021 to choice the Project which is Skill Hackathon and topic is Health and Medicine

Issues:
- I was confuse to implement the Actor and Context function, I need a help to desccription and implementation


# Week 2
TODO:
- Create a Health and Medicine help Chatbot with help of skill hackathon Project. Health and Medicine Chatbot is explain the understanding of importance health and medicine in life.


WIP:
- At this point my main goal is creation of health and medicine environment in the project and their intent, response and condition functions in order to add different functionality for the dialogs. The assistant first needs to distinguish between response and output.
Creating this scenarios to implement them in the code


Done:
- Started with creation of basic functions
- In annotators.basic.py I implemented a yes_intent and no_intent function which helps to determine if user confirms or denies, after that it writes the intent inside ctx.misc. Added yes_intent and no_intent function inside annotate function in main.py
- Created the conditions (health, medicine)
-Created responses for health and medicine chatbot that use a function.
- updated scenario (condition.py, response.py, main.py)
- run_test.py is updated.
- Created a Health and Medicine Jupyter Notebook file.
- - 20 minutes meeting with Oleg Serikov, 03.01.2022, understand the functioning of run_interactive and run_test condition and relation of Actor and Context function also.


Issues:
- I was try lot of new ideas but error and exception are occur, I need a help to create new ideas in Health and Medicine Chatbot Project.

Test output:
```
in_request='hi' -> Sorry
time = 1.0119192600250244
in_request='health' -> Health refers to the extent of a person’s physical, mental, and social well-being. This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. The quality of the social environment in turn can affect a person’s physical and mental health, underscoring the importance of social factors for these twin aspects of our overall well-being.
time = 1.0170891284942627
test passed
```
```
type your answer: hi
in_request='hi' -> Sorry
exec time = 0.008s
type your answer: health
in_request='health' -> Health refers to the extent of a person’s physical, mental, and social well-being. This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. The quality of the social environment in turn can affect a person’s physical and mental health, underscoring the importance of social factors for these twin aspects of our overall well-being.
exec time = 0.005s
type your answer: medicine
in_request='medicine' -> Medicine is the social institution that seeks both to prevent, diagnose, and treat illness and to promote health as just defined. Dissatisfaction with the medical establishment has been growing. Part of this dissatisfaction stems from soaring health-care costs and what many perceive as insensitive stinginess by the health insurance industry, as the 2009 battle over health-care reform illustrated. Some of the dissatisfaction also reflects a growing view that the social and even spiritual realms of human existence play a key role in health and illness. This view has fueled renewed interest in alternative medicine. We return later to these many issues for the social institution of medicine.
exec time = 0.007s
```
# Week 3
....

# Week 4
....
