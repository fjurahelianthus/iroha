# IROHA EBNF 

## LITERAL

```ebnf
INT      [0-9]+
FLOAT    [0-9]+ '.' [0-9]+
STR      「 ... 」
BOOL     是 | 非
```

## COMPOUND TOKEN

```ebnf
PRINT   と言う
RETURN  と答える
```

## TYPE KEYWORDS

```ebnf
INT          数
FLOAT        浮
CHAR         符
BOOL         判
ARRAY_SUFFIX 々
```

## BINDING

```ebnf
CONST       常に
DECL_SEP    の
```

## FUNCTION

```ebnf
FUNC_DECL    の法は
FUNC_DEF     とは
FUNC_USE     を使え
```

## CONTROL FLOW

```ebnf
RANGE_FROM   から
RANGE_TO     まで
RANGE_STEP   ずつ
LOOP_END     繰り返す
WHILE_COND   まで        (**)
IF           でしたら
ELIF         それとも
ELSE         それ以外
BLOCK_END    終わり
```

## OPERATIONS

```ebnf
AND          且
OR           又
NOT          の逆
XOR          異
SHIFT        動
GT           より
GTE          より等
MINUS        -
```

## BUILT-IN FUNCTIONS

```ebnf
ADD          をたす
SUB          をへる
MUL          をかける
DIV          をわる
INSPECT      をみる
INPUT        をきく
···
```

## PARTICLES AND SYMBOLS

```ebnf
WA           は
TO           と
WO           を
COMMA        、
PERIOD       。
LPAREN       （
RPAREN       ）
```

## IDENTIFIER

```ebnf
VAR_ID     {漢字 | カタカナ | [A-Za-z0-9]}+
FUNC_ID    VAR_ID す[る]
```