---
title: "【36】SynthをSuperDirt用に書き換える"
date: 2023-08-24T01:37:38+09:00
tags: [""]
seq: [""]
draft: false
---

### 内容
```
(
SynthDef(
	"SawSynth", {
		arg out, freq = 110, pan = 0.5;
		var detune, sig1, sig2, env, sound;
		detune = 1.001;
		sig1 = Saw.ar(freq).dup;
		sig2 = Saw.ar(freq * detune).dup;
        sound = (sig1 + sig2) * 0.5;
		env = EnvGen.kr(Env.perc(), doneAction:2);
		OffsetOut.ar(out, DirtPan.ar(sound, ~dirt.numChannels, pan, env));
}).add
)

d1 $ sound "SawSynth*4" # n "c4 g5 c5 g4"

d1
  $ sometimesBy 0.8 (jux (iter 8))
  $ sometimes (jux ((3/8) ~>))
  $ stack [
    sound "SawSynth(5, 8, 3)"
    # n "[c5, e5, g5, <a5 b5>]"
    |+| n "<0 -5 -12 12>/2"
    # sustain "[0.5 0.03 0.05 0.1]*2"
  ]
  # delay "0.75" # delaytime (5/8)
```

---
### ツッコミ・考察
- 

---
### 疑問点
- 


---
### リンク
- 