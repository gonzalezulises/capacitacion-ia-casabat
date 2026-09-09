# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # la raíz del repo

import s1, s2
for name, html in (('sesion-1.html', s1.HTML), ('sesion-2.html', s2.HTML)):
    with io.open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{name}: {len(html)} bytes, {html.count("<section")} slides')
