import os      # OS operations


class Color:
    """Just add colors for strings.
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class TxtLayout:
    """Just like the name says, print a text if premaded design
    """

    def __init__(self, text):
        self.text = text

    def header(self):
        print(
            Color.BOLD, Color.GREEN, "[>>] ", Color.END,
            Color.BOLD, self.text,
            Color.END, sep="", end="\n"
        )

    def error(self):
        print(
            Color.BOLD, Color.RED,
            "[!] ", self.text,
            Color.END, sep=""
        )


def clear():
    """ Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')  # clear multiplataform


def input_error(user_input):
    """Display a error message that the user input are not valid.

    Args:
        user_input (str): input of user
    """

    error_msg = TxtLayout(
        f"A opção '{user_input}' não é válida!")
    error_msg.error()
    input("Pressione Enter para continuar.")


def session_header(title):
    session_title = TxtLayout(title)
    session_title.header()
    
def empty_error(text):
     print(Color.RED,Color.BOLD,
                    f"Campo {text} está vazio. ",
                    Color.END,sep="")
