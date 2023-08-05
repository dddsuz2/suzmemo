---
title: "【Splunk Enterprise 2.1】License pooling とは？"
date: 2023-08-02T22:41:20+09:00
tags: ["Splunk"]
seq: ["2-1"]
draft: false
---

- License Stack
  - 個々の License Volume が集約されたもの
  - Enterprise と Enterprise Sales Trial ライセンスのみスタック可能  
- License Master (LM) 
  - Liscense Stack を持ち、Liscense Peer (Liscense Slave) 以下の各インスタンスにライセンスを分配する
  - Liscense Peer 間でライセンスを共有することができる  
- License Pool
  - License stack から割り当てられるライセンスの量

