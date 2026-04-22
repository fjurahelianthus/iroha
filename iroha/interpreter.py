from .ast_nodes import *
from .environment import Environment
from .errors import IrohaError

class IrohaInterpreter:
    def __init__(self):
        self.env = Environment()
        self.builtins = {
            "と言う":  lambda args: print(*args),  # print has no limit on number of arguments
            "と答える": lambda args: ...,
            "たす": self._builtin("たす", 2, lambda args: args[0] + args[1]),
            "へる": self._builtin("へる", 2, lambda args: args[0] - args[1]),
            "かける": self._builtin("かける", 2, lambda args: args[0] * args[1]),
            "わる": self._builtin("わる", 2, lambda args: args[0] / args[1]),
        }
        self.env.define("伊呂波ノ歌", "いろはにほへと　ちりぬるを\nわかよたれそ　　つねならむ\nうゐのおくやま　けふこえて\nあさきゆめみし　ゑひもせす")

    def _builtin(self, func, arity, op):
        def wrapped(args):
            if len(args) != arity:
                raise IrohaError(f"これは違います。")
            return op(args)
        return wrapped
        
    def run(self, program):
        for stmt in program:
            self.exec(stmt)

    def exec(self, node):
        if isinstance(node, Binding):
            self._exec_binding(node)
        elif isinstance(node, FuncCall): 
            self._exec_func_call(node)
        else:
            raise IrohaError(f"だめです。")
    
    def _exec_binding(self, node: Binding):
        value = self.eval(node.value) if node.value is not None else None
        self.env.define(node.name, value)

    def _exec_func_call(self, node: FuncCall):
        args = [self.eval(a) for a in node.args if a is not None]
        if node.func in self.builtins:
            return self.builtins[node.func](args)
        raise IrohaError("だめです。")
    
    def eval(self, node):
        if isinstance(node, IntLiteral):
            return node.value
        elif isinstance(node, FloatLiteral):
            return node.value
        elif isinstance(node, StringLiteral):
            return node.value
        elif isinstance(node, BoolLiteral):
            return node.value
        elif isinstance(node, FuncCall):
            return self._exec_func_call(node)
        elif isinstance(node, str):
            return self.env.get(node)
        elif isinstance(node, Chain):
            result = None
            for step in node.steps:
                args = [self.eval(arg) for arg in step.args]
                if result is not None:
                    args = [result] + args
                result = self.builtins[step.verb](args)
            final_args = [self.eval(arg) for arg in node.final_args]
            if result is not None:
                final_args = [result] + final_args
            return self.builtins[node.verb](final_args)
        elif node is None:
            return None
        else:
            print(f"計算できません: type={type(node)}, value={node!r}")
            raise IrohaError(f"計算できません。")