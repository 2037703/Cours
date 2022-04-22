# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la classe casier
from cours import *

# Importer la boite de dialogue

import interfacecours

# Import ls_Etudiants

#from logique import ls_Etudiants

# Importer le main

from main import *
#Fonctions cacher labels erreur

def cacher_labels_erreur(objet):
    objet.label_cours_erreur_numero.setVisible(False)


######################################################
###### DÉFINITIONS DE LA CLASSE popup_casier ######
######################################################

class PopUpCours(QtWidgets.QDialog, interfacecours.Ui_popup_cours):
    def __init__(self, parent=None):
        super(PopUpCours, self).__init__(parent)
        self.setupUi(self)
        cacher_labels_erreur(self)



    @pyqtSlot()
    def on_pushButton_cours_ajouter_clicked(self):
        """
        Méthode du button ajouter cours
        """

        # Instanciation
        cour = Cours()

        #Entrée de données

        cour.Sigle_cours = self.




