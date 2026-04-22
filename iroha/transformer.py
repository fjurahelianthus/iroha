from lark import Transformer
from .ast_nodes import *

class IrohaTransformer(Transformer):

    def INTEGER(self, token):
        return IntLiteral(value=int(token))
    
    def FLOAT(self, token):
        return FloatLiteral(value=float(token))

    def STRING(self, token):
        # Remove the surrounding 「 and 」
        value = token[1:-1]
        return StringLiteral(value=value)
    
    def BOOL(self, token):
        if token == "是":
            return BoolLiteral(value=True)
        elif token == "非":
            return BoolLiteral(value=False)

    def T_INT(self, token):
        return str(token)
    
    def T_FLOAT(self, token):
        return str(token)
    
    def T_STRING(self, token):
        return str(token)
    
    def T_BOOL(self, token):
        return str(token)
    
    def ID(self, token):
        return str(token)
    
    def binding(self, children):
        if len(children) == 2:
            return Binding(name=children[0], type_ann=children[1], value=None)
        else:
            return Binding(name=children[0], type_ann=children[1], value=children[2])
        
    def args(self, children):
        return children

    def func_call(self, children):
        if len(children) == 1:
            return FuncCall(func=children[0])
        else:
            return FuncCall(func=children[1], args=children[0])
    
    def program(self, children):
        return children