# Testing and verification

Release 0.2.9 uses app/UI 0.2.9 and protocol helper 0.2.4, matching the locally verified runtime bodies. Distribution headers add display and Hub dependency metadata.

## Isolated Berry checks

`tests/sonos_local_checks.ax` exercises protocol and UI using a recorder transport and loopback fixture data. It sends no real HTTP or Sonos audio commands and makes no app-setting writes. The publication check on 0.2.7 passed 135 checks covering request sequencing, SOAP payloads, room / coordinator routing, combined catalogs, queue playback, radio switching while busy, timeout handling, language, labels and button behavior.

The 0.2.8 release passed 167 checks on TC002 firmware 1.2.0, including real observed radio metadata formats, missing/technical titles, song updates, state and volume feedback priorities, and stale metadata after room/station changes.

To run it yourself, install the two helpers, install the check script under a separate name, then launch it from the Web UI. Inspect its `shared` result and the rendered check display. Keep it separate from the main app.

## Startup screen — 0.2.9

177 isolated checks passed on official TC002 firmware 1.2.2. The ten additional
checks cover Menu/Now Playing selection, missing or unknown settings, remembered
category, current music/radio, paused/stopped playback, unavailable rooms,
long-press menu access/cancellation and a short click as the only explicit
resume action. The recorder transport sends no real HTTP or audio commands.

A separate real-device transport allowed only Sonos description, topology,
status and catalog reads and rejected write actions. Both Menu and Now Playing
launched successfully, each with eleven read requests, zero write actions and
no errors. Native framebuffer captures verified the menu and current music
with artwork. Temporary diagnostics were removed. Existing settings and all
unrelated scripts, as well as the separate TC001, were compared and preserved.

## Native pixels

All twelve station symbols were verified against the TC002 framebuffer during development. In 0.2.7, the revised Capital, Kiss Kiss and Lattemiele symbols were each checked for exact 256-pixel output; the other nine were preserved. Radio 105, Radio Bruno and Ciccio Riccio also remain byte-identical to the original approved asset files.

Run `python3 tools/build_radio_logos.py --check-ui` to reproduce the assets and compare their native packed data with the UI. This host-side check does not contact Sonos or the clock.

## Real-device reads and audio

Development checks on official TC002 firmware 1.1.7 read the Sonos topology, friendly names, favorites, saved playlists and playback information. The user's collection contained eight playlists and twelve stations after the catalogs were combined; these are sample counts, not app limits.

The 0.2.8 release was also checked on official TC002 firmware 1.2.0 with live radio metadata. The production app displayed the actual station and song, with a native framebuffer capture; these checks did not send audio controls. Temporary diagnostic apps were removed afterwards.

A real playlist start was confirmed by the user. Audio actions across all providers, group configurations, previous / next behavior and volume have not all been certified by physical end-to-end checks. Automated fake-transport checks verify implementation behavior, not provider compatibility.

`tests/sonos_local_read_ui.ax` is an optional separate diagnostic that explicitly rejects Sonos write actions and previews catalogs / artwork from your network. Configure its seed before use. Its results can contain room names and URIs; keep them private unless you sanitize them.

The radio preview was rendered by the actual TC002 with static fixture data, without invoking HTTP or audio controls. Other repository preview images combine that frame with native pixel assets. No private device snapshots or household identifiers are included.
