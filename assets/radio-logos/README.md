# Twelve native 16×16 radio symbols

Sonos Remote Local 0.2.7 includes twelve compact station symbols. Radio 105, Radio Bruno and Ciccio Riccio retain the original approved pixels and palettes. Radio Capital, Radio Kiss Kiss and Radio Lattemiele use the revised 0.2.7 assets.

![Radio symbols](gallery.png)

| Station | Public TuneIn ID |
| --- | --- |
| Radio 105 | 16526 |
| Radio Bruno | 63651 |
| Ciccio Riccio | 87442 |
| Discoradio | 25858 |
| R101 | 63643 |
| Radio Capital | 6535 |
| Radio Deejay | 1216 |
| Radio Kiss Kiss | 61955 |
| Radio Lattemiele | 73738 |
| RDS 100% Grandi Successi | 16202 |
| RDS Relax | 299243 |
| RTL 102.5 | 6684 |

These are unofficial pixel adaptations for the LED matrix. The full station name scrolls next to the symbol. SVG and PNG assets are native 16×16; enlarged versions repeat pixels without interpolation. The JSON stores the grid, palette and packed two-bit rows.

Run `python3 tools/build_radio_logos.py --check-ui` from the repository root to regenerate the assets and verify the Berry data. `--write-ui` replaces only the marked native-logo data block. The three revised drawings are stored in `approved-brand-overrides.json`.

The **Custom radio logos** setting enables these symbols. Disable it to prefer original station artwork. Disabling direct artwork also hides custom symbols. Other stations use available original artwork or the visible radio fallback. Sonos names, playback URIs and metadata are not rewritten.
