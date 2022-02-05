import re
import logging
from typing import Optional, Union
from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
import df_engine.conditions as cnd
from scenario.condition import healmed_request
from language.dutch import dutch_transform
from language.spanish import spanish_transform
from language.greek import greek_transform
from language.russian import russian_transform
from language.danish import danish_transform
from language.arabic import arabic_transform



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
            TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|oye|Oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام", re.IGNORECASE)},
        },
        "fallback_node": {  # We get to this node if an error occurred while the agent was running
            RESPONSE: "Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'",
            TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|Oye|oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام|أهل", re.IGNORECASE)},
        },
    },
    "english": {
        "node1": {
            RESPONSE: "Hi!, I'm Health and medicine Chatbot Assistant, how may help you?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental_health|Mental_health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: healmed_request,
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental_health|Mental_health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: healmed_request,
            TRANSITIONS: {"node2": cnd.regexp(r"\bappointment|Appointment\b|\bdoctor|Doctor|Physicians|Cardiologists|Gastroenterologists|Dentist|ENT specialist|Gynaecologist", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bhealth|Health\b|\bmedicine|Medicine", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental_health|Mental_health", re.IGNORECASE),
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
                         "node4": cnd.regexp(r"\bdiet|Diet\b|\bmental_health|Mental_health", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bThanks|thanks|Thanking|thanking|Good|good|OK|ok|Ok", re.IGNORECASE),
                         "node6": cnd.regexp(r"\bNo|no|NO|Nothing|nothing", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "bye", TRANSITIONS: {"node1": cnd.exact_match("Hi")}},
        
  },
    "dutch": {
        "node1": {
            RESPONSE: "Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\bafspraak|Afspraak\b|\barts|Arts|Artsen|Cardiologen|Gastro-enterologen|Tandarts|KNO-arts|Gynaecoloog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bgezondheid|Gezondheid\b|\bgeneeskunde|Geneeskunde", re.IGNORECASE),
                         "node4": cnd.regexp(r"\beetpatroon|Eetpatroon\b|\bmentale_gezondheid|Mentale_gezondheid", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bBedankt|bedankt|Bedankt|bedankt|\bGoed|\bgoed|OK|ok|Ok|Met dank", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: dutch_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bafspraak|Afspraak\b|\barts|Arts|Artsen|Cardiologen|Gastro-enterologen|Tandarts|KNO-arts|Gynaecoloog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bgezondheid|Gezondheid\b|\bgeneeskunde|Geneeskunde", re.IGNORECASE),
                         "node4": cnd.regexp(r"\beetpatroon|Eetpatroon\b|\bmentale_gezondheid|Mentale_gezondheid", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bBedankt|bedankt|Bedankt|bedankt|Goed|goed|OK|ok|Ok|Met danks", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: dutch_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bafspraak|Afspraak\b|\barts|Arts|Artsen|Cardiologen|Gastro-enterologen|Tandarts|KNO-arts|Gynaecoloog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bgezondheid|Gezondheid\b|\bgeneeskunde|Geneeskunde", re.IGNORECASE),
                         "node4": cnd.regexp(r"\beetpatroon|Eetpatroon\b|\bmentale_gezondheid|Mentale_gezondheid", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bBedankt|bedankt|Bedankt|bedankt|Goed|goed|OK|ok|Ok|Met danks", re.IGNORECASE)},
        },
        "node4": {
            RESPONSE: dutch_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bafspraak|Afspraak\b|\barts|Arts|Artsen|Cardiologen|Gastro-enterologen|Tandarts|KNO-arts|Gynaecoloog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bgezondheid|Gezondheid\b|\bgeneeskunde|Geneeskunde", re.IGNORECASE),
                         "node4": cnd.regexp(r"\beetpatroon|Eetpatroon\b|\bmentale_gezondheid|Mentale_gezondheid", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bBedankt|bedankt|Bedankt|bedankt|Goed|goed|OK|ok|Ok|Met danks", re.IGNORECASE)},
        },
        "node5": {
            RESPONSE: "Welkom meneer/mama",
            TRANSITIONS: {"node2": cnd.regexp(r"\bafspraak|Afspraak\b|\barts|Arts|Artsen|Cardiologen|Gastro-enterologen|Tandarts|KNO-arts|Gynaecoloog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bgezondheid|Gezondheid\b|\bgeneeskunde|Geneeskunde", re.IGNORECASE),
                         "node4": cnd.regexp(r"\beetpatroon|Eetpatroon\b|\bmentale_gezondheid|Mentale_gezondheid", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bBedankt|bedankt|Bedankt|bedankt|Goed|goed|OK|ok|Ok|Met danks", re.IGNORECASE),
                         "node6": cnd.regexp(r"\bNee|nee|NEE|Niets|niets", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen", 
                  TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|Oye|oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام|أهل", re.IGNORECASE)}
                 },
        
  },
    "spanish": {
        "node1": {
            RESPONSE: "Hola!, soy asistente de un chatbot de salud y medicina, cómo puedo ayudarte?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\bcita|Cita\b|\bmédica|médico|Médica|Médico|Médicos|Médicas|Cardiólogos|Gastroenterólogos|Dentista|Otorrinolaringólogo|Ginecólogo", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsanidad|Sanidad|medicamento|Medicamento", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdieta|Dieta\b|\bsalud_mental|Salud_mental", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bGracias|gracias|Agradecimiento|agradecimiento|Bien|bien|OK|ok|Ok", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: spanish_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bcita|Cita\b|\bmédica|médico|Médica|Médico|Médicos|Médicas|Cardiólogos|Gastroenterólogos|Dentista|Otorrinolaringólogo|Ginecólogo", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsanidad|Sanidad|medicamento|Medicamento", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdieta|Dieta\b|\bsalud_mental|Salud_mental", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bGracias|gracias|Agradecimiento|agradecimiento|Bien|bien|OK|ok|Ok", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: spanish_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bcita|Cita\b|\bmédica|médico|Médica|Médico|Médicos|Médicas|Cardiólogos|Gastroenterólogos|Dentista|Otorrinolaringólogo|Ginecólogo", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsanidad|Sanidad|medicamento|Medicamento", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdieta|Dieta\b|\bsalud_mental|Salud_mental", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bGracias|gracias|Agradecimiento|agradecimiento|Bien|bien|OK|ok|Ok", re.IGNORECASE)},
        },
        "node4": {
            RESPONSE: spanish_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bcita|Cita\b|\bmédica|médico|Médica|Médico|Médicos|Médicas|Cardiólogos|Gastroenterólogos|Dentista|Otorrinolaringólogo|Ginecólogo", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsanidad|Sanidad|medicamento|Medicamento", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdieta|Dieta\b|\bsalud_mental|Salud_mental", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bGracias|gracias|Agradecimiento|agradecimiento|Bien|bien|OK|ok|Ok", re.IGNORECASE)},
        },
        "node5": {
            RESPONSE: "Bienvenido señor/mamá",
            TRANSITIONS: {"node2": cnd.regexp(r"\bcita|Cita\b|\bmédica|médico|Médica|Médico|Médicos|Médicas|Cardiólogos|Gastroenterólogos|Dentista|Otorrinolaringólogo|Ginecólogo", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsanidad|Sanidad|medicamento|Medicamento", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdieta|Dieta\b|\bsalud_mental|Salud_mental", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bGracias|gracias|Agradecimiento|agradecimiento|Bien|bien|OK|ok|Ok", re.IGNORECASE),
                         "node6": cnd.regexp(r"\bNo|no|NO|Nada|nada", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "Claro señor, gracias por su visita, pero puede ir a otros servicios si es necesario, puede escribir 'hola'", 
                  TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|Oye|oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام|أهل", re.IGNORECASE)}
          }
      },
    "greek": {
        "node1": {
            RESPONSE: "Γεια!, είμαι Βοηθός Chatbot για την υγεία και την ιατρική, πώς μπορεί να σας βοηθήσει?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\bραντεβού|Ραντεβού\b|\bγιατρός|Γιατρός|Γιατροί|Καρδιολόγοι|Γαστρεντερολόγοι|Οδοντίατρος|Ειδικός ΩΡΛ|Γυναικολόγος", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bυγεία|Υγεία|φάρμακο|Ιατρική", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bδίαιτα|Δίαιτα\b|\bψυχική_υγειονομικός|ψυχική_υγειονομικός|διατροφή", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bΕυχαριστώ|Ευχαριστώ|Ευχαριστώ|Ευχαριστώ|Καλά|καλά|Εντάξει|εντάξει|Εντάξει", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: greek_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bραντεβού|Ραντεβού\b|\bγιατρός|Γιατρός|Γιατροί|Καρδιολόγοι|Γαστρεντερολόγοι|Οδοντίατρος|Ειδικός ΩΡΛ|Γυναικολόγος", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bυγεία|Υγεία|φάρμακο|Ιατρική", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bδίαιτα|Δίαιτα\b|\bψυχική_υγειονομικός|ψυχική_υγειονομικός|διατροφή", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bΕυχαριστώ|Ευχαριστώ|Ευχαριστώ|Ευχαριστώ|Καλά|καλά|Εντάξει|εντάξει|Εντάξει", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: greek_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bραντεβού|Ραντεβού\b|\bγιατρός|Γιατρός|Γιατροί|Καρδιολόγοι|Γαστρεντερολόγοι|Οδοντίατρος|Ειδικός ΩΡΛ|Γυναικολόγος", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bυγεία|Υγεία|φάρμακο|Ιατρική", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bδίαιτα|Δίαιτα\b|\bψυχική_υγειονομικός|ψυχική_υγειονομικός|διατροφή", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bΕυχαριστώ|Ευχαριστώ|Ευχαριστώ|Ευχαριστώ|Καλά|καλά|Εντάξει|εντάξει|Εντάξει", re.IGNORECASE)},
        },
        "node4": {
            RESPONSE: greek_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bραντεβού|Ραντεβού\b|\bγιατρός|Γιατρός|Γιατροί|Καρδιολόγοι|Γαστρεντερολόγοι|Οδοντίατρος|Ειδικός ΩΡΛ|Γυναικολόγος", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bυγεία|Υγεία|φάρμακο|Ιατρική", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bδίαιτα|Δίαιτα\b|\bψυχική_υγειονομικός|ψυχική_υγειονομικός|διατροφή", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bΕυχαριστώ|Ευχαριστώ|Ευχαριστώ|Ευχαριστώ|Καλά|καλά|Εντάξει|εντάξει|Εντάξει", re.IGNORECASE)},
        },
        "node5": {
            RESPONSE: "Καλώς ήλθατε κύριε/μαμ",
            TRANSITIONS: {"node2": cnd.regexp(r"\bραντεβού|Ραντεβού\b|\bγιατρός|Γιατρός|Γιατροί|Καρδιολόγοι|Γαστρεντερολόγοι|Οδοντίατρος|Ειδικός ΩΡΛ|Γυναικολόγος", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bυγεία|Υγεία|φάρμακο|Ιατρική", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bδίαιτα|Δίαιτα\b|\bψυχική_υγειονομικός|ψυχική_υγειονομικός|διατροφή", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bΕυχαριστώ|Ευχαριστώ|Ευχαριστώ|Ευχαριστώ|Καλά|καλά|Εντάξει|εντάξει|Εντάξει", re.IGNORECASE),
                         "node6": cnd.regexp(r"\bΌχι|όχι|ΟΧΙ|Τίποτα|τίποτα", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "Βεβαίως κύριε, ευχαριστώ για την επίσκεψή σας, αλλά μπορείτε να πάτε σε άλλες υπηρεσίες αν χρειαστεί μπορείτε να πληκτρολογήσετε 'γεια'", 
                  TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|Oye|oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام|أهل", re.IGNORECASE)}
          }
      },
    "russian": {
        "node1": {
            RESPONSE: "Привет! Я Здоровье и медицина Помощник по чат-боту, как может вам помочь?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\bназначение|Назначение\b|\bврач|Доктор|Врачи|Кардиологи|Гастроэнтерологи|Дантист|ЛОР-специалист|Гинеколог", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bздоровье|Здоровье\b|\bлекарство", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bдиета|Диета\b|\bпсихическое_здоровье|Психическое_здоровье", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bСпасибо|спасибо|Благодарю|благодарю|Хорошо|хорошо|ОК|ок|Ok", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: russian_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bназначение|Назначение\b|\bврач|Доктор|Врачи|Кардиологи|Гастроэнтерологи|Дантист|ЛОР-специалист|Гинеколог", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bздоровье|Здоровье\b|\bлекарство", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bдиета|Диета\b|\bпсихическое_здоровье|Психическое_здоровье", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bСпасибо|спасибо|Благодарю|благодарю|Хорошо|хорошо|ОК|ок|Ok", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: russian_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bназначение|Назначение\b|\bврач|Доктор|Врачи|Кардиологи|Гастроэнтерологи|Дантист|ЛОР-специалист|Гинеколог", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bздоровье|Здоровье\b|\bлекарство", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bдиета|Диета\b|\bпсихическое_здоровье|Психическое_здоровье", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bСпасибо|спасибо|Благодарю|благодарю|Хорошо|хорошо|ОК|ок|Ok", re.IGNORECASE)},
        },
        "node4": {
            RESPONSE: russian_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bназначение|Назначение\b|\bврач|Доктор|Врачи|Кардиологи|Гастроэнтерологи|Дантист|ЛОР-специалист|Гинеколог", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bздоровье|Здоровье\b|\bлекарство", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bдиета|Диета\b|\bпсихическое_здоровье|Психическое_здоровье", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bСпасибо|спасибо|Благодарю|благодарю|Хорошо|хорошо|ОК|ок|Ok", re.IGNORECASE)},
        },
        "node5": {
            RESPONSE: "Добро пожаловать, сэр/мама",
            TRANSITIONS: {"node2": cnd.regexp(r"\bназначение|Назначение\b|\bврач|Доктор|Врачи|Кардиологи|Гастроэнтерологи|Дантист|ЛОР-специалист|Гинеколог", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bздоровье|Здоровье\b|\bлекарство", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bдиета|Диета\b|\bпсихическое_здоровье|Психическое_здоровье", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bСпасибо|спасибо|Благодарю|благодарю|Хорошо|хорошо|ОК|ок|Ok", re.IGNORECASE),
                         "node6": cnd.regexp(r"\bНет|нет|НЕТ|Ничего|ничего", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "Конечно сэр, Я благодарю за ваш визит, но вы можете воспользоваться другими услугами, если это необходимо, вы можете ввести 'Привет'", 
                  TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|Oye|oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام|أهل", re.IGNORECASE)}
          },
        
    },
    "danish": {
        "node1": {
            RESPONSE: "Hej!, jeg er Sundhed og Medicin Chatbot assistent, hvordan kan hjælpe dig?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\budnævnelse|Udnævnelse\b|\blæge|Læge|Læger|Kardiologer|Gastroenterologer|Tandlæge|ØNH-specialist|Gynækolog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsundhed|Sundhed\b|\bmedicin|Medicin", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiæt|Diæt\b|\bmental_sundhed|Mental_sundhed", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bTak|tak|Takker|takker|God|god|OK|ok|Ok", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: danish_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\budnævnelse|Udnævnelse\b|\blæge|Læge|Læger|Kardiologer|Gastroenterologer|Tandlæge|ØNH-specialist|Gynækolog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsundhed|Sundhed\b|\bmedicin|Medicin", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiæt|Diæt\b|\bmental_sundhed|Mental_sundhed", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bTak|tak|Takker|takker|God|god|OK|ok|Ok", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: danish_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\budnævnelse|Udnævnelse\b|\blæge|Læge|Læger|Kardiologer|Gastroenterologer|Tandlæge|ØNH-specialist|Gynækolog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsundhed|Sundhed\b|\bmedicin|Medicin", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiæt|Diæt\b|\bmental_sundhed|Mental_sundhed", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bTak|tak|Takker|takker|God|god|OK|ok|Ok", re.IGNORECASE)},
        },
        "node4": {
            RESPONSE: danish_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\budnævnelse|Udnævnelse\b|\blæge|Læge|Læger|Kardiologer|Gastroenterologer|Tandlæge|ØNH-specialist|Gynækolog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsundhed|Sundhed\b|\bmedicin|Medicin", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiæt|Diæt\b|\bmental_sundhed|Mental_sundhed", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bTak|tak|Takker|takker|God|god|OK|ok|Ok", re.IGNORECASE)},
        },
        "node5": {
            RESPONSE: "Velkommen Sir/Mam",
            TRANSITIONS: {"node2": cnd.regexp(r"\budnævnelse|Udnævnelse\b|\blæge|Læge|Læger|Kardiologer|Gastroenterologer|Tandlæge|ØNH-specialist|Gynækolog", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bsundhed|Sundhed\b|\bmedicin|Medicin", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bdiæt|Diæt\b|\bmental_sundhed|Mental_sundhed", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bTak|tak|Takker|takker|God|god|OK|ok|Ok", re.IGNORECASE),
                         "node6": cnd.regexp(r"\bNej|nej|NEJ|Intet|ingenting|ikke noget|Ikke noget", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "Klart herre, jeg takker for dit besøg men din kan gå andre tjenester hvis det er nødvendigt kan du skrive 'hej'", 
                  TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|Oye|oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام|أهل", re.IGNORECASE)}
          },
        
  },
    "arabic": {
        "node1": {
            RESPONSE: "مرحبًا ، أنا مساعد الشات بوت الخاص بالصحة والطب ، كيف يمكن أن يساعدك!?",  
            TRANSITIONS: {"node2": cnd.regexp(r"\bالتعيين|ميعاد\b|\bطبيب|دكتور|أطباء|أطباء القلب|أطباء الجهاز الهضمي|دكتور أسنانأخصائي الأنف والحنجرة|طبيب نساء وولادة", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bصحة\b|\bالطب|طب|دواء", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bالصحة_العقلية\b|\حمية غذائية|حمية", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bشكرًا|شكرًا|شكر|شكر|جيد|جيد|حسنًا|موافق|حسنًا", re.IGNORECASE)},
        },
        "node2": {
            RESPONSE: arabic_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bالتعيين|ميعاد\b|\bطبيب|دكتور|أطباء|أطباء القلب|أطباء الجهاز الهضمي|دكتور أسنانأخصائي الأنف والحنجرة|طبيب نساء وولادة", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bصحة\b|\bالطب|طب|دواء", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bالصحة_العقلية\b|\حمية غذائية|حمية", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bشكرًا|شكرًا|شكر|شكر|جيد|جيد|حسنًا|موافق|حسنًا", re.IGNORECASE)},
            
        },
        "node3": {
            RESPONSE: arabic_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bالتعيين|ميعاد\b|\bطبيب|دكتور|أطباء|أطباء القلب|أطباء الجهاز الهضمي|دكتور أسنانأخصائي الأنف والحنجرة|طبيب نساء وولادة", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bصحة\b|\bالطب|طب|دواء", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bالصحة_العقلية\b|\حمية غذائية|حمية", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bشكرًا|شكرًا|شكر|شكر|جيد|جيد|حسنًا|موافق|حسنًا", re.IGNORECASE)},
        },
        "node4": {
            RESPONSE: arabic_transform,
            TRANSITIONS: {"node2": cnd.regexp(r"\bالتعيين|ميعاد\b|\bطبيب|دكتور|أطباء|أطباء القلب|أطباء الجهاز الهضمي|دكتور أسنانأخصائي الأنف والحنجرة|طبيب نساء وولادة", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bصحة\b|\bالطب|طب|دواء", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bالصحة_العقلية\b|\حمية غذائية|حمية", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bشكرًا|شكرًا|شكر|شكر|جيد|جيد|حسنًا|موافق|حسنًا", re.IGNORECASE)},
        },
        "node5": {
            RESPONSE: "مرحبا يا سيدي / مام",
            TRANSITIONS: {"node2": cnd.regexp(r"\bالتعيين|ميعاد\b|\bطبيب|دكتور|أطباء|أطباء القلب|أطباء الجهاز الهضمي|دكتو أسنانأخصائي الأنف والحنجرة|طبيب نساء وولادة", re.IGNORECASE),
                         "node3": cnd.regexp(r"\bصحة\b|\bالطب|طب|دواء", re.IGNORECASE),
                         "node4": cnd.regexp(r"\bالصحة_العقلية\b|\حمية غذائية|حمية", re.IGNORECASE),
                         "node5": cnd.regexp(r"\bشكرًا|شكرًا|شكر|شكر|جيد|جيد|حسنًا|موافق|حسنًا", re.IGNORECASE),
                         "node6": cnd.regexp(r"\b|لا|لا شيء|لا شيء", re.IGNORECASE)},
        },
        "node6": {RESPONSE: "'بالتأكيد سيدي ، شكرا لزيارتك ولكن يمكنك الذهاب إلى خدمات أخرى إذا لزم الأمر يمكنك كتابة 'أهلين", 
                  TRANSITIONS: {("english", "node1"): cnd.regexp(r"\bHi\b|hi|hello|Hello|hey|Hey", re.IGNORECASE),
                          ("dutch", "node1"): cnd.regexp(r"\bHallo\b|hoi|hallo", re.IGNORECASE),
                          ("spanish", "node1"): cnd.regexp(r"\bHola\b|hola|Oye|oye", re.IGNORECASE),
                          ("greek", "node1"): cnd.regexp(r"\bγεια\b|γεια|γεια σας|Γεια σου|Χαίρετε|γεια|Γεια", re.IGNORECASE),
                          ("russian", "node1"): cnd.regexp(r"\bПривет\b|Здравствуйте|Привет|Эй", re.IGNORECASE),
                          ("danish", "node1"): cnd.regexp(r"\bHej\b|hej|hallo|Hallo|hey|Hey", re.IGNORECASE),
                          ("arabic", "node1"): cnd.regexp(r"\bأهلا\b|مهلا|أهلين|سلام|أهل", re.IGNORECASE)}
          },
        
  }
    
}
                                                                                       

# An actor is an object that processes user input replicas and returns responses
# To create the actor, you need to pass the script of the dialogue `plot`
# And pass the initial node `start_label`
# and the node to which the actor will go in case of an error `fallback_label`
# If `fallback_label` is not set, then its value becomes equal to `start_label` by default
actor = Actor(plot, start_label=("greeting_flow", "start_node"), fallback_label=("greeting_flow", "fallback_node"))

