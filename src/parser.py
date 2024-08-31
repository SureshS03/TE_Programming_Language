class Parser(object):

    def __init__(self,token):
        self.token = token


    def parse(self):

        breaked_line = []
        result = []

        for i in self.token:
            checker = i
            if checker[0] != "EndOfStatement":
                breaked_line.append(checker)

            else:
                self.line_checker(breaked_line)
                result.append(breaked_line)
                breaked_line = []
        
        return result
                        
    def line_checker(self, code):
        token_format = code[0][0]
        if token_format == "DataType":
            self.syntax_checker_DataType(code)
        elif token_format == "Syntax":
            self.syntax_checker_syntax(code)
        else :
            print("ERROR Invalid Code At Front")

    def syntax_checker_DataType(self, token_data):

        if token_data[0][0] == "DataType" and token_data[0][1] == "en":

            if token_data[1][0] != "Variable":
                print("ERROR :- Invalid Data Variable -->" + token_data[1][1])
                exit()
            elif token_data[2][0] != "Operator" or token_data[2][1] != "=":
                print("ERROR :- Invalid Operation -->" + token_data[2][1])
                exit()


        elif token_data[0][0] == "DataType" and token_data[0][1] == "eluthu":

            if token_data[1][0] != "Variable":
                print("ERROR :- Invalid Data Variable -->" + token_data[1][1])
                exit()
            elif token_data[2][0] != "Operator" or token_data[2][1] != "=":
                print("ERROR :- Invalid Operation -->" + token_data[2][1])
                exit()
            elif token_data[3][0] != "String":
                print("ERROR :- Invalid Data Value -->" + token_data[3][1] +", (eluthu only use String)" )
                exit()
            if len(token_data) > 4:
                print("ERROR :- Invalid Code At Last")
                exit()
                    
    def syntax_checker_syntax(self, token_data):

        if token_data[0][0] == "Syntax" and token_data[0][1] == "sollu":

            if token_data[1][0] != "String":
                if token_data[1][0] != "Variable":
                    print("ERROR :- Invalid Syntax -->" + token_data[1][1])
                    exit()
            elif token_data[1][0] == "":
                print("ERROR :- UnDeclared Variable -->" + token_data[1][1])
                exit()
            if len(token_data) > 2:
                print("ERROR :- Invalid Code At Last")
                exit()
        
        
        elif token_data[0][0] == "Syntax" and token_data[0][1] == "kelu":

            if token_data[1][0] != "Variable" and token_data[1][0] != "DataType":
                print("ERROR :- Invalid Syntax Variable " + token_data[1][1])
                exit()
            elif token_data[1][0] == "":
                print("ERROR :- UnDeclared Variable " + token_data[1][1])
                exit()
            try:
                if token_data[2][0] != "String" and token_data[2][0] != "Variable":
                    print("here")
                    print("ERROR :- Invalid Syntax " + token_data[2][1])
                    exit()
            except:
                pass
            if len(token_data) > 4:
                print("here is")
                print("ERROR :- Invalid Code At Last")
                exit()
    