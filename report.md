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

Test output:
```
in_request='hi' -> hi
test passed
```
```
type your answer: hey
in_request='hey' -> hi
exec time = 0.014s
```
```
type your answer: hi
Okey
type your answer: Hi
Hi!!!
type your answer: ok
Okey
type your answer: ok
Okey
```

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

- - I got analysis of my project as you can see in a graph:-

![image](https://user-images.githubusercontent.com/96828026/149023284-53dec799-358b-43f4-8db1-5437a48aa9ff.png)

# Week 3

TODO:
- Modify the Health and Medicine Chatbot Assitant with help of skill hackathon Project. Make the Chatbot more friendly and interactive and include the health and medicine information in Chatbot and Create a graph with help of model and improve accurancy and evaluation of Health and Medicine help Chatbot with the model and graph


WIP:
- At this point my main goal is generating better health and medicine chatbot environment and their plot , response and condition functions in order to add     different functionality for the dialogs. The assistant first needs to understand similarity and difference between test output and interactive output.
- Creating this scenarios to implement them in the chatbot project.
- Provide more information abot Health and Medicine Chatbot Assitant Serive
- create a graph with help of Neural Network Model and using different library Natural Language Toolkit(nltk), Stemming and matplotlib.
- Implement Data Loading and Data Preprocessing in the model
- Implement Bag of words, Tokenization ideas, Hyper-parameters, Chat Dataset,  Loss and optimizer in the  Neural Network model
- Creating this scenarios to implement them in the code


Done:
- Modify the Health and Medicine Chatbot Assitant and modify the plot and condition code
- Make the transformer of Health and Medicine Chatbot Assitant
- Modify the response, Create Data folder and add Data files in Data folder in Chatbot Project Github
- Create Neural Network Model in model folder and create graph in graph folder
- With help of Neural Network model, graph is plotted and generated the losses and no. of epochs(iterations).
- In model, Create data folder in which health and medicine json file.
- Create implementation folder in which nltk.tools(Tokenization, Stemming and Bag of words), PorterStemmer, torch and matplotlib library.
- In NN model, Data Processing, create X_train, y_trian dataset, Hyper-parameters, Chat Dataset, Data Loader and Device config, Train the model, Loss, Criteria and Optimizer steps are present.
- Graph Plot between the Losses(cost) vs Iteration(per hundred).
- Graph Plot Between Evaluation Accuracy  vs Evaluation Losses.


Issues:
- I was try lot of new non mainstream languages, I need a help to create new ideas in Health and Medicine Chatbot Project.

Test output:

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

- I got analysis of my project as you can see in a graph:-
- - - Plot the Losses(cost) vs Iteration(per hundred)

![image](https://user-images.githubusercontent.com/96828026/149247648-457a79bf-e421-4d77-8609-ed6e408b944d.png)

- - - Plot Between Evaluation Accuracy  vs Evaluation Losses

![image](https://user-images.githubusercontent.com/96828026/149247877-5aef1424-407c-419d-9482-d221fbb42d33.png)



# Week 4
....
