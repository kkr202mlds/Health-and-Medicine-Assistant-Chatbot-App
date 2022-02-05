import re
import logging
from typing import Optional, Union
from scenario.main import actor
from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
import df_engine.conditions as cnd
from  scenario.condition import healmed_request


logger = logging.getLogger(__name__)



# turn_handler - a function is made for the convenience of working with an actor
def turn_handler(
    in_request: str, ctx: Union[Context, str, dict], actor: Actor, true_out_response: Optional[str] = None
):
    # Context.cast - gets an object type of [Context, str, dict] returns an object type of Context
    ctx = Context.cast(ctx)
    # Add in current context a next request of user
    ctx.add_request(in_request)
    # pass the context into actor and it returns updated context with actor response
    ctx = actor(ctx)
    # get last actor response from the context
    out_response = ctx.last_response
    # the next condition branching needs for testing
    if true_out_response is not None and true_out_response != out_response:
        msg = f"in_request={in_request} -> true_out_response != out_response: {true_out_response} != {out_response}"
        raise Exception(msg)
    else:
        logging.info(f"in_request={in_request} ->\n {out_response}")
    return out_response, ctx

testing_dialog = [
    
    # English
    ("Hi", "Hi!, I'm Health and medicine Chatbot Assistant, how may help you?"),  # start_node -> node1
    ("I want to book a appointment?","OK! I have book a appointment of Doctor for health checkup for you Sir"),
    ("Physicians", "OK! I have book a appointment of physicians Doctor for you Sir"),  
    ("Thanks", "Welcome Sir/Mam"),  
    ("bye", "Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'"),
    ("Hi", "Hi!, I'm Health and medicine Chatbot Assistant, how may help you?"),
    ("What is health?", "Health refers to the extent of a person’s physical, mental, and social well-being. This definition, taken from the World Health Organization’s treatment of health, emphasizes that health is a complex concept that involves not just the soundness of a person’s body but also the state of a person’s mind and the quality of the social environment in which she or he lives. The quality of the social environment in turn can affect a person’s physical and mental health, underscoring the importance of social factors for these twin aspects of our overall well-being."),  
    ("What is medicine?","Medicine is the social institution that seeks both to prevent, diagnose, and treat illness and to promote health as just defined. Dissatisfaction with the medical establishment has been growing.Part of this dissatisfaction stems from soaring health-care costs and what many perceive as insensitive stinginess by the health insurance industry, as the 2009 battle over health-care reform illustrated. Some of the dissatisfaction also reflects a growing view that the social and even spiritual realms of human existence play a key role in health and illness. This view has fueled renewed interestin alternative medicine. We return later to these many issues for the social institution of medicine."),        #
    ("what is mental_health?", "Mental health refers to cognitive, behavioral, and emotional well-being. It is all about how people think, feel, and behave. People sometimes use the term “mental health” to mean the absence of a mental disorder. Mental health can affect daily living, relationships, and physical health.Mental health as a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community."), 
    ("how  can are change my diet?", "Diet is the sum of food consumed by a person or other organism. The word diet often implies the use of specific intake of nutrition for health or weight-management reasons (with the two often being related). Although humans are omnivores, each culture and each person holds some food preferences or some food taboos. This may be due to personal tastes or ethical reasons. Individual dietary choices may be more or less healthy.Diet includes a variety of plant-based and animal-based foods that provide nutrients to the body. Such nutrients provide the body with energy and keep it running. Nutrients help build and strengthen bones, muscles, and tendons and also regulate body processes (i.e., blood pressure). Water is essential for growth, reproduction and good health. Macronutrients are consumed in relatively large quantities and include proteins, carbohydrates, and fats and fatty acids. Micronutrients – vitamins and minerals – are consumed in relatively smaller quantities, but are essential to body processes."),
    ("what a doctor", "There is a many doctor like following:\n- Physicians\n- Cardiologists\n- Gastroenterologists\n- Dentist\n- ENT specialist\n- Gynaecologist\nPlease write type of doctor according above way"),    
    ("Ok", "Welcome Sir/Mam"),
    ("bye","Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'"),
    # Dutch
    ("hallo", "Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?"),  # start_node -> node1
    ("Ik wil een afspraak boeken?","OKE! Ik heb een afspraak gemaakt met de dokter voor gezondheidscontrole voor u, mijnheer"),
    ("ik wil een arts", "Er zijn veel artsen zoals de volgende:\n- Artsen\n- Cardiologen\n- Gastro-enterologen\n- Tandarts\n- KNO-arts\n- Gynaecoloog\nSchrijf het type arts op volgens bovenstaande manier"),    
    ("Ik wil echt een artsen", "OKE! Ik heb een afspraak gemaakt met artsen Dokter voor u meneer"),
    ("Met spoed een gastro-enterologen nodig", "OKE! Ik heb een afspraak gemaakt met gastro-enterologen Dokter voor u meneer"),
    ("Ik heb een probleem in mijn oor, kan een KNO-arts boeken", "OKE! Ik heb een afspraak gemaakt met kno-arts Dokter voor u meneer"),
    ("Ik wil een tandarts voor mijn tanden", "OKE! Ik heb een afspraak gemaakt met tandarts Dokter voor u meneer"),
    ("Ik heb een hartprobleem, boek een cardiologen", "OKE! Ik heb een afspraak gemaakt met cardiologen Dokter voor u meneer"),
    ("bedankt", "Welkom meneer/mama"),  
    ("nee", "Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen"),
    ("Hoi", "Hallo!, ik ben Chatbot-assistent voor gezondheid en geneeskunde, hoe kan u helpen?"),
    ("Wat is gezondheid?", "Gezondheid verwijst naar de mate van iemands fysieke, mentale en sociale welzijn. Deze definitie, ontleend aan de behandeling van gezondheid door de Wereldgezondheidsorganisatie, benadrukt dat gezondheid een complex concept is dat niet alleen betrekking heeft op de gezondheid van iemands lichaam, maar ook op de gemoedstoestand van een persoon en de kwaliteit van de sociale omgeving waarin hij of zij zich bevindt. leeft. De kwaliteit van de sociale omgeving kan op zijn beurt de fysieke en mentale gezondheid van een persoon beïnvloeden, wat het belang van sociale factoren voor deze tweeledige aspecten van ons algehele welzijn onderstreept."),  
    ("Definieer een geneeskunde","Geneeskunde is de sociale instelling die zowel ziekte wil voorkomen, diagnosticeren en behandelen als de gezondheid zoals zojuist gedefinieerd bevordert. De ontevredenheid over het medische establishment is toegenomen. Een deel van deze ontevredenheid komt voort uit stijgende kosten voor de gezondheidszorg en wat velen beschouwen als ongevoelige gierigheid door de zorgverzekeringsindustrie, zoals de strijd om de hervorming van de gezondheidszorg in 2009 illustreerde. Een deel van de ontevredenheid weerspiegelt ook een groeiende opvatting dat de sociale en zelfs spirituele gebieden van het menselijk bestaan een sleutelrol spelen bij gezondheid en ziekte. Deze visie heeft geleid tot een hernieuwde belangstelling voor alternatieve geneeswijzen. We komen later terug op deze vele kwesties voor de sociale instelling van de geneeskunde."),        #
    ("wat is mentale_gezondheid?", "Geestelijke gezondheid verwijst naar cognitief, gedrags- en emotioneel welzijn. Het gaat erom hoe mensen denken, voelen en zich gedragen. Mensen gebruiken de term 'geestelijke gezondheid' soms om de afwezigheid van een psychische stoornis aan te duiden. Geestelijke gezondheid kan het dagelijks leven, relaties en lichamelijke gezondheid beïnvloeden. Geestelijke gezondheid als een toestand van welzijn waarin het individu zijn of haar eigen capaciteiten realiseert, de normale stress van het leven aankan, productief en vruchtbaar kan werken en een bijdrage kan leveren aan zijn of haar gemeenschap."), 
    ("hoe kan ik mijn eetpatroon veranderen?", "Dieet is de som van voedsel dat door een persoon of een ander organisme wordt geconsumeerd. Het woord dieet impliceert vaak het gebruik van een specifieke inname van voeding om redenen van gezondheid of gewichtsbeheersing (waarbij beide vaak gerelateerd zijn). Hoewel mensen alleseters zijn, heeft elke cultuur en elke persoon bepaalde voedselvoorkeuren of voedseltaboes. Dit kan te wijten zijn aan persoonlijke smaak of ethische redenen. Individuele voedingskeuzes kunnen min of meer gezond zijn. Dieet omvat een verscheidenheid aan plantaardige en dierlijke voedingsmiddelen die het lichaam van voedingsstoffen voorzien. Dergelijke voedingsstoffen voorzien het lichaam van energie en houden het draaiende. Voedingsstoffen helpen bij het opbouwen en versterken van botten, spieren en pezen en reguleren ook lichaamsprocessen (d.w.z. bloeddruk). Water is essentieel voor groei, voortplanting en een goede gezondheid. Macronutriënten worden in relatief grote hoeveelheden geconsumeerd en omvatten eiwitten, koolhydraten en vetten en vetzuren. Micronutriënten – vitamines en mineralen – worden in relatief kleinere hoeveelheden geconsumeerd, maar zijn essentieel voor lichaamsprocessen."),
    ("ik wil een arts", "Er zijn veel artsen zoals de volgende:\n- Artsen\n- Cardiologen\n- Gastro-enterologen\n- Tandarts\n- KNO-arts\n- Gynaecoloog\nSchrijf het type arts op volgens bovenstaande manier"),    
    ("Bedankt", "Welkom meneer/mama"),
    ("Goed service", "Welkom meneer/mama"),
    ("Niets","Natuurlijk meneer, ik dank u voor uw bezoek, maar u kunt indien nodig naar andere diensten gaan, u kunt 'hallo' typen"),
    
    # Greek
    ("γεια", "Γεια!, είμαι Βοηθός Chatbot για την υγεία και την ιατρική, πώς μπορεί να σας βοηθήσει?"),
    ("Θέλω να κλείσω ένα ραντεβού?","ΟΚ! Έχω κλείσει ραντεβού γιατρού για έλεγχο υγείας για εσάς κύριε"),
    ("θελω α γιατρός", "Υπάρχουν πολλοί γιατροί όπως οι ακόλουθοι:\n- Γιατροί\n- Καρδιολόγοι\n- Γαστρεντερολόγοι\n- Οδοντίατρος\n- Ειδικός ΩΡΛ\n- Γυναικολόγος\nΠαρακαλώ γράψτε τον τύπο του γιατρού σύμφωνα με τον παραπάνω τρόπο"),    
    ("Θέλω πραγματικά ένα Γιατροί", "ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό γιατροί για εσάς, κύριε"),
    ("Έχω πρόβλημα στο αυτί μου, μπορώ να κάνω κράτηση α Ειδικός ΩΡΛ", "ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό ειδικός ωρλ για εσάς, κύριε"),
    ("Παροτρύνω ου Γαστρεντερολόγοι", "ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό γαστρεντερολόγοι για εσάς, κύριε"),
    ("Έχω πρόβλημα με την καρδιά, βιβλίο α Καρδιολόγοι", "ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό καρδιολόγοι για εσάς, κύριε"),
    ("Θέλω ένα για Οδοντίατρος τα δόντια μου", "ΕΝΤΑΞΕΙ! Έχω κλείσει ένα ραντεβού με τον γιατρό οδοντίατρος για εσάς, κύριε"),
    ("Ευχαριστώ", "Καλώς ήλθατε κύριε/μαμ"), 
    ("όχι", "Βεβαίως κύριε, ευχαριστώ για την επίσκεψή σας, αλλά μπορείτε να πάτε σε άλλες υπηρεσίες αν χρειαστεί μπορείτε να πληκτρολογήσετε 'γεια'"),
    ("γεια", "Γεια!, είμαι Βοηθός Chatbot για την υγεία και την ιατρική, πώς μπορεί να σας βοηθήσει?"),
    ("τι ειναι υγεία?", "Η υγεία αναφέρεται στην έκταση της σωματικής, ψυχικής και κοινωνικής ευημερίας ενός ατόμου. Αυτός ο ορισμός, που λαμβάνεται από τη θεραπεία της υγείας του Παγκόσμιου Οργανισμού Υγείας, τονίζει ότι η υγεία είναι μια σύνθετη έννοια που περιλαμβάνει όχι μόνο την ευρωστία του σώματος ενός ατόμου αλλά και την κατάσταση του μυαλού ενός ατόμου και την ποιότητα του κοινωνικού περιβάλλοντος στο οποίο ζει. Η ποιότητα του κοινωνικού περιβάλλοντος με τη σειρά της μπορεί να επηρεάσει τη σωματική και ψυχική υγεία ενός ατόμου, υπογραμμίζοντας τη σημασία των κοινωνικών παραγόντων για αυτές τις δίδυμες πτυχές της συνολικής μας ευημερίας."),  
    ("Ορίστε ένα φάρμακο","Η ιατρική είναι ο κοινωνικός θεσμός που επιδιώκει τόσο την πρόληψη, τη διάγνωση και τη θεραπεία ασθενειών και την προαγωγή της υγείας όπως ακριβώς ορίστηκε. Η δυσαρέσκεια με το ιατρικό κατεστημένο έχει αυξηθεί. Μέρος αυτής της δυσαρέσκειας προέρχεται από το αυξανόμενο κόστος της υγειονομικής περίθαλψης και από αυτό που πολλοί αντιλαμβάνονται ως μη ευαίσθητη τσιγκουνιά από τον κλάδο της ασφάλισης υγείας, όπως φαίνεται από τη μάχη του 2009 για τη μεταρρύθμιση της υγειονομικής περίθαλψης. Κάποια από τη δυσαρέσκεια αντικατοπτρίζει επίσης μια αυξανόμενη άποψη ότι οι κοινωνικές και ακόμη και πνευματικές σφαίρες της ανθρώπινης ύπαρξης διαδραματίζουν βασικό ρόλο στην υγεία και την ασθένεια. Αυτή η άποψη έχει τροφοδοτήσει ανανεωμένο ενδιαφέρον για την εναλλακτική ιατρική. Επανερχόμαστε αργότερα σε αυτά τα πολλά θέματα για τον κοινωνικό θεσμό της ιατρικής."),        #
    ("τι είναι ψυχική_υγειονομικός", "Η ψυχική υγεία αναφέρεται στη γνωσιακή, συμπεριφορική και συναισθηματική ευημερία. Έχει να κάνει με το πώς σκέφτονται, αισθάνονται και συμπεριφέρονται οι άνθρωποι. Οι άνθρωποι χρησιμοποιούν μερικές φορές τον όρο «ψυχική υγεία» για να σημαίνει την απουσία ψυχικής διαταραχής. Η ψυχική υγεία μπορεί να επηρεάσει την καθημερινή ζωή, τις σχέσεις και τη σωματική υγεία. Η ψυχική υγεία είναι μια κατάσταση ευεξίας στην οποία το άτομο συνειδητοποιεί τις δικές του ικανότητες, μπορεί να αντιμετωπίσει το φυσιολογικό άγχος της ζωής, μπορεί να εργαστεί παραγωγικά και γόνιμα και μπορεί να συνεισφέρει στην κοινότητά του/της."), 
    ("δίαιτα", "Η δίαιτα είναι το άθροισμα της τροφής που καταναλώνει ένα άτομο ή άλλος οργανισμός. Η λέξη δίαιτα συχνά υποδηλώνει τη χρήση συγκεκριμένης πρόσληψης διατροφής για λόγους υγείας ή διαχείρισης βάρους (με τα δύο συχνά να σχετίζονται). Αν και οι άνθρωποι είναι παμφάγοι, κάθε πολιτισμός και κάθε άτομο έχει κάποιες διατροφικές προτιμήσεις ή κάποια ταμπού για τα τρόφιμα. Αυτό μπορεί να οφείλεται σε προσωπικά γούστα ή ηθικούς λόγους. Οι μεμονωμένες διατροφικές επιλογές μπορεί να είναι λίγο πολύ υγιεινές. Η διατροφή περιλαμβάνει μια ποικιλία φυτικών και ζωικών τροφών που παρέχουν θρεπτικά συστατικά στον οργανισμό. Τέτοια θρεπτικά συστατικά παρέχουν στο σώμα ενέργεια και τον κρατούν σε λειτουργία. Τα θρεπτικά συστατικά βοηθούν στην οικοδόμηση και ενίσχυση των οστών, των μυών και των τενόντων και επίσης ρυθμίζουν τις διεργασίες του σώματος (δηλαδή την αρτηριακή πίεση). Το νερό είναι απαραίτητο για την ανάπτυξη, την αναπαραγωγή και την καλή υγεία. Τα μακροθρεπτικά συστατικά καταναλώνονται σε σχετικά μεγάλες ποσότητες και περιλαμβάνουν πρωτεΐνες, υδατάνθρακες και λίπη και λιπαρά οξέα. Τα μικροθρεπτικά συστατικά - βιταμίνες και μέταλλα - καταναλώνονται σε σχετικά μικρότερες ποσότητες, αλλά είναι απαραίτητα για τις διαδικασίες του σώματος."),
    ("θελω α γιατρός", "Υπάρχουν πολλοί γιατροί όπως οι ακόλουθοι:\n- Γιατροί\n- Καρδιολόγοι\n- Γαστρεντερολόγοι\n- Οδοντίατρος\n- Ειδικός ΩΡΛ\n- Γυναικολόγος\nΠαρακαλώ γράψτε τον τύπο του γιατρού σύμφωνα με τον παραπάνω τρόπο"),    
    ("Ευχαριστώ", "Καλώς ήλθατε κύριε/μαμ"),
    ("τίποτα","Βεβαίως κύριε, ευχαριστώ για την επίσκεψή σας, αλλά μπορείτε να πάτε σε άλλες υπηρεσίες αν χρειαστεί μπορείτε να πληκτρολογήσετε 'γεια'"),
    ("bye", "Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'"),
    
    # Russian
    ("Здравствуйте", "Привет! Я Здоровье и медицина Помощник по чат-боту, как может вам помочь?"),
    ("назначение", "OKE! Ik heb een afspraak gemaakt met de dokter voor gezondheidscontrole voor u, mijnheer"),
    ("Кардиологи", "В ПОРЯДКЕ! Я записал вас на прием к  врачу, сэр."),
    ("Гастроэнтерологи", "В ПОРЯДКЕ! Я записал вас на прием к  врачу, сэр."),
    ("здоровье", "Gezondheid verwijst naar de mate van iemands fysieke, mentale en sociale welzijn. Deze definitie, ontleend aan de behandeling van gezondheid door de Wereldgezondheidsorganisatie, benadrukt dat gezondheid een complex concept is dat niet alleen betrekking heeft op de gezondheid van iemands lichaam, maar ook op de gemoedstoestand van een persoon en de kwaliteit van de sociale omgeving waarin hij of zij zich bevindt. leeft. De kwaliteit van de sociale omgeving kan op zijn beurt de fysieke en mentale gezondheid van een persoon beïnvloeden, wat het belang van sociale factoren voor deze tweeledige aspecten van ons algehele welzijn onderstreept."),
    ("лекарство", "Geneeskunde is de sociale instelling die zowel ziekte wil voorkomen, diagnosticeren en behandelen als de gezondheid zoals zojuist gedefinieerd bevordert. De ontevredenheid over het medische establishment is toegenomen. Een deel van deze ontevredenheid komt voort uit stijgende kosten voor de gezondheidszorg en wat velen beschouwen als ongevoelige gierigheid door de zorgverzekeringsindustrie, zoals de strijd om de hervorming van de gezondheidszorg in 2009 illustreerde. Een deel van de ontevredenheid weerspiegelt ook een groeiende opvatting dat de sociale en zelfs spirituele gebieden van het menselijk bestaan een sleutelrol spelen bij gezondheid en ziekte. Deze visie heeft geleid tot een hernieuwde belangstelling voor alternatieve geneeswijzen. We komen later terug op deze vele kwesties voor de sociale instelling van de geneeskunde."),
    ("диета", "Dieet is de som van voedsel dat door een persoon of een ander organisme wordt geconsumeerd. Het woord dieet impliceert vaak het gebruik van een specifieke inname van voeding om redenen van gezondheid of gewichtsbeheersing (waarbij beide vaak gerelateerd zijn). Hoewel mensen alleseters zijn, heeft elke cultuur en elke persoon bepaalde voedselvoorkeuren of voedseltaboes. Dit kan te wijten zijn aan persoonlijke smaak of ethische redenen. Individuele voedingskeuzes kunnen min of meer gezond zijn. Dieet omvat een verscheidenheid aan plantaardige en dierlijke voedingsmiddelen die het lichaam van voedingsstoffen voorzien. Dergelijke voedingsstoffen voorzien het lichaam van energie en houden het draaiende. Voedingsstoffen helpen bij het opbouwen en versterken van botten, spieren en pezen en reguleren ook lichaamsprocessen (d.w.z. bloeddruk). Water is essentieel voor groei, voortplanting en een goede gezondheid. Macronutriënten worden in relatief grote hoeveelheden geconsumeerd en omvatten eiwitten, koolhydraten en vetten en vetzuren. Micronutriënten – vitamines en mineralen – worden in relatief kleinere hoeveelheden geconsumeerd, maar zijn essentieel voor lichaamsprocessen."),
    ("психическое_здоровье", "Geestelijke gezondheid verwijst naar cognitief, gedrags- en emotioneel welzijn. Het gaat erom hoe mensen denken, voelen en zich gedragen. Mensen gebruiken de term 'geestelijke gezondheid' soms om de afwezigheid van een psychische stoornis aan te duiden. Geestelijke gezondheid kan het dagelijks leven, relaties en lichamelijke gezondheid beïnvloeden. Geestelijke gezondheid als een toestand van welzijn waarin het individu zijn of haar eigen capaciteiten realiseert, de normale stress van het leven aankan, productief en vruchtbaar kan werken en een bijdrage kan leveren aan zijn of haar gemeenschap."),  
    ("Спасибо", "Добро пожаловать, сэр/мама"),
    ("нет", "Конечно сэр, Я благодарю за ваш визит, но вы можете воспользоваться другими услугами, если это необходимо, вы можете ввести 'Привет'"),
    ("bye", "Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'"),
    
    # Danish
    ("Hej", "Hej!, jeg er Sundhed og Medicin Chatbot assistent, hvordan kan hjælpe dig?"),
    ("udnævnelse", "OK! Jeg har booket en tid hos lægen til sundhedstjek for dig Sir"),
    ("Kardiologer", "OK! Jeg har booket en tid til kardiologer læge til dig, hr"),
    ("Tandlæge", "OK! Jeg har booket en tid til tandlæge læge til dig, hr"),
    ("sundhed", "Sundhed refererer til omfanget af en persons fysiske, mentale og sociale velbefindende. Denne definition, taget fra Verdenssundhedsorganisationens behandling af sundhed, understreger, at sundhed er et komplekst begreb, der ikke kun involverer sundheden af en persons krop, men også en persons sindstilstand og kvaliteten af det sociale miljø, hvori hun eller han liv. Kvaliteten af det sociale miljø kan igen påvirke en persons fysiske og mentale sundhed, hvilket understreger betydningen af sociale faktorer for disse dobbelte aspekter af vores generelle velbefindende."),
    ("medicin", "Medicin er den sociale institution, der både søger at forebygge, diagnosticere og behandle sygdom og at fremme sundhed som netop defineret. Utilfredsheden med det medicinske etablissement er vokset. En del af denne utilfredshed stammer fra skyhøje sundhedsudgifter, og hvad mange opfatter som ufølsom nærighed af sygeforsikringsindustrien, som kampen om sundhedsreformen i 2009 illustrerede. Noget af utilfredsheden afspejler også en voksende opfattelse af, at den menneskelige eksistens sociale og endda åndelige områder spiller en nøglerolle for sundhed og sygdom. Denne opfattelse har givet anledning til fornyet interesse for alternativ medicin. Vi vender senere tilbage til disse mange spørgsmål for den sociale institution for medicin."),
    ("diæt", "Kost er summen af ​​mad indtaget af en person eller en anden organisme. Ordet diæt indebærer ofte brugen af ​​et specifikt indtag af ernæring af sundhedsmæssige eller vægttabsmæssige årsager (hvor de to ofte hænger sammen). Selvom mennesker er altædende, har hver kultur og hver person nogle madpræferencer eller nogle madtabuer. Dette kan skyldes personlig smag eller etiske årsager. Individuelle kostvalg kan være mere eller mindre sunde. Kosten omfatter en række plante- og dyrebaserede fødevarer, der giver kroppen næringsstoffer. Sådanne næringsstoffer giver kroppen energi og holder den kørende. Næringsstoffer hjælper med at opbygge og styrke knogler, muskler og sener og regulerer også kropsprocesser (dvs. blodtryk). Vand er afgørende for vækst, reproduktion og et godt helbred. Makronæringsstoffer indtages i relativt store mængder og omfatter proteiner, kulhydrater og fedt og fedtsyrer. Mikronæringsstoffer – vitaminer og mineraler – indtages i relativt mindre mængder, men er afgørende for kroppens processer."),
    ("Takker", "Velkommen Sir/Mam"),
    ("bye", "Sure Sir, I thanks for your visit but your can go other services if needed you can type for english 'hi', for dutch 'Hallo', for spanish 'Hola', for greek 'γεια, for russian 'Привет', for danish 'Hej' and for arabic 'أهلا'"),
    
    # Spanish
    ("Hola", "Hola!, soy asistente de un chatbot de salud y medicina, cómo puedo ayudarte?"),  # start_node -> node1
    ("quiero reservar una cita?","¡OK! He reservado una cita con el médico para un chequeo de salud para usted, señor."),
    ("Quiero un médico", "Hay muchos médicos como los siguientes:\n- Médicos\n- Cardiólogos\n- Gastroenterólogos\n- Dentista\n- Otorrinolaringólogo\n- Ginecólogo\nEscriba el tipo de médico de acuerdo con la forma anterior"),    
    ("I Realmente quiero una médicos", "OK! He reservado una cita con médicos médico para usted, señor."),
    ("Urge un Gastroenterólogos", "OK! He reservado una cita con gastroenterólogos médico para usted, señor."),
    ("Tengo un problema en mi oído, puedo reservar un otorrinolaringólogo", "OK! He reservado una cita con otorrinolaringólogo médico para usted, señor."),
    ("Quiero un dentista para mis dientes", "OK! He reservado una cita con dentista médico para usted, señor."),
    ("Tengo problema del corazón, reserve un Cardiólogos", "OK! He reservado una cita con cardiólogos médico para usted, señor."),
    ("Gracias", "Bienvenido señor/mamá"),  
    ("no", "Claro señor, gracias por su visita, pero puede ir a otros servicios si es necesario, puede escribir 'hola'"),
    ("Oye", "Hola!, soy asistente de un chatbot de salud y medicina, cómo puedo ayudarte?"),
    ("Que es la sanidad?", "La salud se refiere al grado de bienestar físico, mental y social de una persona. Esta definición, tomada del tratamiento de la salud de la Organización Mundial de la Salud, enfatiza que la salud es un concepto complejo que involucra no solo la solidez del cuerpo de una persona sino también el estado mental de una persona y la calidad del entorno social en el que ella o él. vidas. A su vez, la calidad del entorno social puede afectar la salud física y mental de una persona, lo que subraya la importancia de los factores sociales para estos dos aspectos de nuestro bienestar general."),  
    ("Definir un medicamento","La medicina es la institución social que busca tanto prevenir, diagnosticar y tratar la enfermedad como promover la salud tal como se acaba de definir. La insatisfacción con el establecimiento médico ha ido en aumento. Parte de esta insatisfacción se deriva del aumento de los costos de la atención médica y lo que muchos perciben como una tacañería insensible por parte de la industria de seguros de salud, como lo ilustró la batalla de 2009 por la reforma de la atención médica. Parte de la insatisfacción también refleja una visión creciente de que los ámbitos social e incluso espiritual de la existencia humana juegan un papel clave en la salud y la enfermedad. Este punto de vista ha alimentado un interés renovado en la medicina alternativa. Regresaremos más adelante a estos muchos temas para la institución social de la medicina."),        #
    ("que es salud_mental?", "La salud mental se refiere al bienestar cognitivo, conductual y emocional. Se trata de cómo las personas piensan, sienten y se comportan. Las personas a veces usan el término “salud mental” para referirse a la ausencia de un trastorno mental. La salud mental puede afectar la vida diaria, las relaciones y la salud física. La salud mental es un estado de bienestar en el que el individuo se da cuenta de sus propias capacidades, puede hacer frente a las tensiones normales de la vida, puede trabajar de manera productiva y fructífera, y es capaz de hacer una contribución a su comunidad."), 
    ("como puedo cambiar mi dieta?", "La dieta es la suma de los alimentos consumidos por una persona u otro organismo. La palabra dieta a menudo implica el uso de una ingesta específica de nutrición por razones de salud o de control de peso (con las dos a menudo relacionadas). Aunque los humanos somos omnívoros, cada cultura y cada persona tiene unas preferencias alimentarias o unos tabúes alimentarios. Esto puede deberse a gustos personales o razones éticas. Las opciones dietéticas individuales pueden ser más o menos saludables. La dieta incluye una variedad de alimentos de origen vegetal y animal que proporcionan nutrientes al cuerpo. Dichos nutrientes proporcionan energía al cuerpo y lo mantienen en funcionamiento. Los nutrientes ayudan a desarrollar y fortalecer huesos, músculos y tendones y también regulan los procesos corporales (es decir, la presión arterial). El agua es esencial para el crecimiento, la reproducción y la buena salud. Los macronutrientes se consumen en cantidades relativamente grandes e incluyen proteínas, carbohidratos y grasas y ácidos grasos. Los micronutrientes (vitaminas y minerales) se consumen en cantidades relativamente pequeñas, pero son esenciales para los procesos corporales."),
    ("Quiero un médica", "Hay muchos médicos como los siguientes:\n- Médicos\n- Cardiólogos\n- Gastroenterólogos\n- Dentista\n- Otorrinolaringólogo\n- Ginecólogo\nEscriba el tipo de médico de acuerdo con la forma anterior"),    
    ("agradecimiento", "Bienvenido señor/mamá"),
    ("Bien servicio", "Bienvenido señor/mamá"),
    ("nada","Claro señor, gracias por su visita, pero puede ir a otros servicios si es necesario, puede escribir 'hola'")
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
#     run_interactive_mode(actor)





