#import Anybody_LoadOutput.LoadOutput as LoadOutput
#import Anybody_Tools as LoadOutputTools

from Anybody_Package.Anybody_LoadOutput.LoadOutput import define_variables_to_load
from Anybody_Package.Anybody_LoadOutput.LoadOutput import load_simulation_cases
from Anybody_Package.Anybody_LoadOutput.LoadOutput import load_simulation
from Anybody_Package.Anybody_LoadOutput.LoadOutput import create_compared_simulations

from Anybody_Package.Anybody_LoadOutput.Tools import save_results_to_file
from Anybody_Package.Anybody_LoadOutput.Tools import array_to_dictionary

from Anybody_Package.Anybody_LoadOutput.LoadLiterature import load_literature_data
from Anybody_Package.Anybody_LoadOutput.LoadOutput import combine_simulation_cases

import numpy as np

import pandas as pd

# %% Setup des variables à charger

# Muscles
MuscleDictionary = {"Deltoideus lateral": ["deltoideus_lateral", "_part_", [1, 4]],
                    "Deltoideus posterior": ["deltoideus_posterior", "_part_", [1, 4]],
                    "Deltoideus anterior": ["deltoideus_anterior", "_part_", [1, 4]],
                    "Supraspinatus": ["supraspinatus", "_", [1, 6]],
                    "Infraspinatus": ["infraspinatus", "_", [1, 6]],
                    "Serratus anterior": ["serratus_anterior", "_", [1, 6]],
                    "Lower trapezius": ["trapezius_scapular", "_part_", [1, 3]],
                    "Middle trapezius": ["trapezius_scapular", "_part_", [4, 6]],
                    "Upper trapezius": ["trapezius_clavicular", "_part_", [1, 6]],
                    "Biceps brachii long head": ["biceps_brachii_caput_longum", "", []],
                    "Biceps brachii short head": ["biceps_brachii_caput_breve", "", []],
                    "Pectoralis major clavicular": ["pectoralis_major_clavicular", "_part_", [1, 5]],
                    "Pectoralis major sternal": ["pectoralis_major_thoracic", "_part_", [1, 10]],

                    "Pectoralis major": [["pectoralis_major_thoracic", "_part_", [1, 10]],
                                         ["pectoralis_major_clavicular", "_part_", [1, 5]]
                                         ],

                    "Pectoralis minor": ["pectoralis_minor", "_", [1, 4]],
                    "Latissimus dorsi": ["latissimus_dorsi", "_", [1, 11]],
                    "Triceps long head": ["Triceps_LH", "_", [1, 2]],
                    "Upper Subscapularis": ["subscapularis", "_", [1, 2]],
                    "Downward Subscapularis": ["subscapularis", "_", [3, 6]],
                    "Subscapularis": ["subscapularis", "_", [1, 6]],
                    "Teres minor": ["teres_minor", "_", [1, 6]],
                    "Teres major": ["teres_major", "_", [1, 6]],
                    "Rhomboideus": ["rhomboideus", "_", [1, 3]],
                    "Levator scapulae": ["levator_scapulae", "_", [1, 4]],
                    "Sternocleidomastoid clavicular": ["Sternocleidomastoid_caput_clavicular", "", []],
                    "Sternocleidomastoid sternum": ["Sternocleidomastoid_caput_Sternum", "", []],
                    "Coracobrachialis": ["coracobrachialis", "_", [1, 6]]
                    }

MuscleVariableDictionary = {"Fm": {"MuscleFolderPath": "Output.Mus", "AnybodyVariableName": "Fm", "VariableDescription": "Force musculaire [Newton]"},
                            "Ft": {"MuscleFolderPath": "Output.Mus", "AnybodyVariableName": "Ft", "VariableDescription": "Muscles forces [Newton]"},
                            "Fp": {"MuscleFolderPath": "Output.Mus", "AnybodyVariableName": "Fp", "VariableDescription": "Force musculaire passive [Newton]"},
                            "Activity": {"MuscleFolderPath": "Output.Mus", "AnybodyVariableName": "CorrectedActivity", "VariableDescription": "Activité Musculaire [%]", "MultiplyFactor": 100, "combine_muscle_part_operations": ["max", "mean"]},

                            "F origin": {"MuscleFolderPath": "Output.Mus", "AnybodyVariableName": "RefFrameOutput.F", "VariableDescription": "Force Musculaire à l'origine du muscle [N]", "select_matrix_line": 0,
                                          "rotation_matrix_path": "Output.Seg.Scapula.AnatomicalFrame.ISB_Coord.Axes", "inverse_rotation": True, "SequenceComposantes": ["AP", "IS", "ML"],
                                          "combine_muscle_part_operations": ["total", "mean"]},

                            "F insertion": {"MuscleFolderPath": "Output.Mus", "AnybodyVariableName": "RefFrameOutput.F", "VariableDescription": "Force Musculaire à l'insertion du muscle [N]", "select_matrix_line": 1,
                                            "rotation_matrix_path": "Output.Seg.Scapula.AnatomicalFrame.ISB_Coord.Axes", "inverse_rotation": True, "SequenceComposantes": ["AP", "IS", "ML"],
                                            "combine_muscle_part_operations": ["total", "mean"]},

                            "MomentArm": {"MuscleFolderPath": "Output.Mus", "AnybodyVariableName": "MomentArm", "VariableDescription": "Moment arms [mm]",
                                              "combine_muscle_part_operations": ["mean"], "MultiplyFactor": 1000}
                            }

# Variables
VariableDictionary = {"Abduction": {"VariablePath": "Output.JointAngleAbd", "VariableDescription": "Abduction angle [°]"},
                      "Flexion": {"VariablePath": "Output.JointAngleFlx", "VariableDescription": "Flexion angle [°]"},
                      "Temps": {"VariablePath": "Output.Abscissa.t", "VariableDescription": "Flexion temps [s]"},
                      "HHT": {"VariablePath": "Output.Jnt.HHT.Pos", "VariableDescription": "Humeral head displacement [mm]", "MultiplyFactor": 1000, "SequenceComposantes": ["AP", "IS", "ML"]},
                       "ResultanteForce_amplitude": {"VariablePath": "Output.Model.BodyModel.Right.ShoulderArm.Jnt.GH_contact.Reaction.Fout", "VariableDescription": "Force de reaction [Newton]", "MultiplyFactor": -1},
                       "Force_compression": {"VariablePath": "Output.HumReacForce.Val", "VariableDescription": "Compression forces [Newton]", "SequenceComposantes": ["AP", "IS", "ML"], "MultiplyFactor": -1},
                       "Force_cisaillement": {"VariablePath": "Output.HumReacForce.Val", "VariableDescription": "Shear forces [Newton]", "SequenceComposantes": ["AP", "IS", "ML"]}
                      #"ResultanteForce_BS": {"VariablePath": "Output.Model.BodyModel.Right.ShoulderArm.Jnt.GHReactions.ResultanForce.FTotalGlobal", "VariableDescription": "Force de reaction [Newton]","MultiplyFactor": -1, "SequenceComposantes": ["ML", "IS", "AP"]},
                      }


# Constantes (si un fichier AnyFileOut contenant des constantes est créé en même temps que le fichier h5)
# Constantes
ConstantsDictionary = {"AnybodyFileOutPath": "Main.Study.FileOut",  # CHEMIN D'ACCÈS ANYBODY DE L'OBJET AnyFileOut
                       "Paramètres de simulation": ["Case", "MuscleRecruitment", "nStep", "tEnd", "GHReactions", "Movement"],
                       "Mannequin": ["GlenohumeralFlexion", "GlenohumeralAbduction", "GlenohumeralExternalRotation"]
                       }


Variables = define_variables_to_load(VariableDictionary, MuscleDictionary, MuscleVariableDictionary, ConstantsDictionary)


# %% Chargement des fichiers .h5

"""Chemin d'accès au dossier où sont sauvegardes les fichiers h5"""
SaveDataDir = "Saved Simulations"

# Chemin d'accès au dossier dans lequel les fichiers doivent être sauvegardés
SaveSimulationsDirectory = "Saved Simulations"

# Nom des fichiers .h5 (sans l'extension anydata.h5)
Files = [
         # "B&S_0Kg",
         "supra_-20mm",
         "supra_-10mm",
         "supra_0mm",
         "supra_10mm",
         "supra_20mm"
        

         ]

# Noms des simulations
CaseNames = ["supra_-20mm",
             "supra_-10mm",
             "supra_0mm",
             "supra_10mm",
             "supra_20mm"
             
          
             ]

Results = load_simulation_cases(SaveDataDir, Files, CaseNames, Variables)

# Sauvegarde des résultats dans des fichiers .pkl
save_results_to_file(Results, SaveSimulationsDirectory, "Results")

# %% Sauvegarde des dictionnaires de variables

# # Chemin d'accès au dossier dans lequel les fichiers doivent être sauvegardés
SaveVariablesDirectory = "Saved VariablesDictionary"

save_results_to_file(Variables, SaveVariablesDirectory, "Variables")

# %% Chargement du fichier excel de littérature

# Informations about the excel file
file_name = "Data_HHT_invivo"
directory_path = "C:\Anybody_projet"


# Loads the excel
Results_Literature = load_literature_data(file_name, directory_path)

# Saves it to a .pkl file
save_results_to_file(Results_Literature, SaveSimulationsDirectory, "Results_Literature")





