from lark import Lark, Tree, Token
from iroha.transformer import IrohaTransformer
from iroha.interpreter import IrohaInterpreter
from iroha.errors import IrohaError
import sys


def print_tree(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    if isinstance(node, Tree):
        print(prefix + connector + node.data)
        child_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(node.children):
            print_tree(child, child_prefix, i == len(node.children) - 1)
    elif isinstance(node, Token):
        print(prefix + connector + f"{node.type}: {node}")


with open("iroha/grammar.lark", encoding="utf-8") as f:
    parser = Lark(f, parser="lalr", start="program")

if len(sys.argv) != 2:
    print("使い方: python main.py <ファイル>.iroha")
    sys.exit(1)

with open(sys.argv[1], encoding="utf-8") as f:
    source = f.read()

if not source:
    print("いろはにほへと　ちりぬるを\nわかよたれそ　  つねならむ\nうゐのおくやま　けふこえて\nあさきゆめみし　ゑひもせす")
    sys.exit(0)

tree = parser.parse(source)
print(f"入力: {sys.argv[1]}")
print_tree(tree)
ast = IrohaTransformer().transform(tree)
try:
    IrohaInterpreter().run(ast)
except IrohaError as e:
    print(e)
    sys.exit(1)