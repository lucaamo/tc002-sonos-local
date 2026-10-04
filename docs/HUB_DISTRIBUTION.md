# AWTRIX Hub distribution

Two helper modules and one on-demand app for official AWTRIX NG on TC002, 52×16.

| Component | Version | Hub |
| --- | --- | --- |
| Sonos Local Protocol | 0.2.3 | https://awtrix.de/flow/zg8uGt07AUbk |
| Sonos Local UI | 0.2.7 | https://awtrix.de/flow/wskMqqQkNc33 |

The UI declares the protocol as a Hub requirement. The main app declares both helpers; when sending the app to the clock, include its missing dependencies. For manual installation, use `sonos_local_protocol`, `sonos_local_ui`, then `sonos_local_probe`.

Distribution metadata differs from the locally installed prototype: the visible app name is Sonos Remote Local, both helpers declare the 52×16 target, and the files declare their published Hub dependencies. Runtime bodies are unchanged. No device settings, backups or network identifiers are included.
