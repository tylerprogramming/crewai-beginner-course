from langchain_community.tools import tool


@tool("Calculate")
def calculate(equation):
    """ Useful for solving math equations """

    return eval(equation)