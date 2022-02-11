# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:42:01 2022

@author: StillScripts
"""

common = '''import { useReducer } from "react";
import Context, { Action, State } from "./context";

const defaultState: State = {
  data: { title: "hello world " },
};

const reducer = (state: State, action: Action) => {
  switch (action.type) {
    case "submit":
      console.log("submit");
      return {
        ...state,
      };
    case "update":
      console.log(action.payload);
      return {
        ...state,
      };
    default:
      throw new Error();
  }
};

'''

common_2 = '''({ children }) => {
  const [state, dispatch] = useReducer(reducer, defaultState);

  const { data } = state;

  return (
    <Context.Provider value={{ data, dispatch }}>{children}</Context.Provider>
  );
};

'''

def get_template(file_name):
    template = common
    template += f'const {file_name}Provider: React.FC = ('
    template += common_2
    template += f'export default {file_name}Provider;\n'
    return template