# -*- coding: utf-8 -*-
from kit import *


def fig_problems():
    s = ''
    xs = [0, 455, 910, 1364]
    for (n, ic), x in zip([('利用者', 'user'), ('アプリ、画面', 'app'), ('AIモデル', 'cube'), ('業務データ', 'db')], xs):
        s += node(x, 26, 300, 96, n, icon=ic, tag='prob')
    for i in range(3):
        s += arrow(xs[i] + 310, 74, xs[i + 1] - 10, 74)
    for cx, cy, n in [(1664 - 24, 26, 1), (910 + 196, 26, 2), (910 + 246, 26, 3), (910 + 296, 26, 6), (455 + 296, 26, 5), (832, 44, 4)]:
        s += badge(cx, cy, n, 20)
    items = [
        ('権限を超えた参照', 'AIが、本人に見せてはいけないデータまで使って答える。', 'shield'),
        ('データの持ち出し', '業務データが外部のAIサービスに渡り、保持や学習に使われる。', 'globe'),
        ('費用の暴走', '誰がどれだけ使ったか分からず、上限もかけられない。', 'gauge'),
        ('記録が残らない', '何を聞き、何が返ったかを、後から確かめられない。', 'list'),
        ('鍵の散在', 'APIキーがアプリや個人に配られ、漏れても止められない。', 'key'),
        ('処理地域が不明', 'データがどの国で処理され、保持されるかを選べない。', 'globe'),
    ]
    for i, (t, b, ic) in enumerate(items):
        x = (i % 3) * 564; y = 176 + (i // 3) * 256
        s += box(x, y, 536, 232, WHITE, LINE)
        s += f'<rect x="{x}" y="{y + 20}" width="8" height="192" rx="4" fill="{RD}"/>'
        s += badge(x + 58, y + 56, i + 1, 26)
        s += text(x + 100, y + 36, t, 31, INK, 700)
        s += ico(ic, x + 536 - 74, y + 32, 44, RD)
        s += text(x + 36, y + 112, b, 25, SOFT, maxw=470, lh=1.55)
    return svg(670, s, label='業務でAIを使うと起きる6つの問題')


def fig_uc():
    s = ''
    s += node(482, 0, 700, 76, 'メタストア（地域に1つ。東京）', icon='db', theme='ink', tag='uc')
    cx = [82, 632, 1182]
    s += line([(832, 76), (832, 104)], MUTE) + line([(282, 104), (1382, 104)], MUTE)
    for x, t in zip(cx, ['カタログ: 営業（本番）', 'カタログ: 経理（本番）', 'カタログ: AI（共有）']):
        s += line([(x + 200, 104), (x + 200, 130)], MUTE)
        s += node(x, 130, 400, 76, t, icon='book', tag='uc')
        s += line([(x + 200, 206), (x + 200, 234)], MUTE)
    s += line([(282, 234), (1382, 234)], MUTE) + line([(832, 234), (832, 260)], MUTE)
    s += node(482, 260, 700, 70, 'スキーマ（業務領域の中の区分）', theme='plain', center=True, ts=26, tag='uc')
    s += line([(832, 330), (832, 360)], MUTE) + line([(108, 360), (1556, 360)], MUTE)
    objs = [('テーブル', '業務データ', 'table'), ('指標、ビュー', 'メトリックビュー', 'gauge'), ('ファイル', 'ボリューム', 'doc'),
            ('モデル', 'LLM、機械学習', 'cube'), ('関数、ツール', 'エージェントの道具', 'gear'), ('MCPサービス', '外部ツール接続', 'plug'), ('スキル', '手順書（Beta）', 'book')]
    gap = (1664 - 7 * 216) / 6
    for i, (t, sub, ic) in enumerate(objs):
        x = i * (216 + gap)
        col, tint = (TE, TET) if i < 3 else (OR, ORT)
        s += line([(x + 108, 360), (x + 108, 388)], MUTE)
        s += box(x, 388, 216, 156, tint, col, 2.5)
        s += ico(ic, x + 108 - 23, 404, 46, col)
        s += text(x + 108, 460, t, 26, INK, 700, 'middle')
        s += text(x + 108, 500, sub, 21, SOFT, 400, 'middle')
    xr = 3 * 216 + 2 * gap
    s += line([(0, 566), (xr, 566)], TE, 5) + text(xr / 2, 574, 'データ', 26, TE, 700, 'middle')
    s += line([(xr + gap, 566), (1664, 566)], OR, 5) + text((xr + gap + 1664) / 2, 574, 'AI', 26, OR, 700, 'middle')
    s += box(0, 624, 1664, 76, INK, INK)
    s += text(832, 644, '同じ権限（GRANT）、同じ監査ログ、同じリネージが、すべての資産にかかる', 28, WHITE, 700, 'middle')
    return svg(700, s, label='Unity Catalogの階層。データとAIの資産が同じ台帳に並ぶ')


def fig_arch():
    s = ''
    for x, t in [(0, '利用者'), (330, '入口'), (750, '通り道'), (1040, 'AI')]:
        s += text(x, 0, t, 23, MUTE, 700)
    ys = [44, 194, 344]
    for y, (t, ic) in zip(ys, [('従業員', 'user'), ('業務アプリ', 'bld'), ('定期ジョブ', 'layers')]):
        s += node(0, y, 250, 128, t, icon=ic, tag='arch')
        s += arrow(258, y + 64, 322, y + 64)
    for y, (t, sub, ic) in zip(ys, [('Genie One', 'Slack、Teamsからも使える', 'chat'), ('Apps、REST API', '画面と業務システムから', 'app'), ('SQL', 'AI Functionsで一括処理', 'table')]):
        s += node(330, y, 340, 128, t, sub, ic, tag='arch')
        s += arrow(678, y + 64, 742, y + 64)
    s += box(750, 44, 210, 420, INK, INK, 2, 16)
    s += ico('gate', 750 + 105 - 24, 62, 48, '#F0A070')
    s += text(855, 118, 'Unity\nGateway', 28, WHITE, 700, 'middle', lh=1.25)
    for i, t in enumerate(['認証', '権限', '予算', 'レート制限', '記録']):
        yy = 206 + i * 50
        s += box(770, yy, 170, 40, NAVY2, '#3A4A70', 1.5, 20)
        s += text(855, yy + 5, t, 22, WHITE, 500, 'middle')
    s += arrow(968, 254, 1032, 254, OR, 5)
    s += box(1040, 44, 624, 420, 'none', TE, 2.5, 20, '10 7')
    for (x, y), (t, sub, ic) in zip([(1060, 64), (1362, 64), (1060, 264), (1362, 264)],
                                    [('サービングのLLM', 'モデルをAPIで呼ぶ', 'cube'), ('Genie', 'データに言葉で答える', 'chat'),
                                     ('自作エージェント', 'Agent Bricksで開発', 'robot'), ('MCPツール', '外部システムへ接続', 'plug')]):
        s += node(x, y, 282, 180, t, sub, ic, tag='arch')
    s += arrow(855, 468, 855, 516, OR) + arrow(1352, 468, 1352, 516, OR)
    s += box(330, 524, 1334, 100, ORT, OR, 2.5)
    s += ico('book', 354, 550, 48, OR)
    s += text(420, 540, 'Unity Catalog', 30, INK, 700)
    s += text(420, 582, 'データ、モデル、ツールの権限、監査、リネージを1つの台帳で管理する', 24, SOFT)
    x = 330
    for t, ic in [('業務システムのDB', 'db'), ('ファイル、文書', 'doc'), ('SaaS', 'plug')]:
        s += node(x, 652, 300, 60, t, icon=ic, theme='plain', ts=23, isz=30, tag='arch')
        s += arrow(x + 150, 650, x + 150, 630, MUTE, 3)
        x += 330
    s += text(1340, 668, 'データ源', 23, MUTE, 700)
    s += text(0, 516, '※ Genieは質問した本人の権限でデータを引く。Unity GatewayがGenieに対して担うのは予算と監査', 21, SOFT, maxw=296, lh=1.5)
    return svg(716, s, label='全体像。利用者、入口、Unity Gateway、AI、Unity Catalogの関係')


def fig_gw():
    s = text(0, 0, '要求が入る', 23, MUTE, 700) + text(1664, 0, '応答が返る', 23, MUTE, 700, 'end')
    st = [('認証', '呼び出し元の身元を確認', 'te'), ('権限', '実行権限の有無を確認', 'te'), ('予算と制限', '予算と毎分の上限を確認', 'te'),
          ('入力検査', '機微データ検出\n（Beta）', 'grey'), ('振り分け', 'モデルへ配分。障害時は代替へ', 'bl'),
          ('出力検査', '応答を検査\n（Beta）', 'grey'), ('記録', '利用量と入出力を保存', 'ink')]
    for i, (t, d, thm) in enumerate(st):
        x = i * 242
        fill, stroke, tc, sc, ic, dash = THEME[thm]
        s += box(x, 44, 212, 258, fill, stroke, 2.5, 14, dash)
        s += text(x + 22, 58, str(i + 1), 44, ic if thm != 'ink' else '#F0A070', 700)
        s += text(x + 22, 122, t, 28, tc, 700)
        s += text(x + 22, 172, d, 23, sc, maxw=170, lh=1.5)
        if i < 6:
            s += f'<path d="M{x + 219} {163}l14 10-14 10z" fill="{MUTE}"/>'
    s += chips(0, 326, ['入る前に止める（1〜3）'], fill=TET, color=TE, weight=700)
    s += chips(330, 326, ['届け先を決める（5）'], fill=BLT, color=BL, weight=700)
    s += chips(620, 326, ['残す（7）'], fill=INK, color=WHITE, weight=700)
    s += chips(790, 326, ['ベータの検査（4、6）。これに依存しない設計にする'], fill=GRT, color=SOFT, weight=700)
    for i, (t, d, ic) in enumerate([('対象', 'Databricks提供のモデル、外部プロバイダのモデル、MCPツールへの要求', 'plug'),
                                    ('アプリから見ると', '接続先は1つ。モデルの追加や切替を、アプリの改修なしで行える', 'app'),
                                    ('性能と上限', '追加の遅延は50ミリ秒未満。要求は4MB、597秒まで', 'gauge')]):
        s += node(i * 564, 404, 536, 216, t, d, ic, theme='plain', ts=28, ss=24, tag='gw')
    return svg(624, s, label='Unity Gatewayの7段階')


def fig_obo():
    s = ''
    s += node(0, 50, 340, 140, 'Aさん（営業部）', '「今月の売上は？」', 'user', ss=25, tag='obo')
    s += node(0, 410, 340, 140, 'Bさん（経理部）', '「今月の売上は？」', 'user', ss=25, tag='obo')
    s += node(480, 216, 300, 170, 'Genie', '本人の身元を引き継いで実行する', 'chat', theme='ink', tag='obo')
    s += node(900, 200, 300, 200, 'Unity Catalog', '行フィルタと列マスクを適用する', 'shield', theme='or', tag='obo')
    s += arrow(348, 130, 472, 270) + arrow(348, 470, 472, 334)
    s += arrow(788, 300, 892, 300, OR, 5)
    s += arrow(1208, 262, 1312, 130, TE) + arrow(1208, 340, 1312, 470, BL)
    s += text(1320, 0, 'Aさんへの回答', 25, TE, 700)
    s += mtable(1320, 42, [172, 172], [['部門', '売上'], ['営業部', '1,200']])
    s += text(1320, 146, '営業部の行だけが返る', 22, SOFT)
    s += text(1320, 352, 'Bさんへの回答', 25, BL, 700)
    s += mtable(1320, 394, [172, 172], [['部門', '売上'], ['営業部', '1,200'], ['経理部', '300'], ['人事部', '150']])
    s += text(1320, 594, '全部門の行が返る', 22, SOFT)
    s += box(0, 610, 1260, 72, GDT, GD, 2)
    s += ico('warn', 22, 628, 36, GD)
    s += text(74, 630, 'アプリ共通の身元で呼ぶと、全員が同じデータを見る。どの身元で呼ぶかを設計で決める。', 24, INK)
    return svg(690, s, label='同じ質問でも、質問した本人の権限で答えが変わる')


def fig_two():
    s = ''

    def panel(x, col, title, flow, rows, fw):
        o = box(x, 0, 800, 596, WHITE, col, 2.5, 16)
        o += f'<path d="M{x} 84V16a16 16 0 0 1 16-16h768a16 16 0 0 1 16 16v68z" fill="{col}"/>'
        o += text(x + 32, 22, title, 30, WHITE, 700)
        n = len(flow); g = (800 - 60 - n * fw) / (n - 1)
        for i, t in enumerate(flow):
            fx = x + 30 + i * (fw + g)
            o += node(fx, 116, fw, 92, t, center=True, ts=23, theme='plain', pad=12, tag='two')
            if i < n - 1:
                o += arrow(fx + fw + 6, 162, fx + fw + g - 6, 162, col, 3)
        for i, (k, v) in enumerate(rows):
            yy = 244 + i * 84
            o += line([(x + 30, yy), (x + 770, yy)], LINE, 2)
            o += text(x + 36, yy + 26, k, 23, MUTE, 700)
            o += text(x + 220, yy + 22, v, 27, INK, 500)
        return o
    s += panel(0, TE, 'サービングのLLM — 部品として呼ぶ', ['アプリ', 'Unity Gateway', 'モデル'],
               [('モデル', '利用側が選ぶ'), ('権限', 'エンドポイントの実行権限'), ('応答', '即時（同期、ストリーミング）'), ('向く用途', '要約、分類、生成の組み込み')], 210)
    s += panel(864, OR, 'Genie — 完成品として使う', ['質問', 'SQLを作る', '本人の権限で実行', '回答'],
               [('モデル', 'Databricksが選ぶ（選べない）'), ('権限', '質問した本人のデータ権限'), ('応答', '数十秒から数分（非同期）'), ('向く用途', '集計、分析、データの問い合わせ')], 158)
    s += box(0, 622, 1664, 64, GRT, GRT)
    s += text(832, 640, 'この2つの間に、SQLからモデルを呼ぶ AI Functions と、独自に作るエージェント（Agent Bricks）がある', 24, SOFT, 500, 'middle')
    return svg(690, s, label='サービングのLLMとGenieの比較')


def fig_mask():
    s = text(0, 0, '元の表（Unity Catalog）', 26, INK, 700)
    s += mtable(0, 46, [130, 150, 130, 220], [['部門', '顧客', '売上', '連絡先'], ['営業', 'A社', '500', '03-1234-5678'], ['経理', 'B社', '300', '06-2345-6789'],
                                               ['営業', 'C社', '700', '052-345-6789'], ['人事', 'D社', '150', '03-4567-8901'], ['経理', 'E社', '220', '092-567-8901']], rh=52)
    s += arrow(640, 202, 704, 202, TE, 5)
    s += node(712, 66, 300, 128, '行フィルタ', '自部門の行だけ通す', 'shield', theme='te', tag='mask')
    s += node(712, 210, 300, 128, '列マスク', '連絡先を伏せる', 'lock', theme='te', tag='mask')
    s += arrow(1020, 202, 1084, 202, TE, 5)
    s += text(1092, 0, '営業部のAさんに見える表', 26, TE, 700)
    s += mtable(1092, 46, [110, 130, 120, 212], [['部門', '顧客', '売上', '連絡先'], ['営業', 'A社', '500', '＊＊＊＊＊＊'], ['営業', 'C社', '700', '＊＊＊＊＊＊']], rh=52, mute={(1, 3), (2, 3)})
    s += box(1092, 202, 572, 156, GRT, MUTE, 2, 0, '8 6')
    s += text(1378, 262, '経理と人事の行は返らない', 23, MUTE, 500, 'middle')
    s += text(0, 410, '入口が違っても、同じ制御がかかる', 26, INK, 700)
    for i, (t, ic) in enumerate([('SQL', 'table'), ('Genie', 'chat'), ('アプリ', 'app'), ('AIエージェント', 'robot')]):
        s += node(i * 428, 458, 380, 84, t, icon=ic, theme='plain', tag='mask')
        s += arrow(i * 428 + 190, 546, i * 428 + 190, 580, TE, 3)
    s += box(0, 586, 1664, 60, TE, TE)
    s += text(832, 601, 'Unity Catalogの行フィルタと列マスクは、どの入口にも共通で効く', 25, WHITE, 700, 'middle')
    return svg(650, s, label='行フィルタと列マスク')


def fig_budget():
    s = box(0, 0, 800, 520, WHITE, LINE)
    s += ico('gauge', 28, 22, 40, RD) + text(82, 26, '予算: 月の上限を決める', 28, INK, 700)
    base = 430
    s += line([(70, base), (760, base)], INK, 2.5)
    s += line([(70, 170), (760, 170)], RD, 3, '10 8') + text(760, 132, '上限', 22, RD, 700, 'end')
    for x, hgt, lab, over in [(110, 150, '受注アプリ', 0), (280, 260, '要約機能', 1), (450, 90, '経理バッチ', 0), (620, 200, '分析チーム', 0)]:
        s += f'<rect x="{x}" y="{base - hgt}" width="110" height="{hgt}" rx="6" fill="{RD if over else BL}"/>'
        s += text(x + 55, base + 14, lab, 22, SOFT, 500, 'middle')
    s += text(335, 96, '上限に達すると停止', 23, RD, 700, 'middle')
    s += line([(335, 132), (335, 160)], RD, 2.5)
    s += box(864, 0, 800, 520, WHITE, LINE)
    s += ico('gauge', 892, 22, 40, RD) + text(946, 26, 'レート制限: 毎分の上限を決める', 28, INK, 700)
    cap = base - 200
    hs = [60, 90, 130, 80, 190, 280, 300, 170, 90, 70, 120, 60]
    for i, hgt in enumerate(hs):
        x = 864 + 80 + i * 54
        ok = min(hgt, 200)
        s += f'<rect x="{x}" y="{base - ok}" width="38" height="{ok}" rx="4" fill="{BL}"/>'
        if hgt > 200:
            s += f'<rect x="{x}" y="{base - hgt}" width="38" height="{hgt - 200}" rx="4" fill="{RDT}" stroke="{RD}" stroke-width="2" stroke-dasharray="5 4"/>'
    s += line([(864 + 60, base), (864 + 760, base)], INK, 2.5)
    s += line([(864 + 60, cap), (864 + 760, cap)], RD, 3, '10 8') + text(864 + 760, cap - 38, '毎分の上限', 22, RD, 700, 'end')
    s += text(864 + 80 + 6 * 54, 78, '超えた要求には429を返す', 23, RD, 700, 'middle')
    s += text(864 + 760, base + 14, '時間', 22, SOFT, 500, 'end')
    s += box(0, 546, 1664, 100, GDT, GD, 2)
    s += ico('warn', 24, 566, 40, GD)
    s += text(84, 560, '予算による停止は近似で、厳密な上限ではない。暴走の抑止はレート制限と併用する。', 24, INK, 500)
    s += text(84, 600, '設定の単位: 予算は全体の月次と、利用者ごとの日次、月次。レート制限は毎分の要求数とトークン数。', 23, SOFT)
    return svg(650, s, label='予算とレート制限')


def fig_logs():
    s = ''
    s += node(0, 70, 300, 164, 'Unity Gateway', 'AIへの要求と応答', 'gate', theme='ink', tag='logs')
    s += node(0, 424, 300, 164, 'Unity Catalog', 'データと権限の操作', 'book', theme='or', tag='logs')
    st = [(0, '利用テーブル', '誰が、どのモデルを、何トークン使ったか', 'list'), (158, '推論テーブル', '入力と出力の本文', 'doc'),
          (354, '監査ログ', '権限の変更、データへのアクセス', 'shield'), (512, 'リネージ', 'どのデータから作られ、どこで使われるか', 'layers')]
    for y, t, d, ic in st:
        s += node(420, y, 600, 140, t, d, ic, theme='plain', ss=24, tag='logs')
    s += arrow(308, 130, 412, 76) + arrow(308, 172, 412, 224)
    s += arrow(308, 484, 412, 430, OR) + arrow(308, 526, 412, 578, OR)
    s += box(1130, 0, 534, 392, WHITE, LINE)
    s += text(1162, 26, '記録の使い道', 28, INK, 700)
    for i, t in enumerate(['部門別の費用の把握', '異常な利用の検知', '事故が起きたときの調査', '変更の影響調査']):
        s += ico('check', 1162, 94 + i * 72, 36, TE) + text(1214, 96 + i * 72, t, 26, INK)
    s += arrow(1028, 196, 1122, 196, MUTE)
    s += box(1130, 420, 534, 232, RDT, RD, 2.5)
    s += ico('warn', 1158, 444, 40, RD) + text(1212, 448, '記録そのものが機微情報', 27, RD, 700)
    s += text(1162, 512, '入出力の本文にはマスクがかからない。保存先の権限と保持期間を先に決める。', 24, INK, maxw=470, lh=1.55)
    return svg(656, s, label='記録の種類と使い道')


def fig_region():
    s = box(0, 0, 880, 500, TET, TE, 2.5, 24)
    s += ico('shield', 32, 26, 44, TE) + text(92, 30, '国内で処理される（東京のワークスペース）', 28, TE, 700)
    for i, t in enumerate(['日本の階層に属するモデル\n（例: Claude Opus 5.5、Haiku 5.5）', 'Genie Agents（チャット、エージェント）', 'Genie Code', 'Genie Oneのチャット']):
        y = 108 + i * 96
        s += ico('check', 40, y, 38, TE) + text(96, y - (16 if i == 0 else -2), t, 26, INK, 500, lh=1.4)
    s += box(1000, 0, 664, 500, GRT, MUTE, 2.5, 24, '10 7')
    s += ico('globe', 1032, 26, 44, SOFT) + text(1092, 30, '地域をまたいで処理される', 28, SOFT, 700)
    for i, t in enumerate(['グローバルエンドポイントのモデル', 'Genie OneのWeb検索', 'エージェントモードの高速版（Flash）', 'Genie App Builder']):
        y = 108 + i * 96
        s += ico('globe', 1040, y, 38, MUTE) + text(1096, y + 2, t, 26, INK, 500)
    s += f'<rect x="896" y="216" width="88" height="44" rx="22" fill="{OR}"/><circle cx="962" cy="238" r="16" fill="#fff"/>'
    s += text(940, 174, '設定', 22, OR, 700, 'middle') + text(940, 270, 'オン', 22, OR, 700, 'middle') + text(940, 300, '（既定）', 20, SOFT, 400, 'middle')
    s += box(0, 528, 1664, 112, GDT, GD, 2)
    s += ico('warn', 24, 552, 40, GD)
    s += text(84, 546, '「地域をまたぐ処理」は既定でオン。オフにすると右側は使えなくなるが、左側は国内処理のまま使える。', 24, INK, 500)
    s += text(84, 590, '最上位のモデルは提供元で30日保持される。保持を認めない業務では使わない。', 24, SOFT)
    return svg(644, s, label='東京のワークスペースでの処理地域')


def fig_uses():
    s = ''
    items = [('データに言葉で質問する', 'Genie One、Genie Agents', 'chat', '従業員が、業務データに自然な言葉で質問する。SQLを書けなくても集計と分析ができる。', '例: 先月、解約が多かった商品は？'),
             ('業務アプリにAIを組み込む', 'Model Serving、Databricks Apps', 'app', '既存の業務システムや社内アプリから、モデルやエージェントをAPIで呼ぶ。', '例: 問い合わせ文の要約と分類'),
             ('大量のデータをまとめて処理する', 'AI Functions', 'layers', 'SQLの中でモデルを呼び、表の全行に一括で適用する。', '例: 契約書10万件から項目を抽出'),
             ('業務知識を1か所で引く', 'Unity Catalog、Genie Search', 'book', '指標、用語、文書、システム間の依存を1つの台帳に集める。', '例: 仕様変更の影響調査、企画の根拠集め')]
    for i, (t, f, ic, d, ex) in enumerate(items):
        x = (i % 2) * 846; y = (i // 2) * 344
        s += box(x, y, 818, 320, WHITE, LINE, 2, 18)
        s += f'<circle cx="{x + 80}" cy="{y + 84}" r="50" fill="{BLT}"/>' + ico(ic, x + 54, y + 58, 52, BL, 1.7)
        s += badge(x + 122, y + 44, i + 1, 20, BL)
        s += text(x + 158, y + 42, t, 33, INK, 700)
        s += text(x + 158, y + 96, f, 23, BL, 700)
        s += text(x + 40, y + 164, d, 25, SOFT, maxw=740, lh=1.5)
        s += box(x + 40, y + 250, 738, 48, BLT, BLT, 0, 10) + text(x + 60, y + 258, ex, 23, INK, 500)
    return svg(664, s, label='実現できる4つのこと')


def fig_genie():
    s = box(0, 0, 760, 690, WHITE, INK, 2.5, 18)
    s += f'<path d="M0 62V18a18 18 0 0 1 18-18h724a18 18 0 0 1 18 18v44z" fill="{INK}"/>'
    s += ico('chat', 24, 14, 34, '#F0A070') + text(70, 14, 'Genie One', 25, WHITE, 700) + text(736, 18, '画面はイメージ', 20, '#C9D2E3', 400, 'end')
    s += box(322, 92, 410, 62, BLT, BLT, 0, 22) + text(346, 106, '先月、解約が多かった商品は？', 24, INK, 500)
    s += box(28, 186, 640, 404, GRT, GRT, 0, 22)
    s += text(54, 206, '解約は商品Bが最も多く、前月から増えています。', 24, INK, 500)
    for x, hgt, lab, c in [(100, 90, '商品A', BL), (250, 200, '商品B', OR), (400, 120, '商品C', BL)]:
        s += f'<rect x="{x}" y="{480 - hgt}" width="100" height="{hgt}" rx="6" fill="{c}"/>' + text(x + 50, 490, lab, 21, SOFT, 500, 'middle')
    s += line([(70, 480), (540, 480)], INK, 2)
    c, _ = chip(54, 532, '根拠のSQLを表示', fill=WHITE, stroke=LINE, size=21, h=42)
    s += c
    s += box(28, 612, 704, 56, WHITE, LINE, 2, 28) + text(56, 626, '質問を入力', 22, MUTE)
    s += text(850, 0, '答えが返るまでの流れ', 25, MUTE, 700)
    steps = [('対象を選ぶ', '登録した表、指標、例示SQLから候補を絞る'), ('SQLを作る', '質問の意図をSQLに変換する'),
             ('本人の権限で実行する', '見てよい行と列だけが対象になる'), ('答えと根拠を返す', '結果と一緒に、実行したSQLを確認できる')]
    s += line([(878, 80), (878, 80 + 3 * 104)], LINE, 4)
    for i, (t, d) in enumerate(steps):
        y = 50 + i * 104
        s += badge(878, y + 30, i + 1, 28, TE)
        s += text(930, y, t, 29, INK, 700) + text(930, y + 46, d, 23, SOFT)
    s += text(850, 478, '精度を上げる材料', 24, INK, 700)
    s += chips(850, 520, ['指標（メトリックビュー）', '例示SQL', '指示', '用語（Pages）'], fill=TET, color=TE, weight=700)
    s += text(850, 590, '使える入口', 24, INK, 700)
    s += chips(850, 632, ['Genie One', 'Slack', 'Teams', 'API、MCP'], fill=BLT, color=BL, weight=700)
    return svg(690, s, label='Genieに質問して答えが返るまで')


def fig_patterns():
    s = ''
    P = [('Databricksの中にアプリを作る', [('従業員', 0), ('Databricks Apps', 1), ('モデル、Genie', 1)], 'データに近い、社内向けの画面'),
         ('業務システムからモデルを呼ぶ', [('業務システム', 0), ('Unity Gateway', 1), ('サービングのLLM', 1)], '既存システムへの要約、分類、生成の追加'),
         ('業務システムからエージェントを呼ぶ', [('業務システム', 0), ('API、MCP', 1), ('Genie、自作エージェント', 1)], 'データに関する問い合わせ機能'),
         ('SQLのジョブで一括処理する', [('SQLのジョブ', 1), ('AI Functions', 1), ('結果のテーブル', 1)], '大量の文書や明細の一括処理')]
    for i, (t, flow, use) in enumerate(P):
        x = (i % 2) * 846; y = (i // 2) * 348
        s += box(x, y, 818, 320, WHITE, LINE, 2, 18)
        s += badge(x + 52, y + 52, i + 1, 28, BL) + text(x + 98, y + 30, t, 31, INK, 700)
        for j, (n, db) in enumerate(flow):
            fx = x + 30 + j * 269
            s += node(fx, y + 112, 220, 96, n, center=True, ts=24, theme='or' if db else 'white', pad=12, tag='pat')
            if j < 2:
                s += arrow(fx + 226, y + 160, fx + 263, y + 160, INK, 3)
        s += text(x + 32, y + 244, '向く場面', 22, BL, 700) + text(x + 140, y + 242, use, 25, INK, 500)
    return svg(668, s, label='業務アプリへの組み込みの4つの型')


def fig_apps():
    s = box(330, 0, 1334, 560, 'none', TE, 2.5, 24, '10 7')
    s += text(356, 16, 'Databricksのワークスペース（社内のSSOで入る。公開と匿名アクセスはできない）', 23, TE, 700)
    s += node(0, 226, 250, 130, '従業員', 'SSOでログイン', 'user', tag='apps')
    s += arrow(258, 291, 372, 291, INK, 4)
    s += node(380, 190, 330, 202, 'Databricks Apps', 'サーバーレスのコンテナ。最大5インスタンス', 'app', theme='ink', ss=24, tag='apps')
    for y, col, tint, lab, nodes in [(70, TE, TET, '利用者の権限で呼ぶ — 参照と質問', [('SQLウェアハウス', '本人に見える行と列だけ', 'table'), ('Genie', '本人の権限で答える', 'chat')]),
                                     (316, OR, ORT, 'アプリの権限で呼ぶ — 書き込みと共通処理', [('Lakebase', 'アプリの状態と更新データ', 'db'), ('Unity Gateway', 'モデルの呼び出しと記録', 'gate')])]:
        s += box(800, y, 840, 226, tint, col, 2.5, 18)
        s += text(826, y + 16, lab, 24, col, 700)
        for j, (t, d, ic) in enumerate(nodes):
            s += node(824 + j * 404, y + 66, 388, 136, t, d, ic, theme='plain', ss=24, tag='apps')
    s += arrow(718, 256, 792, 190, TE, 4) + arrow(718, 326, 792, 424, OR, 4)
    for i, (t, ic) in enumerate([('自動スケールはなく、稼働中は常時課金', 'gauge'), ('バンドルで管理し、Gitからデプロイ', 'layers'), ('利用者の権限での実行は一般提供済み', 'check')]):
        s += node(i * 564, 590, 536, 76, t, icon=ic, theme='plain', ts=23, isz=34, tag='apps')
    return svg(670, s, label='Databricks Appsの構成')


def fig_know():
    s = text(0, 0, '原本は発生源に置く', 23, MUTE, 700) + text(500, 0, '台帳は1つ', 23, MUTE, 700) + text(1220, 0, '参照口は1つ', 23, MUTE, 700)
    for y, (t, d, ic) in zip([44, 190, 336], [('業務システム', 'テーブル定義と依存関係', 'bld'), ('文書', 'Drive、Jira、Confluence', 'doc'), ('人', '用語、指標の定義、経緯', 'user')]):
        s += node(0, y, 390, 136, t, d, ic, tag='know')
    s += arrow(398, 108, 492, 170) + arrow(398, 252, 492, 252) + arrow(398, 396, 492, 334)
    s += box(500, 44, 600, 416, INK, INK, 2, 20)
    s += ico('book', 530, 66, 46, '#F0A070') + text(592, 72, 'Unity Catalog — 知識の台帳', 29, WHITE, 700)
    for i, (k, v) in enumerate([('指標', 'メトリックビュー'), ('用語と経緯', 'Pages'), ('文書の索引', 'Genie Search'), ('依存関係', 'リネージ、外部リネージ')]):
        y = 140 + i * 76
        s += box(528, y, 544, 62, NAVY2, '#3A4A70', 1.5, 10)
        s += text(548, y + 15, k, 22, '#F0A070', 700) + text(720, y + 13, v, 25, WHITE, 500)
    s += arrow(1108, 170, 1212, 130, OR, 4) + arrow(1108, 334, 1212, 374, OR, 4)
    s += node(1220, 44, 444, 180, 'Genie One', '従業員が質問する窓口', 'chat', theme='or', ss=24, tag='know')
    s += node(1220, 280, 444, 180, 'Genie One MCP', 'アプリとエージェントが同じ台帳を引く', 'plug', theme='or', ss=24, tag='know')
    s += node(0, 500, 818, 170, '影響調査', 'リネージと用語から、変更が及ぶテーブル、システム、指標を追う', 'search', theme='bl', ts=30, ss=25, tag='know')
    s += node(846, 500, 818, 170, '企画立案', '指標、文書、用語を同じ窓口から引き、現状と根拠を集める', 'gauge', theme='bl', ts=30, ss=25, tag='know')
    return svg(674, s, label='業務知識の集約')


def fig_infra():
    s = node(0, 196, 236, 170, '入口', '社内ネットワークとSSOに限定', 'lock', tag='infra')
    s += arrow(244, 281, 292, 281, INK, 4)
    s += box(300, 0, 1064, 596, 'none', TE, 2.5, 24, '10 7')
    s += text(326, 16, 'Databricksアカウント（東京リージョン、メタストアは1つ）', 23, TE, 700)
    for x, (t, d) in zip([324, 668, 1012], [('開発ワークスペース', '開発と検証'), ('本番ワークスペース', '業務アプリとジョブ。本番カタログだけを紐付ける'), ('AI利用ワークスペース', '従業員のAI利用。予算と地域設定を分ける')]):
        s += node(x, 62, 328, 176, t, d, theme='white', ts=26, ss=23, tag='infra')
        s += arrow(x + 164, 242, x + 164, 284, OR, 3)
    s += box(324, 290, 1016, 284, ORT, OR, 2.5, 18)
    s += ico('book', 348, 310, 42, OR) + text(404, 312, 'Unity Catalog', 28, INK, 700) + text(640, 316, 'カタログは「環境 × 業務領域」で作る', 24, SOFT)
    s += chips(348, 384, ['開発 × 営業', '開発 × 経理', '本番 × 営業', '本番 × 経理'], fill=WHITE, stroke=OR, size=24, h=52, gap=20)
    s += chips(348, 462, ['共有', '知識（台帳）', 'AI（モデル、ツール）'], fill=WHITE, stroke=OR, size=24, h=52, gap=20)
    s += text(1020, 474, '領域をまたぐもの', 22, SOFT)
    s += arrow(1372, 281, 1420, 281, INK, 4)
    s += node(1428, 196, 236, 170, '出口', '許可した宛先だけに通信する', 'shield', tag='infra')
    s += node(0, 620, 1664, 64, '構成管理: 基盤はTerraform、アプリとジョブはバンドル。AI利用ワークスペースは本資料の提案（公式の指針は開発と本番の分離まで）', icon='gear', theme='grey', ts=22, isz=32, tag='infra')
    return svg(688, s, label='インフラの構成')


def fig_cover():
    s = ''
    for i, (t, ic, y) in enumerate([('入口', 'chat', 0), ('通り道', 'gate', 150), ('台帳', 'book', 300)]):
        s += f'<rect x="{i * 36}" y="{y}" width="{520 - i * 36}" height="118" rx="18" fill="{NAVY2}" stroke="#3A4A70" stroke-width="2"/>'
        s += ico(ic, i * 36 + 30, y + 34, 50, '#F0A070', 1.6)
        s += text(i * 36 + 104, y + 38, t, 34, WHITE, 700)
        if i < 2:
            s += f'<path d="M260 {y + 122}v22" stroke="#F0A070" stroke-width="4" stroke-linecap="round"/>'
    return svg(420, s, w=520, label='入口、通り道、台帳')
