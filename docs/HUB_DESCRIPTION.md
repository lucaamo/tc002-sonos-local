## Sonos Remote Local — v0.2.9

A **direct Sonos remote for the AWTRIX NG TC002 (52×16)**. The Berry app runs on the clock and communicates with Sonos over your local network using HTTP/SOAP. **No Home Assistant, MQTT broker, computer or bridge is required at runtime.** Audio continues to play on Sonos; music services retain their normal account and internet requirements.

Developed for **official, unmodified AWTRIX NG firmware**, version 0.2.9 checked on **TC002 firmware 1.2.2**. This is a separate project from the earlier [Sonos Remote for Home Assistant](https://github.com/lucaamo/tc002-sonos-remote), which can remain installed.

### New in 0.2.9

**Choose the startup screen: Menu or Now Playing.** Open the app directly on the remembered room's current music or radio, including available metadata and artwork. Opening the screen does not start a playlist, change source or resume paused music. Menu remains the default. Hold the knob to reach Playlists, Radio and Player from Now Playing.

**Updating from 0.2.8:** update the UI helper and main app to **0.2.9**; the protocol helper remains **0.2.4**. Keep the existing script names and settings.

### What it does

- **Choose a room by its friendly name.** Playback follows its existing group coordinator; volume controls the selected room.
- **Browse playlists and favorite radio stations.** The app combines Sonos favorites (`FV:2`) with saved Sonos playlists (`SQ:`), including service playlists saved to Sonos. Duplicate playlist URIs are removed.
- **Use the knob while playing:** music → previous/next track when supported; radio → previous/next favorite station. Rapid radio changes retain the newest requested station while Sonos finishes the current request.
- **Read useful display information:** station name/logo and available song title/artist for radio; room, volume and playback state when metadata is unavailable. Music shows artist, track title and available artwork. Full names scroll; technical radio stream filenames are hidden.
- **Twelve custom native 16×16 radio symbols**, with an option to prefer original artwork: 105, Bruno, Ciccio Riccio, Discoradio, R101, Capital, Deejay, Kiss Kiss, Lattemiele, RDS, RDS Relax and RTL 102.5. All twelve symbols from version 0.2.7 are preserved.
- **Italiano / English**, selected in app settings, plus an on-screen controls guide. The on-demand app remains open until you exit it.

### Installation and setup

1. Send this app to your TC002 and include its required helpers: [Sonos Local Protocol](https://awtrix.de/flow/zg8uGt07AUbk) (0.2.4) and [Sonos Local UI](https://awtrix.de/flow/wskMqqQkNc33) (0.2.9). For manual installation, use the exact names `sonos_local_protocol`, `sonos_local_ui`, then `sonos_local_probe`. The main app retains that internal name for existing local installations.
2. In the Berry app settings, enter the IP address of **one Sonos speaker** under **IP Sonos iniziale / Seed IP**, then save. The clock reads Sonos topology to discover rooms; speakers must be reachable on the LAN, including TCP port 1400. A DHCP reservation for the seed speaker is useful.
3. Choose **Lingua / Language → Italiano or English**, save, and launch **Sonos Remote Local**. Restart the app after a language change. Italian is the default; Sonos-provided names keep their own language.
4. Optionally choose **Schermata iniziale / Startup screen → Now Playing**, save and reopen the app. Menu is the default.
5. Open **Player / Lettore** to select a room, then **Playlists / Playlist** or **Radio** to choose and start a favorite. Use **Refresh favorites / Aggiorna preferiti** after changing your Sonos collection.

### Controls

| Control | Action |
| --- | --- |
| Turn knob in menus | Browse items |
| Short knob click | Confirm a selection; while playing, play/pause |
| Hold knob | Back; from playback, open the main menu |
| Turn knob during music | Previous/next track, if the source supports it |
| Turn knob during radio | Previous/next favorite station |
| Top left/right buttons | Selected-room volume −/+; hold to repeat |
| Short middle button | Show/close the controls guide |
| Hold middle button | Exit to the AWTRIX carousel |

### Beta notes and limits

Starting a playlist **appends it to the existing Sonos queue**, seeks to its first added track and starts playback; the queue is not cleared. The browser reads favorites/saved playlists, not the full streaming-service library. Existing groups are respected, but creating groups, stereo pairs, Sub or surround configurations is not implemented.

Status uses bounded polling with one request at a time and a configurable timeout. Audio commands are not automatically retried. Artwork availability and decoding depend on the source and firmware; custom radio symbols work without downloading images and other stations have a visible radio fallback.

The 0.2.9 protocol/UI passed **177 isolated Berry checks** on firmware 1.2.2, with zero real HTTP/audio commands in those checks. The production app was also verified with live radio song metadata and a native framebuffer capture. The twelve symbols were checked on the TC002 framebuffer, including exact checks of the three revised symbols. A real playlist start was confirmed during development; physical audio controls across every provider and group configuration have not all been verified. This community beta uses unofficial Sonos interoperability, so compatibility may vary.

### Source and documentation

[GitHub project](https://github.com/lucaamo/tc002-sonos-local) · [Release 0.2.9](https://github.com/lucaamo/tc002-sonos-local/releases/tag/v0.2.9) · [Detailed setup](https://github.com/lucaamo/tc002-sonos-local/blob/main/docs/INSTALLATION.md) · [Guida rapida in italiano](https://github.com/lucaamo/tc002-sonos-local/blob/main/docs/QUICKSTART.it.md) · [Report an issue](https://github.com/lucaamo/tc002-sonos-local/issues)

Source available under **PolyForm Noncommercial 1.0.0**. Unofficial community project; not endorsed by Sonos, Ulanzi or AWTRIX. Required Notice: Copyright © Stephan Mühl (Blueforcer) https://github.com/Blueforcer/awtrix-ng
