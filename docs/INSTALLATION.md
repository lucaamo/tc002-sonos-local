# Installation and troubleshooting

## Requirements

Use a TC002 with the official AWTRIX NG firmware and its Berry script editor. Release 0.2.9 was checked on 1.2.2 with a 52×16 display; earlier revisions were developed on 1.1.7. A TC001 / 32×8 panel is not supported.

The TC002 must be able to reach one Sonos speaker and the other rooms on the same LAN, including Sonos HTTP/SOAP on port 1400. Music services are configured in the Sonos app; this project has no Spotify OAuth or account credentials on the clock.

## Manual installation

1. Download the repository or release archive.
2. In the TC002 Web UI, open the Scripts / Berry editor.
3. Add `modules/sonos_local_protocol.ax` as **sonos_local_protocol**, save and check that there is no compile error.
4. Add `modules/sonos_local_ui.ax` as **sonos_local_ui**, save and check that there is no compile error. Both helpers use `@module` and are not carousel apps.
5. Add `apps/sonos_local_probe.ax` as **sonos_local_probe**, save and check that there is no compile error.
6. Open this app's settings. Enter a Sonos speaker IP under **IP Sonos iniziale / Seed IP**, choose **Lingua / Language**, and save.
7. Optionally choose **Startup screen → Now Playing** to open current playback directly. **Menu** remains the default; this setting does not start or resume music. Save and reopen the app after changing it.
8. Launch **Sonos Remote Local** from the device menu or Web UI. Allow the bounded catalog scan to finish before selecting favorites.

For an update, back up your scripts and settings, replace the helpers before the main app, retain the same script names, and check the seed IP and language before relaunching. The existing Home Assistant Sonos Remote app can remain installed.

## Settings

| Setting | Default | Effect |
| --- | --- | --- |
| Language | Italiano | Italian or English interface; restart the app after changing |
| Seed IP | Empty | IP of one Sonos speaker; required |
| Page size | 5 | Favorites returned by each catalog request; maximum 5 |
| Favorite limit | 128 | Combined bounded catalog capacity; maximum 256 |
| Direct artwork | On | Display available track / station artwork |
| Custom radio logos | On | Use native symbols for twelve recognized stations |
| Volume step | 1 | Percentage points per left / right button action |
| Knob hold | 700 ms | Hold threshold for back / menu |
| Message time | 4 s | Temporary status text duration |
| Request timeout | 35 s | Maximum wait per Sonos request, without command retry |
| Context time | 6 s | Room / source information duration during music |
| Scroll speed | 80 | Speed of scrolling text |

Last room and last category are remembered by the app. The seed, language and ordinary options are configured through the Web UI; do not hard-code account data into the script.

## Common issues

**Set Sonos IP / no players:** verify the seed, speaker availability and network reachability. A speaker IP can change after a router restart; a DHCP reservation helps. The app reads topology from the seed and follows existing group coordinators.

**A playlist is missing:** save it in Sonos favorites or as a Sonos playlist. The app reads `FV:2` plus `SQ:`, not the entire streaming-service library. Choose Refresh favorites after editing them. Check the favorite limit for a larger collection.

**Track unavailable:** the Sonos source does not currently expose the requested transport action. Radio playback uses station changes instead of track skips; choose stations from Sonos favorites.

**Waiting for Sonos:** an individual request is in progress. The newest radio selection remains pending. If the timeout occurs, an error is shown and the app does not retry audio commands automatically. Refresh or reopen after resolving the network / service issue.

**Artwork fails:** artwork availability and decoding depend on the source and firmware. Custom radio symbols are independent of downloads; other sources show a visible radio fallback if their image cannot be drawn.

**No song title on radio:** Sonos must provide readable track metadata. The app reads plain text and supported structured fields, and hides stream filenames and technical placeholders. Without usable metadata, the room, volume and playback state are shown. When updating, replace both helpers (protocol 0.2.4, UI 0.2.9) and the main app (0.2.9).

**A playlist grows the queue:** the implementation adds the playlist to the existing Sonos queue and starts at its first added item. Repeated starts can append repeated entries. Clear the queue in the Sonos app if desired.

**Volume changes only one member of a group:** this is intentional. Volume follows the selected room; playback follows that room's coordinator.

**The display returns to the carousel:** the main script must retain `@ondemand`. Hold the top middle button to exit normally. If it exits without that action, check the script compile/runtime error in the Web UI and report the firmware version and trigger.
