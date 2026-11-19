# Couch Player demo playlist

A small, legal demo playlist for trying Couch Player and for app store review.

- **Playlist (M3U):** `https://para9bellum9.github.io/couch-demo/demo.m3u`
- **TV guide (XMLTV):** `https://para9bellum9.github.io/couch-demo/epg.xml` (picked up from the playlist automatically)

The guide is made up and is rebuilt daily by a GitHub Action, so it always covers today and the next two weeks.

## What's in it

| Channel | Stream | Content and license |
|---|---|---|
| Couch Toons HD | Mux public test stream | *Big Buck Bunny* (c) Blender Foundation, peach.blender.org, CC BY 3.0 |
| Couch Fantasy HD | Bitmovin public demo stream | *Sintel* (c) Blender Foundation, durian.blender.org, CC BY 3.0 |
| Couch Sci-Fi 4K | Unified Streaming public demo | *Tears of Steel* (c) Blender Foundation, mango.blender.org, CC BY 3.0 |
| Couch Test Card HD | Apple's public HLS example stream | Apple sample content, published for testing HLS players |
| Couch Live Test | Akamai's public live test stream | Akamai test content, published for testing players |

The streams are hosted by the companies above, not by this repository. Channel names, logos and guide data are original to this demo.
Couch Player itself does not provide or sell any content.

## Editing

Change `channels.py`, then run `python build.py` (or push and let the Action do it).
