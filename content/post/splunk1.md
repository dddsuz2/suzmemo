---
title: "Splunkの主要コンポーネント"
date: 2023-07-10T22:25:40+09:00
tags: - Splunk
categories: -
draft: false
---

- Instance: Splunk が起動しているサーバーのこと
  - StandAlone: 単独サーバーのみで、input, parse, index, search を行う構成のこと
  - Distributed: 複数のサーバーで、input, parse, index, search を行う構成のこと

- Forwader: データを Indexer または別の Forwarder に対して転送するコンポーネント
- Indexer
  1. データをインデックス化し、raw data をイベントに変換する
  2. 検索リクエストに応じて、インデックス化されたデータを検索する
  - Distributed なデプロイメントの場合
    - Search Head と呼ばれるコンポーネントが検索管理を行い、複数の Indexer 間で検索を調整する
    - この場合、個々の Indexer は「検索ピア」と呼ばれる
- Index
  - Splunk によって検索可能な形式に変換された raw data のこと
- Deployment-Server
  - 任意の数のインスタンスの設定をまとめて管理するインスタンス
- Deployment-Client
  - Deployment-Server によってリモートで設定を管理されるインスタンス