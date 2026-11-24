"""Gera mídias sintéticas locais usando somente a biblioteca padrão do Python."""
from pathlib import Path
import math, random, struct, wave, zlib

ROOT = Path(__file__).resolve().parent.parent
IMG, SVG, AUDIO, MIDI = (ROOT/'assets'/name for name in ('img','svg','audio','midi'))
for folder in (IMG, SVG, AUDIO, MIDI, ROOT/'assets'/'video'):
    folder.mkdir(parents=True, exist_ok=True)

def write_wav(path, rate, samples):
    with wave.open(str(path), 'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(rate)
        f.writeframes(b''.join(struct.pack('<h', max(-32768,min(32767,int(s*32767)))) for s in samples))

duration = 2.0
for rate, name in ((8000,'tom-8khz.wav'),(22050,'tom-22050hz.wav'),(44100,'tom-44100hz.wav')):
    write_wav(AUDIO/name, rate, [0.65*math.sin(2*math.pi*440*i/rate) for i in range(int(rate*duration))])
rate=22050; n=int(rate*duration); tone=[0.6*math.sin(2*math.pi*440*i/rate) for i in range(n)]
for bits,name in ((8,'tom-8bits.wav'),(16,'tom-16bits.wav')):
    levels=2**bits; write_wav(AUDIO/name,[0] if False else rate,[round(x*(levels/2-1))/(levels/2-1) for x in tone])
write_wav(AUDIO/'tom-exemplo.wav',rate,tone)
random.seed(7); noisy=[max(-.95,min(.95,x+random.uniform(-.19,.19))) for x in tone]
write_wav(AUDIO/'antes-com-ruido.wav',rate,noisy)
write_wav(AUDIO/'depois-limpo.wav',rate,[x*.95 for x in tone])

# Tiny monophonic MIDI file (middle C, D, E, G), one quarter note per event.
def vlq(value):
    out=[value&0x7f]; value >>= 7
    while value: out.insert(0,(value&0x7f)|0x80); value >>= 7
    return bytes(out)
track=bytearray(b'\x00\xff\x51\x03\x07\xa1\x20')
for note in (60,64,67,72,67,64,60):
    track += b'\x00\x90'+bytes([note,90])+vlq(480)+b'\x80'+bytes([note,0])
track += b'\x00\xff\x2f\x00'
(MIDI/'trilha-exemplo.mid').write_bytes(b'MThd'+struct.pack('>IHHH',6,0,1,480)+b'MTrk'+struct.pack('>I',len(track))+track)
# Render the same tune as a simple WAV, changing notes every half-second.
melody=(60,64,67,72,67,64,60); rendered=[]
for note in melody:
    freq=440*2**((note-69)/12)
    rendered.extend(.35*math.sin(2*math.pi*freq*i/rate) for i in range(rate//2))
write_wav(AUDIO/'trilha-midi-renderizada.wav',rate,rendered)

def svg(path, content):
    (SVG/path).write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 260" role="img">'+content+'</svg>',encoding='utf-8')
grid='<path d="M50 20V220H690" fill="none" stroke="#b8cbc6" stroke-width="2"/><path d="M50 120H690M210 20V220M370 20V220M530 20V220" stroke="#e3ece9"/>'
curve=' '.join(f'{x},{120-78*math.sin((x-50)/640*math.tau)}' for x in range(50,691,4))
svg('onda-sonora.svg',grid+f'<polyline points="{curve}" fill="none" stroke="#087e78" stroke-width="5"/><text x="560" y="250" font-size="15">tempo</text><text x="7" y="34" font-size="15">amplitude</text>')
sampled=' '.join(f'{x},{120-78*math.sin((x-50)/640*math.tau)}' for x in range(50,691,40))
svg('amostragem.svg',grid+f'<polyline points="{curve}" fill="none" stroke="#087e78" stroke-width="4"/><polyline points="{sampled}" fill="none" stroke="#fa8069" stroke-width="3"/>'+''.join(f'<circle cx="{x}" cy="{120-78*math.sin((x-50)/640*math.tau)}" r="6" fill="#fa8069"/>' for x in range(50,691,40)))
quant=''.join(f'<path d="M{50+i*40} {round((120-78*math.sin(i*40/640*math.tau))/20)*20}h30" stroke="#fa8069" stroke-width="5"/>' for i in range(17))
svg('quantizacao.svg',grid+f'<polyline points="{curve}" fill="none" stroke="#087e78" stroke-width="3" opacity=".55"/>'+quant)

# Tiny RGB PNG drawings, generated without imaging packages.
def png(path, painter, w=720, h=440):
    pixels=bytearray([245,247,246]*(w*h))
    def rect(x,y,ww,hh,color):
        for yy in range(max(0,y),min(h,y+hh)):
            for xx in range(max(0,x),min(w,x+ww)):
                k=(yy*w+xx)*3; pixels[k:k+3]=bytes(color)
    painter(rect,w,h)
    raw=b''.join(b'\x00'+pixels[y*w*3:(y+1)*w*3] for y in range(h))
    def chunk(kind,data): return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data)&0xffffffff)
    (IMG/path).write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b''))
def studio(r,w,h):
    r(0,0,w,h,(225,241,235));r(45,50,630,330,(22,57,74));r(74,78,220,110,(38,86,95));r(328,83,280,23,(63,104,109));r(328,120,220,17,(76,119,122));r(120,270,110,12,(250,128,105));r(150,165,50,125,(24,45,58));r(135,145,80,30,(8,126,120));r(169,282,13,60,(24,45,58));r(430,215,110,62,(8,126,120));r(448,230,74,8,(223,243,236));r(448,246,74,8,(223,243,236))
def gear(r,w,h):
    r(0,0,w,h,(235,244,240));r(95,90,180,210,(23,57,74));r(126,66,115,45,(8,126,120));r(160,300,48,74,(23,57,74));r(139,370,90,16,(23,57,74));r(370,110,220,180,(8,126,120));r(392,132,176,136,(223,243,236));r(413,153,134,94,(23,57,74));r(447,183,68,30,(250,128,105));r(464,300,35,75,(23,57,74));r(430,370,104,15,(23,57,74))
png('processo-gravacao.png',studio);png('equipamentos.png',gear)
def poster(r,w,h):
    r(0,0,w,h,(22,57,74));r(60,55,600,330,(8,126,120));r(96,95,528,236,(223,243,236));r(338,133,45,160,(22,57,74));r(280,112,160,45,(22,57,74));r(350,288,20,48,(22,57,74));r(305,332,110,14,(22,57,74))
png('capa-video.png',poster)
print('Mídias geradas em assets/. O MP4 e MP3 reais precisam ser adicionados manualmente; veja MIDIAS_PARA_TROCAR.md.')
