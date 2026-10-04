"""Twelve native 16x16 radio symbols, preserving the three approved v2 icons."""
from pathlib import Path
import argparse
import json

from pixel_assets import png, stamp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "radio-logos"
BLACK = (0, 0, 0)
WHITE = (240, 240, 224)
RED = (230, 25, 20)
YELLOW = (226, 189, 0)
CYAN = (0, 155, 200)

FONT = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "5": ["11111", "10000", "10000", "11110", "00001", "00001", "11110"],
    ".": ["00000", "00000", "00000", "00000", "00000", "00110", "00110"],
    " ": ["00000"] * 7,
}
SMALL = {
    "R": ["110", "101", "110", "101", "101"],
    "D": ["110", "101", "101", "101", "110"],
    "S": ["111", "100", "111", "001", "111"],
    "E": ["111", "100", "110", "100", "111"],
    "L": ["100", "100", "100", "100", "111"],
}
WIDE = {
    "R": ["1110", "1001", "1001", "1110", "1010", "1001", "1001"],
    "D": ["1110", "1001", "1001", "1001", "1001", "1001", "1110"],
    "S": ["1111", "1000", "1000", "1111", "0001", "0001", "1111"],
    "T": ["1111", "0110", "0110", "0110", "0110", "0110", "0110"],
    "L": ["1000", "1000", "1000", "1000", "1000", "1000", "1111"],
}


def blank():
    return [[0] * 16 for _ in range(16)]


def circle(grid, paint, radius):
    for y in range(16):
        for x in range(16):
            if (x - 7.5) ** 2 + (y - 7.5) ** 2 <= radius ** 2:
                grid[y][x] = paint


def text(grid, value, font, x, y, paint):
    for letter in value:
        stamp(grid, font[letter], x, y, paint)
        x += len(font[letter][0]) + 1


def new_icons():
    disco = blank()
    # Geometric white DR and the red underline from Discoradio's wordmark.
    text(disco, "DR", FONT, 2, 3, 1)
    for y in (12, 13, 14):
        for x in range(2 if y == 12 else 1, 15 if y == 12 else 14):
            disco[y][x] = 2

    r101 = blank()
    circle(r101, 1, 8)
    circle(r101, 2, 6)
    # R101 fits in thirteen columns: preserve the full distinctive identifier.
    for y in range(4, 12):
        for x in range(16):
            r101[y][x] = 2
    narrow = {
        "R": ["110", "101", "101", "110", "110", "101", "101"],
        "1": ["11", "01", "01", "01", "01", "01", "11"],
        "0": ["111", "101", "101", "101", "101", "101", "111"],
    }
    text(r101, "R101", narrow, 1, 4, 0)

    capital = blank()
    circle(capital, 1, 8)
    stamp(capital, ["0011111111", "0111111111", "1110000000", "1100000000", "1100000000", "1100000000", "1110000000", "0111111111", "0011111111"], 3, 4, 0)
    for x in range(5, 11):
        capital[1][x] = capital[2][x] = 2

    deejay = blank()
    circle(deejay, 2, 8)
    circle(deejay, 1, 6.7)
    text(deejay, "DJ", FONT, 2, 4, 2)

    kiss = blank()
    # Cyan X, with a central black separation around the white KK monogram.
    for y in range(16):
        left = min(y, 15 - y)
        for x in range(max(0, left - 1), min(16, left + 2)):
            kiss[y][x] = kiss[y][15 - x] = 2
    letters = blank()
    text(letters, "KK", FONT, 2, 4, 1)
    for y in range(16):
        for x in range(16):
            if letters[y][x]:
                for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0 <= nx < 16 and 0 <= ny < 16:
                        kiss[ny][nx] = 0
    for y in range(16):
        for x in range(16):
            if letters[y][x]:
                kiss[y][x] = 1

    latte = blank()
    # White outer pill, black interior: yellow letter strokes stay separated.
    for y in range(2, 14):
        latte[y][0 if 4 <= y <= 11 else 1] = 1
        latte[y][15 if 4 <= y <= 11 else 14] = 1
    for x in range(3, 13):
        latte[1][x] = latte[14][x] = 1
    letters = blank()
    text(letters, "LM", FONT, 2, 4, 2)
    for y in range(16):
        for x in range(16):
            if letters[y][x]:
                latte[y][x] = 2

    rds = blank()
    for y in range(16):
        start = 2 - y // 6
        for x in range(start, min(16, start + 14)):
            rds[y][x] = 1
    text(rds, "RDS", WIDE, 1, 4, 2)

    relax = blank()
    for y in range(7):
        for x in range(1, 15):
            relax[y][x] = 1
    text(relax, "RDS", SMALL, 2, 1, 2)
    text(relax, "REL", SMALL, 2, 9, 2)
    for y in range(8, 16):
        relax[y][0] = relax[y][15] = 1
    for x in range(16):
        relax[15][x] = 1

    rtl = blank()
    circle(rtl, 1, 8)
    for y in range(3, 13):
        inset = max(0, (y - 8) // 3)
        for x in range(inset, 16 - inset):
            rtl[y][x] = 0
    text(rtl, "RTL", WIDE, 1, 4, 2)

    return [
        ("discoradio", "Discoradio", "25858", disco, [BLACK, WHITE, RED, BLACK]),
        ("r101", "R101", "63643", r101, [BLACK, RED, WHITE, BLACK]),
        ("radio-capital", "Radio Capital", "6535", capital, [BLACK, WHITE, RED, BLACK]),
        ("radio-deejay", "Radio Deejay", "1216", deejay, [BLACK, RED, WHITE, BLACK]),
        ("radio-kiss-kiss", "Radio Kiss Kiss", "61955", kiss, [BLACK, WHITE, CYAN, BLACK]),
        ("radio-lattemiele", "Radio Lattemiele", "73738", latte, [BLACK, WHITE, YELLOW, BLACK]),
        ("rds", "RDS 100% Grandi Successi", "16202", rds, [BLACK, RED, WHITE, BLACK]),
        ("rds-relax", "RDS Relax", "299243", relax, [BLACK, (180, 30, 40), WHITE, BLACK]),
        ("rtl-102-5", "RTL 102.5", "6684", rtl, [BLACK, RED, WHITE, BLACK]),
    ]


def berry_data(icons, packed):
    block = "    # BEGIN LOCAL RADIO LOGOS 16X16\n    self.logo_rows = [\n"
    block += ",\n".join("      [" + ",".join(f"0x{n:08X}" for n in row) + "]" for row in packed) + "\n    ]\n"
    block += "    self.logo_palettes = [\n"
    block += ",\n".join("      [" + ",".join(f"0x{(c[0]<<16)|(c[1]<<8)|c[2]:06X}" for c in item["palette"]) + "]" for item in icons) + "\n    ]\n"
    block += "    # ID pubblici TuneIn: mai ID domestici FV:2 o account Sonos.\n"
    block += "    self.logo_ids = " + json.dumps({item["station_id"]:i for i, item in enumerate(icons)}) + "\n"
    names = {item["name"]:i for i, item in enumerate(icons)}
    names.update({"105":0, "CiccioRiccio":2, "RadioCapital":5, "Deejay":6, "Kiss Kiss":7, "Lattemiele":8, "RDS":9, "RTL102.5":11})
    block += "    self.logo_names = " + json.dumps(names) + "\n    # END LOCAL RADIO LOGOS 16X16"
    return block


def build(write_ui=False, check_ui=False):
    approved = json.loads((ROOT / "assets/radio-logo-trials/v2/pixel-data.json").read_text())
    icons = approved["icons"]
    for item, station_id in zip(icons, ("16526", "63651", "87442")):
        item["station_id"] = station_id
    for slug, name, station_id, grid, palette in new_icons():
        icons.append({"slug":slug, "name":name, "station_id":station_id, "grid":grid, "palette":palette})
    replacements = json.loads((OUT / "approved-brand-overrides.json").read_text())["icons"]
    by_slug = {item["slug"]:item for item in replacements}
    for item in icons:
        if item["slug"] in by_slug:
            item["grid"] = by_slug[item["slug"]]["grid"]
            item["palette"] = by_slug[item["slug"]]["palette"]
    packed = [[sum(cell << (x * 2) for x, cell in enumerate(row)) for row in item["grid"]] for item in icons]
    assert packed[:3] == approved["packed_rows"], "Approved pixels must remain exact"
    OUT.mkdir(parents=True, exist_ok=True)
    for item in icons:
        grid, palette = item["grid"], item["palette"]
        assert len(grid) == 16 and all(len(row) == 16 and all(0 <= c < 4 for c in row) for row in grid)
        rects = [f'<rect x="{x}" y="{y}" width="1" height="1" fill="#{bytes(palette[c]).hex()}"/>'
                 for y, row in enumerate(grid) for x, c in enumerate(row) if c]
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" shape-rendering="crispEdges">'
               + '<rect width="16" height="16" fill="#000000"/>' + "".join(rects) + '</svg>\n')
        (OUT / (item["slug"] + ".svg")).write_text(svg)
        (OUT / (item["slug"] + ".png")).write_bytes(png(grid, palette))
        (OUT / (item["slug"] + "-large.png")).write_bytes(png(grid, palette, 16))
        if item in icons[:3]:
            assert (OUT / (item["slug"] + ".png")).read_bytes() == (ROOT / "assets/radio-logo-trials/v2" / (item["slug"] + ".png")).read_bytes()
    (OUT / "pixel-data.json").write_text(json.dumps({"icons":icons, "packed_rows":packed}, indent=2) + "\n")
    # Deterministic, pixel-sharp labeled gallery; PNG is an export of our native assets.
    palette = [BLACK, (22, 24, 28), WHITE]
    for item in icons:
        for color in item["palette"]:
            if tuple(color) not in palette:
                palette.append(tuple(color))
    sheet = [[1] * 1168 for _ in range(808)]
    for i, item in enumerate(icons):
        ox, oy = 8 + (i % 4) * 290, 8 + (i // 4) * 266
        for y in range(244):
            for x in range(280):
                sheet[oy + y][ox + x] = 0
        for y, row in enumerate(item["grid"]):
            for x, cell in enumerate(row):
                paint = palette.index(tuple(item["palette"][cell]))
                for dy in range(12):
                    for dx in range(12):
                        sheet[oy + 12 + y * 12 + dy][ox + 44 + x * 12 + dx] = paint
        label = item["name"].upper().replace(" 100% GRANDI SUCCESSI", "")
        label_grid = [[0] * (len(label) * 6) for _ in range(7)]
        text(label_grid, label, FONT, 0, 0, 1)
        tx = ox + (280 - len(label_grid[0]) * 2) // 2
        for y, row in enumerate(label_grid):
            for x, cell in enumerate(row):
                if cell:
                    for dy in range(2):
                        for dx in range(2):
                            sheet[oy + 219 + y * 2 + dy][tx + x * 2 + dx] = 2
    (OUT / "gallery.png").write_bytes(png(sheet, palette))
    fragment = berry_data(icons, packed)
    ui = ROOT / "modules/sonos_local_ui.ax"
    source = ui.read_text()
    if write_ui:
        start = source.index("    # BEGIN LOCAL RADIO LOGOS 16X16")
        end = source.index("    # END LOCAL RADIO LOGOS 16X16", start) + len("    # END LOCAL RADIO LOGOS 16X16")
        ui.write_text(source[:start] + fragment + source[end:])
    if check_ui:
        assert fragment in ui.read_text(), "Native UI rows, palettes or mappings differ from generated assets"
    print("12 native icons generated; approved three remain byte-identical")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-ui", action="store_true", help="Replace only the marked native logo data block")
    parser.add_argument("--check-ui", action="store_true", help="Verify that the UI includes the generated rows, colors and mappings")
    args = parser.parse_args()
    build(args.write_ui, args.check_ui)
