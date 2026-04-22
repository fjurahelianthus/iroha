# IROHA

An esoteric programming language based on Japanese grammar and lexicons.

## Overview

**IROHA** is an interpreter-based esolang where programs are written using Japanese characters and grammar structures. Keywords are hiragana particles, type names are kanji, and identifiers are composed of kanji and katakana. Every statement ends with a Japanese period `。`.

## Example

```text
xは数の1です。              # bind integer 1 to x
yは符の「こんにちは」です。  # bind string "こんにちは" to y
zは判の是です。              # bind boolean true to z
wは浮の3.14です。            # bind float 3.14 to w
xと言う。                   # print x
```

## Language Design

### Character Roles

| Character Type      | Role                                                  |
| ------------------- | ----------------------------------------------------  |
| Kanji `漢字`        | Type names, built-in verb stems, part of identifiers  |
| Hiragana `平仮名`   | Grammar keywords and particle are all reserved        |
| Katakana `片仮名`   | Part of identifiers (may be mixed with kanji)         |
| Full-width symbols  | Syntax punctuation：`（）「」。、`                    |

### Types

| Type keyword | Meaning                                                 |
| ------------ | ------------------------------------------------------- |
| `数`         | Integer                                                 |
| `浮`         | Float                                                   |
| `符`         | String                                                  |
| `判`         | Boolean (`是` = true, `非` = false)                     |
| `数々`       | Integer array (々 can be stacked for higher dimensions) |

### Binding

```text
xは数の1です。          # typed binding with value
xは数です。             # declaration without value
xは常に数の1です。       # constant binding
```

### Function Calls

```text
xと言う。               # print x
aとbをたす。            # add a and b
```

### Built-in Verbs

| Verb      | Meaning       |
| --------- | ------------- |
| `と言う`  | print         |
| `と答える`| return        |
| `たす`    | addition      |
| `へる`    | subtraction   |
| `かける`  | multiplication|
| `わる`    | division      |
| `みる`    | debug inspect |
| `きく`    | read input    |

### Functions (planned)

```text
# Declaration
計算するの法は数のa、数のbと数のcを使え。

# Definition
計算するとは、
aとbをたすと答える。
終わり。

# Call
aとbを計算する。
```

### Control Flow (planned)

```text
# Range loop
1から10まで、
  <body>
繰り返す。

# While loop
xは是まで、
  <body>
繰り返す。

# Conditional
xは1でしたら、
  <then>
それとも xは2でしたら、
  <elif>
それ以外、
  <else>
終わり。
```

### Operators

**Comparison:**

- `xはyより` → x < y
- `xはyより等` → x ≤ y
- x > y: swap operand order

**Logical / Bitwise:**

| Symbol  | Meaning      |
| ------- | ------------ |
| `且`    | AND          |
| `又`    | OR           |
| `の逆`  | NOT (postfix)|
| `異`    | XOR          |
| `動`    | shift        |

**Grouping:** `（x且y）の逆`

**Precedence:** `動` > `且` > `又` > `異` > `の逆`

## Implementation

- **Language:** Python
- **Parser:** [Lark](https://github.com/lark-parser/lark) (LALR mode)
- **Target:** Tree-walking interpreter

### Project Structure

```text
iroha/
├── iroha/
│   ├── grammar.lark     # LALR grammar
│   ├── ast_nodes.py     # AST node dataclasses
│   ├── transformer.py   # Parse tree → AST
│   ├── environment.py   # Variable scoping
│   └── errors.py        # IrohaError, IrohaWarning
├── docs/
│   ├── SPEC.md          # Language design reference
│   ├── EBNF.md          # Token and grammar rules
│   └── Structure.md     # Codebase structure
└── test/
    ├── env_test.py
    └── tree_parse.py
```

## Getting Started

### Requirements

```bash
pip install lark
```

### Run Tests

```bash
python test/env_test.py
python test/tree_parse.py
```

## Error Style

Errors and warnings follow a Japanese style to match the language aesthetic:

```text
誤り: xは知らない。      # undefined variable
誤り: これは違います。    # type error
誤り: だめです。         # illegal operation
警告: もう噛んじゃう     # ambiguous comma-separated arguments
```

## License

See [LICENSE](LICENSE).
