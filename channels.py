# The demo channels. Every stream is openly licensed or published by its owner for testing players.
BASE = "https://para9bellum9.github.io/couch-demo"

CHANNELS = [
    dict(id="couch.toons", name="Couch Toons HD", logo="toons", group="Demo · Open Movies",
         url="https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
         shows=[("Big Buck Bunny", "A giant rabbit takes on three bullying rodents. Animated short by the Blender Foundation (2008), CC BY 3.0."),
                ("Big Buck Bunny: Encore", "Another chance to catch Blender's classic open movie. (c) Blender Foundation, peach.blender.org, CC BY 3.0.")]),
    dict(id="couch.fantasy", name="Couch Fantasy HD", logo="fantasy", group="Demo · Open Movies",
         url="https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8",
         shows=[("Sintel", "A young woman searches for her lost dragon friend. Open movie by the Blender Foundation (2010), CC BY 3.0."),
                ("Sintel: The Search Continues", "Blender's fantasy short. (c) Blender Foundation, durian.blender.org, CC BY 3.0.")]),
    dict(id="couch.scifi", name="Couch Sci-Fi 4K", logo="scifi", group="Demo · Open Movies",
         url="https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8",
         shows=[("Tears of Steel", "Scientists in Amsterdam try to save the world from robots. Open movie by the Blender Foundation (2012), CC BY 3.0."),
                ("Tears of Steel: Late Show", "Blender's live-action sci-fi short. (c) Blender Foundation, mango.blender.org, CC BY 3.0.")]),
    dict(id="couch.testcard", name="Couch Test Card HD", logo="testcard", group="Demo · Test Signals",
         url="https://devstreaming-cdn.apple.com/videos/streaming/examples/img_bipbop_adv_example_fmp4/master.m3u8",
         shows=[("Picture Check", "Apple's public HLS example stream, with several qualities, audio tracks and subtitles."),
                ("Audio & Subtitle Check", "Try the audio and subtitle menus in the player. Apple's public HLS example stream.")]),
    dict(id="couch.live", name="Couch Live Test", logo="live", group="Demo · Test Signals",
         url="https://cph-p2p-msl.akamaized.net/hls/live/2000341/test/master.m3u8",
         shows=[("Live Test Signal", "A real live stream published by Akamai for testing players."),
                ("Live Test Signal: Overnight", "Akamai's public live test stream.")]),
]
