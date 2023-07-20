Prérequis:

Installer python ( télécharger l'installer adéquat ici https://www.python.org/downloads/release/python-3102/ ) --> à la fin de l'installatioon cliquer sur Disable path length limit --> ajouter python au PATH 
Dans la barre de recherche windows, chercher variables d'environnement, cliquer, puis cliquer sur Path sous Variables utilisiateur et coller le chemin d'accès à Python qui doit ressembler à ceci C:\Users\nomutilisateur\AppData\Local\Programs\Python\Python310\
Sous variables systèmes faire nouveau path et coller de nouveau C:\Users\max\AppData\Local\Programs\Python\Python310\
Vérifier que python est bien installé en exécutant la commande python dans un invite de commandes
Reboot la machine
Installer pip grace à pip.py  ( pour windows se placer dans le répertoire bombcrypto avec une invite de commandes, et faire python ./pip.py ) ( pour linux sudo apt install python3-pip )
Ajouter pip au PATH -> variables d'environnement et y ajouter le chemin 
Installer Keyboard; opencv; PIL et Pillow avec les commandes suivantes
pip install Keybord
pip install opencv-python
pip install opencv-python-headless --> librairie sans GUI sinon fonctionne pas sur VM sans CG


pour linux python3-tk python3-dev et scrot --> sudo apt install python3-tk python3-dev
sudo apt install scrot


Exécuter le fichier test3.py avec python pour lancer


traces des commandes exécutées sous linux :
différence entre installer des modules sous sudo ou non
du coup on part d'ici full sudo su
pour résoudre File "/usr/local/lib/python3.8/dist-packages/Xlib/protocol/display.py", line 129, in __init__
    raise error.DisplayConnectionError(self.display_name, r.reason)
Xlib.error.DisplayConnectionError: Can't connect to display ":0.0": b'No protocol specified\n'
faire pip install safeeyes

xhost +
