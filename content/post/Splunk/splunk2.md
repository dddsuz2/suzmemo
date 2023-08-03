---
title: "【Splunk Enterprise 2.0】Splunk Enterprise と Splunk Cloud の違い"
date: 2023-08-02T22:22:13+09:00
tags: ["Splunk"]
seq: ["2"]
draft: false
---

| |  Splunk Enterprise | Splunk Cloud |
| ---- | ---- | ---- |
|  CLI  |  利用可能  |　利用不可　|
|  Splunk Apps  |  利用者が自由に決められる  |　Splunkによって承認されたアプリのみ |
| Direct TCP/UDP network input | 利用可能 | 利用不可 |
| Scripted Alerts | 利用可能 | 承認されたアプリのみ利用可能 |
| License pooling | 利用可能 | 利用不可 |
| HEC | 利用可能 | 利用可能(ELB on port 443 のみ) |
| Splunk API | デフォルトで利用可能 | IP Allow List を使用すれば利用可能 |
| Network Connection | TCP or UDP | オンプレミス上の Forwarder からのTCPのみ（UF credentials が必要）|


[【Splunk Enterprise 2-1】License pooling とは？]({{< ref "splunk2-1.md" >}}) 
- License Poolong って何やねんと思ったときの説明

