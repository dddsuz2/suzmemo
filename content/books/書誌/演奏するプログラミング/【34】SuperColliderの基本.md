---
title: "【34】SuperColliderの基本"
date: 2023-08-23T02:22:20+09:00
tags: [""]
seq: [""]
draft: false
---

### 内容
- SuperColliderは、音響合成用プログラミング言語
  - リアルタイム音響合成とアルゴリズミック・コンポジションに特化している

- `{SinOsc.ar(440)}.play`
  - 440Hzのサイン波が片方のチャンネルから出力される
- `{SinOsc.ar([440, 660])}.play`
  - 左から440Hz, 右に660HzのSin波が出力される

```
({
	var freq, detune, sig1, sig2;
	freq = 110;
	detune = 1.001;
	sig1 = Saw.ar(freq).dup;
	sig2 = Saw.ar(freq * detune).dup;
	(sig1 + sig2) * 0.5;
	}.play)
```

- `freq`は基本周波数
- `detune`は基本周波数から少しだけずらすため
- `sig1`と`sig2`はそれぞれ`Saw.ar()`からの出力を代入


---
### ツッコミ・考察
- 

---
### 疑問点
- 


---
### リンク
- 