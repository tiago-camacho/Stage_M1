!/usr/bin/env python
 -*- coding: utf-8 -*-
# Code pour poser les questions à l'utilisateur

# Espèce
espece = input("Quelle est l'espèce que vous souhaitez analyser ? ")

# Type de séquençage
type_sequencage = input("Quel est le type de séquençage utilisé? ARN ou ADN 

# Objectif de l'analyse
objectif_analyse = input("Quel est l'objectif de l'analyse des séquences ? ")

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
