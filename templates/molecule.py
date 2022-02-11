# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:27:42 2022

@author: stillScripts
"""

common = '''{
  heading: string;
  items: string[];
}

'''
common_2 = '''{ heading, items }) => {
  return (
    <div className="">
      <h2>{heading}</h2>
      {items.map((item, id) => (
        <div key={`${item}-${id}`}>{item}</div>
      ))}
    </div>
  );
};

'''

def get_template(file_name):
    template = f'export interface {file_name}Props '
    template += common
    template += f'const {file_name}: React.FC<{file_name}Props> = ('
    template += common_2
    template += f'export default {file_name};\n'
    return template
    