# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit
from kit import *
from figs import *

DOC = '業務でAIを安全に使う仕組み'
PARTS = {0: ('はじめに', INK), 1: ('1  なぜ、そこまでできるのか', TE), 2: ('2  何を防げるのか', RD), 3: ('3  何を実現できるのか', BL), 4: ('4  採用する場合の前提', GD)}
S = []


def slide(part, title, body, notes='', lead=''):
    name, col = PARTS[part]
    ld = f'<p class="lead">{lead}</p>' if lead else ''
    S.append(f'<section class="s" style="--pc:{col}"><div class="bar"></div><div class="top"><span class="chip">{name}</span></div>'
             f'<h2 class="title">{title}</h2>{ld}<div class="body">{body}</div><aside>{notes}</aside></section>')


def i(name, col=INK, size=40):
    return f'<svg class="ic" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg>'


import base64
IMG = 'D:/vscode-worspace/ai-utilization-roadmap/docs/img/15/'
PSTART = {}


def uri(f):
    return 'data:image/png;base64,' + base64.b64encode(open(IMG + f, 'rb').read()).decode()


def official(part, title, imgs, src, points=None, notes='', dark=False):
    """imgs: list of (file, width, height, label)"""
    cls = 'of dark' if dark else 'of'
    pics = ''.join((f'<p class="of-l">{lab}</p>' if lab else '') + f'<img src="{uri(f)}" width="{w}" height="{h}" alt="{title}">' for f, w, h, lab in imgs)
    side = ('<ul class="of-p">' + ''.join(f'<li>{x}</li>' for x in points) + '</ul>') if points else ''
    body = f'<div class="of-w"><div class="{cls}">{pics}</div>{side}</div><p class="cap">出典: {src}（2026年11月16日取得）</p>'
    slide(part, '<span class="ofk">公式の図</span>' + title, body, notes)


_slide = slide


def slide(part, *a, **k):
    PSTART.setdefault(part, len(S) + 1)
    _slide(part, *a, **k)


# 1 cover
S.append(f'''<section class="s cover"><div class="cv-l"><p class="cv-k">機能説明資料 ｜ 構成案の1つとして</p>
<h1 class="cv-t">業務でAIを<br>安全に使う仕組み</h1>
<p class="cv-s">Databricksの機能で、何を防げ、何を実現できるか</p>
<p class="cv-d">2026年11月</p></div><div class="cv-r">{fig_cover()}</div>
<aside>業務アプリへのAI組み込みと、業務データを使うAI活用の基盤について、構成案の1つであるDatabricksの機能を説明する。採用を前提にした資料ではない。</aside></section>''')

# 2
slide(0, 'この資料は、3つの問いに答える', f'''
<div class="g3">
<div class="q" style="--c:{TE};--t:{TET}"><p class="qn">問い 1</p><h3>なぜ、そこまでできるのか</h3><p>データとAIを同じ台帳で管理し、AIへの要求を1つの関所に通す仕組みを説明する。</p><p class="qp">@P1@ページ</p></div>
<div class="q" style="--c:{RD};--t:{RDT}"><p class="qn">問い 2</p><h3>何を防げるのか</h3><p>権限を超えた参照、費用の暴走、記録の欠落など、6つの問題への対応と、その限界を示す。</p><p class="qp">@P2@ページ</p></div>
<div class="q" style="--c:{BL};--t:{BLT}"><p class="qn">問い 3</p><h3>何を実現できるのか</h3><p>データへの質問、業務アプリへの組み込み、一括処理、業務知識の台帳という4つの使い方を示す。</p><p class="qp">@P3@ページ</p></div>
</div>
<div class="note-row">{i('doc', MUTE, 34)}<p>採用する場合の構成と確認事項は@P4@ページに置く。開発者が使うコーディングエージェントは別資料で扱う。</p></div>''',
      '最初に資料の位置づけを伝える。Databricksは構成案の1つであり、この資料の目的は機能の理解にある。',
      '業務アプリへのAI組み込みと、業務データを使うAI活用の基盤として、Databricksを構成案の1つに挙げている。この資料は、その機能を説明する。')

# 3
slide(0, '業務でAIを使うと、6つの問題が起きる', fig_problems(),
      '以降のページは、この6つの番号に対応させて説明する。上の帯は、問題が起きる場所を示している。')

official(0, 'Databricksの製品構成と、この資料で扱う範囲', [('platform-stack.png', 1100, 550, '')],
         'Databricks「Data Intelligence Platform」製品ページ (databricks.com/product/data-intelligence-platform)',
         ['この資料が扱うのは、中央の「Unified governance」（Unity Catalog、Unity Gateway）と、その上に載るGenie、Agent Bricks、Apps', '下の2層（データとインフラ）は、既存のデータ基盤として前提に置く', '統制の層が中央にあり、上のAIと下のデータの両方にかかる構造になっている'],
         'Databricks自身の説明でも、統制は独立した層として中央に置かれている。', dark=True)
# 4-8
slide(1, 'データもAIも、同じ台帳と同じ権限で管理する', fig_uc(),
      'これが「なぜそこまでできるのか」への答えの中心。モデルやツールもテーブルと同じ階層に置かれるので、AIだけ別の権限管理を作らなくてよい。')
official(1, 'すべての資産が、メタストアとカタログの下に並ぶ', [('uc-object-hierarchy.png', 1664, 594, '')],
         'Databricks公式ドキュメント「What is Unity Catalog?」(docs.databricks.com/aws/en/data-governance/unity-catalog/)',
         None, '前ページの図の元になる公式の階層図。Table、Volumeと同じ並びにFunction、Model、Serviceがある点に注目する。')
slide(1, '全体像: 入口、通り道、台帳の3層でできている', fig_arch(),
      '誰がどの入口から使っても、モデルとツールへの要求はUnity Gatewayを通り、データへのアクセスはUnity Catalogの権限で決まる。')
official(1, '統制の層が、データとAIの資産をまとめて覆う', [('platform-unified-governance.png', 1036, 620, '')],
         'Databricks「Data Intelligence Platform」製品ページ (databricks.com/product/data-intelligence-platform)',
         ['上の帯がUnity CatalogとUnity Gateway。アクセス制御、リネージ、AIの統制、費用の管理を担う', '下に並ぶのが統制の対象。表、ファイル、モデル、エージェント、スキル、MCPとツール', 'データ用とAI用で統制を分けない、という設計が読み取れる'],
         '公式の説明でも、統制の対象としてデータとAIの資産が同列に並んでいる。')
slide(1, 'AIへの要求は、1つの関所を通る', fig_gw(),
      '1から3で止め、5で届け先を決め、7で残す。4と6の検査はベータなので、これに頼らない設計にする。')
official(1, '検査は、要求が届く前と、応答が返る前の2回かかる', [('service-policy-phases.png', 1420, 520, '')],
         'Databricks公式ドキュメント「Service policies」(docs.databricks.com/aws/en/data-governance/unity-catalog/service-policies/)',
         None, '前ページの4番と6番にあたるベータ機能の公式の図。許可、拒否、人による確認の3つの結果がある。人による確認はMCPだけが対象。')
slide(1, 'AIは、質問した本人が見てよいデータだけで答える', fig_obo(),
      '同じ質問でも、本人の権限によって答えが変わる。AI用に別の権限設定を作るのではなく、データ側の権限がそのまま効く。')
slide(1, 'AIは2種類ある: 部品のLLMと、完成品のGenie', fig_two(),
      'アプリの機能として埋め込むならサービングのLLM、データに答えさせるならGenie。統制のかかり方も違う。')

# 9
rows = [(1, '権限を超えた参照', 'Unity Catalogの権限、行フィルタと列マスク、本人の権限での実行', '効く', 'ok'),
        (2, 'データの持ち出し', 'モデルはDatabricks内、または保持なしのエンドポイントで動く。出口ポリシーで宛先を絞る', '条件付き', 'cond'),
        (3, '費用の暴走', '全体と利用者ごとの予算、毎分のレート制限', '効く', 'ok'),
        (4, '記録が残らない', '利用テーブル、推論テーブル、監査ログ', '効く', 'ok'),
        (5, '鍵の散在', 'OAuthとサービスプリンシパルで呼ぶ。外部プロバイダの鍵は接続設定に集約し、配らない', '効く', 'ok'),
        (6, '処理地域が不明', '地域をまたぐ処理の設定、モデル単位の許可', '条件付き', 'cond')]
tb = '<table class="mx"><tr><th style="width:26%">問題</th><th>防ぐ仕組み</th><th style="width:15%">効き方</th></tr>'
for n, p, m, e, c in rows:
    tb += f'<tr><td><span class="nb">{n}</span><b>{p}</b></td><td>{m}</td><td><span class="st {c}">{e}</span></td></tr>'
tb += '</table><p class="cap">「条件付き」の内容: 2は最上位のモデルが提供元で30日保持されること、6はモデルと機能によって国外処理になることを指す。停止が近似である点など細部は次ページ以降に示す。</p>'
slide(2, '6つの問題に、それぞれ仕組みが対応する', tb, '4つは標準の機能で防げる。2つはモデルと設定の選び方に条件がある。')

slide(2, '見せてよい行と列だけが、AIに渡る', fig_mask(), '問題1への対応。権限をデータ側で一度決めれば、SQLでもGenieでもアプリでも同じ結果になる。')
slide(2, '予算とレート制限で、使いすぎを止める', fig_budget(), '問題3への対応。予算は月単位の歯止め、レート制限は瞬間的な暴走の歯止め。両方を使う。')
slide(2, '誰が、いつ、何を使ったかが残る', fig_logs(), '問題4への対応。ただし本文を含む記録は、それ自体が守る対象になる。')
slide(2, 'どこで処理されるかは、機能とモデルで決まる', fig_region(), '問題2と6への対応。日本のワークスペースでは、Genieの主要機能は国内で処理される。')

# 14 limits
lim = [('lock', '既定のままでは開いている', ['Databricks提供のモデルとMCPは、既定で全利用者が実行できる。取り消して付け直す', '地域をまたぐ処理は既定でオンになっている', '個人アクセストークンは無効化し、OAuthに統一する']),
       ('gate', '関所を通らない経路がある', ['AI Functionsにかかるのは、利用量の記録と予算だけ', 'ワークスペース直結のMCPと旧来のエンドポイントは通らない', 'Genie本体にかかるのは予算と監査。レート制限と検査は公式に記載がない']),
       ('warn', 'ベータ、または記載がない', ['入出力の検査はベータ。日本語への対応は公式に記載がない', 'エージェントのツール実行を利用者の権限で行う機能はプレビュー', '推論テーブルに保存される本文にはマスクがかからない'])]
h = '<div class="g3">'
for ic, t, items in lim:
    h += f'<div class="lm"><div class="lm-h">{i(ic, RD, 44)}<h3>{t}</h3></div><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'
h += '</div>'
slide(2, '設定しないと効かない点、まだ防げない点がある', h, '機能があることと、効いていることは別。左は設定で閉じられる。中央は使う経路を限定して避ける。右は実機で確認する。',
      '「防げる」は、次の3種類の前提の上に成り立つ。')

# 15-19
slide(3, '実現できることは、大きく4つある', fig_uses(), '以降の4ページで、それぞれの仕組みを順に示す。')
slide(3, '言葉で質問すると、データから答えが返る', fig_genie(), '画面は説明用のイメージ。答えと一緒に実行したSQLを確認できる点が、業務で使ううえで重要になる。')
slide(3, '業務アプリへの組み込みは、4つの型から選ぶ', fig_patterns(), '社外向けの画面と既存の業務システムは2か3。アプリは業務側に置き、AIをAPIとして受け取る。',
      '橙の箱がDatabricks側、白の箱が業務側。')
slide(3, 'Databricks Appsは、2つの権限を使い分けて動く', fig_apps(), 'データの参照とGenieへの質問は利用者の権限、書き込みと共通処理はアプリの権限、と分ける。')
official(3, 'アプリの権限で呼ぶ場合と、利用者の権限で呼ぶ場合', [('apps-service-principal.png', 1120, 251, 'アプリの権限（サービスプリンシパル）で呼ぶ: 全員が同じデータを見る'), ('apps-user-auth.png', 1120, 267, '利用者の権限で呼ぶ: 本人が見てよいデータだけを見る')],
         'Databricks公式ドキュメント「Configure authorization in a Databricks app」(docs.databricks.com/aws/en/dev-tools/databricks-apps/auth)',
         None, '上はアプリの身元に権限が要る。下は利用者本人に権限が要る。どちらを使うかで、見えるデータの範囲が決まる。')
slide(3, '業務知識の台帳を1つにし、人もAIも同じ窓口で引く', fig_know(), '全部を複製して1か所に入れるのではない。文書は元の場所に置いたまま索引し、台帳と参照口を1つにする。')

official(3, '意味の層の上に、Genieと外部の利用口が載る', [('semantic-layer.png', 800, 650, '')],
         'Databricks「Unity Catalog」製品ページ (databricks.com/product/unity-catalog)',
         ['最上段が利用口。Genie、MCP・SQL・API、ダッシュボード', '中段が意味の層。Genie Ontology（学習された文脈）と、利用者が定義するドメイン、用語集、指標', '最下段が発生源。データレイク、連携先、業務アプリ', '前ページの「台帳は1つ、参照口は1つ」は、この構造に対応する'],
         '知識の台帳という考え方は、Databricksの製品構成でも意味の層として位置づけられている。')
# 20
slide(4, '環境はワークスペースで、領域はカタログで分ける', fig_infra(), '最初に決めるのは、ワークスペースの数、カタログの切り方、地域をまたぐ処理の設定の3点。')

# 21
cond = [('通り道を1本にする', '要求をUnity Gateway経由に限定し、通らない経路を設定で閉じる'),
        ('ベータに依存しない', '検査などのベータ機能がなくても成り立つ設計にする'),
        ('処理地域と保持を決める', 'モデル単位で国内処理と保持条件を確認し、許可一覧にする'),
        ('呼び出しの身元を検証する', '利用者の権限で動くはずの処理が、共通の身元に切り替わらないことを確かめる')]
chk = ['Databricks Appsの応答の時間切れ（秒数の記載がない）', 'Genieへのレート制限と検査の適用', '入出力検査の日本語への対応', '日本語文書の解析精度', '利用者のトークンが欠けたときの挙動']
h = '<div class="g2"><div><h3 class="sub">成立する4つの条件</h3>'
for n, (t, d) in enumerate(cond):
    h += f'<div class="cd"><span class="cn">{n + 1}</span><div><b>{t}</b><p>{d}</p></div></div>'
h += '</div><div><h3 class="sub">実機で確認する項目</h3><div class="ck">' + ''.join(f'<p>{i("search", GD, 30)}<span>{x}</span></p>' for x in chk)
h += '</div><p class="cap">いずれも公式ドキュメントに数値または記載がない項目。</p></div></div>'
slide(4, '採用を判断する前に、条件と未確認の点を押さえる', h, '左は設計で満たす条件、右は検証環境で確かめる項目。')

# 22
sm = [(TE, TET, 'なぜ、そこまでできるのか', ['データとAIが同じ台帳（Unity Catalog）にある', 'AIへの要求が1つの関所（Unity Gateway）を通る', 'AIは質問した本人の権限で動く']),
      (RD, RDT, '何を防げるのか', ['権限を超えた参照、費用の暴走、記録の欠落、鍵の散在は標準機能で防げる', '持ち出しと処理地域は、モデルと設定の選び方に条件がある', '既定の設定と、関所を通らない経路は閉じる必要がある']),
      (BL, BLT, '何を実現できるのか', ['従業員が、データに言葉で質問できる', '業務アプリに、4つの型でAIを組み込める', '業務知識を1つの台帳にまとめ、影響調査と企画立案に使える'])]
h = '<div class="g3">'
for c, t, ttl, items in sm:
    h += f'<div class="q sm" style="--c:{c};--t:{t}"><h3>{ttl}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'
h += '</div>'
slide(0, 'まとめ: 3つの問いへの答え', h, '機能としては業務のAI活用に必要な統制がそろっている。採用の判断には、@PC@ページの条件と確認項目が前提になる。')

N = len(S)
rng = lambda a, b: f'{a}〜{b}'
PP = {'@P1@': rng(PSTART[1], PSTART[2] - 1), '@P2@': rng(PSTART[2], PSTART[3] - 1), '@P3@': rng(PSTART[3], PSTART[4] - 1), '@P4@': rng(PSTART[4], N - 1), '@PC@': str(N - 1)}
S = [__import__('functools').reduce(lambda x, kv: x.replace(*kv), PP.items(), x) for x in S]
frames = ''
for n, s in enumerate(S):
    foot = '' if n == 0 else f'<div class="foot"><span>{DOC}</span><span>{n + 1} / {N}</span></div>'
    frames += f'<div class="frame" data-n="{n + 1}">{s.replace("<aside>", foot + "<aside>")}</div>\n'

CSS = '''*{margin:0;box-sizing:border-box}
html,body{height:100%;background:#0B1226;overflow:hidden;font-family:'Noto Sans JP','BIZ UDPGothic','Yu Gothic UI','Meiryo','Hiragino Sans',sans-serif}
#stage{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
#scaler{width:1920px;height:1080px;flex:none;position:relative}
.frame{display:none;width:1920px;height:1080px;overflow:hidden;position:absolute;inset:0}
.frame.on{display:block}
section.s{width:1920px;height:1080px;position:relative;background:PAPER;color:INK;padding:60px 128px 0;display:flex;flex-direction:column}
section.s>aside{display:none}
svg text{font-family:inherit}
.bar{position:absolute;left:0;top:0;bottom:0;width:14px;background:var(--pc)}
.top{height:42px;flex:none;display:flex;align-items:center}
.chip{font-size:22px;font-weight:700;color:#fff;background:var(--pc);padding:5px 20px;border-radius:999px;letter-spacing:.04em}
.title{font-size:54px;line-height:1.25;font-weight:700;margin-top:18px;letter-spacing:.01em}
.lead{font-size:27px;line-height:1.55;color:SOFT;margin-top:12px}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;padding:16px 0 92px}
.fig{display:block}
.foot{position:absolute;left:128px;right:128px;bottom:30px;display:flex;justify-content:space-between;font-size:20px;color:MUTE;border-top:2px solid LINE;padding-top:10px}
.ic{flex:none}
.ofk{display:inline-block;font-size:24px;font-weight:700;color:var(--pc);border:3px solid var(--pc);border-radius:10px;padding:4px 14px;margin-right:20px;vertical-align:middle;position:relative;top:-6px}
.of-w{display:flex;gap:40px;align-items:center}
.of{flex:none;background:#fff;border:2px solid LINE;border-radius:18px;padding:22px;display:flex;flex-direction:column;gap:10px}
.of.dark{background:#0B0F14;border-color:#0B0F14}
.of img{display:block}
.of-l{font-size:25px;font-weight:700;color:INK;margin-top:6px}
.of-p{list-style:none;display:flex;flex-direction:column;gap:24px}
.of-p li{font-size:26px;line-height:1.6;padding-left:30px;position:relative}
.of-p li:before{content:"";position:absolute;left:0;top:15px;width:14px;height:14px;border-radius:50%;background:var(--pc)}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:56px}
.q{background:#fff;border:2px solid LINE;border-top:12px solid var(--c);border-radius:18px;padding:34px 34px 30px;display:flex;flex-direction:column;gap:18px;min-height:520px}
.q .qn{font-size:24px;font-weight:700;color:var(--c);letter-spacing:.08em}
.q h3{font-size:33px;line-height:1.35}
.q p{font-size:29px;line-height:1.7;color:SOFT}
.q .qp{margin-top:auto;font-size:23px;font-weight:700;color:var(--c);background:var(--t);align-self:flex-start;padding:6px 18px;border-radius:999px}
.q.sm{min-height:560px}.q.sm h3{font-size:36px;color:var(--c)}
.q ul{list-style:none;display:flex;flex-direction:column;gap:22px;margin-top:8px}
.q li{font-size:28px;line-height:1.6;padding-left:30px;position:relative}
.q li:before{content:"";position:absolute;left:0;top:17px;width:14px;height:14px;border-radius:50%;background:var(--c)}
.note-row{display:flex;gap:16px;align-items:center;margin-top:34px;font-size:25px;color:SOFT}
.mx{width:100%;border-collapse:separate;border-spacing:0 9px;font-size:25px;line-height:1.45}
.mx th{text-align:left;font-size:22px;color:MUTE;padding:0 24px 0}
.mx td{background:#fff;padding:12px 24px;border-top:2px solid LINE;border-bottom:2px solid LINE;vertical-align:middle}
.mx td:first-child{border-left:2px solid LINE;border-radius:14px 0 0 14px;font-size:28px;white-space:nowrap}
.mx td:last-child{border-right:2px solid LINE;border-radius:0 14px 14px 0}
.nb{display:inline-flex;width:44px;height:44px;border-radius:50%;background:RD;color:#fff;font-weight:700;align-items:center;justify-content:center;margin-right:16px;font-size:24px;vertical-align:middle}
.st{display:inline-block;font-size:24px;font-weight:700;padding:6px 20px;border-radius:999px}
.st.ok{background:TET;color:TE}.st.cond{background:GDT;color:GD}
.cap{font-size:21px;line-height:1.5;color:SOFT;margin-top:10px}
.lm{background:#fff;border:2px solid LINE;border-radius:18px;padding:32px;min-height:500px}
.lm-h{display:flex;gap:16px;align-items:center;padding-bottom:20px;border-bottom:3px solid RD;margin-bottom:24px}
.lm h3{font-size:32px;line-height:1.3}
.lm ul{list-style:none;display:flex;flex-direction:column;gap:22px}
.lm li{font-size:26px;line-height:1.6;padding-left:28px;position:relative}
.lm li:before{content:"";position:absolute;left:0;top:16px;width:12px;height:12px;background:RD;border-radius:3px}
.sub{font-size:30px;margin-bottom:20px;color:GD}
.cd{display:flex;gap:20px;background:#fff;border:2px solid LINE;border-radius:14px;padding:20px 24px;margin-bottom:14px;align-items:flex-start}
.cn{flex:none;width:48px;height:48px;border-radius:50%;background:GD;color:#fff;font-size:26px;font-weight:700;display:flex;align-items:center;justify-content:center}
.cd b{font-size:28px}.cd p{font-size:24px;line-height:1.55;color:SOFT;margin-top:4px}
.ck{background:GDT;border-radius:18px;padding:28px 32px;display:flex;flex-direction:column;gap:22px}
.ck p{display:flex;gap:16px;align-items:center;font-size:27px;line-height:1.4}
section.cover{background:INK;color:#fff;display:flex;flex-direction:row;align-items:center;gap:60px;padding:0 128px}
.cv-l{flex:1}
.cv-k{font-size:26px;font-weight:700;color:#F0A070;letter-spacing:.08em}
.cv-t{font-size:104px;line-height:1.22;font-weight:700;margin-top:36px;letter-spacing:.01em}
.cv-s{font-size:36px;color:#C9D2E3;margin-top:40px;line-height:1.5}
.cv-d{font-size:24px;color:#8E9AB5;margin-top:72px}
.cv-r{flex:none}
#bar{position:fixed;left:0;right:0;bottom:0;display:flex;gap:12px;align-items:center;justify-content:center;padding:8px;font-size:14px;color:#C9D2E3;background:rgba(11,18,38,.85);opacity:0;transition:opacity .2s}
body:hover #bar{opacity:1}
#bar button{font:inherit;color:#F7F6F2;background:#1F2F54;border:1px solid #3A4A70;border-radius:6px;padding:4px 12px;cursor:pointer}
#notes{position:fixed;left:0;right:0;bottom:44px;max-height:30%;overflow:auto;padding:16px 24px;font-size:18px;line-height:1.7;color:#101C36;background:#FAF8F4;border-top:3px solid #C2410C;display:none}
body.shownotes #notes{display:block}
@media print{@page{size:1920px 1080px;margin:0}html,body{height:auto;overflow:visible;background:none}#stage{position:static;display:block}
#scaler{transform:none!important;height:auto}.frame{display:block;position:relative;break-after:page}#bar,#notes{display:none!important}}'''
for k, v in dict(PAPER=PAPER, INK=INK, SOFT=SOFT, MUTE=MUTE, LINE=LINE, TET=TET, TE=TE, GDT=GDT, GD=GD, RDT=RDT, RD=RD).items():
    import re as _re
    CSS = _re.sub(r'(?<![A-Za-z#])' + k + r'(?![A-Za-z])', v, CSS)

JS = '''(function(){
var f=[].slice.call(document.querySelectorAll('.frame')),i=0,sc=document.getElementById('scaler'),pg=document.getElementById('pg'),nt=document.getElementById('notes');
function fit(){sc.style.transform='scale('+Math.min(innerWidth/1920,innerHeight/1080)+')';}
function go(n){i=Math.max(0,Math.min(f.length-1,n));f.forEach(function(e,k){e.classList.toggle('on',k===i)});
pg.textContent=(i+1)+' / '+f.length;var a=f[i].querySelector('aside');nt.textContent=a?a.textContent:'';try{history.replaceState(null,'','#'+(i+1))}catch(e){}}
addEventListener('resize',fit);
addEventListener('keydown',function(e){
if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '||e.key==='Enter'){go(i+1);e.preventDefault()}
else if(e.key==='ArrowLeft'||e.key==='PageUp'||e.key==='Backspace'){go(i-1);e.preventDefault()}
else if(e.key==='Home')go(0);else if(e.key==='End')go(f.length-1);
else if(e.key==='n'||e.key==='N')document.body.classList.toggle('shownotes');
else if(e.key==='f'||e.key==='F'){if(document.fullscreenElement)document.exitFullscreen();else if(document.documentElement.requestFullscreen)document.documentElement.requestFullscreen()}});
document.getElementById('stage').addEventListener('click',function(e){go(i+(e.clientX<innerWidth/3?-1:1))});
document.getElementById('prev').onclick=function(){go(i-1)};document.getElementById('next').onclick=function(){go(i+1)};
document.getElementById('nb').onclick=function(){document.body.classList.toggle('shownotes')};
fit();go((parseInt(location.hash.slice(1),10)||1)-1);})();'''

HTML = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{DOC} — Databricksの機能で防げること、実現できること</title>
<style>
{CSS}
</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{defs()}</svg>
<div id="stage"><div id="scaler">
{frames}</div></div>
<div id="notes"></div>
<div id="bar"><button id="prev">←</button><span id="pg"></span><button id="next">→</button><button id="nb">ノート (N)</button><span>← → で移動 ／ F で全画面 ／ 印刷でPDF化</span></div>
<script>
{JS}
</script>
</body>
</html>
'''
out = sys.argv[1]
open(out, 'w', encoding='utf-8', newline='\n').write(HTML)
print('slides', N, 'bytes', os.path.getsize(out))
for w in kit.WARN:
    print('WARN', w)
