# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:57:05 2022

@author: StillScripts
"""

common = '''import React from "react";

export interface State {
  data: Record<string, any>;
}

export type Action =
  | { type: "submit"; payload: undefined }
  | { type: "update"; payload: Record<string, any> };

export interface ProviderValues extends State {
  dispatch: React.Dispatch<Action>;
}

'''



def get_template(file_name):
    template = common
    template += f'const {file_name}Context = React.createContext<Partial<ProviderValues>>('
    template += '{});\n\n'
    template += f'export default {file_name}Context;\n'
    return template
    