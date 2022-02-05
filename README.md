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
# Task

![image](https://user-images.githubusercontent.com/96828026/152642971-e9c732cc-42d1-44fa-87af-536cb89e8414.png)

![image](https://user-images.githubusercontent.com/96828026/152643267-3fe0f093-29a1-47d2-b259-4e963b09fa36.png)

## Test output:

- run_test() result:-
# English
```
2022-01-27 08:00:34,556-           root:105:        turn_handler():INFO - in_request=Hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
2022-01-27 08:00:34,572-           root:105:        turn_handler():INFO - in_request=I want to book a appointment? ->
 OK! I have book a appointment of Doctor for health checkup for you Sir
2022-01-27 08:00:34,582-           root:105:        turn_handler():INFO - in_request=I want a doctor ->
 There is a many doctor like following:
- Physicians
- Cardiologists
- Gastroenterologists
- Dentist
- ENT specialist
- Gynaecologist
Please write type of doctor according above way
2022-01-27 08:00:34,601-           root:105:        turn_handler():INFO - in_request=I Really want a Physicians ->
 OK! I have book a appointment of physicians Doctor for you Sir
2022-01-27 08:00:34,614-           root:105:        turn_handler():INFO - in_request=Urgently want a Gastroenterologists ->
 OK! I have book a appointment of gastroenterologists Doctor for you Sir
2022-01-27 08:00:34,630-           root:105:        turn_handler():INFO - in_request=I have problem in my ear, Can book a ENT specialist ->
 OK! I have book a appointment of ent specialist Doctor for you Sir
2022-01-27 08:00:34,645-           root:105:        turn_handler():INFO - in_request=I want a Dentist for my teeth ->
 OK! I have book a appointment of dentist Doctor for you Sir
2022-01-27 08:00:34,667-           root:105:        turn_handler():INFO - in_request=I have heart problem, book a Cardiologists ->
 OK! I have book a appointment of cardiologists Doctor for you Sir
2022-01-27 08:00:34,687-           root:105:        turn_handler():INFO - in_request=Thanks ->
 Welcome Sir/Mam
2022-01-27 08:00:34,705-           root:105:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'
2022-01-27 08:00:34,725-           root:105:        turn_handler():INFO - in_request=Hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
2022-01-27 08:00:34,737-           root:105:        turn_handler():INFO - in_request=What is health? ->
 Health refers to the extent of a person’s physical, mental, and social well-being. This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. The quality of the social environment in turn can affect a person’s physical and mental health, underscoring the importance of social factors for these twin aspects of our overall well-being.
2022-01-27 08:00:34,759-           root:105:        turn_handler():INFO - in_request=Define a medicine ->
 Medicine is the social institution that seeks both to prevent, diagnose, and treat illness and to promote health as just defined. Dissatisfaction with the medical establishment has been growing.Part of this dissatisfaction stems from soaring health-care costs and what many perceive as insensitive stinginess by the health insurance industry, as the 2009 battle over health-care reform illustrated. Some of the dissatisfaction also reflects a growing view that the social and even spiritual realms of human existence play a key role in health and illness. This view has fueled renewed interestin alternative medicine. We return later to these many issues for the social institution of medicine.
2022-01-27 08:00:34,771-           root:105:        turn_handler():INFO - in_request=what is mental_health? ->
 Mental health refers to cognitive, behavioral, and emotional well-being. It is all about how people think, feel, and behave. People sometimes use the term “mental health” to mean the absence of a mental disorder. Mental health can affect daily living, relationships, and physical health.Mental health as a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community.
2022-01-27 08:00:34,793-           root:105:        turn_handler():INFO - in_request=how  can are change my diet? ->
 Diet is the sum of food consumed by a person or other organism. The word diet often implies the use of specific intake of nutrition for health or weight-management reasons (with the two often being related). Although humans are omnivores, each culture and each person holds some food preferences or some food taboos. This may be due to personal tastes or ethical reasons. Individual dietary choices may be more or less healthy.Diet includes a variety of plant-based and animal-based foods that provide nutrients to the body. Such nutrients provide the body with energy and keep it running. Nutrients help build and strengthen bones, muscles, and tendons and also regulate body processes (i.e., blood pressure). Water is essential for growth, reproduction and good health. Macronutrients are consumed in relatively large quantities and include proteins, carbohydrates, and fats and fatty acids. Micronutrients – vitamins and minerals – are consumed in relatively smaller quantities, but are essential to body processes.
2022-01-27 08:00:34,816-           root:105:        turn_handler():INFO - in_request=I want a doctor ->
 There is a many doctor like following:
- Physicians
- Cardiologists
- Gastroenterologists
- Dentist
- ENT specialist
- Gynaecologist
Please write type of doctor according above way
2022-01-27 08:00:34,838-           root:105:        turn_handler():INFO - in_request=Thanks ->
 Welcome Sir/Mam
2022-01-27 08:00:34,855-           root:105:        turn_handler():INFO - in_request=Good Service ->
 Welcome Sir/Mam
2022-01-27 08:00:34,882-           root:105:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'
<-- Test Successful -->
```
- run_interactive_mode(actor) result:-

## English
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
# Dutch
- - test output
```
2022-01-27 16:04:33,211-           root:383:        turn_handler():INFO - in_request=hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
2022-01-27 16:04:33,227-           root:383:        turn_handler():INFO - in_request=Ik wil een afspraak boeken? ->
 OKE! Ik heb een afspraak gemaakt met de dokter voor gezondheidscontrole voor u, mijnheer
2022-01-27 16:04:33,251-           root:383:        turn_handler():INFO - in_request=ik wil een arts ->
 Er zijn veel artsen zoals de volgende:
- Artsen
- Cardiologen
- Gastro-enterologen
- Tandarts
- KNO-arts
- Gynaecoloog
Schrijf het type arts op volgens bovenstaande manier
2022-01-27 16:04:33,281-           root:383:        turn_handler():INFO - in_request=Ik wil echt een artsen ->
 OKE! Ik heb een afspraak gemaakt met artsen Dokter voor u meneer
2022-01-27 16:04:33,311-           root:383:        turn_handler():INFO - in_request=Met spoed een gastro-enterologen nodig ->
 OKE! Ik heb een afspraak gemaakt met gastro-enterologen Dokter voor u meneer
2022-01-27 16:04:33,341-           root:383:        turn_handler():INFO - in_request=Ik heb een probleem in mijn oor, kan een KNO-arts boeken ->
 OKE! Ik heb een afspraak gemaakt met kno-arts Dokter voor u meneer
2022-01-27 16:04:33,380-           root:383:        turn_handler():INFO - in_request=Ik wil een tandarts voor mijn tanden ->
 OKE! Ik heb een afspraak gemaakt met tandarts Dokter voor u meneer
2022-01-27 16:04:33,410-           root:383:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardiologen ->
 OKE! Ik heb een afspraak gemaakt met cardiologen Dokter voor u meneer
2022-01-27 16:04:33,439-           root:383:        turn_handler():INFO - in_request=bedankt ->
 Welkom meneer/mama
2022-01-27 16:04:33,473-           root:383:        turn_handler():INFO - in_request=nee ->
 Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen
2022-01-27 16:04:33,486-           root:383:        turn_handler():INFO - in_request=Hoi ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
2022-01-27 16:04:33,513-           root:383:        turn_handler():INFO - in_request=Wat is gezondheid? ->
 Gezondheid verwijst naar de mate van iemands fysieke, mentale en sociale welzijn. Deze definitie, ontleend aan de behandeling van gezondheid door de Wereldgezondheidsorganisatie, benadrukt dat gezondheid een complex concept is dat niet alleen betrekking heeft op de gezondheid van iemands lichaam, maar ook op de gemoedstoestand van een persoon en de kwaliteit van de sociale omgeving waarin hij of zij zich bevindt. leeft. De kwaliteit van de sociale omgeving kan op zijn beurt de fysieke en mentale gezondheid van een persoon beïnvloeden, wat het belang van sociale factoren voor deze tweeledige aspecten van ons algehele welzijn onderstreept.
2022-01-27 16:04:33,544-           root:383:        turn_handler():INFO - in_request=Definieer een geneeskunde ->
 Geneeskunde is de sociale instelling die zowel ziekte wil voorkomen, diagnosticeren en behandelen als de gezondheid zoals zojuist gedefinieerd bevordert. De ontevredenheid over het medische establishment is toegenomen. Een deel van deze ontevredenheid komt voort uit stijgende kosten voor de gezondheidszorg en wat velen beschouwen als ongevoelige gierigheid door de zorgverzekeringsindustrie, zoals de strijd om de hervorming van de gezondheidszorg in 2009 illustreerde. Een deel van de ontevredenheid weerspiegelt ook een groeiende opvatting dat de sociale en zelfs spirituele gebieden van het menselijk bestaan een sleutelrol spelen bij gezondheid en ziekte. Deze visie heeft geleid tot een hernieuwde belangstelling voor alternatieve geneeswijzen. We komen later terug op deze vele kwesties voor de sociale instelling van de geneeskunde.
2022-01-27 16:04:33,577-           root:383:        turn_handler():INFO - in_request=wat is mentale_gezondheid? ->
 Geestelijke gezondheid verwijst naar cognitief, gedrags- en emotioneel welzijn. Het gaat erom hoe mensen denken, voelen en zich gedragen. Mensen gebruiken de term 'geestelijke gezondheid' soms om de afwezigheid van een psychische stoornis aan te duiden. Geestelijke gezondheid kan het dagelijks leven, relaties en lichamelijke gezondheid beïnvloeden. Geestelijke gezondheid als een toestand van welzijn waarin het individu zijn of haar eigen capaciteiten realiseert, de normale stress van het leven aankan, productief en vruchtbaar kan werken en een bijdrage kan leveren aan zijn of haar gemeenschap.
2022-01-27 16:04:33,603-           root:383:        turn_handler():INFO - in_request=hoe kan ik mijn eetpatroon veranderen? ->
 Dieet is de som van voedsel dat door een persoon of een ander organisme wordt geconsumeerd. Het woord dieet impliceert vaak het gebruik van een specifieke inname van voeding om redenen van gezondheid of gewichtsbeheersing (waarbij beide vaak gerelateerd zijn). Hoewel mensen alleseters zijn, heeft elke cultuur en elke persoon bepaalde voedselvoorkeuren of voedseltaboes. Dit kan te wijten zijn aan persoonlijke smaak of ethische redenen. Individuele voedingskeuzes kunnen min of meer gezond zijn. Dieet omvat een verscheidenheid aan plantaardige en dierlijke voedingsmiddelen die het lichaam van voedingsstoffen voorzien. Dergelijke voedingsstoffen voorzien het lichaam van energie en houden het draaiende. Voedingsstoffen helpen bij het opbouwen en versterken van botten, spieren en pezen en reguleren ook lichaamsprocessen (d.w.z. bloeddruk). Water is essentieel voor groei, voortplanting en een goede gezondheid. Macronutriënten worden in relatief grote hoeveelheden geconsumeerd en omvatten eiwitten, koolhydraten en vetten en vetzuren. Micronutriënten – vitamines en mineralen – worden in relatief kleinere hoeveelheden geconsumeerd, maar zijn essentieel voor lichaamsprocessen.
2022-01-27 16:04:33,642-           root:383:        turn_handler():INFO - in_request=ik wil een arts ->
 Er zijn veel artsen zoals de volgende:
- Artsen
- Cardiologen
- Gastro-enterologen
- Tandarts
- KNO-arts
- Gynaecoloog
Schrijf het type arts op volgens bovenstaande manier
2022-01-27 16:04:33,677-           root:383:        turn_handler():INFO - in_request=Bedankt ->
 Welkom meneer/mama
2022-01-27 16:04:33,719-           root:383:        turn_handler():INFO - in_request=Goed service ->
 Welkom meneer/mama
2022-01-27 16:04:33,763-           root:383:        turn_handler():INFO - in_request=Niets ->
 Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen
<-- Test Successful -->
```
- - interactive output

## Dutch
```
type your answer: Hallo
2022-01-27 11:39:22,858-           root: 32:        turn_handler():INFO - in_request=Hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.043s
type your answer: Ik wil echt een artsen
2022-01-27 11:39:37,514-           root: 32:        turn_handler():INFO - in_request=Ik wil echt een artsen ->
 OKE! Ik heb een afspraak gemaakt met artsen Dokter voor u meneer
exec time = 0.022s
type your answer: Met spoed een gastro-enteroloog nodig
2022-01-27 11:42:26,733-           root: 32:        turn_handler():INFO - in_request=Met spoed een gastro-enteroloog nodig ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.025s
type your answer: gastro-enteroloog
2022-01-27 11:42:48,535-           root: 32:        turn_handler():INFO - in_request=gastro-enteroloog ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.042s
type your answer: Met spoed een gastro-enterologen nodig
2022-01-27 11:45:18,513-           root: 32:        turn_handler():INFO - in_request=Met spoed een gastro-enterologen nodig ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.088s
type your answer: Hallo
2022-01-27 11:45:41,348-           root: 32:        turn_handler():INFO - in_request=Hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.054s
type your answer: Met spoed een gastro-enterologen nodig
2022-01-27 11:45:48,288-           root: 32:        turn_handler():INFO - in_request=Met spoed een gastro-enterologen nodig ->
 OKE! Ik heb een afspraak gemaakt met gastro-enterologen Dokter voor u meneer
exec time = 0.024s
type your answer: I have problem in my ear, Can book a ENT specialist
2022-01-27 11:47:06,477-           root: 32:        turn_handler():INFO - in_request=I have problem in my ear, Can book a ENT specialist ->
 Welkom meneer/mama
exec time = 0.026s
type your answer: Ik heb een probleem in mijn oor, kan een KNO-arts boeken
2022-01-27 11:48:47,819-           root: 32:        turn_handler():INFO - in_request=Ik heb een probleem in mijn oor, kan een KNO-arts boeken ->
 OKE! Ik heb een afspraak gemaakt met kno-arts Dokter voor u meneer
exec time = 0.023s
type your answer: Ik wil een tandarts voor mijn tanden
2022-01-27 11:51:29,739-           root: 32:        turn_handler():INFO - in_request=Ik wil een tandarts voor mijn tanden ->
 OKE! Ik heb een afspraak gemaakt met tandarts Dokter voor u meneer
exec time = 0.023s
type your answer: Ik heb een hartprobleem, boek een cardioloog
2022-01-27 11:53:06,589-           root: 32:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardioloog ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.026s
type your answer: Ik heb een hartprobleem, boek een cardiologen
2022-01-27 11:54:27,541-           root: 32:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardiologen ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.032s
type your answer: Ik heb een hartprobleem, boek een cardiologen
2022-01-27 11:54:42,654-           root: 32:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardiologen ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.049s
type your answer: Ik heb een hartprobleem, boek een cardiologen
2022-01-27 11:55:21,658-           root: 32:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardiologen ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.049s
type your answer: Ik heb een hartprobleem, boek een cardiologen
2022-01-27 11:58:33,894-           root: 32:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardiologen ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.032s
type your answer: Hallo
2022-01-27 12:00:32,055-           root: 32:        turn_handler():INFO - in_request=Hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.033s
type your answer: Ik heb een hartprobleem, boek een cardiologen
2022-01-27 12:00:36,580-           root: 32:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardiologen ->
 OKE! Ik heb een afspraak gemaakt met cardiologen Dokter voor u meneer
exec time = 0.025s
type your answer: OK! I have book a appointment of cardiologen Doctor for you Sir
2022-01-27 12:47:03,808-           root: 32:        turn_handler():INFO - in_request=OK! I have book a appointment of cardiologen Doctor for you Sir ->
 OKE! Ik heb een afspraak gemaakt met cardiologen Dokter voor u meneer
exec time = 0.026s
type your answer: Ik heb een hartprobleem, boek een cardiologen
2022-01-27 13:02:25,973-           root: 32:        turn_handler():INFO - in_request=Ik heb een hartprobleem, boek een cardiologen ->
 OKE! Ik heb een afspraak gemaakt met cardiologen Dokter voor u meneer
exec time = 0.024s
type your answer: bedankt
2022-01-27 15:39:15,783-           root: 32:        turn_handler():INFO - in_request=bedankt ->
 Welkom meneer/mama
exec time = 0.030s
type your answer: OK
2022-01-27 15:39:59,096-           root: 32:        turn_handler():INFO - in_request=OK ->
 Welkom meneer/mama
exec time = 0.036s
type your answer: nee
2022-01-27 15:41:02,806-           root: 32:        turn_handler():INFO - in_request=nee ->
 Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen
exec time = 0.036s
type your answer: hallo
2022-01-27 15:43:43,208-           root: 32:        turn_handler():INFO - in_request=hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.018s
type your answer: ok doei
2022-01-27 15:44:07,026-           root: 32:        turn_handler():INFO - in_request=ok doei ->
 Welkom meneer/mama
exec time = 0.028s
type your answer: nee help
2022-01-27 15:44:56,038-           root: 32:        turn_handler():INFO - in_request=nee help ->
 Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen
exec time = 0.032s
type your answer: Wat is gezondheid?
2022-01-27 15:46:35,088-           root: 32:        turn_handler():INFO - in_request=Wat is gezondheid? ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.015s
type your answer: hallo
2022-01-27 15:47:38,277-           root: 32:        turn_handler():INFO - in_request=hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.037s
type your answer: Wat is gezondheid?
2022-01-27 15:47:43,378-           root: 32:        turn_handler():INFO - in_request=Wat is gezondheid? ->
 Gezondheid verwijst naar de mate van iemands fysieke, mentale en sociale welzijn. Deze definitie, ontleend aan de behandeling van gezondheid door de Wereldgezondheidsorganisatie, benadrukt dat gezondheid een complex concept is dat niet alleen betrekking heeft op de gezondheid van iemands lichaam, maar ook op de gemoedstoestand van een persoon en de kwaliteit van de sociale omgeving waarin hij of zij zich bevindt. leeft. De kwaliteit van de sociale omgeving kan op zijn beurt de fysieke en mentale gezondheid van een persoon beïnvloeden, wat het belang van sociale factoren voor deze tweeledige aspecten van ons algehele welzijn onderstreept.
exec time = 0.022s
type your answer: Definieer een geneeskunde
2022-01-27 15:49:45,514-           root: 32:        turn_handler():INFO - in_request=Definieer een geneeskunde ->
 Geneeskunde is de sociale instelling die zowel ziekte wil voorkomen, diagnosticeren en behandelen als de gezondheid zoals zojuist gedefinieerd bevordert. De ontevredenheid over het medische establishment is toegenomen. Een deel van deze ontevredenheid komt voort uit stijgende kosten voor de gezondheidszorg en wat velen beschouwen als ongevoelige gierigheid door de zorgverzekeringsindustrie, zoals de strijd om de hervorming van de gezondheidszorg in 2009 illustreerde. Een deel van de ontevredenheid weerspiegelt ook een groeiende opvatting dat de sociale en zelfs spirituele gebieden van het menselijk bestaan een sleutelrol spelen bij gezondheid en ziekte. Deze visie heeft geleid tot een hernieuwde belangstelling voor alternatieve geneeswijzen. We komen later terug op deze vele kwesties voor de sociale instelling van de geneeskunde.
exec time = 0.021s
type your answer: wat is mentale_gezondheid?
2022-01-27 15:51:32,041-           root: 32:        turn_handler():INFO - in_request=wat is mentale_gezondheid? ->
 Geestelijke gezondheid verwijst naar cognitief, gedrags- en emotioneel welzijn. Het gaat erom hoe mensen denken, voelen en zich gedragen. Mensen gebruiken de term 'geestelijke gezondheid' soms om de afwezigheid van een psychische stoornis aan te duiden. Geestelijke gezondheid kan het dagelijks leven, relaties en lichamelijke gezondheid beïnvloeden. Geestelijke gezondheid als een toestand van welzijn waarin het individu zijn of haar eigen capaciteiten realiseert, de normale stress van het leven aankan, productief en vruchtbaar kan werken en een bijdrage kan leveren aan zijn of haar gemeenschap.
exec time = 0.030s
type your answer: hoe kan ik mijn dieet veranderen?
2022-01-27 15:53:55,860-           root: 32:        turn_handler():INFO - in_request=hoe kan ik mijn dieet veranderen? ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.029s
type your answer: hallo
2022-01-27 15:54:02,116-           root: 32:        turn_handler():INFO - in_request=hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.037s
type your answer: hoe kan ik mijn eetpatroon veranderen?
2022-01-27 15:54:30,051-           root: 32:        turn_handler():INFO - in_request=hoe kan ik mijn eetpatroon veranderen? ->
 Dieet is de som van voedsel dat door een persoon of een ander organisme wordt geconsumeerd. Het woord dieet impliceert vaak het gebruik van een specifieke inname van voeding om redenen van gezondheid of gewichtsbeheersing (waarbij beide vaak gerelateerd zijn). Hoewel mensen alleseters zijn, heeft elke cultuur en elke persoon bepaalde voedselvoorkeuren of voedseltaboes. Dit kan te wijten zijn aan persoonlijke smaak of ethische redenen. Individuele voedingskeuzes kunnen min of meer gezond zijn. Dieet omvat een verscheidenheid aan plantaardige en dierlijke voedingsmiddelen die het lichaam van voedingsstoffen voorzien. Dergelijke voedingsstoffen voorzien het lichaam van energie en houden het draaiende. Voedingsstoffen helpen bij het opbouwen en versterken van botten, spieren en pezen en reguleren ook lichaamsprocessen (d.w.z. bloeddruk). Water is essentieel voor groei, voortplanting en een goede gezondheid. Macronutriënten worden in relatief grote hoeveelheden geconsumeerd en omvatten eiwitten, koolhydraten en vetten en vetzuren. Micronutriënten – vitamines en mineralen – worden in relatief kleinere hoeveelheden geconsumeerd, maar zijn essentieel voor lichaamsprocessen.
exec time = 0.027s
type your answer: ik wil een arts
2022-01-27 15:57:20,657-           root: 32:        turn_handler():INFO - in_request=ik wil een arts ->
 Er zijn veel artsen zoals de volgende:
- Artsen
- Cardiologen
- Gastro-enterologen
- Tandarts
- KNO-arts
- Gynaecoloog
Schrijf het type arts op volgens bovenstaande manier
exec time = 0.027s
type your answer: Bedankt
2022-01-27 15:58:30,928-           root: 32:        turn_handler():INFO - in_request=Bedankt ->
 Welkom meneer/mama
exec time = 0.027s
type your answer: Goed service
2022-01-27 15:59:48,948-           root: 32:        turn_handler():INFO - in_request=Goed service ->
 Welkom meneer/mama
exec time = 0.030s
type your answer: doei
2022-01-27 16:00:48,387-           root: 32:        turn_handler():INFO - in_request=doei ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.033s
type your answer: Hallo
2022-01-27 16:02:34,582-           root: 32:        turn_handler():INFO - in_request=Hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.034s
type your answer: Niets
2022-01-27 16:02:36,290-           root: 32:        turn_handler():INFO - in_request=Niets ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
exec time = 0.035s
type your answer: hallo
2022-01-27 16:02:41,066-           root: 32:        turn_handler():INFO - in_request=hallo ->
 Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?
exec time = 0.035s
type your answer: Goed service
2022-01-27 16:02:51,996-           root: 32:        turn_handler():INFO - in_request=Goed service ->
 Welkom meneer/mama
exec time = 0.026s
type your answer: Niets
2022-01-27 16:02:57,936-           root: 32:        turn_handler():INFO - in_request=Niets ->
 Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen
exec time = 0.028s
```

# Spanish
- - test output
```
2022-01-27 19:44:01,331-           root:383:        turn_handler():INFO - in_request=Hola ->
 Hola!, soy asistente de un chatbot de salud y medicina, cómo puedo ayudarte?
2022-01-27 19:44:01,348-           root:383:        turn_handler():INFO - in_request=quiero reservar una cita? ->
 ¡OK! He reservado una cita con el médico para un chequeo de salud para usted, señor.
2022-01-27 19:44:01,372-           root:383:        turn_handler():INFO - in_request=Quiero un médico ->
 Hay muchos médicos como los siguientes:
- Médicos
- Cardiólogos
- Gastroenterólogos
- Dentista
- Otorrinolaringólogo
- Ginecólogo
Escriba el tipo de médico de acuerdo con la forma anterior
2022-01-27 19:44:01,389-           root:383:        turn_handler():INFO - in_request=I Realmente quiero una médicos ->
 OK! He reservado una cita con médicos médico para usted, señor.
2022-01-27 19:44:01,420-           root:383:        turn_handler():INFO - in_request=Urge un Gastroenterólogos ->
 OK! He reservado una cita con gastroenterólogos médico para usted, señor.
2022-01-27 19:44:01,461-           root:383:        turn_handler():INFO - in_request=Tengo un problema en mi oído, puedo reservar un otorrinolaringólogo ->
 OK! He reservado una cita con otorrinolaringólogo médico para usted, señor.
2022-01-27 19:44:01,496-           root:383:        turn_handler():INFO - in_request=Quiero un dentista para mis dientes ->
 OK! He reservado una cita con dentista médico para usted, señor.
2022-01-27 19:44:01,551-           root:383:        turn_handler():INFO - in_request=Tengo problema del corazón, reserve un Cardiólogos ->
 OK! He reservado una cita con cardiólogos médico para usted, señor.
2022-01-27 19:44:01,625-           root:383:        turn_handler():INFO - in_request=Gracias ->
 Welkom meneer/mama
2022-01-27 19:44:01,697-           root:383:        turn_handler():INFO - in_request=no ->
 Claro señor, gracias por su visita, pero puede ir a otros servicios si es necesario, puede escribir 'hola'
2022-01-27 19:44:01,744-           root:383:        turn_handler():INFO - in_request=Oye ->
 Hola!, soy asistente de un chatbot de salud y medicina, cómo puedo ayudarte?
2022-01-27 19:44:01,811-           root:383:        turn_handler():INFO - in_request=Que es la sanidad? ->
 La salud se refiere al grado de bienestar físico, mental y social de una persona. Esta definición, tomada del tratamiento de la salud de la Organización Mundial de la Salud, enfatiza que la salud es un concepto complejo que involucra no solo la solidez del cuerpo de una persona sino también el estado mental de una persona y la calidad del entorno social en el que ella o él. vidas. A su vez, la calidad del entorno social puede afectar la salud física y mental de una persona, lo que subraya la importancia de los factores sociales para estos dos aspectos de nuestro bienestar general.
2022-01-27 19:44:01,850-           root:383:        turn_handler():INFO - in_request=Definir un medicamento ->
 La medicina es la institución social que busca tanto prevenir, diagnosticar y tratar la enfermedad como promover la salud tal como se acaba de definir. La insatisfacción con el establecimiento médico ha ido en aumento. Parte de esta insatisfacción se deriva del aumento de los costos de la atención médica y lo que muchos perciben como una tacañería insensible por parte de la industria de seguros de salud, como lo ilustró la batalla de 2009 por la reforma de la atención médica. Parte de la insatisfacción también refleja una visión creciente de que los ámbitos social e incluso espiritual de la existencia humana juegan un papel clave en la salud y la enfermedad. Este punto de vista ha alimentado un interés renovado en la medicina alternativa. Regresaremos más adelante a estos muchos temas para la institución social de la medicina.
2022-01-27 19:44:01,870-           root:383:        turn_handler():INFO - in_request=que es salud_mental? ->
 La salud mental se refiere al bienestar cognitivo, conductual y emocional. Se trata de cómo las personas piensan, sienten y se comportan. Las personas a veces usan el término “salud mental” para referirse a la ausencia de un trastorno mental. La salud mental puede afectar la vida diaria, las relaciones y la salud física. La salud mental es un estado de bienestar en el que el individuo se da cuenta de sus propias capacidades, puede hacer frente a las tensiones normales de la vida, puede trabajar de manera productiva y fructífera, y es capaz de hacer una contribución a su comunidad.
2022-01-27 19:44:01,886-           root:383:        turn_handler():INFO - in_request=como puedo cambiar mi dieta? ->
 La dieta es la suma de los alimentos consumidos por una persona u otro organismo. La palabra dieta a menudo implica el uso de una ingesta específica de nutrición por razones de salud o de control de peso (con las dos a menudo relacionadas). Aunque los humanos somos omnívoros, cada cultura y cada persona tiene unas preferencias alimentarias o unos tabúes alimentarios. Esto puede deberse a gustos personales o razones éticas. Las opciones dietéticas individuales pueden ser más o menos saludables. La dieta incluye una variedad de alimentos de origen vegetal y animal que proporcionan nutrientes al cuerpo. Dichos nutrientes proporcionan energía al cuerpo y lo mantienen en funcionamiento. Los nutrientes ayudan a desarrollar y fortalecer huesos, músculos y tendones y también regulan los procesos corporales (es decir, la presión arterial). El agua es esencial para el crecimiento, la reproducción y la buena salud. Los macronutrientes se consumen en cantidades relativamente grandes e incluyen proteínas, carbohidratos y grasas y ácidos grasos. Los micronutrientes (vitaminas y minerales) se consumen en cantidades relativamente pequeñas, pero son esenciales para los procesos corporales.
2022-01-27 19:44:01,925-           root:383:        turn_handler():INFO - in_request=Quiero un médica ->
 Hay muchos médicos como los siguientes:
- Médicos
- Cardiólogos
- Gastroenterólogos
- Dentista
- Otorrinolaringólogo
- Ginecólogo
Escriba el tipo de médico de acuerdo con la forma anterior
2022-01-27 19:44:01,955-           root:383:        turn_handler():INFO - in_request=agradecimiento ->
 Welkom meneer/mama
2022-01-27 19:44:02,002-           root:383:        turn_handler():INFO - in_request=Bien servicio ->
 Welkom meneer/mama
2022-01-27 19:44:02,033-           root:383:        turn_handler():INFO - in_request=nada ->
 Claro señor, gracias por su visita, pero puede ir a otros servicios si es necesario, puede escribir 'hola'
```
# Greek
```
2022-01-28 01:42:40,334-           root:382:        turn_handler():INFO - in_request=γεια ->
 Γεια!, είμαι Βοηθός Chatbot για την υγεία και την ιατρική, πώς μπορεί να σας βοηθήσει?
2022-01-28 01:42:40,353-           root:382:        turn_handler():INFO - in_request=Θέλω να κλείσω ένα ραντεβού? ->
 ΟΚ! Έχω κλείσει ραντεβού γιατρού για έλεγχο υγείας για εσάς κύριε
2022-01-28 01:42:40,367-           root:382:        turn_handler():INFO - in_request=θελω α γιατρός ->
 Υπάρχουν πολλοί γιατροί όπως οι ακόλουθοι:
- Γιατροί
- Καρδιολόγοι
- Γαστρεντερολόγοι
- Οδοντίατρος
- Ειδικός ΩΡΛ
- Γυναικολόγος
Παρακαλώ γράψτε τον τύπο του γιατρού σύμφωνα με τον παραπάνω τρόπο
2022-01-28 01:42:40,398-           root:382:        turn_handler():INFO - in_request=Θέλω πραγματικά ένα Γιατροί ->
 ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό γιατροί για εσάς, κύριε
2022-01-28 01:42:40,423-           root:382:        turn_handler():INFO - in_request=Έχω πρόβλημα στο αυτί μου, μπορώ να κάνω κράτηση α Ειδικός ΩΡΛ ->
 ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό ειδικός ωρλ για εσάς, κύριε
2022-01-28 01:42:40,461-           root:382:        turn_handler():INFO - in_request=Παροτρύνω ου Γαστρεντερολόγοι ->
 ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό γαστρεντερολόγοι για εσάς, κύριε
2022-01-28 01:42:40,503-           root:382:        turn_handler():INFO - in_request=Έχω πρόβλημα με την καρδιά, βιβλίο α Καρδιολόγοι ->
 ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό καρδιολόγοι για εσάς, κύριε
2022-01-28 01:42:40,584-           root:382:        turn_handler():INFO - in_request=Θέλω ένα για Οδοντίατρος τα δόντια μου ->
 ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό οδοντίατρος για εσάς, κύριε
2022-01-28 01:42:40,659-           root:382:        turn_handler():INFO - in_request=Ευχαριστώ ->
 Καλώς ήλθατε κύριε/μαμ
2022-01-28 01:42:40,714-           root:382:        turn_handler():INFO - in_request=όχι ->
 Βεβαίως κύριε, ευχαριστώ για την επίσκεψή σας, αλλά μπορείτε να πάτε σε άλλες υπηρεσίες αν χρειαστεί μπορείτε να πληκτρολογήσετε 'γεια'
2022-01-28 01:42:40,732-           root:382:        turn_handler():INFO - in_request=γεια ->
 Γεια!, είμαι Βοηθός Chatbot για την υγεία και την ιατρική, πώς μπορεί να σας βοηθήσει?
2022-01-28 01:42:40,767-           root:382:        turn_handler():INFO - in_request=τι ειναι υγεία? ->
 Η υγεία αναφέρεται στην έκταση της σωματικής, ψυχικής και κοινωνικής ευημερίας ενός ατόμου. Αυτός ο ορισμός, που λαμβάνεται από τη θεραπεία της υγείας του Παγκόσμιου Οργανισμού Υγείας, τονίζει ότι η υγεία είναι μια σύνθετη έννοια που περιλαμβάνει όχι μόνο την ευρωστία του σώματος ενός ατόμου αλλά και την κατάσταση του μυαλού ενός ατόμου και την ποιότητα του κοινωνικού περιβάλλοντος στο οποίο ζει. Η ποιότητα του κοινωνικού περιβάλλοντος με τη σειρά της μπορεί να επηρεάσει τη σωματική και ψυχική υγεία ενός ατόμου, υπογραμμίζοντας τη σημασία των κοινωνικών παραγόντων για αυτές τις δίδυμες πτυχές της συνολικής μας ευημερίας.
2022-01-28 01:42:40,803-           root:382:        turn_handler():INFO - in_request=Ορίστε ένα φάρμακο ->
 Η ιατρική είναι ο κοινωνικός θεσμός που επιδιώκει τόσο την πρόληψη, τη διάγνωση και τη θεραπεία ασθενειών και την προαγωγή της υγείας όπως ακριβώς ορίστηκε. Η δυσαρέσκεια με το ιατρικό κατεστημένο έχει αυξηθεί. Μέρος αυτής της δυσαρέσκειας προέρχεται από το αυξανόμενο κόστος της υγειονομικής περίθαλψης και από αυτό που πολλοί αντιλαμβάνονται ως μη ευαίσθητη τσιγκουνιά από τον κλάδο της ασφάλισης υγείας, όπως φαίνεται από τη μάχη του 2009 για τη μεταρρύθμιση της υγειονομικής περίθαλψης. Κάποια από τη δυσαρέσκεια αντικατοπτρίζει επίσης μια αυξανόμενη άποψη ότι οι κοινωνικές και ακόμη και πνευματικές σφαίρες της ανθρώπινης ύπαρξης διαδραματίζουν βασικό ρόλο στην υγεία και την ασθένεια. Αυτή η άποψη έχει τροφοδοτήσει ανανεωμένο ενδιαφέρον για την εναλλακτική ιατρική. Επανερχόμαστε αργότερα σε αυτά τα πολλά θέματα για τον κοινωνικό θεσμό της ιατρικής.
2022-01-28 01:42:40,825-           root:382:        turn_handler():INFO - in_request=τι είναι ψυχική_υγειονομικός ->
 Η ψυχική υγεία αναφέρεται στη γνωσιακή, συμπεριφορική και συναισθηματική ευημερία. Έχει να κάνει με το πώς σκέφτονται, αισθάνονται και συμπεριφέρονται οι άνθρωποι. Οι άνθρωποι χρησιμοποιούν μερικές φορές τον όρο «ψυχική υγεία» για να σημαίνει την απουσία ψυχικής διαταραχής. Η ψυχική υγεία μπορεί να επηρεάσει την καθημερινή ζωή, τις σχέσεις και τη σωματική υγεία. Η ψυχική υγεία είναι μια κατάσταση ευεξίας στην οποία το άτομο συνειδητοποιεί τις δικές του ικανότητες, μπορεί να αντιμετωπίσει το φυσιολογικό άγχος της ζωής, μπορεί να εργαστεί παραγωγικά και γόνιμα και μπορεί να συνεισφέρει στην κοινότητά του/της.
2022-01-28 01:42:40,850-           root:382:        turn_handler():INFO - in_request=δίαιτα ->
 Η δίαιτα είναι το άθροισμα της τροφής που καταναλώνει ένα άτομο ή άλλος οργανισμός. Η λέξη δίαιτα συχνά υποδηλώνει τη χρήση συγκεκριμένης πρόσληψης διατροφής για λόγους υγείας ή διαχείρισης βάρους (με τα δύο συχνά να σχετίζονται). Αν και οι άνθρωποι είναι παμφάγοι, κάθε πολιτισμός και κάθε άτομο έχει κάποιες διατροφικές προτιμήσεις ή κάποια ταμπού για τα τρόφιμα. Αυτό μπορεί να οφείλεται σε προσωπικά γούστα ή ηθικούς λόγους. Οι μεμονωμένες διατροφικές επιλογές μπορεί να είναι λίγο πολύ υγιεινές. Η διατροφή περιλαμβάνει μια ποικιλία φυτικών και ζωικών τροφών που παρέχουν θρεπτικά συστατικά στον οργανισμό. Τέτοια θρεπτικά συστατικά παρέχουν στο σώμα ενέργεια και τον κρατούν σε λειτουργία. Τα θρεπτικά συστατικά βοηθούν στην οικοδόμηση και ενίσχυση των οστών, των μυών και των τενόντων και επίσης ρυθμίζουν τις διεργασίες του σώματος (δηλαδή την αρτηριακή πίεση). Το νερό είναι απαραίτητο για την ανάπτυξη, την αναπαραγωγή και την καλή υγεία. Τα μακροθρεπτικά συστατικά καταναλώνονται σε σχετικά μεγάλες ποσότητες και περιλαμβάνουν πρωτεΐνες, υδατάνθρακες και λίπη και λιπαρά οξέα. Τα μικροθρεπτικά συστατικά - βιταμίνες και μέταλλα - καταναλώνονται σε σχετικά μικρότερες ποσότητες, αλλά είναι απαραίτητα για τις διαδικασίες του σώματος.
2022-01-28 01:42:40,874-           root:382:        turn_handler():INFO - in_request=θελω α γιατρός ->
 Υπάρχουν πολλοί γιατροί όπως οι ακόλουθοι:
- Γιατροί
- Καρδιολόγοι
- Γαστρεντερολόγοι
- Οδοντίατρος
- Ειδικός ΩΡΛ
- Γυναικολόγος
Παρακαλώ γράψτε τον τύπο του γιατρού σύμφωνα με τον παραπάνω τρόπο
2022-01-28 01:42:40,911-           root:382:        turn_handler():INFO - in_request=Ευχαριστώ ->
 Καλώς ήλθατε κύριε/μαμ
2022-01-28 01:42:40,958-           root:382:        turn_handler():INFO - in_request=τίποτα ->
 Βεβαίως κύριε, ευχαριστώ για την επίσκεψή σας, αλλά μπορείτε να πάτε σε άλλες υπηρεσίες αν χρειαστεί μπορείτε να πληκτρολογήσετε 'γεια'
2022-01-28 01:42:40,974-           root:382:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
2022-01-28 01:42:41,018-
```

# Russian
```
Привет! Я Здоровье и медицина Помощник по чат-боту, как может вам помочь?
2022-01-28 01:42:41,045-           root:382:        turn_handler():INFO - in_request=назначение ->
 OKE! Ik heb een afspraak gemaakt met de dokter voor gezondheidscontrole voor u, mijnheer
2022-01-28 01:42:41,077-           root:382:        turn_handler():INFO - in_request=Кардиологи ->
 В ПОРЯДКЕ! Я записал вас на прием к  врачу, сэр.
2022-01-28 01:42:41,111-           root:382:        turn_handler():INFO - in_request=Гастроэнтерологи ->
 В ПОРЯДКЕ! Я записал вас на прием к  врачу, сэр.
2022-01-28 01:42:41,131-           root:382:        turn_handler():INFO - in_request=здоровье ->
 Gezondheid verwijst naar de mate van iemands fysieke, mentale en sociale welzijn. Deze definitie, ontleend aan de behandeling van gezondheid door de Wereldgezondheidsorganisatie, benadrukt dat gezondheid een complex concept is dat niet alleen betrekking heeft op de gezondheid van iemands lichaam, maar ook op de gemoedstoestand van een persoon en de kwaliteit van de sociale omgeving waarin hij of zij zich bevindt. leeft. De kwaliteit van de sociale omgeving kan op zijn beurt de fysieke en mentale gezondheid van een persoon beïnvloeden, wat het belang van sociale factoren voor deze tweeledige aspecten van ons algehele welzijn onderstreept.
2022-01-28 01:42:41,160-           root:382:        turn_handler():INFO - in_request=лекарство ->
 Geneeskunde is de sociale instelling die zowel ziekte wil voorkomen, diagnosticeren en behandelen als de gezondheid zoals zojuist gedefinieerd bevordert. De ontevredenheid over het medische establishment is toegenomen. Een deel van deze ontevredenheid komt voort uit stijgende kosten voor de gezondheidszorg en wat velen beschouwen als ongevoelige gierigheid door de zorgverzekeringsindustrie, zoals de strijd om de hervorming van de gezondheidszorg in 2009 illustreerde. Een deel van de ontevredenheid weerspiegelt ook een groeiende opvatting dat de sociale en zelfs spirituele gebieden van het menselijk bestaan een sleutelrol spelen bij gezondheid en ziekte. Deze visie heeft geleid tot een hernieuwde belangstelling voor alternatieve geneeswijzen. We komen later terug op deze vele kwesties voor de sociale instelling van de geneeskunde.
2022-01-28 01:42:41,190-           root:382:        turn_handler():INFO - in_request=диета ->
 Dieet is de som van voedsel dat door een persoon of een ander organisme wordt geconsumeerd. Het woord dieet impliceert vaak het gebruik van een specifieke inname van voeding om redenen van gezondheid of gewichtsbeheersing (waarbij beide vaak gerelateerd zijn). Hoewel mensen alleseters zijn, heeft elke cultuur en elke persoon bepaalde voedselvoorkeuren of voedseltaboes. Dit kan te wijten zijn aan persoonlijke smaak of ethische redenen. Individuele voedingskeuzes kunnen min of meer gezond zijn. Dieet omvat een verscheidenheid aan plantaardige en dierlijke voedingsmiddelen die het lichaam van voedingsstoffen voorzien. Dergelijke voedingsstoffen voorzien het lichaam van energie en houden het draaiende. Voedingsstoffen helpen bij het opbouwen en versterken van botten, spieren en pezen en reguleren ook lichaamsprocessen (d.w.z. bloeddruk). Water is essentieel voor groei, voortplanting en een goede gezondheid. Macronutriënten worden in relatief grote hoeveelheden geconsumeerd en omvatten eiwitten, koolhydraten en vetten en vetzuren. Micronutriënten – vitamines en mineralen – worden in relatief kleinere hoeveelheden geconsumeerd, maar zijn essentieel voor lichaamsprocessen.
2022-01-28 01:42:41,223-           root:382:        turn_handler():INFO - in_request=психическое_здоровье ->
 Geestelijke gezondheid verwijst naar cognitief, gedrags- en emotioneel welzijn. Het gaat erom hoe mensen denken, voelen en zich gedragen. Mensen gebruiken de term 'geestelijke gezondheid' soms om de afwezigheid van een psychische stoornis aan te duiden. Geestelijke gezondheid kan het dagelijks leven, relaties en lichamelijke gezondheid beïnvloeden. Geestelijke gezondheid als een toestand van welzijn waarin het individu zijn of haar eigen capaciteiten realiseert, de normale stress van het leven aankan, productief en vruchtbaar kan werken en een bijdrage kan leveren aan zijn of haar gemeenschap.
2022-01-28 01:42:41,248-           root:382:        turn_handler():INFO - in_request=Спасибо ->
 Добро пожаловать, сэр/мама
2022-01-28 01:42:41,291-           root:382:        turn_handler():INFO - in_request=нет ->
 Конечно сэр, Я благодарю за ваш визит, но вы можете воспользоваться другими услугами, если это необходимо, вы можете ввести 'Привет'
2022-01-28 01:42:41,307-           root:382:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
```

# Danish
```
2022-01-28 01:42:41,347-           root:382:        turn_handler():INFO - in_request=Hej ->
 Hej!, jeg er Sundhed og Medicin Chatbot assistent, hvordan kan hjælpe dig?
2022-01-28 01:42:41,373-           root:382:        turn_handler():INFO - in_request=udnævnelse ->
 OK! Jeg har booket en tid hos lægen til sundhedstjek for dig Sir
2022-01-28 01:42:41,392-           root:382:        turn_handler():INFO - in_request=Kardiologer ->
 OK! Jeg har booket en tid til kardiologer læge til dig, hr
2022-01-28 01:42:41,412-           root:382:        turn_handler():INFO - in_request=Tandlæge ->
 OK! Jeg har booket en tid til tandlæge læge til dig, hr
2022-01-28 01:42:41,452-           root:382:        turn_handler():INFO - in_request=sundhed ->
 Sundhed refererer til omfanget af en persons fysiske, mentale og sociale velbefindende. Denne definition, taget fra Verdenssundhedsorganisationens behandling af sundhed, understreger, at sundhed er et komplekst begreb, der ikke kun involverer sundheden af en persons krop, men også en persons sindstilstand og kvaliteten af det sociale miljø, hvori hun eller han liv. Kvaliteten af det sociale miljø kan igen påvirke en persons fysiske og mentale sundhed, hvilket understreger betydningen af sociale faktorer for disse dobbelte aspekter af vores generelle velbefindende.
2022-01-28 01:42:41,480-           root:382:        turn_handler():INFO - in_request=medicin ->
 Medicin er den sociale institution, der både søger at forebygge, diagnosticere og behandle sygdom og at fremme sundhed som netop defineret. Utilfredsheden med det medicinske etablissement er vokset. En del af denne utilfredshed stammer fra skyhøje sundhedsudgifter, og hvad mange opfatter som ufølsom nærighed af sygeforsikringsindustrien, som kampen om sundhedsreformen i 2009 illustrerede. Noget af utilfredsheden afspejler også en voksende opfattelse af, at den menneskelige eksistens sociale og endda åndelige områder spiller en nøglerolle for sundhed og sygdom. Denne opfattelse har givet anledning til fornyet interesse for alternativ medicin. Vi vender senere tilbage til disse mange spørgsmål for den sociale institution for medicin.
2022-01-28 01:42:41,507-           root:382:        turn_handler():INFO - in_request=diæt ->
 Kost er summen af ​​mad indtaget af en person eller en anden organisme. Ordet diæt indebærer ofte brugen af ​​et specifikt indtag af ernæring af sundhedsmæssige eller vægttabsmæssige årsager (hvor de to ofte hænger sammen). Selvom mennesker er altædende, har hver kultur og hver person nogle madpræferencer eller nogle madtabuer. Dette kan skyldes personlig smag eller etiske årsager. Individuelle kostvalg kan være mere eller mindre sunde. Kosten omfatter en række plante- og dyrebaserede fødevarer, der giver kroppen næringsstoffer. Sådanne næringsstoffer giver kroppen energi og holder den kørende. Næringsstoffer hjælper med at opbygge og styrke knogler, muskler og sener og regulerer også kropsprocesser (dvs. blodtryk). Vand er afgørende for vækst, reproduktion og et godt helbred. Makronæringsstoffer indtages i relativt store mængder og omfatter proteiner, kulhydrater og fedt og fedtsyrer. Mikronæringsstoffer – vitaminer og mineraler – indtages i relativt mindre mængder, men er afgørende for kroppens processer.
2022-01-28 01:42:41,571-           root:382:        turn_handler():INFO - in_request=Takker ->
 Velkommen Sir/Mam
2022-01-28 01:42:41,655-           root:382:        turn_handler():INFO - in_request=bye ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'
```

## Resources
TODO:
- I was make new Non-Mainstream Languages Health and Medicine Chatbot Assitant and also contain Mainstream Languages Health and Medicine Chatbot Assitant inbuilt.


WIP:
- At this point my main goal is generating non-mainstream health and medicine chatbot environment, response and condition functions in order to add different languages functionality for the train and test health and medicine dialogs. That assistant first needs to understand different languages between test output and interactive output.
- Creating this scenarios to implement them in the Chatbot Project.
- Provide more languages about Health and Medicine Chatbot Assitant Service.
- Creating this scenarios to implement them in the code


Done:
- Modify the Health and Medicine Chatbot Assitant according to different mainstream and non mainstream languages.
- Create different transformer of Health and Medicine Chatbot Assitant according to different mainstream and non mainstream languages.
-  Generate new Health and Medicine Chatbot Assitant Support Service according to different mainstream and non mainstream languages.
- Modify the response, Create Data folder and add Data files in Data folder in Chatbot Project Github according to different mainstream and non mainstream languages.
- Make friendly Health and Medicine Chatbot Assitant for different countries and languages of people for their help.
- Create data and languages folder of different countries
- Create also mainstream languages in english folder


Issues:
- I was try lot of new things.

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
