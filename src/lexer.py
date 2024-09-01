# Import re Python Package For Handling Expressions
import re

class Lexer(object):
    def __init__(self, code):
        self.code = code

    def tokenize(self):
        token = []

        # Split code into tokens using regex to handle all possible tokens
        code = re.findall(r'\w+|[=+*/-]|".*?"|\'.*?\'|;', self.code)

        index = 0

        while index < len(code):
            words = code[index]

            # Check for strings
            if re.match(r'^".*"$|^\'.*\'$', words):
                token.append(['String', words[1:-1]])

            # Check for DataType keywords
            elif words == "en" or words == "eluthu":
                token.append(['DataType', words])

            # Check for Syntax keywords
            elif words == "sollu" or words == "kelu":
                token.append(['Syntax', words])

            # Check for Variables (alphabetic sequences)
            elif re.match('^[a-zA-Z]+$', words):
                token.append(['Variable', words])

            # Check for Numbers
            elif re.match('^[0-9]+$', words):
                token.append(['Number', words])

            # Check for Operators
            elif words in "+-=/*":
                token.append(['Operator', words])

            # Check for End of Statement
            elif words == ';':
                token.append(['EndOfStatement', words])

            index += 1

        return token
