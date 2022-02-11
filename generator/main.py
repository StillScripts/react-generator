# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:42:03 2022

@author: StillScripts

"""

'''
    Call a function which generates react files 
    based on the parameters.
'''

from file_write import write
from folder_check import check
from templates.file_types import Files
from templates.main import get_template

def generate_file(file_type, file_path, file_name):
    # Create custom file_path and file_name
    extension = ".ts"
    if not file_type == Files.CONTEXT:
        extension += "x"
    file_path += f"{file_name}"
    completed_file_name = f'{file_name}{extension}'
    
    # Create the folder for the specific 
    check.check_or_make(file_path)
    
    # Create the file
    write.create_file(
        f"{file_path}/{completed_file_name}", 
       get_template(file_type, file_name)
    )
    
    # Create the provider file if making context
    if (file_type == Files.CONTEXT):
        write.create_file(
            f"{file_path}/{file_name}Provider.tsx", 
            get_template(Files.PROVIDER, file_name)
        )
    
    # Add an index export file for components
    if file_type in (Files.ATOM, Files.MOLECULE, Files.TEMPLATE, Files.PAGE):
        write.create_file(f"{file_path}/index.ts", 'export { default } from ' + f'"./{file_name}";')
    
def generator(file_type, file_names):
    path = ""
    if file_type == Files.PAGE:
        path += "pages/"
        check.check_or_make(path) # make page folder
    else:
        path += "src/"
        check.check_or_make(path) # make src directory
        if file_type in (Files.ATOM, Files.MOLECULE):
            path += "components/"
            check.check_or_make(path) # make components directory
            if file_type == Files.ATOM:
                path += "atoms/"
            else:
                path += "molecules/"
        elif file_type == Files.TEMPLATE:
            path += "templates/"
        elif file_type == Files.CONTEXT:
            path += "context/"
        check.check_or_make(path)
    export_script = ""
    for name in file_names:
        generate_file(file_type, path, name)
        export_script += "export { default as "
        export_script += f"{name}"
        export_script += ' } from "./'
        export_script += f'{name}";\n'
    if file_type not in (Files.PAGE, Files.CONTEXT):
        write.create_file(f'{path}index.ts', export_script)    
        
generator(Files.ATOM, ["Button", "PageLink", "Tab"])
