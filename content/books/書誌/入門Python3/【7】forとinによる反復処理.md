---
title: "【7】forとinによる反復処理"
date: 2023-08-05T15:35:25+09:00
tags: [""]
seq: [""]
draft: false
---

Pythonはイテレータを頻繁に使う
とりあえず文字列をループで処理してみる
```python
>>> word = 'thud'
>>> offset = 0
>>> while offset < len(word):
...     print(word[offset])
...     offset += 1
...
t
h
u
d
```

よりパイソニックなコード
```python
>>> for letter in word:
...     print(letter)
...
t
h
u
d
```

