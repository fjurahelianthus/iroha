from lark import Transformer
from .ast_nodes import *

VERB_TE_MAP = {  # TE FORMS for chaining
    "たして": "たす",
    "かけて": "かける",
    "へって": "へる",
    "わって": "わる",
}

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
        result = [c for c in children if c is not None]
        return result# filter out None values from optional args
    
    def chain_step(self, children):
        args = children[0]
        verb = VERB_TE_MAP[str(children[1])]
        return FuncCall(func=verb, args=args)

    def chain(self, children):
        steps = [c for c in children if isinstance(c, FuncCall)]
        final_args = children[-2]
        final_verb = str(children[-1])
        # evaluate the chain into nested FuncCalls: xとyをたして、zをかける → かける(たす(x, y), z)
        result = steps[0]
        for step in steps[1:]:
            args = [result] + step.args
            result = FuncCall(func=step.func, args=args)
        return FuncCall(func=final_verb, args=[result] + final_args)

    def func_call(self, children):
        if len(children) == 1:
            if isinstance(children[0], FuncCall):
                return children[0]  # chain rule already produced a FuncCall
            return FuncCall(func=str(children[0])) # bare FUNC_ID
        else:
            func = str(children[-1]) #　the function name is always the last element
            args = children[0] if isinstance(children[0], list) else [children[0]] # the first element is the argument list, but if there's only one argument it won't be a list
            return FuncCall(func=func, args=args) # 1と2をたすという
    
    def program(self, children):
        return children