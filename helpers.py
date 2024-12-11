from IPython.display import Markdown, display

def printmd(string):
    """
    Display the given text as Markdown.

    :param string(str): The markdown-formatted string to be
    displayed
    """
    display(Markdown(string))
