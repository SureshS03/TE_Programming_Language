class Functions(object):

    def __init__(self,code):
        self.code = code
        self.String = ""
    
    def Func_checker(self ,code):

        for i,j in code:
            if j == 'matti_podu':
                output = self.matti_podu(code)
                return output

            elif j == 'piri':
                output = self.piri(code)
                return output
                #print('Function is working')
        
        
    def matti_podu(self , code):

        string = code[4][1]
        #print(string)
        string = ''.join(reversed(string))
        return string
        #print(string)

    def piri(self , code):
        pass