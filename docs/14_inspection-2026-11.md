# 既存資料の点検結果（2026-11-15）

調査基準日: 2026年11月15日。前回（2026-10-07、[12_revision-points-2026-10.md](12_revision-points-2026-10.md)）以降の変化を、公式ドキュメントと報道に照らして点検した。
Databricksの活用方針と開発エージェント構成の調査結果は [13_databricks-and-agent-architecture.html](13_databricks-and-agent-architecture.html) にまとめた。

**状態: 以下はすべて未適用**（点検結果の一覧）。優先度 A=事実が変わった／誤解を生む、B=前提が古い、C=追記で強くなる。

## A. 事実が変わった箇所

| # | 対象 | 現在の記述 | 修正内容 | 根拠 |
|---|------|-----------|---------|------|
| A-1 | 03 §4④⑧・検討項目E、04_4、04_5、08 全体 | 「Unity AI Gateway」「Unity AI GW」 | 製品名は **Unity Gateway**（2026-08-04 GA）。全資料で名称を統一 | Databricks docs |
| A-2 | 08 3類型表、03 §3表・図2、04_3 | 業務エージェント＝「Agent Bricks（ガバナンス・評価込み）」。04_3は「Agent Bricksの文書検索サブエージェント」 | Knowledge Assistant／Supervisor Agent は **2026-10-12に旧機能扱い**。後継はコード型＝Agent Bricks CLI＋Agent Runtime、ノーコード型＝Genie Agent。東京では旧2機能にクロスGeo処理が必要 | Databricks 10月リリースノート、region support |
| A-3 | 04_4 Phase 2、08 E-4、03 E-4 | 「Databricks managed MCP」（UC関数・SQL・Genie・Vector Search を設定で提供） | 現行は2系統。**system.ai のDatabricks提供MCP**（Unity Gateway経由・統制対象）と、**ワークスペース直結エンドポイント**（/api/2.0/mcp/、Public Preview、**Unity Gatewayを通らない**）。統制の前提として前者に限定する旨を明記。Genie One MCPはGA、旧ベータエンドポイントは2026-10-31廃止 | Databricks MCP docs |
| A-4 | 11 §5 モデル表 | Claude Fable 5.1（$10/$50）、Haiku 4.5、Gemini 3.5 Pro／Flash、GPT-6.1 Sol「要確認」 | **Claude Fable 5.2**（11/9、$8/$40）、**Haiku 5.5**（10月）、**Gemini 4 Carbon／Hydrogen／Argon**（10〜11月）、**GPT-6.1 Terra**（10/26）、GPT-6.1 SolがCodex既定。Gemini 3.6 Flash等は退役 | 各社公表、Databricks supported models |
| A-5 | 11 §6 提供元別の到達点・時系列 | 2026年10月初旬まで | **GitHub Universe（10/28）**: Copilotアプリ、Copilot Fusion GA（旧HydraFusion）、Copilot Projects、Connectors、GitHub EnterpriseへのCopilot包含。**Antigravity** Orchestrator・/swarm。**AgentCore** 次世代ランタイム既定・Web Search API GA。**Unity Gateway** のCopilot対応（11/11）・デスクトップMDM配布 | GitHub Blog、AWS What's New、Databricks release notes |
| A-6 | 08 E-1 弱み欄 | 「外部モデルEndpointのPrivateLinkはPublic Preview」 | 閉域関連はコンテキストベースのイングレス制御とサーバーレスからAWSリソースへのプライベート接続が **GA（10/12）**。例外条件①（閉域要件×PrivateLink未GA）の判定を再評価 | Databricks 10月リリースノート |

## B. 古くなった前提

| # | 対象 | 更新内容 |
|---|------|---------|
| B-1 | 03 §10 リスク、L1方針 | リスク表に **AI開発ツールの供給網・認証情報** を追加（Cursorの拡張機能改ざん、AI基盤の認証情報窃取、指示ファイル経由の乗っ取り、設定ファイルへの秘密情報混入）。対策は13資料6章の4層 |
| B-2 | 04_2 ハーネス §2 権限統制 | セキュリティ基準を追加: エージェントのバージョン下限、起動ディレクトリの制限、ローカル設定ファイルのgitignore固定とシークレットスキャン、設定ファイル変更のレビュー必須、未確認通信の拒否 |
| B-3 | 04_1 マーケットプレイス | プラグイン・拡張機能の **許可リストとバージョン固定**、公開後一定期間を置いた導入。Unity Gatewayのスキル管理（Beta）を利用記録の取得手段として併記 |
| B-4 | 08 E-1〜E-3、03 E-3 | **クロスGeo処理が既定オン**（非US/EUワークスペース）である点、モデル別の国内処理可否とデータ保持（最上位モデルは30日保持）を判断軸に追加 |
| B-5 | 08 比較表「端末エージェントの接続」 | 対応エージェントを更新: Claude Code、Codex、Copilot CLI／VS Code、Gemini CLI、Cursor（MCPのみ）、デスクトップアプリ。サブスクリプション中継、集中設定、MDM配布 |
| B-6 | 04_5 ダッシュボード | Unity Gatewayの利用ダッシュボードv1.0、system.ai_gateway.usage、統合トレース（Beta）、AI Functions費用の予算算入を取得源に追加。「記録自体が機微情報」として保持期間・マスクの設計を追記 |
| B-7 | 04_3 ナレッジ | Genie Ontology／Genie Search が **GA（11/9）**。Unity Catalog Pages（GA）・Wikis（Beta）。Genie Agentのボリューム内ファイル分析（PP） |
| B-8 | 04_6 AI SRE | データ基盤側の運用監視としてGenie ZeroOps（Beta）を比較対象に追記 |
| B-9 | 05 ループ詳説、03 D-3 | 実行基盤候補にAgentCore次世代ランタイム、Copilot Automations／Projects、Databricks Agent Runtimeを反映 |
| B-10 | 09 §11 製品・モデル戦略、10 §08 | Coding agent候補とモデル例を現行に更新。Databricks行を「Unity Gateway／Agent Bricks／Genie」の3本立てに |

## C. 追記すると強くなる

| # | 対象 | 追記内容 |
|---|------|---------|
| C-1 | 03 §3 / AWS構成 | 13資料の「3つの面と1つの統制線」（開発面・業務AI面・運用面）を全体像に対応付け。開発エージェントもUnity Gateway経由にできる点を明記 |
| C-2 | 03 検討項目 | 新規項目: クロスGeo設定とワークスペース分離／コーディングエージェントのモデル調達3案（Databricks従量・サブスク中継・Bedrock登録）／ベータ機能の採用基準 |
| C-3 | 04_7 ウォッチ | 情報源にセキュリティ勧告（各ベンダーのセキュリティ通知、CVE、CSA等）を追加。判定ルーブリックに「セキュリティ修正は即展開」を明記 |
| C-4 | 06 事例集 | 反面教師としてCursor事案（実行トレースに秘密情報→委託先経由で流出→配布経路の改ざん）を追加 |
| C-5 | 全ページナビ | 13資料へのリンクを追加。基準日の注記を更新 |

## 変更不要と判断したもの

- ゲートウェイの一次判定ルール「原則Unity Gateway、例外条件でBedrock直接」: 維持。Bedrock上のモデルをUnity Gatewayに外部プロバイダとして登録できるため、記録と予算の一元化はむしろ容易になった。
- 設計原則「共通にするのは仕組み、分離するのは実行資源」: 維持。
- ④と⑧の論理構成（ツール接続の関所／モデル呼び出しの関所）: 維持。Unity Gatewayが両方を担う範囲が広がった。
- METR、DORA、EU AI Actの記述: 新しい一次資料なし。

## 確認できなかった点

- Cursor事案の利用者数・日付は報道間で差がある。Cursor自身の公表ページは未確認。
- Databricksのモデル別の国内処理可否は、公式のコンプライアンスページとリージョン別一覧で記載が一致しない箇所がある（例: Claude Sonnet 5）。実機確認が必要。
- ガードレールの日本語対応、Agent Runtimeの料金単位・制限値は公式ページに記載がない。
- GPT-6.1 Sol／Terraの価格、Gemini 4各モデルの価格は一次資料で未確認。
