import pandas as pd

from data_loader import load_data


data = load_data()

# Tables de Dimension 
def dim(col):
    dim = data[col].unique()
    return dim


# KPIs
nbre_program = len(data)
nbre_actions_effectuee = data.Valeur.sum()

# Fonction pour conpter le nombre valeurs uniques pour une colonne donnée
def count_col(col):
    nbre_val = len(dim(col))
    return nbre_val

# Fonction pour faire des aggrégation
def top_N_par_col(cols:list):
    top_N = data.groupby(cols)["Valeur"].sum().sort_values(ascending=False)
    return top_N


# Fonction de repartition du nombre d'actions par champ
def sum_actions_par_col(col):
    sum_actions = data.groupby([col])["Valeur"].sum()
    return sum_actions


# Col ayant le plus bénéficié d'action
def most_benefit(col):
    val = data.groupby(col)["Valeur"].sum().sort_values(ascending=False)
    if val.index[0]!="Autres":
        return (val.index[0], val.iloc[0])
    else:
        return (val.index[1], val.iloc[1])

most_actions_par_region = data.groupby(["Région"])["Valeur"].sum().sort_values(ascending=False)
#most_actions_par_region = data.groupby(["Région", "Catégorie"])["Valeur"].sum()
#filtre = 
