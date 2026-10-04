"""Rebuild publication covers from native assets (requires Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/publication'
FONT='/System/Library/Fonts/Helvetica.ttc'
def font(size):
    try: return ImageFont.truetype(FONT,size)
    except OSError: return ImageFont.truetype('DejaVuSans.ttf',size)
def base(kicker,title,subtitle):
    img=Image.new('RGB',(1400,900),'#0e1822')
    d=ImageDraw.Draw(img)
    d.rounded_rectangle((60,55,385,101),radius=16,fill='#d4ae1a')
    d.text((79,63),kicker,font=font(24),fill='#101820')
    d.text((60,135),title,font=font(68),fill='#f5f3e7')
    d.text((63,225),subtitle,font=font(29),fill='#bac6cf')
    return img,d
img,d=base('TC002  /  52 x 16','Sonos Remote Local','Direct Sonos control from your clock  |  v0.2.7')
d.rounded_rectangle((59,295,1341,710),radius=28,fill='#283443')
d.rounded_rectangle((84,320,1316,685),radius=15,fill='#000000')
frame=Image.open(OUT/'native-radio-fixture.png')
frame=frame.resize((1196,368),Image.Resampling.NEAREST)
img.paste(frame,(102,320))
d.text((64,741),'Playlists  /  Favorite radio  /  Rooms  /  Volume',font=font(35),fill='#f5f3e7')
d.text((65,808),'Italiano + English   •   No Home Assistant or MQTT   •   Community beta',font=font(25),fill='#bac6cf')
d.text((65,852),'Native TC002 preview with example data',font=font(18),fill='#7f94a5')
img.save(OUT/'cover.png')
for slug,label,subtitle,lines in [
 ('protocol-cover','Sonos Local Protocol','Helper module v0.2.3 for Sonos Remote Local',[
 ('HTTP / SOAP','One request at a time'),('ROOM TOPOLOGY','Coordinator-aware playback'),('FAVORITE CATALOGS','Sonos favorites + saved playlists')]),
 ('ui-cover','Sonos Local UI','Helper module v0.2.7 for Sonos Remote Local',[
 ('KNOB + BUTTONS','Menus, playback and room volume'),('ITALIANO / ENGLISH','Friendly names and clear controls'),('16 x 16 RADIO SYMBOLS','Twelve native pixel icons')])]:
 im,dd=base('TC002  /  MODULE',label,subtitle)
 for i,(a,b) in enumerate(lines):
  y=320+i*135
  dd.rounded_rectangle((62,y,1050,y+105),radius=16,fill='#223242')
  dd.text((92,y+17),a,font=font(27),fill='#d4ae1a')
  dd.text((92,y+56),b,font=font(29),fill='#f5f3e7')
 for i,station in enumerate(['radio-105','radio-bruno','ciccio-riccio']):
  icon=Image.open(ROOT/'assets/radio-logos'/f'{station}.png').resize((144,144),Image.Resampling.NEAREST)
  im.paste(icon,(1130,300+i*164))
 dd.text((64,798),'Runs on official AWTRIX NG  •  No host runtime required',font=font(28),fill='#bac6cf')
 dd.text((64,852),'Install through the main app or before Sonos Remote Local',font=font(23),fill='#7f94a5')
 im.save(OUT/f'{slug}.png')
print('Three publication covers generated')
