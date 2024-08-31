import sys
import os
import lexer
import parser
import translater

def main():

    welcome = "Welcome to TE programming language"
    terminal_width = os.get_terminal_size().columns
    text = welcome.center(terminal_width)
    print(text)
    for i in range(terminal_width):
        print("-", end="")


    if len(sys.argv) != 2:
        print("Usage: TE filename.TE")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".TE"):
        print("Error: File must have a .TE extension")
        sys.exit(1)


    try:
        #print(filename)
        with open(filename, 'r') as file:

            # reading the file (test.TE)
            content = file.read()

        # give the file to lexer for asgining it as code
        lex = lexer.Lexer(content)

        # call tokenize function
        token = lex.tokenize()

        parse = parser.Parser(token)
        asset = parse.parse()

        ts = translater.Translater(asset)
        trans = ts.Spliter()
    
    except FileNotFoundError:
        print("Here")
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

if __name__ == '__main__':
    main()