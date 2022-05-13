#Grammar indicators
INT="INT"
PLUS="PLUS"
MINUS="MINUS"
MUL="MUL"
DIV="DIV"
LP="("
RP=")"
END="END"



"""
MYGRAMMAR:
?start: expr
expr: term | factor
term: LP expr+ RP | expr+
?factor: var | NUMBER
var: /["+"-"-"-"*"-"%"]/
LP: /["("]/
RP: /[")"]/
%import common.NUMBER
%import common.WS
%ignore WS
"""

def testing():
    #testing to replace an external file
    problems=[['(2+5)','7'], ['(9+9)','18'], ['(9%3)','3.0'], ['((9+9)*9)','162'], ['(9*(9+9))','162'], ['(((9+2)-((3*1))%(2*2)))','10.25'], ['(((((3+9)-2)*192234)%3)*2)','1281560.0']]
    for i in problems:
        while True:
            text = i[0]
            if text.isalpha():
                continue
            if not text:
                continue
            lexer = indicator(text)
            interpreter = grammar(lexer)
            result = interpreter.expr()
            result=str(result)
            if result == i[1]:
                b = "True"
            else:
                b = "False"
            print(text+' should equal '+result+'~~~'+b)
            break


class indicator(object):
    #initalize
    def __init__(self, eq):
        self.eq = eq
        self.pos = 0
        self.current_char = self.eq[self.pos]
    #move up an index
    def advance(self):
        self.pos += 1
        if self.pos > len(self.eq) - 1:
            self.current_char = None
        else:
            self.current_char = self.eq[self.pos]
    #basically the %ignore.WS
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    #checks for number
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    #gets the symbol at that location
    def findToken(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return token(INT, self.integer())
            elif self.current_char == '+':
                self.advance()
                return token(PLUS, '+')
            elif self.current_char == '-':
                self.advance()
                return token(MINUS, '-')
            elif self.current_char == '*':
                self.advance()
                return token(MUL, '*')
            elif self.current_char == '%':
                self.advance()
                return token(DIV, '%')
            elif self.current_char == '(':
                self.advance()
                return token(LP, '(')
            elif self.current_char == ')':
                self.advance()
                return token(RP, ')')
            else:
                raise SyntaxError('Invalid character')
        return token(END, None)


class grammar(object):
    def __init__(self, y):
        self.y = y
        self.current_token = self.y.findToken()

    def set(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.y.findToken()
        else:
            raise SyntaxError('Invalid syntax')



    #The reason I split up the different symbols was to spread things out for me so it wasnt so cluttered
    #It also helps when making them for testing
    def factor(self):
        token = self.current_token
        if token.type == INT:
            self.set(INT)
            return token.value
        elif token.type == LP:
            self.set(LP)
            result = self.expr()
            self.set(RP)
            return result
    
    def term(self):
        result = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.set(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.set(DIV)
                result = result / self.factor()
        return result
    
    def expr(self):
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.set(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.set(MINUS)
                result = result - self.term()
        return result

class token(object):
    #initalize
    def __init__(self, type, value):
        self.type = type
        self.value = value
    #string return
    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

def main():
    testing()
    #Asks for input and gives answer eventually
    while True:
        eq = input('BigMathGuy$ ')
        if eq.isalpha():
            continue
        if not eq:
            continue
        x = indicator(eq)
        y = grammar(x)
        result = y.expr()
        print(result)



main()
