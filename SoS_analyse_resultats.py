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
from Anybody_Package.Anybody_Graph.GraphFunctions import ForceMeasure_bar_plot_direction

from Anybody_Package.Anybody_Graph import PremadeGraphs

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% Contrôle de la taille des polices des graphiques

#Contrôle de la taille de la police globale
matplotlib.rcParams.update({'font.size': 14})

#Contrôle des tailles de chaque partie partie du graphique
#Titre des cases des subplots
matplotlib.rcParams.update({'axes.titlesize': 14})

#Titre du graphique
matplotlib.rcParams.update({'figure.titlesize': 14})

#Nom des axes
matplotlib.rcParams.update({'axes.labelsize': 14})

#Graduations des axes
matplotlib.rcParams.update({'xtick.labelsize': 14})
matplotlib.rcParams.update({'ytick.labelsize': 14})

#Légende
matplotlib.rcParams.update({'legend.fontsize': 14})


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
                                  "DeWilde et al., 2002": {"marker": "X", "markersize": 6,"linestyle": ""},
                                  "r=1": {"color": "darkslateblue", "linestyle": "solid"},
                                  "r=0.8": {"color": "mediumslateblue", "linestyle": "dashed"},
                                  "r=0.6": {"color": "mediumorchid", "linestyle": "dashdot"},
                                  "supra_20mm": {"color": "darkslateblue", "linestyle": "solid"},
                                  "supra_0mm": {"color": "mediumslateblue", "linestyle": "dashed"},
                                  "supra_-20mm": {"color": "mediumorchid", "linestyle": "dashdot"},
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
# Liste des muscles avec une seule surface de wrapping
muscle_surface = ["Supraspinatus", 
                 "Infraspinatus", 
                 "Deltoideus anterior",
                 "Deltoideus lateral",
                 "Deltoideus posterior"
                 ]

# Liste des muscles avec plusieurs surface de wrapping
muscle_multisurface = ["Deltoideus posterior",
                       "Subscapularis"
                       ]

AllMuscles_List = list(Variables["Muscles"].keys())


#Calcul Instabilité Ratio
for case in Results:
    # Pour Shear où on additionne le shear IS et AP
    Results[case]["Instability Ratio"] = {"Description": "Instability ratio", "SequenceComposantes": "Total"}
    # ratio = norme(Ap, IS)/ML
    #Results[case]["Instability Ratio"]["Total"] = (abs(Results[case]["Force_cisaillement"]["IS"]) + abs(Results[case]["Force_cisaillement"]["AP"])) / abs(Results[case]["Force_compression"]["ML"])
    Results[case]["Instability Ratio"]["Total"] = np.sqrt((Results[case]["Force_cisaillement"]["IS"])**2 + (Results[case]["Force_cisaillement"]["AP"])**2)/ abs(Results[case]["Force_compression"]["ML"])


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
graph(Results_Literature["Translation"], "Abduction", "Translation", "Posterior displacement", cases_on="all", composante_y=["AP"], add_graph=True, ylim = [-4, 10])

graph(Results, "Abduction", "HHT", "Translations inférieures-supérieures", cases_on="all", composante_y=["IS"])
graph(Results_Literature["Translation"], "Abduction", "Translation", "Superior displacement", cases_on="all", composante_y=["IS"], add_graph=True, ylim = [-4, 10])

graph(Results, "Abduction", "HHT", "Translations medio-laterales", cases_on="all", composante_y=["ML"])
graph(Results_Literature["Translation"], "Abduction", "Translation", "Medial displacement", cases_on="all", composante_y=["ML"], add_graph=True, ylim = [-4, 10])

# #Comparaison des bras de levier
PremadeGraphs.muscle_graph_from_list(Results,  Muscles_Main, [3, 3], "Abduction", "MomentArm", "Muscles principaux : Bras de levier des muscles", cases_on="all", composante_y=["Mean"])
PremadeGraphs.muscle_graph_from_list(Results_Literature["BL"], Muscle_Comp_Main, [3, 3], "Abduction", "Moment arm", "Muscles principaux : Bras de levier des muscles", cases_on="all", composante_y=["Total"], add_graph=True)

PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "MomentArm", "Muscles auxiliaires : Bras de levier des muscles", cases_on="all", composante_y=["Mean"])
PremadeGraphs.muscle_graph_from_list(Results_Literature["BL"], Muscle_Comp_Aux, [3, 3], "Abduction", "Moment arm", "Muscles principaux : Bras de levier des muscles", cases_on="all", composante_y=["Total"], add_graph=True)

# # #Forces musculaire actives
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Main, [3, 3], "Abduction", "Fm", "Muscles principaux : Forces actives des muscles", cases_on="all", composante_y=["Total"], hide_center_axis_labels=True)
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Fm", "Muscles auxiliaires : Forces actives des muscles", cases_on="all", composante_y=["Total"], hide_center_axis_labels=True)

# #Forces musculaire passives
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Main, [3, 3], "Abduction", "Fp", "Muscles principaux : Forces pasives des muscles", cases_on="all", composante_y=["Total"], hide_center_axis_labels=True)
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Fp", "Muscles auxiliaires : Forces passives des muscles", cases_on="all", composante_y=["Total"], hide_center_axis_labels=True)

# #Forces musculaire total
PremadeGraphs.muscle_graph_from_list(Results, Muscles_Main, [3, 3], "Abduction", "Ft","Muscles principaux : Forces des muscles total", cases_on="all", composante_y=["Total"],hide_center_axis_labels=True)
PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Ft", "Muscles auxiliaires : Forces des muscles total", cases_on="all", composante_y=["Total"], hide_center_axis_labels=True, same_lim=True)

#Contribution musculaires IS
graph(Results, "Abduction", "Ctb infra", "Muscles contribution IS", cases_on="all", composante_y=["IS"], subplot={"dimension": [2, 3], "number": 1}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb supra", "Muscles contribution IS", cases_on="all", composante_y=["IS"], subplot={"dimension": [2, 3], "number": 2}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb subscap", "Muscles contribution IS", cases_on="all", composante_y=["IS"], subplot={"dimension": [2, 3], "number": 3}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_ant", "Muscles contribution IS", cases_on="all", composante_y=["IS"], subplot={"dimension": [2, 3], "number": 4}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_lat", "Muscles contribution IS", cases_on="all", composante_y=["IS"], subplot={"dimension": [2, 3], "number": 5}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_post", "Muscles contribution IS", cases_on="all", composante_y=["IS"], subplot={"dimension": [2, 3], "number": 6}, figsize=[20, 10])

#Contribution musculaires AP
graph(Results, "Abduction", "Ctb infra", "Muscles contribution AP", cases_on="all", composante_y=["AP"], subplot={"dimension": [2, 3], "number": 1}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb supra", "Muscles contribution AP", cases_on="all", composante_y=["AP"], subplot={"dimension": [2, 3], "number": 2}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb subscap", "Muscles contribution AP", cases_on="all", composante_y=["AP"], subplot={"dimension": [2, 3], "number": 3}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_ant", "Muscles contribution AP", cases_on="all", composante_y=["AP"], subplot={"dimension": [2, 3], "number": 4}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_lat", "Muscles contribution AP", cases_on="all", composante_y=["AP"], subplot={"dimension": [2, 3], "number": 5}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_post", "Muscles contribution AP", cases_on="all", composante_y=["AP"], subplot={"dimension": [2, 3], "number": 6}, figsize=[20, 10])

#Contribution musculaires ML
graph(Results, "Abduction", "Ctb infra", "Muscles contribution ML", cases_on="all", composante_y=["ML"], subplot={"dimension": [2, 3], "number": 1}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb supra", "Muscles contribution ML", cases_on="all", composante_y=["ML"], subplot={"dimension": [2, 3], "number": 2}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb subscap", "Muscles contribution ML", cases_on="all", composante_y=["ML"], subplot={"dimension": [2, 3], "number": 3}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_ant", "Muscles contribution ML", cases_on="all", composante_y=["ML"], subplot={"dimension": [2, 3], "number": 4}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_lat", "Muscles contribution ML", cases_on="all", composante_y=["ML"], subplot={"dimension": [2, 3], "number": 5}, figsize=[20, 10])
graph(Results, "Abduction", "Ctb delt_post", "Muscles contribution ML", cases_on="all", composante_y=["ML"], subplot={"dimension": [2, 3], "number": 6}, figsize=[20, 10])

"""Script pour les graphiques"""

from Anybody_Package.Anybody_Graph.GraphFunctions import ForceMeasure_bar_plot

muscle_list = ["Deltoid anterior", "Deltoid lateral", "Biceps long head", "Deltoid posterior", "Supraspinatus", "Infraspinatus", "Subscapularis", "Others"]
for composante in ["AP", "IS", "ML"]: 
    
    ForceMeasure_bar_plot(Results,"ForceMeasure", "", muscle_list, data_index=0, composante=composante, cases_on="all", stacked=False, figsize=[10, 20], subplot={"dimension": [4, 1], "number": 1}, subplot_title="10° abduction",ylim = [-35, 125])
    ForceMeasure_bar_plot(Results, "ForceMeasure", "", muscle_list, data_index=30, composante=composante, cases_on="all", stacked=False, figsize=[10, 20], subplot={"dimension": [4, 1], "number": 2}, subplot_title="50° abduction",ylim = [-35, 125])
    ForceMeasure_bar_plot(Results, "ForceMeasure", "", muscle_list, data_index=46, composante=composante, cases_on="all", stacked=False, figsize=[10, 30], subplot={"dimension": [4, 1], "number": 3}, subplot_title="90° abduction",ylim = [-35, 125])
    #ForceMeasure_bar_plot(Results, f"Forces {composante}", muscle_list, data_index=69, composante=composante, cases_on="all", stacked=False, figsize=[10, 30], subplot={"dimension": [3, 1], "number": 3}, subplot_title="130° abduction", legend_position="center left")
    ForceMeasure_bar_plot(Results, "ForceMeasure", f"Compression forces", muscle_list, data_index=69, composante=composante, cases_on="all", stacked=False, figsize=[10, 30], subplot={"dimension": [4, 1], "number": 4}, subplot_title="130° abduction", legend_position="center left",ylim = [-35, 125])
    
    ForceMeasure_bar_plot(Results,"MomentMeasure", "", muscle_list, data_index=0, composante=composante, cases_on="all", stacked=False, figsize=[10, 20], subplot={"dimension": [4, 1], "number": 1}, subplot_title="10° abduction",ylim = [-35, 125])
    ForceMeasure_bar_plot(Results, "MomentMeasure", "", muscle_list, data_index=30, composante=composante, cases_on="all", stacked=False, figsize=[10, 20], subplot={"dimension": [4, 1], "number": 2}, subplot_title="50° abduction",ylim = [-35, 125])
    ForceMeasure_bar_plot(Results, "MomentMeasure", "", muscle_list, data_index=46, composante=composante, cases_on="all", stacked=False, figsize=[10, 30], subplot={"dimension": [4, 1], "number": 3}, subplot_title="90° abduction",ylim = [-35, 125])
    #ForceMeasure_bar_plot(Results, f"Forces {composante}", muscle_list, data_index=69, composante=composante, cases_on="all", stacked=False, figsize=[10, 30], subplot={"dimension": [3, 1], "number": 3}, subplot_title="130° abduction", legend_position="center left")
    ForceMeasure_bar_plot(Results, "MomentMeasure", f"Compression forces", muscle_list, data_index=69, composante=composante, cases_on="all", stacked=False, figsize=[10, 30], subplot={"dimension": [4, 1], "number": 4}, subplot_title="130° abduction", legend_position="center left",ylim = [-35, 125])


ForceMeasure_bar_plot_direction(Results, "ForceMeasure", "", muscle_list, data_index=0, cases_on="all", figsize=[30, 10])
ForceMeasure_bar_plot_direction(Results, "ForceMeasure","", muscle_list, data_index=30, cases_on="all", figsize=[30, 10])
ForceMeasure_bar_plot_direction(Results, "ForceMeasure","", muscle_list, data_index=46, cases_on="all", figsize=[30, 10])
# ForceMeasure_bar_plot(Results, "ForceMeasure",f"Forces {composante}", muscle_list, data_index=69, composante=composante, cases_on="all", stacked=False, figsize=[10, 30], subplot={"dimension": [3, 1], "number": 3}, subplot_title="130° abduction", legend_position="center left")
ForceMeasure_bar_plot_direction(Results,"ForceMeasure", f"Compression forces", muscle_list, data_index=69, cases_on="all", figsize=[30, 10], stacked=False, legend_position="center left")

#total_force_AP = (Results[case]["ForceMeasure Infraspinatus"]["AP"])+(Results[case]["ForceMeasure Supraspinatus"]["AP"])+(Results[case]["ForceMeasure Subscapularis"]["AP"])+(Results[case]["ForceMeasure Deltoid anterior"]["AP"])+(Results[case]["ForceMeasure Deltoid posterior"]["AP"])+(Results[case]["ForceMeasure Deltoid lateral"]["AP"])


#Forces surfaces
# PremadeGraphs.graph_all_muscle_fibers(Results, muscle_surface, "Abduction", "F surface", combined_muscle_on=False, cases_on="all", composante_y_muscle_part=["AP"])
# PremadeGraphs.graph_all_muscle_fibers(Results, muscle_surface, "Abduction", "F surface", combined_muscle_on=False, cases_on="all", composante_y_muscle_part=["IS"])
# PremadeGraphs.graph_all_muscle_fibers(Results, muscle_surface, "Abduction", "F surface", combined_muscle_on=False, cases_on="all", composante_y_muscle_part=["ML"])

#Forces multi surfaces
# PremadeGraphs.graph_all_muscle_fibers(Results, muscle_multisurface, "Abduction", "F surface", combined_muscle_on=False, cases_on="all", composante_y_muscle_part=["AP"])
# PremadeGraphs.graph_all_muscle_fibers(Results, muscle_multisurface, "Abduction", "F surface", combined_muscle_on=False, cases_on="all", composante_y_muscle_part=["IS"])
# PremadeGraphs.graph_all_muscle_fibers(Results, muscle_multisurface, "Abduction", "F surface", combined_muscle_on=False, cases_on="all", composante_y_muscle_part=["ML"])

#Activité musculaire
# PremadeGraphs.muscle_graph_from_list(Results,  Muscles_Main, [3, 3], "Abduction", "Activity", "Muscles principaux : activité musculire", cases_on="all", composante_y=["Mean"], hide_center_axis_labels=True)
# PremadeGraphs.muscle_graph_from_list(Results, Muscles_Aux, [3, 3], "Abduction", "Activity", "Muscles auxiliaires : activité musculire", cases_on="all", composante_y=["Mean"], hide_center_axis_labels=True)

#Force de reaction dans le chainon_amplitude
# graph(Results, "Abduction", "ResultanteForce_amplitude", "Amplitude de la force de Reaction (N)", cases_on="all")

#Force de reaction compression et cisaillement
# graph(Results, "Abduction", "Force_cisaillement", "Shear forces in the anterior direction", cases_on="all", composante_y=["AP"]])
# graph(Results, "Abduction", "Force_cisaillement", "Shear forces in the superior direction", cases_on="all", composante_y=["IS"])
# graph(Results, "Abduction", "Force_compression", "Superior forces", cases_on="all", composante_y=["ML"])

#Instability Ratio
graph(Results, "Abduction", "Instability Ratio", "Instability Ratio", cases_on="all", composante_y=["Total"])

# # Obtenir les axes des graphiques
# axes = plt.gcf().get_axes()

# # Masquer les noms des axes sur les graphiques non souhaités
# for i, ax in enumerate(axes):
#     if i % 3 == 0:  # Colonnes de gauche
#         ax.set_xlabel('Votre xlabel')
#     if i >= 6:  # Lignes du bas
#         ax.set_ylabel('Votre ylabel')
    # ax.tick_params(axis='both', which='both', length=0, width=0)
