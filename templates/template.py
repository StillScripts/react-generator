# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:38:08 2022

@author: danie
"""

common = '''{
	return (
		<div>
			<header>navbar</header>
			<main>page content</main>
			<footer>footer</footer>
		</div>
	);
};

'''

def get_template(file_name):
    template = f'export interface {file_name}Props'
    template += ' {}\n\n'
    template += f'const {file_name}: React.FC<{file_name}Props> = () =>'
    template += common
    template += f'export default {file_name};\n'
    return template