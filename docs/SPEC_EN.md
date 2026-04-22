# IROHA Language Specification

## Implementation

- **Language:** Python
- **Parser:** Lark (LALR mode)
- **Target:** Tree-walking interpreter

---

## Character Set Roles

| Character Type | Role |
|----------------|------|
| Kanji `漢字` | Type names, built-in verb stems, part of identifiers |
| Hiragana `平仮名` | Grammar keywords and particles — all reserved |
| Katakana `片仮名` | Part of identifiers (may be mixed with kanji) |
| Full-width symbols | Syntax punctuation: `（）「」。、` |

**Identifier rules:** Any combination of kanji and katakana, resolved by longest match. Pure-kanji sequences are checked against the reserved word list. Function identifiers must end with `する` or `す`.

---

## Type System

| Keyword | Meaning |
|---------|---------|
| `数` | Integer |
| `浮` | Float |
| `符` | Character or string |
| `判` | Boolean (`是` = true, `非` = false) |
| `数々` | One-dimensional integer array |
| `数々々` | Two-dimensional integer array (`々` can be stacked for higher dimensions) |

---

## Binding

```
xは数の1です。          # typed binding with value
xは数です。             # declaration without value
xは常に数の1です。      # constant binding
```

---

## Functions

```
# Declaration
計算するの法は数のa、数のbと数のcを使え。

# Definition
計算するとは、
aとbをたすと答える。
終わり。

# Call
aとbを計算する。
a、bとcを計算する。
```

> ⚠️ `a、b、cを計算する。` → warning: もう噛んじゃう (ambiguous comma-separated arguments)

---

## Control Flow

```
# Range loop
1から10まで[2ずつ]、
  <body>
繰り返す。

# While loop
xは是まで、
  <body>
繰り返す。

# Conditional
xは1でしたら、
  <then>
[それとも xは2でしたら、
  <elif>]             # arbitrarily many elif branches
それ以外、
  <else>              # optional
終わり。
```

---

## Built-in Verbs

| Verb | Meaning |
|------|---------|
| `と言う` | print (compound token) |
| `と答える` | return (compound token) |
| `をたす` | addition |
| `をへる` | subtraction |
| `をかける` | multiplication |
| `をわる` | division |
| `をみる` | debug inspect |
| `をきく` | read input |

---

## Operators

**Comparison:**

- `xはyより` → x > y
- `xはyより等` → x >= y
- For x < y: swap operand order

**Logical / Bitwise:**

| Symbol | Meaning |
|--------|---------|
| `且` | AND |
| `又` | OR |
| `の逆` | NOT (postfix) |
| `異` | XOR |
| `動` | shift |

**Grouping:** `（x且y）の逆`

**Precedence:** `動` > `且` > `又` > `異` > `の逆`

---

## Lexer Notes

- `と言う` and `と答える` are tokenized as single compound tokens to eliminate ambiguity with the particle `と`
- Hiragana sequences are tokenized directly as keywords
- Mixed kanji-katakana sequences are resolved by longest match as identifiers
- Identifiers ending in `する`/`す` are tokenized as `FUNC_ID`
- Content between `「` and `」` is a string literal; all characters including full-width symbols are allowed verbatim with no escape processing
- Numeric literals and unary minus use ASCII digits and half-width symbols, consistent with modern languages

---

## Error Style

```
エラー：xは知らない。       # undefined variable
エラー：これは違います。     # type error
エラー：だめです。           # illegal operation
警告：もう噛んじゃう         # ambiguous comma-separated arguments
```
