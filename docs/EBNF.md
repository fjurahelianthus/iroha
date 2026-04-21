# IROHA EBNF 規則

## 字面值

```ebnf
INT      [0-9]+
FLOAT    [0-9]+ '.' [0-9]+
STR      「 ... 」
BOOL     是 | 非
```

## 復合詞元

```ebnf
PRINT   と言う
RETURN  と答える
```

## 型別關鍵字

```ebnf
INT          数
FLOAT        浮
CHAR         符
BOOL         判
ARRAY_SUFFIX 々
```

## Binding

```ebnf
CONST       常に
DECL_SEP    の
```

## 函數

```ebnf
FUNC_DECL    の法は
FUNC_DEF     とは
FUNC_USE     を使え
```

## 控制流

```ebnf
RANGE_FROM   から
RANGE_TO     まで
RANGE_STEP   ずつ
LOOP_END     繰り返す
WHILE_COND   まで        (* 和 RANGE_TO 同形，靠 context 區分 *)
IF           でしたら
ELIF         それとも
ELSE         それ以外
BLOCK_END    終わり
```

## 運算子

```ebnf
AND          且
OR           又
NOT          の逆
XOR          異
SHIFT        動
LT           より
LTE          より等
MINUS        -
```

## 內建函數

```ebnf
ADD          をたす
SUB          をへる
MUL          をかける
DIV          をわる
INSPECT      をみる
INPUT        をきく
···
```

## 助詞/標點

```ebnf
WA           は
TO           と
WO           を
COMMA        、
PERIOD       。
LPAREN       （
RPAREN       ）
```

## 識別符

```ebnf
VAR_ID     {漢字 | カタカナ | [A-Za-z0-9]}+
FUNC_ID    VAR_ID す[る]
```