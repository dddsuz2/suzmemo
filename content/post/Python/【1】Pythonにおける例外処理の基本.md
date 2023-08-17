---
title: "【1】Pythonにおける例外処理の基本"
date: 2023-08-17T21:35:50+09:00
tags: [""]
seq: [""]
draft: false
---

- 基本中の基本は、`try ... except ...`

```python
import logging

try:
    1/0
except ZeroDivisionError:
    logging.warning("test")
```

- 何も例外が発生しない時、`except`の実行は飛ばされる
- `try`で例外が発生すると、`except`キーワードの後に指定されている例外かどうか判定される
  - 指定されている例外の場合、`except`句が実行された後、実行が継続される
  - 指定されていない例外の場合、`unhandled exception`となり、エラーが出力され、実行が止まる


```python
import logging

try:
    1/0
except ZeroDivisionError:
    logging.warning("test")

print(1+1)

try:
    1/0
except ValueError:
    logging.warning("test")

print(3+3)

--------------------------------------
2
WARNING:root:test
Traceback (most recent call last):
  File "z:\home\dada\test\Python\Exception\test.py", line 11, in <module>
    1/0
ZeroDivisionError: division by zero

```

- `except`で例外をキャッチできた場合、そのまま実行が続くのがミソですな
  - じゃないとこの世のプログラム異常終了しまくるでな
  
- `except`では複数のエラーを指定できる

```python
import logging

try:
    1/0
except (ValueError,ZeroDivisionError):
    logging.warning("test")

print(1+1)

-----------------------------------
2
WARNING:root:test
```