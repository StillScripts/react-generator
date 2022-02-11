# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:46:41 2022

@author: StillScripts
"""

common = '''{
  return (
    <div>
      <Head>
        <title>My Page | Website</title>
        <meta name="description" content="This is a web page" />
      </Head>
      <div>content...</div>
    </div>
  );
};

'''

def get_template(file_name):
    template = 'import Head from "next/head";\n\n'
    template += f'const {file_name}Page: React.FC = () => \n'
    template += common
    template += f'export default {file_name}Page;\n'
    return template