# ----------------------------------------------------------------------------------------
# -     MON PROJET EST DE REALISER UN RELEVE DE NOTES D'UN ETUDIANT AVEC DU PROGAMME PYTON
# ----------------------------------------------------------------------------------------


releve={}  ##Declaration d'un dictionnaire releve qui conserve l'ue et la note 


credit=(4, 4, 2, 2, 3, 4, 2, 2, 2)  
## les ue ne changerons pas au cours du programme donc je vais utliser les tuples 
UE=("MTH102","Calcul differentielle", 
     "Anglais", "Francais", "Python",
    "Language C", 
     "Dessin Tech", "GEO102", 
     "tp calcul diff",
   )  



def taille(UE):
    compteur=0
    for i in UE:
        compteur+=1
    return compteur

# UE=(("mth19", 2), ("geo19", 4))        j'utilise cette ligne de code en commentaire  pour tester le programme 

def AjouterNote(releve, UE):
   
    for ue in UE:
        print("--------------------------------")
        print(f" UE :  {ue}")
        print("--------------------------------")

        print(f"Vous avez fait un devoir de  classe en {ue} ?si OUI appuyer 1 au contraire appuyer la touche 0\n1.0ui\n0.Non")
        choix=int(input("Choix:"))
        Note=[]
        if choix==1:

            noteDev=float(input("Note de classe:"))
            noteExam=float(input("note_Examen:"))

            Note.append(noteDev)
            Note.append(noteExam)

        elif choix==0:
            noteExam=float(input("note_Examen:"))
            Note.append(noteExam)
        releve[ue]=Note



#                               MENU
def  Menu():
    print("==============================================")
    print("MENU DE GESTION DES DONNES DES ETUDIANTS      ")
    print("=============================================")

    print("1.AFFICHER TOUT LE RELEVE DE NOTE DU SEMESTRE")
    print("2.ENREGISTREMENT DE VOS DONNNES ")
    print("3.CLASSEMENT DANS L'ORDRE DE MERITE SELON LA MOYENNE DE L'UE")
    print("4.AFFICHER LA MEILLEUR NOTE OBTENUE")
    print("6.AFFICHER LA PLUS FAIBLE NOTE DU SEMESTRE ")
    print("8.NOMBRE D'UE DU SEMESTRE")
    print("9.QUITTER\n\n")




# calcule de la moyenne de chaque UE  | moyUE= noteUE * credit


#Moyenne Generale MOyGENERAL=(Somme de moyUE)/(total de credit du semestre)
#
#

##CALCUL DE LA MOYENNE DE CHAQUE UE EN FONCTION DES CREDIT
