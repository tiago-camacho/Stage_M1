!/usr/bin/env python
-*- coding: utf-8 -*-

# Code pour poser les questions à l'utilisateur
# chaque reponse possible devera etre mise dans le readme
# Espèce
espece = input("Quelle est l'espèce que vous souhaitez analyser ? ")

# Type de séquençage
type_sequencage = input("Quel est le type de séquençage utilisé (ARN, ADN, etc.) ? ")

# Données brutes
donnees_brutes = input("Disposez-vous déjà de données brutes de séquençage ? (Oui/Non) ")

# Répertoire des données
repertoire_donnees = input("Dans quel répertoire se trouvent les données de séquençage ? ")

# Qualité des données
qualite_donnees = input("Quelle est la qualité des données de séquençage ? (Bonne, moyenne, faible) ")

# Objectif de l'analyse
objectif_analyse = input("Quel est l'objectif de l'analyse des séquences ? ")

# Type de séquence d'intérêt
type_sequence_interet = input("Quel type de séquence spécifique voulez-vous analyser ? ")

# Plateforme de séquençage
plateforme_sequençage = input("Quelle est la plateforme de séquençage utilisée ? ")

# Taille des données
taille_donnees = input("Quelle est la taille des données de séquençage (en gigaoctets ou en nombre de lectures) ? ")

# Niveau de multiplexage
niveau_multiplexage = input("Combien d'échantillons différents sont multiplexés dans vos données ? ")

# Format des données
format_donnees = input("Quel est le format des données de séquençage (FASTQ, BAM, etc.) ? ")

# Environnement informatique
environnement_informatique = input("Sur quelle plateforme ou système d'exploitation allez-vous exécuter l'analyse ? ")

# Contraintes de ressources
contraintes_ressources = input("Y a-t-il des contraintes de ressources (mémoire, processeur, etc.) pour l'analyse ? ")

# Prétraitement des données
pretraitement_donnees = input("Les données nécessitent-elles un prétraitement spécifique avant l'analyse ? (Oui/Non) ")

# Interprétation des résultats
interpretation_resultats = input("Comment souhaitez-vous interpréter les résultats (graphiques, tableaux, statistiques, etc.) ? ")

# Niveau d'expertise
niveau_expertise = input("Quel est votre niveau d'expertise en bioinformatique ? (Débutant, intermédiaire, avancé) ")

# Code pour choisir l'outil approprié

if espece == "humain" and type_sequencage == "ARN":
    if objectif_analyse == "Détection de réarrangements":
        if niveau_expertise == "Débutant":
            outil_selectionne = "IMGT/HighV-QUEST"
        else:
            outil_selectionne = "MiXCR"
    elif objectif_analyse == "Recherche de mutations":
        outil_selectionne = "MiXCR"
    elif objectif_analyse == "Quantification des expressions":
        outil_selectionne = "Cell Ranger"
    else:
        outil_selectionne = "Presto"
elif espece == "souris" and type_sequencage == "ARN":
    if objectif_analyse == "Détection de réarrangements":
        outil_selectionne = "MiXCR"
    elif objectif_analyse == "Recherche de mutations":
        outil_selectionne = "MiXCR"
    elif objectif_analyse == "Quantification des expressions":
        outil_selectionne = "Cell Ranger"
    else:
        outil_selectionne = "Presto"
else:
    outil_selectionne = "Presto"  # Cas par défaut si les combinaisons d'options ne correspondent à aucun outil spécifique

# Utilisez l'outil sélectionné dans votre programme
print("L'outil recommandé pour votre analyse est :", outil_selectionne)
