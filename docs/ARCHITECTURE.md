# Architecture

`apps/sonos_local_probe.ax` declares settings, on-demand behavior and the TC002 display target, then creates `sonos_local_ui.Remote`. Its retained script name allows existing local installs to update without moving saved settings.

`sonos_local_ui` implements menus, bilingual labels, button / knob behavior, bounded status messages, scrolling and artwork. Native radio symbols use sixteen packed 32-bit rows and four palette entries per station. Artist names and room names are not shortened to generated aliases.

`sonos_local_protocol` implements HTTP/SOAP discovery from a manually configured seed. It reads device descriptions and Sonos topology, then resolves service control URLs. Playback targets the selected room's coordinator; RenderingControl volume targets the selected room.

Favorites are paged from `FV:2`, then saved playlists from `SQ:`. Their original URI and metadata are retained for playback; duplicate URIs are removed. Starting a queue-based playlist uses AddURIToQueue, the room coordinator's queue URI, Seek to the first returned added track, then Play. Radio uses its original favorite URI / metadata, then Play.

Only one request is in flight. XML bodies have a 32 KiB bound, catalog requests have a bounded page size / total limit, and each request has a configurable timeout. There is no automatic retry of audio commands. Rapid radio changes retain the latest pending favorite rather than issuing parallel playback requests.

Existing groups are discovered, not changed. There is no SSDP listener, UPnP event subscription, OAuth, Home Assistant or MQTT connection. Python tools are optional development utilities and are not part of the clock's runtime.
