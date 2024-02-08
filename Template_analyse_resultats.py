#import Anybody_LoadOutput.Tools as LoadOutputTools

from Anybody_Package.Anybody_LoadOutput.Tools import load_results_from_file

from Anybody_Package.Anybody_Graph.GraphFunctions import graph
from Anybody_Package.Anybody_Graph.GraphFunctions import COP_graph
from Anybody_Package.Anybody_Graph.GraphFunctions import muscle_graph
from Anybody_Package.Anybody_Graph.GraphFunctions import define_simulations_line_style
from Anybody_Package.Anybody_Graph.GraphFunctions import define_simulation_description
from Anybody_Package.Anybody_Graph.GraphFunctions import define_COP_contour

from Anybody_Package.Anybody_LoadOutput.LoadOutput import combine_simulation_cases
from Anybody_Package.Anybody_LoadOutput.LoadLiterature import load_literature_data

from Anybody_Package.Anybody_Graph import PremadeGraphs

import matplotlib

# %% Contrôle de la taille des polices des graphiques

# Contrôle de la taille de la police globale
# matplotlib.rcParams.update({'font.size': 10})

# Contrôle des tailles de chaque partie partie du graphique
# Titre des cases des subplots
# matplotlib.rcParams.update({'axes.titlesize': 10})

# Titre du graphique
# matplotlib.rcParams.update({'figure.titlesize': 10})

# Nom des axes
# matplotlib.rcParams.update({'axes.labelsize': 10})

# Graduations des axes
# matplotlib.rcParams.update({'xtick.labelsize': 10})
# matplotlib.rcParams.update({'ytick.labelsize': 10})

# Légende
# matplotlib.rcParams.update({'legend.fontsize': 10})


# %% Setup des couleurs et légendes

# Définition des styles des simulations dans les graphiques (couleurs, forme de ligne taille...)
# Noms des couleurs : https://matplotlib.org/stable/gallery/color/named_colors.html
# Types de marqueurs : https://matplotlib.org/stable/api/markers_api.html
# Type de lignes : https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# SimulationsLineStyleDictionary = {"NOM_DE_LA_SIMULATION_1": {"color": "NOM_DE_LA_COULEUR", "marker": "", "markersize": 1, "linestyle": "-", "linewidth": 1},
#                                   "NOM_DE_LA_SIMULATION_2": {"color": "NOM_DE_LA_COULEUR", "marker": "", "markersize": 1, "linestyle": "-", "linewidth": 1},
#                                   "Wickham": {"color": "black", "marker": "", "markersize": 1, "linestyle": "--", "linewidth": 2}
#                                   }
SimulationsLineStyleDictionary = {"Dal Maso P1": {"marker": "+", "markersize": 12,"linestyle": ""},#litt HTT
                                  "Dal Maso P2": {"marker": "o", "markersize": 8,"linestyle": ""},
                                  "Dal Maso P3": {"marker": "v", "markersize": 8,"linestyle": ""},
                                  "Giphart et al, 2013": {"marker": "^", "markersize": 8,"linestyle": ""},
                                  "Graichen et al, 2000": {"marker": "<", "markersize": 8,"linestyle": ""},
                                  "Massimini et al, 2012": {"marker": ">", "markersize": 8,"linestyle": ""}, 
                                  "Matsuki et al, 2012": {"marker": "1", "markersize": 12,"linestyle": ""},
                                  "Nishinaka et al, 2008": {"marker": "2", "markersize": 12,"linestyle": ""},
                                  "Yamaguchi et al, 2000": {"marker": "s", "markersize": 8,"linestyle": ""},
                                  "Bergmann et al, 2007": {"marker": "X", "markersize": 12,"linestyle": ""}, #litt Force contact
                                  "Garner and Pandy, 2001": {"marker": "+", "markersize": 10,"linestyle": ""},#litt BL
                                  "Graichen et al., 2001": {"marker": "o", "markersize": 6,"linestyle": ""},
                                  "Hamilton et al., 2015": {"marker": "v", "markersize": 6,"linestyle": ""},
                                  "Howell et al., 1986": {"marker": "s", "markersize": 6,"linestyle": ""},
                                  "Hughes et al., 1998": {"marker": "^", "markersize": 6,"linestyle": ""},
                                  "Kuechle et al., 1997": {"marker": "<", "markersize": 6,"linestyle": ""},
                                  "Liu et al., 1997": {"marker": ">", "markersize": 6,"linestyle": ""},
                                  "Nakajima et al., 1999": {"marker": "1", "markersize": 10,"linestyle": ""},
                                  "Poppen and Walker, 1978": {"marker": "2", "markersize": 10,"linestyle": ""},
                                  "Otis et al., 1994": {"marker": "3", "markersize": 10,"linestyle": ""},
                                  "DeWilde et al., 2002": {"marker": "X", "markersize": 6,"linestyle": ""}
                                  }

# Texte de description des simulations dans les légendes
SimulationDescriptionDictionary = {"NOM_DE_LA_SIMULATION_1": "TEXTE_DE_DESCRIPTION_1",
                                   "NOM_DE_LA_SIMULATION_2": "TEXTE_DE_DESCRIPTION_2",
                                   "Wickham": "Wickham et al. 2010, n=24",
                                   "Bergmann": "Bergmann et al. 2007"
                                   }

# Fonctions pour définir les légendes et styles des graphiques en fonction des noms des simulations dans les dictionnaires
define_simulations_line_style(SimulationsLineStyleDictionary)
define_simulation_description(SimulationDescriptionDictionary)


# %%                                                Chargement des résultats sauvegardés
# Chemin d'accès au dossier dans lequel les fichiers ont été sauvegardés
SaveSimulationsDirectory = "Saved Simulations"

# NOM_DE_SIMULATION = LoadOutputTools.load_results_from_file(SaveSimulationsDirectory, "NOM_DU_FICHIER_DE_SAUVEGARDE_DE_SIMULATION")
Results = load_results_from_file(SaveSimulationsDirectory, "Results")

# %%                                                Chargement autres résultats et variables

# Chargement des dictionnaires de variable
SaveVariablesDirectory = "Saved VariablesDictionary"

# Chargement des variables de simulation sauvegardées
Variables = load_results_from_file(SaveVariablesDirectory, "Variables")

# %%                                                Chargement des données de littérature

Results_Literature = load_results_from_file(SaveSimulationsDirectory, "Results_Literature")

# %% Liste des catégories de muscles

# 9 muscles --> graphique 3x3
Muscles_Main = ["Deltoideus anterior",
                "Deltoideus lateral",
                "Deltoideus posterior",
                "Infraspinatus",
                "Supraspinatus",
                "Subscapularis",
                "Lower trapezius",
                "Middle trapezius",
                "Upper trapezius"
                
                ]

# 9 muscles --> graphique 3x3
# {"Nom_Muscle": composante_y}
Muscles_Aux = ["Pectoralis major clavicular",
               "Pectoralis major sternal",
               "Pectoralis minor",
               "Teres major",
               "Teres minor",
               "Rhomboideus",
               "Serratus anterior",
               "Biceps brachii long head",
               "Biceps brachii short head"
               ]

# 6 muscles --> graphique 2x3
Muscles_Extra = ["Sternocleidomastoid sternum",
                 "Sternocleidomastoid clavicular",
                 "Latissimus dorsi",
                 "Levator scapulae",
                 "Coracobrachialis",
                 "Triceps long head",
                 ]


# Muscles qui varient
Muscles_Variation = ["Deltoideus anterior",
                     "Deltoideus lateral",
                     "Deltoideus posterior",
                     "Triceps long head"
                     ]

# Muscles for comparison with Wickham et al. data
# 3x3
Muscle_Comp_Main = ["Deltoideus anterior",
                    "Deltoideus lateral",
                    "Deltoideus posterior",
                    "Infraspinatus",
                    "Supraspinatus",
                    "Subscapularis",
                    "Lower trapezius",
                    "Middle trapezius",
                    "Upper trapezius",
                    ]

# 2x3
Muscle_Comp_Aux = ["Pectoralis major clavicular",
                   "Pectoralis major sternal",
                   "Pectoralis minor",
                   "Teres major",
                   "Teres minor",
                   "Rhomboideus",
                   "Serratus anterior",
                   "Biceps brachii long head",
                   "Biceps brachii short head"
                   ]


# Muscles qui varient
Muscles_Comp_Variation = ["Deltoideus anterior",
                          "Deltoideus lateral",
                          "Deltoideus posterior"
                          ]

AllMuscles_List = list(Variables["Muscles"].keys())


# %% Graphiques

# graphique normaux
# graph(Results, "Abduction", "GHLin", "titre", cases_on="all", composante_y=["IS"])

# Activité des muscles
#PremadeGraphs.muscle_graph_from_list(Results, Muscles_Main, [3, 3], "Abduction", "Activity", "Muscles principaux : Activation maximale des muscles", cases_on="all", composante_y=["Max"])

# Muscles par parties individuelles
# PremadeGraphs.graph_all_muscle_fibers(Results, AllMuscles_List, "Abduction", "Activity", composante_y_muscle_combined=["Max"], cases_on="all")

# Comparaison des activités avec la littérature (avec les listes de muscles de l'étude de Wickham)
# PremadeGraphs.muscle_graph_from_list(Results, Muscle_Comp_Main, [3, 3], "Abduction", "Activity", "Muscles principaux : Activation maximale des muscles", cases_on="all", composante_y=["Max"])
# PremadeGraphs.muscle_graph_from_list(Results_Literature["Activity"], Muscle_Comp_Main, [3, 3], "Abduction", "Activity", "Muscles principaux : Activation maximale des muscles", cases_on="all", composante_y=["Max"], add_graph=True)

#Comparaison entre les simulations des translations de la tête humérales
graph(Results, "Abduction", "HHT", "Translations antéro-postérieures", cases_on="all", composante_y=["AP"])
graph(Results_Literature["Translation"], "Abduction", "Translation", "Translations antéro-postérieures", cases_on="all", composante_y=["AP"], add_graph=True)

graph(Results, "Abduction", "HHT", "Translations inférieures-supérieures", cases_on="all", composante_y=["IS"])
graph(Results_Literature["Translation"], "Abduction", "Translation", "Translations inférieures-supérieures", cases_on="all", composante_y=["IS"], add_graph=True)

graph(Results, "Abduction", "HHT", "Translations medio-laterales", cases_on="all", composante_y=["ML"])
graph(Results_Literature["Translation"], "Abduction", "Translation", "Translations medio-laterales", cases_on="all", composante_y=["ML"], add_graph=True)

#Comparaison des bras de levier
PremadeGraphs.muscle_graph_from_list(Results,  Muscles_Main, [3, 3], "Abduction", "MomentArm", "Muscles principaux : Bras de levier des muscles", cases_on="all", composante_y=["Mean"])
PremadeGraphs.muscle_graph_from_list(Results_Literature["BL"], Muscle_Comp_Main, [3, 3], "Abduction", "Moment arm", "Muscles principaux : Bras de levier des muscles", cases_on="all", composante_y=["Total"], add_graph=True)

PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "MomentArm", "Muscles auxiliaires : Bras de levier des muscles", cases_on="all", composante_y=["Mean"])
PremadeGraphs.muscle_graph_from_list(Results_Literature["BL"], Muscle_Comp_Aux, [3, 3], "Abduction", "Moment arm", "Muscles principaux : Bras de levier des muscles", cases_on="all", composante_y=["Total"], add_graph=True)

# #Forces musculaire actives
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Main, [3, 3], "Abduction", "Fm", "Muscles principaux : Forces actives des muscles", cases_on="all", composante_y=["Total"])
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Fm", "Muscles auxiliaires : Forces actives des muscles", cases_on="all", composante_y=["Total"])

# #Forces musculaire passives
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Main, [3, 3], "Abduction", "Fp", "Muscles principaux : Forces pasives des muscles", cases_on="all", composante_y=["Total"])
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Fp", "Muscles auxiliaires : Forces passives des muscles", cases_on="all", composante_y=["Total"])

#Forces musculaire total
PremadeGraphs.muscle_graph_from_list(Results, Muscles_Main, [3, 3], "Abduction", "Ft", "Muscles principaux : Forces des muscles total", cases_on="all", composante_y=["Total"])
PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Ft", "Muscles auxiliaires : Forces des muscles total", cases_on="all", composante_y=["Total"])

#Activité musculaire
PremadeGraphs.muscle_graph_from_list(Results,  Muscles_Main, [3, 3], "Abduction", "Activity", "Muscles principaux : activité musculire", cases_on="all", composante_y=["Mean"])
PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Activity", "Muscles auxiliaires : activité musculire", cases_on="all", composante_y=["Mean"])

#Force de reaction dans le chainon
graph(Results, "Abduction", "ResultanteForce_BS", "Force resultante", cases_on="all", composante_y=["AP"])
graph(Results_Literature["ForceContact"], "Abduction", "ForceContact", "Force résultante", cases_on="all", composante_y=["AP"], add_graph=True)

graph(Results, "Abduction", "ResultanteForce_BS", "Force resultante", cases_on="all", composante_y=["ML"])
graph(Results_Literature["ForceContact"], "Abduction", "ForceContact", "Force résultante", cases_on="all", composante_y=["ML"], add_graph=True)

graph(Results, "Abduction", "ResultanteForce_BS", "Force resultante", cases_on="all", composante_y=["IS"])
graph(Results_Literature["ForceContact"], "Abduction", "ForceContact", "Force résultante", cases_on="all", composante_y=["IS"], add_graph=True)