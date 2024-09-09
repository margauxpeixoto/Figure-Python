# -*- coding: utf-8 -*-

"""Scripts pour charger les variables (lignes à ajouter dans 'VariableDictionary')"""

"ForceMeasure Infraspinatus": {"VariablePath": "Output.Main.Model.ForceMeasure_infra.F", "VariableDescription": 'Force [N]', "SequenceComposantes": ["AP", "IS", "ML"]},
"ForceMeasure Supraspinatus": {"VariablePath": "Output.Main.Model.ForceMeasure_supra.F", "VariableDescription": 'Force [N]', "SequenceComposantes": ["AP", "IS", "ML"]},
"ForceMeasure Subscapularis": {"VariablePath": "Output.Main.Model.ForceMeasure_subscap.F", "VariableDescription": 'Force [N]', "SequenceComposantes": ["AP", "IS", "ML"]},
"ForceMeasure Deltoideus anterior": {"VariablePath": "Output.Main.Model.ForceMeasure_delt_ant.F", "VariableDescription": 'Force [N]', "SequenceComposantes": ["AP", "IS", "ML"]},
"ForceMeasure Deltoideus posterior": {"VariablePath": "Output.Main.Model.ForceMeasure_delt_post.F", "VariableDescription": 'Force [N]', "SequenceComposantes": ["AP", "IS", "ML"]},
"ForceMeasure Deltoideus lateral": {"VariablePath": "Output.Main.Model.ForceMeasure_delt_lat.F", "VariableDescription": 'Force [N]', "SequenceComposantes": ["AP", "IS", "ML"]},


"""Script pour les graphiques"""

from Anybody_Package.Anybody_Graph.GraphFunctions import ForceMeasure_bar_plot

muscle_list = ["Deltoideus anterior", "Deltoideus lateral", "Deltoideus posterior", "Supraspinatus", "Infraspinatus"]
for composante in ["AP", "IS", "ML"]:
    
    ForceMeasure_bar_plot(Results, "", muscle_list, data_index=0, composante=composante, cases_on="all", stacked=False, figsize=[15, 20], subplot={"dimension": [3, 1], "number": 1}, subplot_title="15° abduction")
    ForceMeasure_bar_plot(Results, "", muscle_list, data_index=49, composante=composante, cases_on="all", stacked=False, figsize=[15, 30], subplot={"dimension": [3, 1], "number": 2}, subplot_title="90° abduction")
    ForceMeasure_bar_plot(Results, f"Forces {composante}", muscle_list, abduction_angle_index=69, composante=composante, cases_on="all", stacked=False, figsize=[15, 30], subplot={"dimension": [3, 1], "number": 3}, subplot_title="120° abduction", legend_position="center-left")
