import tkinter as tk

#les variables
size1 = 0
size2 = 0
proba1 = []
proba2 = []
H = 0
I = []


#Valider les probabilitées
#def validP():
#    global H, error2
#    H = 0
#    for x in range(size1):
#        i = -math.log(proba1[x], 2)
#        I.append(i)
#        H += p[x]*I[x]    
#    print("\nH= " + str(round(H, 2)) +" bits/symbole\n")


# Demander a ajouter les probabilitées
def demandeP():
    global p1, p2
    #destroy les frames si existantent
    try:
        for widgets in p1.winfo_children():
            widgets.destroy()
        for widgets in p2.winfo_children():
            widgets.destroy()
    except: 
        pass
    
    #creation des frames
    p1 = tk.Frame(prob, bg="#444")
    p2 = tk.Frame(prob, bg="#444")
    
    # creating de variables pour les proba des 2 sources
    for i in range(size1):
        proba1.append(tk.StringVar())
    for i in range(size2):
        proba2.append(tk.StringVar())
    
    # creation des titres + inputs des 2 sources
    for i in range(size1):
        tk.Label(p1, text="P"+str(i+1), bg="#444", fg="#fff",font=("Arial", 13), padx=15, pady=10).grid(row=i, column=0)
        tk.Entry(p1, bg="#444", fg="#fff",font=("Arial", 12), textvariable=proba1[i]).grid(row=i, column=1)
    for i in range(size2):
        tk.Label(p2, text="P"+str(i+1), bg="#444", fg="#fff",font=("Arial", 13), padx=15, pady=10).grid(row=i, column=0)
        tk.Entry(p2, bg="#444", fg="#fff",font=("Arial", 12), textvariable=proba2[i]).grid(row=i, column=1)
        
    #affichage de tout
    tk.Label(prob, text="Px", bg="#444", fg="#fff",font=("Arial", 13), padx=15, pady=10).grid(row=0, column=0)
    tk.Label(prob, text="Py", bg="#444", fg="#fff",font=("Arial", 13), padx=15, pady=10).grid(row=0, column=1)
    p1.grid(row=1, column=0)
    p2.grid(row=1, column=1)
    prob.grid(row=0, column=1)
    tk.Button(window, text="Valider", bg="#444", fg="#fff",font=("Arial", 11), padx=10, pady=3, command=validP).grid(row=1, column=1)
    error2 = tk.Label(window, text="Les valeurs donnée sont erroné (ORTHOGRAPHEUH)", bg="#444", fg="#f00",font=("Arial", 12), padx=20, pady=10)
    # suppression de l'erreur
    error.pack_forget()
    



# Valider les tailles des sources
def validSizes():
    global size1, size2
    #essayer de les cast en int
    try:
        size1 = int(var1.get())
        size2 = int(var2.get())
        demandeP()      # afficher le menu d'ajout des probabilitées
    # sinon afficher une erreur
    except:
        prob.grid_forget()
        error.pack()

# Configuration de la fenetre
window = tk.Tk()
window.title("BigTp")
window.geometry("+350+50")
window.config(bg="#444")

# creation de la frame principale de demarrage
main = tk.Frame(window, bg="#444")

#ajout du titre
tk.Label(main, text="Big TP 1", bg="#444", fg="#fff",font=("Arial", 24), padx=20, pady=10).pack(pady=20)


# Configuration du cadre de la taille des sources
sizes = tk.Frame(main, bg="#444")
titles = tk.Frame(sizes, bg="#444") # partie des titres pour les entries
inputs = tk.Frame(sizes, bg="#444") # partie des inputs

#les titres des entries
tk.Label(titles, text="Taille de la 1ere source", bg="#444", fg="#fff",font=("Arial", 13), padx=15, pady=10).grid(row=0, column=0)
tk.Label(titles, text="Taille de la 2eme source", bg="#444", fg="#fff",font=("Arial", 13), padx=15, pady=10).grid(row=1, column=0)

#les entries
var1 = tk.StringVar()
var2 = tk.StringVar()
tk.Entry(inputs, bg="#444", fg="#fff",font=("Arial", 12), textvariable=var1).grid(row=0, column=0, padx=20, pady=(5, 16))
tk.Entry(inputs, bg="#444", fg="#fff",font=("Arial", 12), textvariable=var2).grid(row=1, column=0, padx=20)

#affichier les frames de chaque partie
titles.grid(row=0, column=0)
inputs.grid(row=0, column=1)

#afficher la frame principale des tailles
sizes.pack()

# Affichage d'un bouton de confirmation
tk.Button(main, text="Valider", bg="#444", fg="#fff",font=("Arial", 15), padx=20, pady=10, command=validSizes).pack(pady = 30)

# positionnement d'un label invisible en cas d'erreur
error = tk.Label(main, text="Les valeurs donnée sont erroné (ORTHOGRAPHEUH)", bg="#444", fg="#f00",font=("Arial", 12), padx=20, pady=10)

# Affichage de la frame principale
main.grid(row=0, column=0)

#creation d'une frame pour la partie des probabilités
prob = tk.Frame(window, bg="#444")
p1 = tk.Frame(prob, bg="#444")
p2 = tk.Frame(prob, bg="#444")


window.mainloop()