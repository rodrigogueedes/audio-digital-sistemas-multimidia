from pathlib import Path
import re

pages = [Path('index.html'), *Path('paginas').glob('*.html')]
old_icon = '<span class="brand-mark" aria-hidden="true">♫</span>'
for page in pages:
    asset = 'assets/svg/logo-audio.svg' if page.parent == Path('.') else '../assets/svg/logo-audio.svg'
    html = page.read_text(encoding='utf-8')
    html = html.replace(old_icon, f'<img class="brand-logo" src="{asset}" alt="">')
    html = re.sub(r'</title>', f'</title><link rel="icon" href="{asset}" type="image/svg+xml">', html, count=1)
    page.write_text(html, encoding='utf-8')
