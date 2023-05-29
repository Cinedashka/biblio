import tkinter as tk
from tkinter import ttk, messagebox
from database import Database



root = tk.Tk()
root.title("Livre Database")
root.geometry("700x400")
root.configure(background="")

db = Database('bibliotheque.db')

# Styling
style = ttk.Style()
style.configure("TButton", background="#FF6B6B", foreground="#4949c6")
style.configure("TLabel", background="#F4F4F4", foreground="#4949c6")
style.configure("TEntry", background="#FFFFFF", fieldbackground="#4949c6")
style.configure("TText", background="#FFFFFF", foreground="#4949c6")

# Input Form Interface
def switch_to_input_form():
    display_frame.pack_forget()
    input_frame.pack()

def ajouter_livres():
   
   titre = entry_titre.get()
   annee = entry_annee.get()
   exemplaires = entry_exemplaires.get()
   nom_auteur = entry_nom_auteur.get()
   prenom_auteur = entry_prenom_auteur.get()




   if titre and annee and exemplaires and nom_auteur and prenom_auteur:
        try:
            annee = int(annee)  # Make sure age is a valid integer
            exemplaires = int(exemplaires)
        except ValueError:
            messagebox.showerror("Invalid Annee and exemplaires", "Please enter a valid integer for annee and exemplaires.")
            return
        db.ajouter_livres(titre, annee, exemplaires, nom_auteur, prenom_auteur)
        result_label.configure(text="Les informations ont été sauvegardées avec succès dans la base de données 'biblitheque.db'.")
        clear_input_fields()
        switch_to_display_form()  # Refresh the display table
   else:
        result_label.configure(text="Veuillez remplir tous les champs.", foreground="black")


    
    
# In the Database class:
def clear_input_fields():
    entry_titre.delete(0,tk.END)
    entry_annee.delete(0, tk.END)
    entry_exemplaires.delete(0, tk.END)
    entry_nom_auteur.delete(0, tk.END)
    entry_prenom_auteur.delete(0, tk.END)
# Display Form Interface
def switch_to_display_form():
    input_frame.pack_forget()
    display_frame.pack()
    afficher_livres()

def afficher_livres():
    livres = db.recuperer_livres()

    for row in table.get_children():
        table.delete(row)

    for livre in livres:
        table.insert("", "end", values=(livre.id, livre.titre, livre.annee, livre.exemplaires, livre.nom_auteur, livre.prenom_auteur))

    result_label.configure(text="Les informations ont été récupérées avec succès depuis la base de données 'personnes.db'.")

# Input Form
input_frame = tk.Frame(root, bg="#F4F4F4")
input_label = ttk.Label(input_frame, text="Nouveau Livre", font=("Helvetica", 16), background="#F4F4F4")

input_label.pack(pady=5)
result_label = ttk.Label(input_frame, text="", background="#F4F4F4")
result_label.pack()

titre_label = ttk.Label(input_frame, text="Titre:", background="#F4F4F4")
titre_label.pack()
entry_titre = ttk.Entry(input_frame)
entry_titre.pack()

annee_label = ttk.Label(input_frame, text="Annee d'edition:", background="#F4F4F4")
annee_label.pack()
entry_annee = ttk.Entry(input_frame)
entry_annee.pack()

exemplaire_label = ttk.Label(input_frame, text="Nombre d'exemplaires:", background="#F4F4F4")
exemplaire_label.pack()
entry_exemplaires = ttk.Entry(input_frame)
entry_exemplaires.pack()

nom_label = ttk.Label(input_frame, text="Nom de l'auteur:", background="#F4F4F4")
nom_label.pack()
entry_nom_auteur = ttk.Entry(input_frame)
entry_nom_auteur.pack()

prenom_label = ttk.Label(input_frame, text="Prenom de l'auteur:", background="#F4F4F4")
prenom_label.pack()
entry_prenom_auteur = ttk.Entry(input_frame)
entry_prenom_auteur.pack()


ajouter_button = ttk.Button(input_frame, text="Ajouter", command=ajouter_livres)
ajouter_button.pack(pady=10)

switch_to_display_button = ttk.Button(input_frame, text="Imprimer", command=switch_to_display_form)
switch_to_display_button.pack()

# Display Form
display_frame = tk.Frame(root, bg="#F4F4F4")

display_label = ttk.Label(display_frame, text="Livres enregistrées", font=("Helvetica", 16), background="#F4F4F4")
display_label.pack(pady=10)

table_frame = ttk.Frame(display_frame)
table = ttk.Treeview(table_frame, columns=("ID", "Titre", "Annee d'edition", "Nombre d'exemplaire", "Nom de l'auteur" , "Prenom de l'auteur"), show="headings")
table.heading("ID", text="ID")
table.heading("Titre", text="Titre")
table.heading("Annee d'edition", text="Annee d'edition")
table.heading("Nombre d'exemplaire", text="Nombre d'exemplaire")
table.heading("Nom de l'auteur", text="Nom de l'auteur")
table.heading("Prenom de l'auteur", text="Prenom de l'auteur")

table.column("ID", width=20)
table.column("Titre", width=150)
table.column("Annee d'edition", width=100)
table.column("Nombre d'exemplaire", width=130)
table.column("Nom de l'auteur", width=100)
table.column("Prenom de l'auteur", width=120)

table.tag_configure("oddrow", background="#E8E8E8")
table.tag_configure("evenrow", background="#FFFFFF")

table.pack(padx=10, pady=10)
table_frame.pack(padx=10, pady=5)

switch_to_input_button = ttk.Button(display_frame, text="Retour", command=switch_to_input_form)
switch_to_input_button.pack(pady=10)

# Other Functions
def on_quit():
    db.fermer_connexion()
    root.destroy()

# Quit Button
quit_button = ttk.Button(root, text="Quitter", command=on_quit)
quit_button.pack(pady=10)

# Start the program
switch_to_input_form()
root.mainloop()

print("Fin du programme.")