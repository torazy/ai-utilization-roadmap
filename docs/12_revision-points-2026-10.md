# 既存資料の修正記録（2026-10-07 再調査）

調査基準日: 2026年10月7日。企画書(03)・詳細シリーズ(04_x/05〜08)・ロードマップ(09)・運営モデル(10)の記述を公開一次情報と突き合わせ、以下を適用した。
用語・モデル・最新機能の解説は [11_glossary-and-landscape.html](11_glossary-and-landscape.html) に集約した。

## 適用済み: 事実誤りの訂正

| # | 対象 | 旧記述 | 修正後 | 根拠 |
|---|------|--------|--------|------|
| A-1 | 03 §3, 出典[20] | Copilot coding agent「2026年3月GA」 | **2025年9月25日GA** | GitHub Changelog 2025-09-25 |
| A-3 | 03 §1・§3表・D-1・出典[20]、04_5 | 「premium request 10〜30件/回」 | premium request制は **2026年6月1日に廃止**。トークン従量の **AI Credits** へ。Business/Enterpriseは席料金に含有分あり | GitHub Billing docs |
| A-4 | 03 §4①、04_1 | スキル共用先「Gemini CLI」 | **Antigravity CLI（旧Gemini CLI、2026年6月18日置換）**。SKILL.mdはAgent Skills公開標準で30ツール超が対応 | The Register 2026-05-20、noqta.tn |
| A-5 | 07 検証レポート | 「Opus 4.6」「GPT-5.4/5.5」 | 検証当時の実在確認はそのまま。現行名は11資料参照と注記。Symphony・GPT-5.5・GLM-5は再調査で実在確認 | platform.claude.com、OpenAI changelog |

**取り下げ:** 当初の指摘A-2「Claude/Codexを選べるのはPro+/Enterpriseのみ」は誤り。2026年2月4日にEnterprise/Pro+、**2月26日にBusiness/Pro** にも展開済み（出典[26]のGitHub Changelogで確認）。03は日付の内訳を補足するに留めた。

## 適用済み: 古くなった前提の更新

| # | 対象 | 更新内容 |
|---|------|---------|
| B-1 | 03 §1 課題④ | 「従量課金化」→「AI Credits従量制（席料金に含有分あり）」 |
| B-2 | 03 §3表・図2・AWS構成カード・D-3、05 §2 | 自律ループの実行基盤を2択から **4候補**（GitHub Actions／Copilot定期実行、Claude Code Routines、Managed Agents・Codex Automations、AgentCore harness）に拡張。比較軸: 閉域・予算上限・イベント起動・既存CI資産 |
| B-3 | 08 E-1比較表 | 行「端末エージェントの接続」を追加: **Unity Gateway CLI**（2026-09-24）で1コマンド接続 |
| B-4 | 04_4、09 §11 | managed MCP が **Unity Gateway統制下に統合**（2026-08-06、ベータ） |
| B-5 | 03 §8 KPI、04_5 | Claude Code **管理ダッシュボード拡充**（2026-07: PR数・受け入れ行数・スキル採用率・コミット当たりコスト）。⑤の自作範囲は「ツール横断の統合」に |
| B-6 | 05 §2、07 | マルチエージェント・無人実行の最新動向を **各社横断** で記述（Copilot定期実行・Agent merge、Codex Automations・Symphony、Claude Code Agent Teams・動的ワークフロー・Routines、AWS DevOps Agent） |
| B-7 | 04_6、09 | AWS DevOps Agent に **スケジュールSREボット・MCP/A2A接続**（2026-06） |
| B-9 | 09 §11 | Coding agent候補を「GitHub Copilot / OpenAI Codex / Claude Code / Google Antigravity」に更新 |

## 適用済み: 追記

| # | 対象 | 追記内容 |
|---|------|---------|
| C-1 | 04_2 §1 | 公開ハーネス391本の実測（2026-09-24）: 効くもの・効きにくいもの・現状の弱点。出典[7]追加 |
| C-2 | 04_1、04_2 | Agent Skills公開標準、AGENTS.mdの採用数がCLAUDE.mdを上回る |
| C-4 | 04_7 §1・§2-1 | 情報源を各社横断に更新（Copilot／OpenAI／Claude／Antigravity／AWS／Databricks） |
| C-8 | 全ページ | 企画書ナビ・詳細シリーズナビ・07・10から **11用語ガイド** へリンク。03出典[27]追加、フッター更新 |

## 未適用（次回改版で判断）

| # | 対象 | 内容 | 理由 |
|---|------|------|------|
| B-8 | 03／09／10 | 基準日の統一（03=2026-07、09=2026-08-25、10=2026-09-08、11=2026-10-07） | 各資料の改版タイミングで実施 |
| B-9' | 03 §4⑥・AWS構成図 | 既定モデル候補（標準ティア＝Opus 5.5等）の明記 | モデル名は11資料に集約し、企画書本文は製品名非依存の方針を維持 |
| C-3 | 03 §4②、04_2 | 製品側のPRレビュー機能（Copilot code review、Claude Code Code Review）で②の評価サブエージェントを代替できる範囲 | 検討項目として起票する判断が必要 |
| C-5 | 09 §11 | モデル更新頻度の実感値（約5日に1本） | 11資料§5に記載済み。09への転記は改版時 |
| C-6 | 03 §4⑧、08 | Claude Enterprise Inference Hooks・Compliance API | ベータ段階。GA後に再評価 |
| C-7 | 03 §5、10 §10 | 5層（プロンプト→コンテキスト→ハーネス→ループ→グラフ）とL1/L2/L3ラダーの対応付け | 教育設計の改版時 |
| C-9 | 03 §9 B | Claude調達2経路（Enterprise席＋API従量／Bedrock従量）の価格前提 | 検討項目Bの改版時 |

## 変更しないと判断したもの

- METR研究の扱い（09・10）: 2026-02-24の設計変更と選択バイアスの注記は反映済み。追加の大規模RCTは未公開。
- DORA: 最新は2025年版。引用は現状のまま。
- EU AI Act の日程（09）: 変更なし。
- Copilot agent mode の content exclusion 非対応（10 §08）: 変更なし。
