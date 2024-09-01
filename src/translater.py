import os
class Translater(object):

    def __init__(self, token):
        self.token = token
        self.String = ""
    
    def file_write(self, line):
        with open("py_src_code.py", "a") as file:
            file.write(line)
            file.write("\n")

    def Spliter(self):
        
        for index in self.token:
            
            if index[0][0] == "DataType":
                self.DataType_trans(index)
            elif index[0][0] == "Syntax":
                self.Syntax_trans(index)
        with open('py_src_code.py', 'r') as file:
            codes = file.read()

        try:
            exec(codes)
            os.remove("py_src_code.py")
        except Exception as e:
            if e == KeyboardInterrupt:
                print("Program Interrupted")
                os.remove("py_src_code.py")
            print(f"Error in the code , {e}")
            os.remove("py_src_code.py")

            
    def DataType_trans(self, code):

        if code[0][1] == "en":
            
            index = len(code)
            for i in range(1, index):
                self.String += code[i][1]
            self.file_write(self.String)
            self.String = ""
        elif code[0][1] == "eluthu":
            self.String += code[1][1] + code[2][1] + "'"+code[3][1]+"'"
            self.file_write(self.String)
            self.String = ""
            

    def Syntax_trans(self, code):

        if code[0][1] == "sollu":

            if code[1][0] == "String":
                self.String += "print(" + "'" + code[1][1] + "'" + ")"
            else:
                self.String += "print(" + code[1][1] + ")"
            self.file_write(self.String)
            self.String = ""
        elif code[0][1] == "kelu":
            if len(code) < 3:
                self.String += code[1][1] + "=" + "input()"
            elif code[1][0] == "DataType":
                try:
                    if len(code) < 5:
                        self.String += code[2][1] + "=" + "int(input(" + "'" + code[3][1] + "'" + "))"
                except:
                    self.String += code[2][1] + "=" + "int(input())"
            elif len(code) < 4:    
                self.String += code[1][1] + "=" + "input(" + "'" + code[2][1] + "'" + ")"
            self.file_write(self.String)
            self.String = ""

        

