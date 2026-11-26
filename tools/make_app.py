#!/usr/bin/env python3
"""お祭りカレンダーアプリ（/app/）用のデータ app/festivals.json を、tools/content/calendar.html の表から作る。
build.py の最後に呼ばれる。日付はカレンダーの表（公式発表で確かめたもの）だけを使う。"""
import json, os, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def strip(s): return re.sub(r"<[^>]+>", "", s).strip()

def parse_range(text, yr):
    t = strip(text)
    m = re.search(r"(?:(20\d\d)年)?(\d{1,2})月(\d{1,2})日", t)
    if not m: return None, None
    y, mo, d = int(m.group(1) or yr), int(m.group(2)), int(m.group(3))
    start = datetime.date(y, mo, d)
    end = start
    r = re.search(r"〜\s*(?:(\d{1,2})月)?(\d{1,2})日", t[m.end():])
    if r:
        emo = int(r.group(1) or mo); ed = int(r.group(2))
        ey = y + (1 if emo < mo else 0)
        end = datetime.date(ey, emo, ed)
    return start.isoformat(), end.isoformat()

def main():
    src = open(os.path.join(ROOT, "tools", "content", "calendar.html"), encoding="utf-8").read()
    items = []
    for t in re.findall(r"<table.*?</table>", src, re.S):
        hd = re.search(r"<th>(開催日[^<]*)</th>", t)
        if not hd: continue
        yr = re.search(r"(20\d\d)", hd.group(1)); yr = int(yr.group(1)) if yr else 2026
        for tr in re.findall(r"<tr>(.*?)</tr>", t, re.S):
            td = re.findall(r"<td>(.*?)</td>", tr, re.S)
            if len(td) < 6: continue
            start, end = parse_range(td[0], yr)
            if not start: continue
            link = re.search(r'href="([^"]+)"', td[1]) or re.search(r'href="([^"]+)"', td[5])
            items.append({"start": start, "end": end, "dateText": strip(td[0]), "name": strip(td[1]),
                          "pref": strip(td[2]), "place": strip(td[3]), "highlight": strip(td[4]),
                          "url": link.group(1) if link else "/calendar/"})
    items.sort(key=lambda x: x["start"])
    out = {"updated": datetime.date.today().isoformat(), "source": "お祭り.net カレンダー（主催者・自治体・観光協会の公式発表で確認した日程）", "items": items}
    os.makedirs(os.path.join(ROOT, "app"), exist_ok=True)
    p = os.path.join(ROOT, "app", "festivals.json")
    json.dump(out, open(p + ".tmp", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(p + ".tmp", p)
    print("app items", len(items))

if __name__ == "__main__":
    main()
