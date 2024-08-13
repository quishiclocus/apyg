""" Modules provide system print functions. """
import sys


class Phoenetic():
    """Phoenetic Class

    Attributes
    ----------
    Send the password in, get phoenetic printout back.
    """
    # Init

    def __init__(self):
        # Phoenetic Alphabet.
        self.phoenetics = {"A": "Alpha",
                           "B": "Bravo",
                           "C": "Charlie",
                           "D": "Delta",
                           "E": "Echo",
                           "F": "Foxtrot",
                           "G": "Golf",
                           "H": "Hotel",
                           "I": "India",
                           "J": "Juliett",
                           "K": "Kilo",
                           "L": "Lima",
                           "M": "Mike",
                           "N": "November",
                           "O": "Oscar",
                           "P": "Papa",
                           "Q": "Quebec",
                           "R": "Romeo",
                           "S": "Sierra",
                           "T": "Tango",
                           "U": "Uniform",
                           "V": "Victor",
                           "W": "Whiskey",
                           "X": "X-ray",
                           "Y": "Yankee",
                           "Z": "Zulu",
                           "a": "alpha",
                           "b": "bravo",
                           "c": "charlie",
                           "d": "delta",
                           "e": "echo",
                           "f": "foxtrot",
                           "g": "golf",
                           "h": "hotel",
                           "i": "india",
                           "j": "juliett",
                           "k": "kilo",
                           "l": "lima",
                           "m": "mike",
                           "n": "november",
                           "o": "oscar",
                           "p": "papa",
                           "q": "quebec",
                           "r": "romeo",
                           "s": "sierra",
                           "t": "tango",
                           "u": "uniform",
                           "v": "victor",
                           "w": "whiskey",
                           "x": "x-ray",
                           "y": "yankee",
                           "z": "zulu",
                           "1": "One",
                           "2": "Two",
                           "3": "Three",
                           "4": "Four",
                           "5": "Five",
                           "6": "Six",
                           "7": "Seven",
                           "8": "Eight",
                           "9": "Niner",
                           "0": "Zero",
                           "!": "Bang",
                           "\"": "Double-Quote",
                           "#": "Hash",
                           "$": "Dollar",
                           "%": "Percent",
                           "&": "Ampersand",
                           "'": "Single-Quote",
                           "(": "Open-Parentheses",
                           ")": "Close-Parentheses",
                           "*": "Asterisk",
                           "+": "Plus-Sign",
                           ",": "Comma",
                           "-": "Dash",
                           ".": "Dot",
                           "/": "Slash",
                           ":": "Colon",
                           ";": "Semicolon",
                           "=": "Equals-Sign",
                           "?": "Question-Mark",
                           "@": "At-Sign",
                           "[": "Open-Bracket",
                           "]": "Close-Bracket",
                           "^": "Carat",
                           "_": "Underscore",
                           "{": "Open-Curly-Bracket",
                           "}": "Close-Curly-Bracket"}

    # Phoenetic printing.
    def print_new_password_phoenetic(self, pword):
        """print_new_password_phoenetic

        Prints phoenetic spelling of generated password.
        """
        count = 0
        if pword:
            sys.stdout.write(" ")
        for j in pword:
            sys.stdout.write(self.phoenetics[j])
            if count < (len(pword) - 1):
                sys.stdout.write("_")
            count += 1

    def phoenetic_function(self):
        """phoenetic_function

        TBD in future.
        """
        return
