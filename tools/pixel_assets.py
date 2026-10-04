"""Small dependency-free PNG and pixel drawing helpers."""
import struct
import zlib

def png(grid, palette, scale=1):
    height, width = len(grid), len(grid[0])
    raw = bytearray()
    for row in grid:
        line = b"".join(bytes(palette[cell]) * scale for cell in row)
        for _ in range(scale):
            raw.extend(b"\0" + line)
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width * scale, height * scale, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def stamp(grid, pattern, x, y, paint=0):
    for dy, row in enumerate(pattern):
        for dx, cell in enumerate(row):
            if cell == "1":
                grid[y + dy][x + dx] = paint


