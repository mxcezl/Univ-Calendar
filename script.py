from icalendar import Calendar, Event
from datetime import datetime

class Cours:
    def __init__(self, desc, debut, fin, dur, salle):
        self.description = desc
        self.debut = debut
        self.fin = fin
        self.duree = dur
        self.salle = salle

    def afficher(self):
        print("DESCRIPTION : ", self.description)
        print("DEBUT : ", self.debut)
        print("FIN : ", self.fin)
        print("DUREE : ", self.duree)
        print(self.salle)

    @property
    def __get_debut(self):
        return self.debut

    @property
    def __get_description(self):
        return self.description
    
    
class Cours_Semaine:
    def __init__(self):
        self.liste_cours = []
        
    def ajouter_cours(self, cours):
        self.liste_cours.append(cours)
        
    def prochain_cours(self):
        d_now = datetime.now()
        for cours in self.liste_cours:
            if d_now < cours.debut: # Car dans l'ordre chronologique dans .ics
                
                delta = cours.debut - d_now
                hours = delta.seconds//3600
                minutes = (delta.seconds - hours*3600) // 60
                
                print("\nProchain cours dans ", str(hours), "h", str(minutes), '\n')
                return cours
        return -1 # Pas de prochain cours
            

    def afficher_cours(self):
        for cours in self.liste_cours:
            cours.afficher()

cal = open("D:\\Python_WS\\20200916173359.ics",'rb')
lc = Cours_Semaine()
gcal = Calendar.from_ical(cal.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        c = Cours(component.get("DESCRIPTION"), component.get("DTSTART").dt, component.get("DTEND").dt, component.get("DURATION").dt, component.get("LOCATION"))
        lc.ajouter_cours(c)
cal.close()


lc.prochain_cours().afficher()

