"""Writes demo.m3u and epg.xml (guide from yesterday through the next 14 days, in 30-minute slots)."""
import datetime as dt
from xml.sax.saxutils import escape, quoteattr
from channels import BASE, CHANNELS

DAYS_AHEAD = 14
SLOT = dt.timedelta(minutes=30)

def m3u():
    lines = [f'#EXTM3U url-tvg="{BASE}/epg.xml" x-tvg-url="{BASE}/epg.xml"']
    for c in CHANNELS:
        lines.append(f'#EXTINF:-1 tvg-id="{c["id"]}" tvg-name="{c["name"]}" tvg-logo="{BASE}/logos/{c["logo"]}.png" '
                     f'group-title="{c["group"]}",{c["name"]}')
        lines.append(c["url"])
    return "\n".join(lines) + "\n"

def epg(now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    start = (now - dt.timedelta(days=1)).replace(minute=0, second=0, microsecond=0)
    end = now + dt.timedelta(days=DAYS_AHEAD)
    fmt = lambda t: t.strftime("%Y%m%d%H%M%S +0000")
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<tv generator-info-name="Couch Player demo">']
    for c in CHANNELS:
        out.append(f'  <channel id={quoteattr(c["id"])}><display-name>{escape(c["name"])}</display-name>'
                   f'<icon src={quoteattr(BASE + "/logos/" + c["logo"] + ".png")}/></channel>')
    for n, c in enumerate(CHANNELS):
        t, i = start, n  # offset each channel so the guide doesn't look identical in every row
        while t < end:
            title, desc = c["shows"][i % len(c["shows"])]
            out.append(f'  <programme start="{fmt(t)}" stop="{fmt(t + SLOT)}" channel={quoteattr(c["id"])}>'
                       f'<title lang="en">{escape(title)}</title><desc lang="en">{escape(desc)}</desc></programme>')
            t += SLOT
            i += 1
    out.append('</tv>')
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    open("demo.m3u", "w").write(m3u())
    open("epg.xml", "w").write(epg())
    print("wrote demo.m3u and epg.xml")
