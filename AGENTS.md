# お祭り.net（xn--t8j0g025t.net）作業ルール

GitHub Pages で公開する静的サイト。tools/build.py が tools/content/*.html から全ページを生成する（戦車.comの仕組みを流用）。

## ページの元ファイル
- tools/content/matsuri__<slug>.html → /matsuri/<slug>/（お祭りガイド）。matsuri__index.html → /matsuri/。calendar.html → /calendar/。index.html → /
- slug は英小文字と数字のみ（ハイフン不可）
- 1行目：<title>（末尾「｜お祭り.net」）、2行目：meta description（120字以内）、3行目以降：本文HTML
- 本文は `<h1>`、`<p class="updated">最終確認日：YYYY年M月D日</p>`、導入の `<p>`、そのあと素の `<h2>` 見出しと <p>/<ul>/<h3>/<table> だけ。最初の表は縦型（<th>項目</th><td>値</td>）
- 最後は `<section class="sources"><h2>出典</h2><ul>…</ul></section>`
- calendar.html の「開催日（…年）」の表：開催日／お祭り／都道府県／場所／見どころ／公式ページ の6列。開催日は「2027年1月15日（金）」のように年を入れる。トップの「次のお祭り」3件はこの表から毎日自動で選ばれる
- 写真：tools/photos/targets.tsv に slug と日本語名を足すと Actions が Wikimedia Commons から取得

## 守ること
- 日程・時刻・料金は主催者・自治体・観光協会・文化庁・観光庁・JNTOなど公式の情報源で確かめたものだけ。Wikipedia・個人ブログ・まとめサイトは使わない
- その年の発表がない日程は「未発表」。「毎年○日」とされていても、年の発表を確認してから表に載せる
- 確かめられない数字・日付は書かない。資料で違うときはそのことを書く
- 1ページ本文3,000文字以上（トップ・一覧・カレンダー・規約ページを除く。一覧はお祭りが増えれば自然に長くなる）。使い回し・数合わせのページは作らない
- 公式サイトと誤解されない書き方（個人運営・非公式）
