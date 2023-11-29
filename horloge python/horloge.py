import datetime
import time

while True:
    heure_actuelle = datetime.datetime.now()
    heure = heure_actuelle.strftime("%H:%M:%S")  
    print("\r" + heure, end="", flush=True)  
    time.sleep(1)  