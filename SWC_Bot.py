#######MODULES#######################################################################################################################

from pyautogui import *
import time
from pynput.mouse import Button, Controller
import pyautogui
import datetime

#######USEFULL_FONCTIONS#######

print("let's dark summon!!!")
mouse = Controller()

def click():
    mouse.press(Button.left) 
    time.sleep(0.5) 
    mouse.release(Button.left)

def wait_and_click(message):
    w = 0
    while w == 0:
          print(f"recherche {message}")
          image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
          if image is not None:
              print(f"{message} trouvé")
              pyautogui.moveTo(image)
              time.sleep(1)
              pyautogui.click(image)
              w = 1
    return image

def wait_and_click_grey(message):
    w = 0
    while w == 0:
          print(f"recherche {message}")
          image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=True, confidence=0.70)
          if image is not None:
              print(f"{message} trouvé")
              pyautogui.moveTo(image)
              time.sleep(1)
              pyautogui.click(image)
              w = 1
    return image

def wait_and_click_peu_precis_grey(message):
    w = 0
    while w == 0:
          print(f"recherche {message}")
          image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=True, confidence=0.55)
          if image is not None:
              print(f"{message} trouvé")
              time.sleep(1)
              pyautogui.click(image)
              
              w = 1
    return image

def wait_and_click_precis(message):
    w = 0
    while w == 0:
          print(f"recherche {message}")
          image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
          if image is not None:
              print(f"{message} trouvé")
              time.sleep(1)
              pyautogui.click(image)
              
              w = 1
    return image

def wait_and_click_powerfull(message, count, repeat):
    if repeat == 5:
         suffixes = ["", "2", "3", "4", "5"]
    if repeat == 15:
        suffixes = ["", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15"]
    w = 0
    while w < count:
        for suffix in suffixes:
            print(f"recherche {message}{suffix}.png")
            image = pyautogui.locateCenterOnScreen(message + suffix + ".png", region=(76, 116, 2560, 1440), grayscale=False, confidence=0.65)
            if image is not None:
                print(f"{message}{suffix} trouvé")
                pyautogui.click(image)
                time.sleep(8)
                break
            w = w + 1
    
    return image

def wait_and_click_powerfull_precis(message, count, repeat):
    if repeat == 5:
         suffixes = ["", "2", "3", "4", "5"]
    if repeat == 15:
        suffixes = ["", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15"]
    if repeat == 18:
        suffixes = ["", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14","15","16","17","18"]
    w = 0
    while w < count:
        for suffix in suffixes:
            print(f"recherche {message}{suffix}.png")
            image = pyautogui.locateCenterOnScreen(message + suffix + ".png", region=(76, 116, 2560, 1440), grayscale=False, confidence=0.76)
            if image is not None:
                print(f"{message}{suffix} trouvé")
                pyautogui.click(image)
                time.sleep(8)
                break
            w = w + 1
    
    return image

def find_and_click(message):
    print(f"recherche {message}")
    image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if image is not None:
        print(f"{message} trouvé")
        pyautogui.moveTo(image)
        time.sleep(1)
        pyautogui.click(image)
    return image

def find_and_click_grey(message):
    print(f"recherche {message}")
    image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=True, confidence=0.70)
    if image is not None:
        print(f"{message} trouvé")
        pyautogui.moveTo(image)
        time.sleep(1)
        pyautogui.click(image)
    return image

def find_and_click_pas_precis(message):
    print(f"recherche {message}")
    image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=True, confidence=0.60)
    if image is not None:
        print(f"{message} trouvé")
        pyautogui.moveTo(image)
        time.sleep(1)
        pyautogui.click(image)
    return image

def find_and_click_rapide(message):
    print(f"recherche {message}")
    image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
    if image is not None:
        print(f"{message} trouvé")
        pyautogui.moveTo(image)
        time.sleep(0.5)
        pyautogui.click(image)
    return image

def find_and_click_precis(message):
    print(f"recherche {message}")
    image = pyautogui.locateCenterOnScreen(message + ".png", region=(0, 0, 2560, 1440), grayscale=False, confidence=0.95)
    if image is not None:
        print(f"{message} trouvé")
        pyautogui.moveTo(image)
        time.sleep(1)
        pyautogui.click(image)
    return image

def searchVictory():
    w = 0
    while w == 0:
        victory = pyautogui.locateCenterOnScreen('victory.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
        if victory is not None:
          print("victory trouvé")
          time.sleep(1)
          w = 1
        loose = pyautogui.locateCenterOnScreen('loose.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70)
        if loose is not None:
            print("loose trouvé")
            find_and_click('tryagain')
    return victory

#####IN_GAME##################################################################################################################################

def arene():
    count = 0
    wait_and_click('arene')
    wait_and_click('arene_defi')
    wait_and_click('arene_before')
    wait_and_click('refresh')
    wait_and_click('refresh_list')
    while count < 8:
        scroll = -110
        if find_and_click('defier') is not None:
            find_and_click('defier')
            wait_and_click('rednes')
            if count == 0:
                wait_and_click_precis('team3')
                wait_and_click_precis('team2')
            find_and_click('combat_rapide')
            find_and_click('combat_lent')
            wait_and_click('ok2')
            count = count +1
            print(count)
            print(count)
            wait_and_click('arene_before')
            time.sleep(3)
            wait_and_click('arene_before')
        if find_and_click('defier') is None:
            scroll = scroll -110
            find_and_click('arene_before')
            pyautogui.moveTo(762,566)
            time.sleep(1)
            pyautogui.scroll(scroll)
    wait_and_click('exitFleche')
    time.sleep(2)
    pyautogui.click(70,74)
    time.sleep(2)
    wait_and_click('menu')

def areneImplacable(count):
    wait_and_click('arene')
    wait_and_click('arene_implaccable')
    for i in range(count):
        find_and_click('ok')
        find_and_click('ok2')
        find_and_click('ok3')
        wait_and_click('matching')
        time.sleep(25)
        wait_and_click('arme_feu')
        pyautogui.moveTo(870,236)
        time.sleep(1)
        pyautogui.click(870,236)
        time.sleep(1.5)
        wait_and_click('confirmer')
        time.sleep(12)
        wait_and_click('arme_feu')
        wait_and_click('arme_eau')
        wait_and_click('confirmer')
        time.sleep(20)
        wait_and_click('rednes_implaccable')
        for x in range(20):
            time.sleep(0.5)
            find_and_click_grey('skill1_feu')
            time.sleep(0.5)
            find_and_click_grey('skill2_feu')
            time.sleep(0.5)
            find_and_click_grey('skill3_feu')
            time.sleep(0.5)
            pyautogui.moveTo(1173,328)
            time.sleep(0.5)
            pyautogui.click(1173,328)
            time.sleep(0.5)
            pyautogui.moveTo(1236,328)
            time.sleep(0.5)
            pyautogui.click(1236,328)


        find_and_click('ok')
        find_and_click('ok2')
        find_and_click('ok3')

def cairos(element, niveau, repeat):
    """Fonction pour lancer des combats dans les donjons de Cairos."""
    wait_and_click("cairos")
    wait_and_click(f"e{element.capitalize()}") if element in ["magie", "feu", "eau", "vent", "dark", "light"] else wait_and_click("arcemon")
    wait_and_click(f"niv{niveau}")
    wait_and_click("entrer")
    wait_and_click("combat")
    for _ in range(repeat):
        searchVictory()
        if _ < repeat :
            wait_and_click("tryagain")
            time.sleep(2)
            find_and_click('annuler')
    searchVictory()
    wait_and_click("exit")
    time.sleep(10)
    wait_and_click("exitCairos")
    wait_and_click('menu')
    

def donjon(boss):
    """Fonction pour lancer des combats dans les donjons spéciaux."""
    wait_and_click("donjon")
    
    
    if boss == "iles":
        wait_and_click("fissure")
    if boss == "ruines":
        wait_and_click("fissure")
    if boss == "colline":
        wait_and_click('raid')
    if boss == "papillon":
        wait_and_click('raid')
    wait_and_click(boss)
    wait_and_click("participation")
    wait_and_click("ok")
    if boss == "iles":
        wait_and_click('ready')
    if boss == "ruines":
        wait_and_click('ready')
    time.sleep(1)
    wait_and_click_peu_precis_grey("auto")
    searchVictory()
    time.sleep(5)
    find_and_click('ok')
    time.sleep(2)
    find_and_click('ok2')
    time.sleep(30)
    find_and_click("exit")
    time.sleep(1)
    find_and_click("exitRaid2")
    time.sleep(1)
    find_and_click('ok')
    time.sleep(1)
    find_and_click('ok2')
    time.sleep(1)
    find_and_click('menu')
    time.sleep(1)
    find_and_click_grey('quitter')
    time.sleep(2)
    find_and_click('ok')
    time.sleep(20)
    find_and_click('exitFleche')
    time.sleep(5)
    pyautogui.click(70,74)
    time.sleep(5)
    find_and_click("menu")
    time.sleep(2)
    

def croissance(target, niveau, repeat):
    """Fonction pour lancer des combats dans les missions de croissance."""
    wait_and_click("croissance")
    if target in ["cEau", "cFeu", "cVent"]:
        wait_and_click("entrainement")
        wait_and_click(target)
    elif target in ["araignee", "rhodoes", "tallades", "borbo", "shoerekly"]:
        wait_and_click("aventure")
        wait_and_click(target)
    else:
        wait_and_click("subjugation")
        wait_and_click(target.capitalize())
    wait_and_click('difficile')
    wait_and_click_precis(f"niv{niveau}")
    wait_and_click("entrer")
    wait_and_click("combat")
    for _ in range(repeat):
        searchVictory()
        find_and_click("tryagain")
        time.sleep(2)
        find_and_click('annuler')
        time.sleep(10)
    time.sleep(2)
    find_and_click("exit")
    time.sleep(20)
    find_and_click('exitFleche')
    time.sleep(2)
    find_and_click('exitFleche')
    time.sleep(2)
    find_and_click("menu")
    time.sleep(2)
    find_and_click("menu")

def go_mine(sleep):
        wait_and_click('sac')
        wait_and_click_precis('herbe')
        wait_and_click_precis('minerai')
        time.sleep(1.5)
        move_to((1200, 222))
        wait_and_click('geoloc')
        wait_and_click('minage')
        wait_and_click('go')
        time.sleep(sleep)
        #wait_and_click('retirer_carte')
        

def move_to(position):
        pyautogui.moveTo(position)
        time.sleep(1)
        pyautogui.click(position)
        


def research_canal(canal):
        time.sleep(0.5)
        move_to((154,123))
        time.sleep(1)
        wait_and_click('canal')
        time.sleep(1)
        find_and_click('fleche_next')
        x = 0
        while x < canal:
            x = x + 3
            find_and_click_precis('c' + str(x))
        find_and_click('ok')
        find_and_click('fleche_next')
        x = 0
        while x < canal:
            x = x + 1
            find_and_click_precis('c' + str(x))
            if x == 5 or x == 10 or x == 15 or x == 20 or x == 25:
                find_and_click('ok')
        find_and_click('ok')
        find_and_click('fleche_next')
        while x < canal:
            x = x + 1
            find_and_click_precis('c' + str(x))
            if x == 5 or x == 10 or x == 15 or x == 20 or x == 25:
                find_and_click('ok')
        find_and_click('ok')
        find_and_click('fleche_next')
        if x == 5 or x == 10 or x == 15 or x == 20 or x == 25:
                find_and_click('ok')
            
            




def move(direction):
    pyautogui.keyDown(direction)
    time.sleep(0.5)
    pyautogui.keyUp(direction)

    
def tour_celeste(count):
    x = 0
    while x < count:
        wait_and_click('next')
            
def peche(count):
    wait_and_click('menu')
    wait_and_click('parametres')
    wait_and_click('controles')
    wait_and_click('fixe')
    wait_and_click('exitFleche')
    wait_and_click('sac')
    wait_and_click_precis('herbe')
    wait_and_click_precis('poisson')
    wait_and_click('poisson2')
    wait_and_click('geoloc')
    wait_and_click('go')
    wait_and_click('peche')
    x = 0
    while x < count:
        wait_and_click('drop_peche')
        time.sleep(3)
        x = x + 1
    wait_and_click('exitPeche')
    wait_and_click('oui')
    wait_and_click('menu')

def recharge():
    def recharge_type(categorie, count):
        time.sleep(2)
        wait_and_click('entry_plus')
        time.sleep(2)
        wait_and_click('cristaux')
        for _ in range(count):
            wait_and_click(categorie)
        find_and_click('recharger_entree')
        time.sleep(1)
        find_and_click('recharger')

    wait_and_click('croissance')
    wait_and_click('aventure')
    recharge_type('recharge_croissance', 3)
    time.sleep(1)
    wait_and_click('exitFleche')
    wait_and_click('exitFleche')
    wait_and_click('quete')
    wait_and_click('repetitive')
    wait_and_click('repetitive_plus')
    wait_and_click('recharger_entree_repetitive')
    wait_and_click('repetitive_plus')
    wait_and_click('recharger_entree_repetitive')
    wait_and_click('exitFleche')
    wait_and_click('exitFleche')
    """wait_and_click('cairos')
    recharge_type('recharge_cairos', 2)
    wait_and_click_precis('exitCairos')"""
    """ wait_and_click('expedition')
    wait_and_click('tallades_feu')
    time.sleep(1)
    wait_and_click('entrer')
    recharge_type('plus_3', 2)
    wait_and_click('rhodoes_eau')
    wait_and_click('entrer')
    recharge_type('plus_3', 3)
    time.sleep(3)
    wait_and_click('exitFleche')
    wait_and_click('exitFleche')"""

def repeat_quest():
    wait_and_click('quete')
    wait_and_click('repetitive')
    wait_and_click('rukurangma')
    wait_and_click('q55')
    wait_and_click('accepter') 
    wait_and_click('result_repeat')
    time.sleep(2)
    wait_and_click('sac')
    time.sleep(1)
    pyautogui.click()
    time.sleep(10)
    find_and_click('sac')


def expedition(target, niveau, repeat):
    wait_and_click_precis('expedition')
    
    if target in ["expedition_speciale", "tallades_feu", "araignee_vent", "rhodoes_eau"]:
        wait_and_click_precis(target)
    elif target in ["shoerekly_light", "borbo_dark"]:
        pyautogui.moveTo(188,520)
        time.sleep(1)
        pyautogui.scroll(-110)
        wait_and_click(target)

    for x in range(0,4):
        if x == niveau:
            print("x")
            wait_and_click_precis('niv'+ str(x))

    wait_and_click('entrer')
    time.sleep(2)
    wait_and_click('combat')

    for y in range(repeat):
        searchVictory()
        find_and_click('tryagain')
        time.sleep(2)
        find_and_click('annuler')

    time.sleep(1)
    wait_and_click('exit')
    wait_and_click('exitFleche')
    wait_and_click('menu')


def histoire():
    for x in range (0,500):
            for y in range (0, 10):
                find_and_click_pas_precis('appuyer_histoire')
                time.sleep(3)
                find_and_click('acceptt')
                time.sleep(1)
                find_and_click('ok3')
                time.sleep(0.5)
                pyautogui.click(660,506)
                time.sleep(0.5)
                pyautogui.click(660,506)
                time.sleep(0.5)
                pyautogui.click(660,506)
                time.sleep(0.5)
                find_and_click('story_next')
    

def daypass():
    local = time.localtime()
    hour = time.strftime("%H", local)
    print(hour)
    if hour == "01":
        find_and_click('croix_pointage')
        
def raid():
    wait_and_click('accept')
    """wait_and_click('creerGroupe')
    wait_and_click('inviter')
    wait_and_click('qkent')
    wait_and_click('entrer2')"""
    wait_and_click('ready2')
    wait_and_click('chargement')
    time.sleep(25)
    wait_and_click('auto')
    for x in range(0,100):
        find_and_click('vita')
        time.sleep(1)
    
    searchVictory()
    wait_and_click('ok2')
    wait_and_click('exitRaid2')
    wait_and_click('ok3')

def newMinage():
    wait_and_click('sac')
    wait_and_click_precis('herbe')
    wait_and_click_precis('minerai2')
    time.sleep(1.5)
    wait_and_click('cobalt')
    wait_and_click('geoloc')
    wait_and_click('minage')
    time.sleep(1.5)
    pyautogui.moveTo(1069,359)
    time.sleep(1)
    pyautogui.click(1069,359)
    time.sleep(90)
    research_canal(15)

    w = 0
    while w == 0:
        if pyautogui.locateCenterOnScreen('minage_auto.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70) is not None:
            print("minage_auto trouvé")
            find_and_click_rapide('minage_auto')
            w = 1
            break
        else:    
            pyautogui.keyDown('s')
            time.sleep(1.5)
            pyautogui.keyUp('s')
            time.sleep(0.5)
        if pyautogui.locateCenterOnScreen('minage_auto.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70) is not None:
            print("minage_auto trouvé")
            find_and_click_rapide('minage_auto')
            w = 1
            break
        else:    
            pyautogui.keyDown('s')
            time.sleep(1.5)
            pyautogui.keyUp('s')
            time.sleep(0.5)
        if pyautogui.locateCenterOnScreen('minage_auto.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70) is not None:
            print("minage_auto trouvé")
            find_and_click_rapide('minage_auto')
            w = 1
            break
        else:    
            pyautogui.keyDown('d')
            time.sleep(1.5)
            pyautogui.keyUp('d')
            time.sleep(0.5)   
        if pyautogui.locateCenterOnScreen('minage_auto.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70) is not None:
            print("minage_auto trouvé")
            find_and_click_rapide('minage_auto')
            w = 1
            break
        else:    
            pyautogui.keyDown('d')
            time.sleep(1.5)
            pyautogui.keyUp('d')
            time.sleep(0.5)
        if pyautogui.locateCenterOnScreen('minage_auto.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70) is not None:
            print("minage_auto trouvé")
            find_and_click_rapide('minage_auto')
            w = 1
            break
        else:    
            pyautogui.keyDown('z')
            time.sleep(1.5)
            pyautogui.keyUp('z')
            time.sleep(0.5)
        if pyautogui.locateCenterOnScreen('minage_auto.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70) is not None:
            print("minage_auto trouvé")
            find_and_click_rapide('minage_auto')
            w = 1
            break
        else:    
            pyautogui.keyDown('z')
            time.sleep(1.5)
            pyautogui.keyUp('z')
            time.sleep(0.5)
        if pyautogui.locateCenterOnScreen('minage_auto.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.70) is not None:
            print("minage_auto trouvé")
            find_and_click_rapide('minage_auto')
            w = 1
            break
        else:    
            pyautogui.keyDown('q')
            time.sleep(1.5)
            pyautogui.keyUp('q')
            time.sleep(0.5)
    if w == 1:
        print("go dodo")
        time.sleep(3600)


def fabrication(count):
    x = 0
    while x < count:
        wait_and_click_grey('fabrication')
        wait_and_click_grey('fabrication')
        x = x + 1 



            
def exploration():
    wait_and_click_grey('home')
    time.sleep(60)
    wait_and_click('capitaine')
    wait_and_click('exploration')
    time.sleep(5)
    x = 0
    while x < 3:
        wait_and_click('exploration_terminee')
        time.sleep(2.5)
        move_to((154,123))
        time.sleep(0.5)
        wait_and_click('ok_explo')
        time.sleep(0.5)
        wait_and_click('commencer_explo')
        time.sleep(2)
        wait_and_click('commencer_explo2')
        x = x + 1
    time.sleep(1)
    wait_and_click('qgexit')
    time.sleep(1)
    wait_and_click('menu')


def thunasse(count, canal):
    y = 0
    while y < count:
        wait_and_click('menu')
        time.sleep(2)
        wait_and_click('carte')
        wait_and_click('rukurangma3')
        wait_and_click_precis('ranite')
        wait_and_click('thunes4')
        wait_and_click('ok')
        f = 0
        while f < 8:
            find_and_click_grey('croix')
            time.sleep(1.5)
            f = f + 1
        wait_and_click_grey('ig')
        pyautogui.keyDown('s')
        time.sleep(1.5)
        pyautogui.keyUp('s')
        pyautogui.keyDown('d')
        time.sleep(0.5)
        pyautogui.keyUp('d')
        time.sleep(1)
        find_and_click_precis('skill1_feu')
        time.sleep(4)
        find_and_click_precis('skill3_feu')
        wait_and_click('menu')
        time.sleep(2)
        wait_and_click('carte')
        wait_and_click('rukurangma3')
        wait_and_click_precis('ranite')
        wait_and_click('thunes5')
        wait_and_click('ok')
        f = 0
        while f < 5:
            find_and_click_grey('croix')
            time.sleep(1.5)
            f = f + 1
        wait_and_click_grey('ig')
        pyautogui.keyDown('d')
        time.sleep(3)
        pyautogui.keyUp('d')
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        find_and_click_grey('ig')
        find_and_click_precis('skill1_feu')
        time.sleep(2)
        find_and_click_precis('skill3_feu')
        wait_and_click('menu')
        time.sleep(2)
        wait_and_click('carte')
        wait_and_click('rukurangma3')
        wait_and_click_precis('caladi')
        wait_and_click('thunes1')
        wait_and_click('ok')
        f = 0
        while f < 8:
            find_and_click_grey('croix')
            time.sleep(1.5)
            f = f + 1
        wait_and_click_grey('ig')
        pyautogui.keyDown('q')
        time.sleep(1.5)
        pyautogui.keyUp('q')
        pyautogui.keyDown('s')
        time.sleep(0.5)
        pyautogui.keyUp('s')
        find_and_click_precis('skill1_feu')
        time.sleep(2.5)
        find_and_click_precis('skill3_feu')
        wait_and_click('menu')
        time.sleep(2)
        wait_and_click('carte')
        wait_and_click('rukurangma3')
        wait_and_click_precis('caladi')
        wait_and_click('thunes3')
        wait_and_click('ok')
        f = 0
        while f < 5:
            find_and_click_grey('croix')
            time.sleep(1.5)
            f = f + 1
        wait_and_click_grey('ig')
        pyautogui.keyDown('q')
        time.sleep(4)
        pyautogui.keyUp('q')
        find_and_click_precis('skill1_feu')
        time.sleep(2)
        find_and_click_precis('skill3_feu')
        time.sleep(3)
        y = y + 1
        research_canal(canal)

def event():
    wait_and_click_precis('exclamation')
    wait_and_click_precis('normal')
    wait_and_click_grey('autoopm')
    wait_and_click('exit')



"""print("Let's routine")
    wait_and_click('menu')
    wait_and_click('parametres')
    wait_and_click('controles')
    wait_and_click('fixe')
    wait_and_click('exitFleche')"""

def combiner(count):
    z = 0
    while z < count:
        wait_and_click('allselect')
        time.sleep(1)
        wait_and_click('combinerrunes')
        wait_and_click('ok4')
        wait_and_click('ok3')

#######MAIN##############################################################################################################################  

def main():
    n = input("1- Routine\n2- Cairos\n3- Chemins de Croissance\n4- Donjon groupe\n5- Arène\n6- Tour des Epreuves\n7- Tour Celeste\n8- Arene\n9- Journal de Garde\n10- Quetes\n11- Metiers\n\nPlease enter a number : ")

    if n == '1':
        

        """y = 0
        while y < 15:
            event()"""
        #histoire()
        #recharge()
        time.sleep(2)
        arene()
        time.sleep(2)
        cairos("magie", 10, 3)
        ###CAIROS###
        #cairos("arcemon", 3, 3)
        ###COISSANCE###
        #croissance("araignee", 15, 6)
        #####DONJON###
        donjon("colline")
        donjon("papillon")
        #donjon('ruines')
        #donjon('iles')
        ####EXPEDITION#####
        #expedition("tallades_feu", 3, 2)
        #expedition("shoerekly_light",3 , 2)
        #expedition("araignee_vent",3 , 2)
        #expedition("rhodoes_eau", 4, 2)
        #expedition("borbo_dark", 3, 2)
        #expedition("res_eau", 2, 2)
        
        time.sleep(2)
        ###REPEAT QUEST###
        repeat_quest()
        #arene()
        newMinage()
        exploration()
        #areneImplacable(8)
        ####ARENE####
        arene()
        #croissance("tallades", 14, 16)
        #croissance("araignee", 13, 20)
        print("eheh routine réussie!!!!!!!!!")
        #arene()
        #areneImplacable(7)"""
        go_mine(90)
        thunasse(500,30)
        arene()

        #fabrication(200)

    if n == '2':
        wait_and_click('chro')
        wait_and_click('chro2')
        go_mine(90)
        thunasse(500,30)
    
    if n == '3':
        #histoire()
        #combiner(150)
        #time.sleep(4)
        #wait_and_click('sactest')
        #croissance("araignee", 1, 300)
        croissance("tallades", 1, 300)
        exploration()
        arene()
        go_mine(90)
        thunasse(500,30)
        
    

              
if __name__ == "__main__":
    main()