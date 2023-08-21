---
title: "【6】Synth（楽器）を演奏する"
date: 2023-08-21T00:00:47+09:00
tags: [""]
seq: [""]
draft: false
---

- `bd`, `cp`, `glitch` などはサンプラーを再生している
- 波形をリアルタイムに生成する楽器をシンセサイザーという
  - `sc3-plugin`でインストールしたシンセを鳴らしてみる
  
```haskell
d1 $ n "<f'maj g'maj e'min a'min>"
# sound "supermandolin"
# room 0.5
# size 0.9
```

- `d1 $ sound "supersaw"`では鳴らなかった
  - なんで？環境問題かな