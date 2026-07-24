# ----------------------------------------------------------------------------------------
#     PROJET : RELEVE DE NOTES D'ETUDIANTS EN PYTHON
#     Version corrigee - utilise dict, liste et tuple de facon coherente
# ----------------------------------------------------------------------------------------

# ---- LES UE ET LEURS CREDITS (fixes -> tuple) ----
# Chaque UE est associee a son credit. On les regroupe DIRECTEMENT ensemble
# dans une liste de tuples : c'est le point cle qui evite le bug des "listes
# paralleles" (UE d'un cote, credit de l'autre, et on espere que les index
# correspondent toujours -> source classique d'erreurs).

UE_CREDITS = (
    ("MTH102", 4),
    ("Calcul differentiel", 4),
    ("Anglais", 2),
    ("Francais", 2),
    ("Python", 3),
    ("Langage C", 4),
    ("Dessin Tech", 2),
    ("GEO102", 2),
    ("TP Calcul diff", 2),
)

# ---- BASE DE DONNEES DES ETUDIANTS ----
# dictionnaire de dictionnaires : { numero_carte : {infos + releve} }
# Ca permet de gerer PLUSIEURS etudiants, pas un seul comme avant.
Etudiants = {}


def ajouter_etudiant():
    """Enregistre un etudiant et ses notes pour chaque UE."""
    print("--------------------------------------")
    print("ENREGISTREMENT DE L'ETUDIANT")
    print("--------------------------------------")

    numero_carte = input("Numero de carte : ")
    nom = input("Nom de l'etudiant : ")
    prenom = input("Prenom de l'etudiant : ")

    releve = {}  # { nom_ue : [notes] }

    for ue, credit in UE_CREDITS:
        print(f"\n--- UE : {ue} (credit : {credit}) ---")
        choix = input("Avez-vous fait un devoir de classe ? (1=Oui / 0=Non) : ")

        notes = []
        if choix == "1":
            note_dev = float(input("Note de classe (/20) : "))
            note_exam = float(input("Note d'examen (/20) : "))
            notes.append(note_dev)
            notes.append(note_exam)
        else:
            note_exam = float(input("Note d'examen (/20) : "))
            notes.append(note_exam)

        releve[ue] = notes

    # On stocke TOUT dans un seul dict propre a cet etudiant
    Etudiants[numero_carte] = {
        "nom": nom,
        "prenom": prenom,
        "releve": releve,
    }

    print(f"\n✅ Etudiant {prenom} {nom} enregistre avec succes.\n")


def moyenne_ue(notes):
    """Calcule la moyenne d'une seule UE a partir de sa liste de notes."""
    if len(notes) == 2:
        # Devoir de classe (40%) + Examen (60%) -> ponderation classique
        return notes[0] * 0.4 + notes[1] * 0.6
    else:
        return notes[0]


def moyenne_generale(etudiant):
    """Calcule la moyenne generale ponderee par les credits."""
    total_points = 0
    total_credits = 0

    for ue, credit in UE_CREDITS:
        notes = etudiant["releve"][ue]
        moy = moyenne_ue(notes)
        total_points += moy * credit
        total_credits += credit

    return total_points / total_credits if total_credits else 0


def afficher_releve(numero_carte):
    """Affiche le releve de notes complet d'un etudiant."""
    if numero_carte not in Etudiants:
        print("❌ Etudiant introuvable.")
        return

    etudiant = Etudiants[numero_carte]
    print("===============================================================")
    print(f"  RELEVE DE NOTES - {etudiant['prenom']} {etudiant['nom']} (N° {numero_carte})")
    print("===============================================================")
    print(f"{'UE':<25}{'Credit':<10}{'Moyenne':<10}")
    print("-" * 45)

    for ue, credit in UE_CREDITS:
        notes = etudiant["releve"][ue]
        moy = moyenne_ue(notes)
        print(f"{ue:<25}{credit:<10}{moy:<10.2f}")

    moy_gen = moyenne_generale(etudiant)
    print("-" * 45)
    print(f"MOYENNE GENERALE : {moy_gen:.2f}/20")
    print(mention(moy_gen))
    print()


def mention(moyenne):
    """Retourne la mention selon la moyenne generale."""
    if moyenne >= 16:
        return "Mention : Tres Bien"
    elif moyenne >= 14:
        return "Mention : Bien"
    elif moyenne >= 12:
        return "Mention : Assez Bien"
    elif moyenne >= 10:
        return "Mention : Passable"
    else:
        return "Mention : Insuffisant (non admis)"


def classement():
    """Classe tous les etudiants par moyenne generale decroissante."""
    if not Etudiants:
        print("❌ Aucun etudiant enregistre.")
        return

    # On construit une liste de tuples (moyenne, nom, prenom, numero)
    # -> le tuple est parfait ici : donnee courte, groupee, et triable facilement.
    resultats = []
    for numero, infos in Etudiants.items():
        moy = moyenne_generale(infos)
        resultats.append((moy, infos["nom"], infos["prenom"], numero))

    resultats.sort(reverse=True)  # tri decroissant sur le 1er element du tuple (la moyenne)

    print("===============================================================")
    print("                  CLASSEMENT PAR ORDRE DE MERITE")
    print("===============================================================")
    for rang, (moy, nom, prenom, numero) in enumerate(resultats, start=1):
        print(f"{rang}. {prenom} {nom} (N° {numero}) - Moyenne : {moy:.2f}/20")
    print()


def meilleure_note():
    """Affiche l'etudiant ayant la meilleure moyenne generale."""
    if not Etudiants:
        print("❌ Aucun etudiant enregistre.")
        return

    meilleur = max(
        Etudiants.items(),
        key=lambda item: moyenne_generale(item[1])
    )
    numero, infos = meilleur
    print(f" Meilleure moyenne : {infos['prenom']} {infos['nom']} "
          f"avec {moyenne_generale(infos):.2f}/20\n")


def plus_faible_note():
    """Affiche l'etudiant ayant la plus faible moyenne generale."""
    if not Etudiants:
        print("❌ Aucun etudiant enregistre.")
        return

    plus_faible = min(
        Etudiants.items(),
        key=lambda item: moyenne_generale(item[1])
    )
    numero, infos = plus_faible
    print(f"  Moyenne la plus faible : {infos['prenom']} {infos['nom']} "
          f"avec {moyenne_generale(infos):.2f}/20\n")


def nombre_ue():
    print(f"Nombre d'UE ce semestre : {len(UE_CREDITS)}\n")


def afficher_tous():
    """Affiche le releve de tous les etudiants enregistres."""
    if not Etudiants:
        print("❌ Aucun etudiant enregistre.")
        return
    for numero in Etudiants:
        afficher_releve(numero)


def menu():
    print("==============================================")
    print("   MENU DE GESTION DES DONNEES DES ETUDIANTS")
    print("==============================================")
    print("1. Afficher tout le releve de notes du semestre")
    print("2. Enregistrer un nouvel etudiant")
    print("3. Classement par ordre de merite")
    print("4. Afficher la meilleure moyenne")
    print("5. Afficher la plus faible moyenne")
    print("6. Nombre d'UE du semestre")
    print("9. Quitter")


def main():
    while True:
        menu()
        choix = input("Votre choix : ")

        if choix == "1":
            afficher_tous()
        elif choix == "2":
            ajouter_etudiant()
        elif choix == "3":
            classement()
        elif choix == "4":
            meilleure_note()
        elif choix == "5":
            plus_faible_note()
        elif choix == "6":
            nombre_ue()
        elif choix == "9":
            print("A bientot !")
            break
        else:
            print("❌ Choix invalide, reessayez.\n")


if __name__ == "__main__":
    main()