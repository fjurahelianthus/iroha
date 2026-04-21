# IROHA Language Specification

## Implementation
- Implementation language: Python
- Parser: lark (LALR mode)
- Execution: interpreted

---

## Character Set Layering

| Character type | Role |
|----------------|------|
| Kanji | Reserved type names, builtin names, part of identifiers |
| Hiragana | Grammar keywords and particles — all reserved |
| Katakana | Part of identifiers (may mix freely with kanji) |
| Full-width symbols | Syntactic punctuation: （）「」。、 |

**Identifier rules:** Any combination of kanji and katakana, resolved via longest match. A pure-kanji sequence is checked against the reserved word list first. A function identifier must end in する or す.

---

## Type System

| Type | Meaning |
|------|---------|
| `数` | Integer |
| `浮` | Float |
| `符` | Character |
| `符々` | String |
| `判` | Boolean (values: `是` / `非`) |
| `数々` | 1D integer array |
| `数々々` | 2D integer array (々 stacks arbitrarily for higher dimensions) |

---

## Binding

```
xは数の1です。       # explicit typed binding
xは数です。          # declaration without value
常に数の1。          # const
```

---

## Functions

```
# Signature
計算するの法は数のa、数のbと数のcを使え。

# Definition
計算するとは、
  aとbをたす
  と答える。

# Call
aとbを計算する。
a、bとcを計算する。
```

> ⚠️ `a、b、cを計算する。` — warning: もう噛んじゃう

`と答える` is the return statement. It is tokenized as a single compound token, not as the particle と followed by a verb.

---

## Control Flow

```
# Range loop
1から10まで2ずつ繰り返す。

# While loop
xは是まで繰り返す。

# Conditionals
xは1でしたら、
  「はい」と言う。
それとも xは2でしたら、
  「いいえ」と言う。
それ以外、
  「いいえ」と言う。
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

`と言う` and `と答える` are tokenized as compound tokens to resolve ambiguity with the particle と used in argument lists.

---

## Operators

**Comparison:**
- `xはyより` → x < y
- `xはyより等` → x ≤ y
- For x > y or x ≥ y, swap the operands.

**Logical / Bitwise:**

| Symbol | Meaning |
|--------|---------|
| `且` | AND |
| `又` | OR |
| `の逆` | NOT (postfix) |
| `異` | XOR |
| `動` | shift |

**Grouping:** `（x且y）の逆`

Scope of `の逆` binds to the immediately preceding operand or grouped expression only.

---

## Lexer Notes

- `と言う` and `と答える` are tokenized as single compound tokens before any other rules are applied.
- Hiragana-only sequences are always tokenized as keywords or particles.
- Kanji-katakana mixed sequences use longest match and are tokenized as `IDENTIFIER`.
- Pure-kanji sequences use longest match, then checked against the reserved word list; if not reserved, treated as `IDENTIFIER`.
- Sequences ending in する or す are tokenized as `FUNC_IDENTIFIER`.

---

## Error Messages

Compiler diagnostics are written in Japanese.

```
エラー：xは知らない。        # undefined variable
エラー：これは違います。      # type mismatch
エラー：だめです。            # illegal operation
警告：もう噛んじゃう          # all arguments separated by 、
```