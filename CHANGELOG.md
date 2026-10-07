# Changelog

## 0.2.9 — 2026-10-07

- Add **Startup screen: Menu / Now Playing**, with Menu as the existing default.
- Open the remembered room's current music or radio screen without starting, resuming or changing playback.
- Keep the long knob press as the route back to the main menu.
- Preserve existing settings and fall back to Menu for missing or unrecognized startup values.
- 177 isolated Berry checks passed on official TC002 firmware 1.2.2. Both startup views were also checked against live Sonos data with a read-only transport.
- App and UI version: 0.2.9. Protocol helper remains 0.2.4.

## 0.2.8 — 2026-10-05

- Show the current radio song and artist when readable Sonos metadata is available.
- Parse DIDL, plain ICY text, TYPE=SNG fields and Song packets without displaying stream filenames, placeholders, query parameters or identifiers.
- Keep station names and symbols visible; preserve room, volume and playback state as the fallback.
- Clear previous song metadata when changing room or station.
- 167 isolated Berry checks passed on TC002 firmware 1.2.0, with zero real HTTP or audio commands.
- App and UI version: 0.2.8. Protocol helper version: 0.2.4.

## 0.2.7 — 2026-10-04

- Revised native 16×16 symbols for Radio Capital, Radio Kiss Kiss and Radio Lattemiele.
- Preserved the approved Radio 105, Radio Bruno and front-facing Ciccio Riccio symbols and the other six station symbols.
- First separate GitHub / AWTRIX Hub distribution of Sonos Remote Local, with installation instructions and dependency declarations.
- App and UI version: 0.2.7. Protocol helper version: 0.2.3.

## Earlier local beta development

- Added room selection, clear knob menus, selected-room volume and coordinator-based playback controls.
- Added Italiano / English settings and an on-screen controls guide.
- Combined Sonos favorites and saved Sonos playlists; fixed queue-based playlist playback and source-aware track navigation.
- Changed radio knob behavior to previous / next favorite station, with a pending choice while Sonos is busy and bounded request timeouts.
- Replaced technical radio stream filenames with station, room, playback state and volume information.
- Added twelve custom native radio symbols and an original-artwork option.
- Kept the app open on demand, with the middle-button hold as the native exit.
