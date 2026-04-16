import os

def create_project_structure(project_name, files_dict):
    """
    files_dict: Un diccionario donde la clave es el nombre del archivo 
    y el valor es el código generado.
    """
    if not os.path.exists(project_name):
        os.makedirs(project_name)
    
    for file_path, content in files_dict.items():
        full_path = os.path.join(project_name, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
    
    return f"Proyecto {project_name} creado con éxito."
