from lark import Transformer
from ast_nodes import *

class IrohaTransformer(Transformer):

    def INTEGER(self, token):
        return IntLiteral(value=int(token))
    
    def ID(self, token):
        return str(token)
    
    def type_ann(self, children):
        return str(children[0])
    
    def binding(self, children):
        if len(children) == 2:
            return Binding(name=children[0], type_ann=children[1], value=None)
        else:
            return Binding(name=children[0], type_ann=children[1], value=children[2])