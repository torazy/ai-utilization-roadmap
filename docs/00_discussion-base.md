# 生成AI活用による開発プロセス変革 — 企画ディスカッション土台資料

作成日: 2026-07-06 / ステータス: ディスカッション用たたき台 v0.1

---

## 1. 調査サマリ（最新動向・先進事例）

### 1.1 エンタープライズ導入の現状（なぜ「バラバラ導入」では頭打ちになるか）

- エンタープライズAIコーディングエージェント市場は2026年4月時点で年換算約100億ドル規模。コード補完から「エージェント駆動開発」へ主戦場が移行（Gartner）。
- エンジニアリングリーダーの90%が改善を報告、平均生産性向上は19.3%。ただし出力を信頼するのは29%のみ（2024年の40%から低下）。→ 検証・評価の仕組みなしでは信頼が下がる。
- **エージェントのパイロットの88%が本番に到達しない**。原因はエージェント自体ではなく、分離環境・ガバナンス・コンプライアンス統制・データ管理といった「デプロイ基盤」の欠如（Northflank）。
- DORA 2025: 「AIは増幅器（amplifier）」— 健全な開発システムは加速するが、摩擦や欠陥もそのまま増幅する。**内部プラットフォームへの投資がAI投資の価値実現の決定的なイネーブラー**。エネーブルメント施策とCommunity of Practice（実践共同体）が成功要因。

### 1.2 ハーネスエンジニアリング / ループエンジニアリング

- **ハーネスエンジニアリング**: AIエージェントが自律的に正しく働ける「環境・文脈・評価・フィードバックループ」を人間が設計する手法。
  - OpenAI Codexチームの実践: ①AGENTS.md（リポジトリでの作業方法を機械可読で記述）②ワンコマンドで起動する再現可能な開発環境（worktree単位の分離）③CIで機械的に強制される不変条件（アーキテクチャ境界・フォーマット・データ検証）。
  - Anthropic: 計画・生成・評価を分離した3エージェントハーネスで長時間自律開発を実現。Skills（プロンプト+ツール+ドキュメントのバンドル）がオープン標準化。
- **ループエンジニアリング**: Addy Osmani提唱（2026年6月）。人間が都度プロンプトを打つのをやめ、スケジュール/イベント駆動で複数エージェントを自律的に回し続ける「制御レイヤー」を設計する手法。ハーネス（単一エージェントの実行環境）の1つ上の階層。
- 含意: **ハーネスは「リポジトリ資産」（AGENTS.md/CLAUDE.md、CI、devcontainer）として整備するもの**であり、これ自体が新しい「開発標準」の実体になる。従来の文書ベース開発標準より浸透しやすい（エージェントが強制的に従うため）。

### 1.3 ツールの使い分けとコスト

- GitHub Copilot: 2026年6月1日からシート課金→従量課金に移行。IDE内補完・軽微な修正に最適（<200msの補完、多IDE対応）。
- Claude Code: 自律エージェント型。SWE-bench Verified ~80.8%。大規模リファクタ、レガシー解析、MCP経由でインフラ/ドキュメント/運用データを跨ぐタスクに強い。
- 業界推奨のハイブリッド: **全員にCopilot（エディタ内作業）+ 上位20%程度（リファクタ・プラットフォーム作業を担う層）にClaude Code**。50人組織でCopilot年1.1万〜2.3万ドル vs Claude Max年6万〜12万ドルの差 → 全員に最上位ツールは非効率。
- Gemini（Google Workspace）: 全社員が使える汎用チャット/ドキュメント作業レイヤーとして位置づけ（非エンジニア含む）。

### 1.4 運用工程のAI化（AI SRE / AIOps）

- 2026年、AIOpsは「異常検知の改善」から**自律的エージェント運用**へ進化。AI SRE = アラート発火と同時に調査を開始し、根本原因を数分で特定し、修復を提案/実行するエージェント。
- AWS DevOps Agent、Azure SRE Agent が2026年3月にGA。テレメトリ・コード・デプロイ履歴・リソースコンテキストを横断分析。
- 効果実績: MTTR平均17.8%削減、先進導入では30〜70%削減。障害報告書の自動起草も一般化。

### 1.5 レガシーシステム × AI

- **富士通が2026年3月、ソースコード解析から設計書を自動生成する生成AIサービスを国内SaaSで開始。作業時間約97%削減**（COBOL等対応）。
- 研究面: Reversaフレームワーク等、「仕様書なきレガシー」を**AIエージェントが作業可能な運用仕様（インベントリ、アーキテクチャ、ドメインモデル、Gherkinテスト仕様）に変換**するリバースドキュメンテーションが確立しつつある。
- 発見フェーズ（依存関係マッピング、隠れた仕様の解析）が最も効果が実証されている領域。Thoughtworks試算で1万行モジュールあたり6週間の解析作業を数時間に圧縮。
- 含意: **「設計書がない古いシステム」はAI変革の障害ではなく、最初の投資対効果が最も出やすいターゲット**。生成したドキュメントはそのままエージェントのコンテキスト（ハーネス）になる。

### 1.6 ナレッジ × AI

- 2026年のエンタープライズRAGは「知識ランタイム」へ: 検索・検証・推論・アクセス制御・監査証跡を統合したオーケストレーション層。ハイブリッド検索（ベクトル+BM25+リランカー）+ グラフ併用が標準。
- **MCP（Model Context Protocol）が業界標準化**。異なるベンダーのエージェント同士がナレッジを相互利用。エージェントのデータアクセス権限は「代行するユーザーと同一」が原則。
- 「蓄積もAI」: 障害対応記録・PRレビュー・設計判断をエージェントが自動で構造化ナレッジに変換し、自己更新するナレッジベースが実用段階（Neo4j LLM Graph RAG等）。

### 1.7 Databricks（既存資産の活用）

- **Agent Bricks**: エージェント構築プラットフォーム。主要モデル（Claude/GPT/Gemini/Llama等）対応、**Lakebaseによるマネージドエージェントメモリ**、MCPベースのツールアクセス、Lakehouse上のデータへの高速エージェント検索。
- **Genie One + Genie Ontology**: 組織の全ナレッジの「オントロジー（自己改善するコンテキスト層）」を構築し、業務チームが構造化/非構造化データを横断してエージェントに仕事をさせる。
- Mosaic AI: サーバレスGPU、エージェント評価（Agent Evaluation）、Unity Catalogによるガバナンス統合。
- 含意: **ナレッジ基盤・データ利活用エージェント・エージェント評価はDatabricks上に構築するのが自然**（新規基盤投資を抑えられる）。

### 1.8 ガバナンス・規制動向

- 経産省・総務省「AI事業者ガイドライン第1.2版」（2026年3月31日公表）: AIエージェント・Human-in-the-Loop運用・学習データのトレーサビリティが明確化。
- EU AI Act: 2026年8月執行。高リスクAIに監査可能性と人間の監督を要求。
- エージェントのガードレールは4層（計画・推論・アクション・出力）で設計。「Policy-as-Prompt」（ガバナンスルールを実行可能なガードレールに変換）が実装パターンとして確立。

### 1.9 スキル・プラグインの組織内共有

- Claude Codeのプラグイン（スキル+MCPサーバ+コマンド+フック+エージェントのバンドル）は、**社内Gitリポジトリ（marketplace.json）だけで社内マーケットプレイスを構築可能**。CLIで各開発者の環境に同期。
- マルチハーネス対応マーケットプレイス（Claude Code / Copilot / Gemini CLI / Cursor共用）のOSS実装も登場 → **ツール非依存の「社内スキル資産」として管理する潮流**。

### 1.10 効果測定

- **DX Core 4**（DORA + SPACE + DevExを統合した測定フレームワーク）が2026年のデファクト。
- DORAスループット系（変更リードタイム、デプロイ頻度、復旧時間）+ 安定性系（変更失敗率、手戻り率）+ AI固有指標（利用率、AI起因の変更失敗率、節約時間 — 平均3.6時間/週/人）。
- 教訓: 「利用率」だけ測ると失敗する。**アウトカム（リードタイム・品質・MTTR）とセットで測る**。

---

## 2. たたき台: 何を作るか — 「AI開発プラットフォーム」3層モデル

```
┌─────────────────────────────────────────────────┐
│ L3: 部門・業務固有レイヤー（各部門が所有）           │
│   業務固有スキル/エージェント、業務ナレッジ、          │
│   システム固有ハーネス（各リポジトリのAGENTS.md等）    │
├─────────────────────────────────────────────────┤
│ L2: 共通イネーブルメント基盤（CoEが所有）            │
│   ① 社内スキル/プラグイン・マーケットプレイス          │
│   ② 標準ハーネステンプレート                        │
│      (AGENTS.md/CLAUDE.md雛形、CI不変条件、          │
│       devcontainer、レビュー/テストループ)            │
│   ③ ナレッジ基盤 (Databricks: Genie Ontology +      │
│      RAG + 自動蓄積パイプライン)                     │
│   ④ MCPゲートウェイ (社内システムへの統制された接続)   │
│   ⑤ 効果測定・コスト管理ダッシュボード                │
│   ⑥ 運用AI (AI SRE: 障害調査・リカバリ支援・報告生成)  │
├─────────────────────────────────────────────────┤
│ L1: ガバナンス・方針レイヤー（共通で決めること）       │
│   ツール選定マトリクス / データ分類と利用可否 /        │
│   セキュリティ・ガードレール / コストポリシー /        │
│   人材育成レベル定義 / Human-in-the-Loop基準         │
└─────────────────────────────────────────────────┘
```

### L1: 共通で決めること（ルール/ガイドライン）

| 種別 | 内容 |
|---|---|
| **ルール**（must） | データ分類と各AIサービスへの投入可否、認証・権限（エージェントは利用者と同一権限）、本番変更のHuman-in-the-Loop基準、監査ログ |
| **方針**（should） | ツール使い分けマトリクス、コスト予算モデル（従量課金の上限・配賦）、モデル選定の考え方 |
| **ガイドライン**（recommend） | プロンプト/ハーネス設計プラクティス、レビュー観点、スキル作成・公開手順 |

### ツール使い分けマトリクス（初期案）

| ユースケース | 推奨ツール | 理由 |
|---|---|---|
| エディタ内の補完・小修正 | GitHub Copilot | 低コスト・低レイテンシ・多IDE |
| 大規模リファクタ、レガシー解析、横断調査 | Claude Code | 自律エージェント、MCP連携 |
| 設計書ドラフト、議事録、メール、非開発業務 | Gemini (Workspace) | 全社員ライセンス済み |
| データ分析・BI・業務エージェント | Databricks (Genie/Agent Bricks) | データガバナンス統合 |
| 障害調査・運用 | AI SRE (Claude Code + MCP or 専用サービス) | テレメトリ横断 |

### L2の中核: 「ハーネス=新しい開発標準」

従来型の文書ベース開発標準は浸透しなかった → **標準をリポジトリ内の機械可読な資産（AGENTS.md、CIルール、テンプレート）として配布**する。エージェントがそれに従って動くため、標準が「自動的に実行される」。人間向け文書はその副産物として生成。

---

## 3. 進め方（4フェーズ案）

### Phase 0: アセスメント（〜2ヶ月）
- 現状調査: 部署ごとのツール利用実態、コスト、スキルレベル、対象システム棚卸し
- DX Core 4ベースラインの測定開始
- ガバナンスL1の初版策定（ルール/方針/ガイドライン）

### Phase 1: 基盤構築 + パイロット（3〜6ヶ月）
- 共通基盤の最小構成: 社内マーケットプレイス、標準ハーネステンプレート、コストダッシュボード
- **灯台チーム（lighthouse team）2〜3チーム**でパイロット:
  - ①レガシー文書化（設計書リバース生成）→ 効果が数字で示しやすい
  - ②ハーネス整備済みリポジトリでのエージェント開発
- 教育プログラム開始（3階層: 全員向けリテラシー / 開発者向けエージェント活用 / チャンピオン向けハーネス設計）

### Phase 2: 横展開 + 運用AI（6〜12ヶ月）
- パイロットの型を全部門に展開（部門チャンピオン経由）
- AI SRE導入: 障害一次調査・報告書ドラフト自動化から開始 → リカバリ支援へ
- ナレッジ自動蓄積パイプライン稼働（障害記録・PR・設計判断 → Databricks上のナレッジ基盤へ）

### Phase 3: 自律化・ループエンジニアリング（12ヶ月〜）
- スケジュール/イベント駆動の自律ループ: 夜間の自動テスト補強、依存更新、ドキュメント鮮度維持、バックログ自動消化
- ナレッジの「蓄積もAI・活用もAI」の完全ループ
- 効果を役員報告し、投資を再配分

---

## 4. 推進体制（案）

```
経営スポンサー（役員）
   │
AI CoE（小規模・専任 4〜8名）
 ├─ プラットフォームチーム: L2基盤の構築・運用
 ├─ イネーブルメントチーム: 教育・伴走支援・スキル収集と横展開
 └─ ガバナンス担当: L1の策定・改訂、コスト監視（情シス/セキュリティと兼務可）
   │
部門チャンピオン（各部門1〜2名、兼務）
 ├─ 部門固有スキル/ハーネスの整備（L3）
 └─ Community of Practice（実践共同体）の運営
```

ポイント:
- CoEは「統制」でなく「イネーブルメント（できるようにする）」が主務。DORAの知見: 集合的に学び共有する仕組み（CoP）が成功要因。
- 部門の自律性は維持（L3は部門所有）。共通化するのは「共通化した方が全員が速くなるもの」だけ。
- 3〜6ヶ月ごとに「共通化候補」を部門からCoEへ吸い上げるレビューサイクル。

---

## 5. 狙う効果（KPI案）

| カテゴリ | 指標 | 目安 |
|---|---|---|
| 開発生産性 | 変更リードタイム、節約時間/週 | 業界平均: +19.3%生産性、3.6h/週/人 |
| 品質 | 変更失敗率、AI起因不具合率 | 悪化させないことが第一目標 |
| 運用 | MTTR、障害報告作成時間 | 業界実績: MTTR 30〜70%削減 |
| レガシー | 設計書カバレッジ、解析リードタイム | 富士通事例: 文書化工数97%減 |
| 活用度 | ツール利用率、スキル再利用数、CoP参加率 | アウトカムとセットで測定 |
| コスト | AI支出/開発者、成果あたりコスト | 従量課金の上限管理 |

---

## 6. 未決の論点（ディスカッション対象）

1. **スコープと規模**: 対象は開発部門全体で何名・何チーム・何システムか。パイロット候補はどこか。
2. **セキュリティ前提**: ソースコード・障害情報をどのAIサービスまで出せるか（データ分類の現状）。Claude Code等の新規調達の稟議ルートは。
3. **Databricksの守備範囲**: ナレッジ基盤をDatabricksに寄せるか、開発ナレッジは別（GitHub/社内Wiki+RAG）にするか。Databricks運用チームとの関係。
4. **コストモデル**: 従量課金（Copilot 2026/6〜、Claude Code）の予算をCoE一括か部門配賦か。上限アラートの閾値。
5. **底上げ vs 先端のバランス**: 「Geminiチャット止まり」層の底上げ教育と、先端層のハーネス/ループ高度化に、どの比率で投資するか。
6. **レガシー文書化の優先順位**: 最初に文書化するシステムの選定基準（変更頻度×リスク×担当者の残存期間?）。
7. **CoEの人繰り**: 専任を出せるか。初期は外部パートナー活用か。
8. **効果測定の開始時期**: ベースライン測定を企画承認前に始めるか（推奨: 始める。効果主張の説得力が変わる）。

---

## 参考ソース

- 市場・導入動向: [Gartner Enterprise AI Coding Agent Market](https://www.gartner.com/en/articles/enterprise-ai-coding-agent-market) / [Faros.ai Scaling Guide](https://www.faros.ai/blog/enterprise-ai-coding-assistant-adoption-scaling-guide) / [Northflank Deployment](https://northflank.com/blog/enterprise-ai-coding-agent-deployment)
- ハーネス/ループ: [Harness Engineering Study (arXiv)](https://arxiv.org/html/2602.14690v5) / [Anthropic 3-Agent Harness (InfoQ)](https://www.infoq.com/news/2026/04/anthropic-three-agent-harness-ai/) / [ループエンジニアリングとは (AI総合研究所)](https://www.ai-souken.com/article/what-is-loop-engineering) / [ハーネスエンジニアリング (Findy)](https://jp.findy-team.io/blog/ai-casestudy/harness-engineering/) / [内側ループと外側ループ (@IT)](https://atmarkit.itmedia.co.jp/ait/articles/2607/03/news016.html)
- ツール比較: [Claude Code vs Copilot (morphllm)](https://www.morphllm.com/comparisons/claude-code-vs-copilot) / [Pricing比較 (Septim Labs)](https://septimlabs.com/blog/claude-code-vs-github-copilot-pricing-2026) / [CTO Guide (Teamvoy)](https://teamvoy.com/blog/claude-code-vs-github-copilot-cto-guide/)
- AI SRE: [Rootly AI SRE Guide](https://rootly.com/ai-sre-guide) / [AWS DevOps Agent](https://aws.amazon.com/blogs/devops/leverage-agentic-ai-for-autonomous-incident-response-with-aws-devops-agent/) / [incident.io 2026](https://incident.io/blog/5-best-ai-powered-incident-management-platforms-2026)
- レガシー: [富士通 設計書自動生成](https://global.fujitsu/en-global/pr/news/2026/03/30-01) / [Reversa (arXiv)](https://arxiv.org/html/2605.18684) / [Augment Code Modernization Guide](https://www.augmentcode.com/guides/application-modernization)
- ナレッジ: [Enterprise RAG 2026 (Keerok)](https://keerok.tech/en/blog/enterprise-rag-building-an-ai-knowledge-base-in-2026/) / [RAG 2026-2030 (NStarX)](https://nstarxinc.com/blog/the-next-frontier-of-rag-how-enterprise-knowledge-systems-will-evolve-2026-2030/)
- Databricks: [Agent Bricks DAIS 2026](https://www.databricks.com/blog/agent-bricks-dais-2026) / [Genie One発表](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team)
- ガバナンス: [AI事業者ガイドライン1.2解説 (AI総合研究所)](https://www.ai-souken.com/article/ai-generation-guidelines-introduction) / [Policy-as-Prompt (arXiv)](https://arxiv.org/abs/2509.23994) / [CSA Control Layer](https://cloudsecurityalliance.org/blog/2026/03/17/from-guardrails-to-governance-why-enterprise-ai-needs-a-control-layer)
- プラグイン共有: [Claude Code Plugins Docs](https://code.claude.com/docs/en/plugins) / [Thoughtworks Radar](https://www.thoughtworks.com/en-us/radar/tools/claude-code-plugin-marketplace) / [マルチハーネスMarketplace (GitHub)](https://github.com/wshobson/agents)
- 効果測定: [DORA 2025 Report](https://dora.dev/dora-report-2025/) / [DX Core 4 / DORA解説 (DX)](https://getdx.com/blog/dora-metrics/) / [Platform Engineering (DORA)](https://dora.dev/capabilities/platform-engineering/)
