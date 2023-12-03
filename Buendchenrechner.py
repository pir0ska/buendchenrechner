#Damit macht man einen clear screen im Terminal
import os
os.system("clear")

while(1):
    print("BÜNDCHENRECHNER")
    print()
    
    #fertige Maße ohne NZ
    buendchen_umfang = float (input("Wie groß soll der finale Umfang des Bündchens sein (excl. NZ, in cm)?\nEingabe: "))
    buendchen_hoehe = float(input("Wie groß soll die finale Höhe des Bündchens sein (excl. NZ, in cm)?\nEingabe: "))
    stoffbreite = float(input("Wie breit ist der Stoff (in cm)?\nEingabe: "))
    
    print()
    
    #Zuschnitt
    nahtzugabe = 0.7
    zuschnitt_breite_ein_teil = buendchen_umfang + (2 * nahtzugabe)
    zuschnitt_breite_zwei_teile = buendchen_umfang/2 + (2 * nahtzugabe)
    zuschnitt_hoehe = (buendchen_hoehe * 2) + (2 * nahtzugabe)
    
    print()
    print("So groß wird das finale Bündchen (excl. NZ):")
    print()
    print("Bündchenumfang final, ohne NZ:".ljust(30),buendchen_umfang,"cm")
    print("Bündchenhöhe final, ohne NZ:".ljust(30),buendchen_hoehe,"cm")
    print()
    print("Und so groß musst du den Stoff zuschneiden (incl. NZ):")
    print()
    #if-Abfrage, ob Bündchenumfang größer oder kleiner als die Stoffbreite ist
    if buendchen_umfang + (2 * nahtzugabe) >= stoffbreite:
        print("Zuschnitt Breite (2-mal zuschneiden):".ljust(38),zuschnitt_breite_zwei_teile,"cm")
    else:
        print("Zuschnitt Breite (1-mal zuschneiden):".ljust(38),zuschnitt_breite_ein_teil,"cm")
        
    print("Zuschnitt Höhe:".ljust(38),zuschnitt_hoehe,"cm")
    
    print()
    
    input("Wenn du willst, dass das Programm nochmal ausgeführt wird drücke Enter. Zum Beenden, schließe das Fenster.")
    print()
    print()
    print()