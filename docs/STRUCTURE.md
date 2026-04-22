# IROHA 專案結構

## 目錄樹

```
iroha/
├── docs/
│   ├── EBNF.md          # 詞元與文法的 EBNF 規則
│   ├── SPEC.md          # 語言設計總結（類型系統、語法、內建動詞）
│   └── Structure.md     # 本文件
├── iroha/               # 主套件
│   ├── ast_nodes.py     # AST 節點定義
│   ├── grammar.lark     # Lark LALR 文法
│   ├── transformer.py   # 剖析樹 → AST 的轉換器
│   ├── environment.py   # 執行期變數環境
│   └── errors.py        # 自訂錯誤與警告類別
├── test/
│   ├── env_test.py      # Environment 單元測試
│   └── tree_parse.py    # 剖析器與 Transformer 整合測試
├── README.md
└── LICENSE
```

---

## 各模組說明

### `iroha/grammar.lark` — 文法定義

使用 [Lark](https://github.com/lark-parser/lark) 的 LALR 模式撰寫。

| 規則 | 說明 |
|------|------|
| `program` | 一或多個 `statement` |
| `statement` | `binding`（綁定）或 `func_call`（函式呼叫），以`。`結尾 |
| `binding` | 變數宣告，格式為 `xは数の1です。` 或 `xは数です。` |
| `type_ann` | 類型標記：`数`/`浮`/`符`/`判` |
| `expr` | 整數、浮點、字串、布林字面值，或識別符 |
| `func_call` | `expr を FUNC_ID` |

終止符規則請參閱 [EBNF.md](EBNF.md)。

---

### `iroha/ast_nodes.py` — AST 節點

以 Python `dataclass` 定義。

| 類別 | 欄位 | 說明 |
|------|------|------|
| `IntLiteral` | `value: int` | 整數字面值 |
| `FloatLiteral` | `value: float` | 浮點數字面值 |
| `StringLiteral` | `value: str` | 字串字面值（去除`「」`） |
| `BoolLiteral` | `value: bool` | 布林字面值（`是`→`True`，`非`→`False`） |
| `Binding` | `name`, `type_ann`, `value?` | 變數綁定，`value` 可為 `None`（僅宣告） |

`Literal` 是上述四種字面值的 `Union` 型別別名。

---

### `iroha/transformer.py` — 剖析樹轉換器

繼承 Lark 的 `Transformer`，將剖析樹節點逐一轉換為 AST 節點。

| 方法 | 對應文法符號 | 輸出 |
|------|------------|------|
| `INTEGER` | `INTEGER` token | `IntLiteral` |
| `FLOAT` | `FLOAT` token | `FloatLiteral` |
| `STRING` | `STRING` token | `StringLiteral`（去除括號） |
| `BOOL` | `BOOL` token | `BoolLiteral` |
| `T_INT/T_FLOAT/T_STRING/T_BOOL` | 類型關鍵字 token | `str` |
| `ID` | `ID` token | `str` |
| `binding` | `binding` 規則 | `Binding` |

---

### `iroha/environment.py` — 變數環境

實作鏈式作用域查找。

| 方法 | 說明 |
|------|------|
| `define(name, value)` | 在當前作用域定義變數 |
| `set(name, value)` | 在當前作用域覆蓋變數 |
| `get(name)` | 查找變數，找不到時往 `parent` 遞迴，最終拋出 `NameError` |

建立子作用域：`Environment(parent=env)`。

---

### `iroha/errors.py` — 錯誤類別

| 類別 | 基底 | 訊息前綴 |
|------|------|---------|
| `IrohaError` | `Exception` | `誤り: ` |
| `IrohaWarning` | `Warning` | `警告: ` |

---

## 執行流程

```
原始碼字串
    │
    ▼
Lark（grammar.lark，LALR）
    │  剖析樹
    ▼
IrohaTransformer（transformer.py）
    │  AST
    ▼
直譯器（尚未實作）
    │  使用 Environment 執行
    ▼
輸出
```
