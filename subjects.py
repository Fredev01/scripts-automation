""" 
This module is for making a list of folders for my subjects.
"""
import os
# from pathlib import Path

root: str = '/home/angel/Escritorio'
cuatrimestre: str = 'quinto_cuatri'
path: str = os.path.join(root, cuatrimestre)
subjects: list = [
    'APLICACIONES_DE_IoT',
    'DESARROLLO_MÓVIL_MULTIPLATAFORMA',
    'INTEGRADORA_II',
    'APLICACIONES_WEB_PARA_I4.0',
    'Cloud_Database',
    'EXPRESIÓN_ORAL_ESCRITA_II',
    'Ingles_V'
]

folders:str = [
    'Files_pdf',
    'Files_word',
    'Files_powerpoint',
    'Imagenes'
]
unidades: list = [
    'Unit_1',
    'Unit_2',
    'Unit_3'
]
os.mkdir(path)
try:
    for subject in subjects:
        new_path = os.path.join(path, subject)
        os.mkdir(new_path)
        # print(new_path)
        for unit in unidades:
            child_path = os.path.join(new_path, unit)
            os.mkdir(child_path)
            for folder in folders:
                path_file = os.path.join(child_path, folder)
                # print(path_file)
                os.mkdir(path_file)
            # print(child_path)

except Exception as e:
    print(f"ocurrio un error {e}")