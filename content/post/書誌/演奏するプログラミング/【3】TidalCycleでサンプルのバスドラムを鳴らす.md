---
title: "【3】TidalCycleでサンプルのバスドラムを鳴らす"
date: 2023-08-20T23:45:58+09:00
tags: [""]
seq: [""]
draft: false
---

- `d1 $ sound "bd"`
  - `d1`は生成したパターンの`SuperDirt`へのコネクションを意味している
  - `d1` ~ `d9`まで存在している
    - TidalCycleでは9個のトラックを並行して演奏できる
  - `sound`が関数名で、`bd`が引数