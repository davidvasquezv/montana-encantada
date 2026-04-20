"""Run after every Mobirise publish: python fix_3d.py"""
import re

PANNELLUM_DOMO = '''
<section class="mbr-section" id="galeria-domo" style="padding: 0; background: #1a1a1a;">
    <h2 class="mbr-section-title mbr-fonts-style align-center py-4" style="color: #232323; background: #ffffff; font-family: 'Gilda Display', serif;">Vista 3D</h2>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.css">
    <div id="panorama" style="width: 100%; height: 80vh;"></div>
    <script>
        (function() {
            var s = document.createElement('script');
            s.src = 'https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.js';
            s.onload = function() {
                pannellum.viewer('panorama', {
                    type: 'equirectangular',
                    panorama: 'assets/images/domovista3d.jpg',
                    autoLoad: true,
                    autoRotate: -2,
                    hfov: 110,
                    showControls: true
                });
            };
            document.head.appendChild(s);
        })();
    </script>
</section>
'''

PANNELLUM_CABANA = '''
<section class="mbr-section" id="vista3d-interna" style="padding: 0; background: #1a1a1a;">
    <h2 class="mbr-section-title mbr-fonts-style align-center py-4" style="color: #232323; background: #ffffff; font-family: 'Gilda Display', serif;">Vista 3D Interna</h2>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.css">
    <div id="panorama-interna" style="width: 100%; height: 80vh;"></div>
    <script>
        (function() {
            var s = document.createElement('script');
            s.src = 'https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.js';
            s.onload = function() {
                pannellum.viewer('panorama-interna', {
                    type: 'equirectangular',
                    panorama: 'assets/images/casainterna3d.jpg',
                    autoLoad: true,
                    autoRotate: -2,
                    hfov: 110,
                    showControls: true
                });
                pannellum.viewer('panorama-externa', {
                    type: 'equirectangular',
                    panorama: 'assets/images/cada externa3d.jpg',
                    autoLoad: true,
                    autoRotate: -2,
                    hfov: 110,
                    showControls: true
                });
            };
            document.head.appendChild(s);
        })();
    </script>
</section>

<section class="mbr-section" id="vista3d-externa" style="padding: 0; background: #1a1a1a;">
    <h2 class="mbr-section-title mbr-fonts-style align-center py-4" style="color: #232323; background: #ffffff; font-family: 'Gilda Display', serif;">Vista 3D Externa</h2>
    <div id="panorama-externa" style="width: 100%; height: 80vh;"></div>
</section>
'''

GUESTS_FIX = '''
<script>
document.addEventListener('DOMContentLoaded', function() {
    var guestsCount = document.querySelector('.guests-count');
    var arrows = document.querySelector('.guests .date-col');
    if (!guestsCount || !arrows) return;
    var count = 1;
    var min = 1, max = 6;
    arrows.querySelector('.mbri-arrow-up').addEventListener('click', function(e) {
        e.stopPropagation();
        if (count < max) { count++; guestsCount.textContent = count; }
    });
    arrows.querySelector('.mbri-arrow-down').addEventListener('click', function(e) {
        e.stopPropagation();
        if (count > min) { count--; guestsCount.textContent = count; }
    });

    var btnReservar = document.getElementById('btn-reservar');
    if (btnReservar) {
        btnReservar.addEventListener('click', function(e) {
            e.preventDefault();
            var checkin = document.querySelector('.check-in-input') ? document.querySelector('.check-in-input').value : '';
            var checkout = document.querySelector('.check-out-input') ? document.querySelector('.check-out-input').value : '';
            var guests = guestsCount.textContent;
            var mensaje = document.querySelector('input[name="mensaje"]') ? document.querySelector('input[name="mensaje"]').value : '';
            var text = 'Hola, quiero reservar en Montaña Encantada.';
            if (checkin) text += ' Check-in: ' + checkin + '.';
            if (checkout) text += ' Check-out: ' + checkout + '.';
            text += ' Huéspedes: ' + guests + '.';
            if (mensaje) text += ' ' + mensaje;
            window.open('https://wa.me/50663833317?text=' + encodeURIComponent(text), '_blank');
        });
    }
});
</script>
'''

MENU_FIX = '''    <nav class="navbar navbar-dropdown navbar-expand-lg">
        <div class="navbar-brand">
            <span class="navbar-logo">
                <a href="index.html">
                    <img src="assets/images/logo1.png" alt="Montaña Encantada" style="height: 3.8rem;">
                </a>
            </span>
            <span class="navbar-caption-wrap mbr-section-btn">
                <a class="navbar-caption text-white display-7" href="index.html">
                    MONTAÑA ENCANTADA
                </a>
            </span>
        </div>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav nav-dropdown mbr-section-btn" data-app-modern-menu="true"><li class="nav-item">
                    <a class="nav-link link text-white display-7" href="index.html#header6-0">
                        Inicio
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link link text-white display-7" href="index.html#features15-7">
                        Hospedaje
                    </a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link link dropdown-toggle text-white display-7" data-toggle="dropdown-submenu" aria-expanded="false">
                        Galería
                    </a>
                    <div class="dropdown-menu">
                        <a class="dropdown-item text-white display-7" href="domo.html">Domo</a>
                        <a class="dropdown-item text-white display-7" href="cabana.html">Cabaña</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link link text-white display-7" href="index.html#testimonials2-8">
                        Reseñas
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link link text-white display-7" href="index.html#maps4-9">
                        Contacto
                    </a>
                </li></ul>
            <div class="icons-menu">
              <a href="https://wa.me/50663833317" target="_blank">
                <span class="p-2 mbr-iconfont socicon-whatsapp socicon"></span>
              </a>
              <a href="https://www.instagram.com/montana.encantada/" target="_blank">
                <span class="p-2 mbr-iconfont socicon-instagram socicon"></span>
              </a>
              <a href="https://www.tiktok.com/@glamping.encantada" target="_blank">
                <span class="p-2 mbr-iconfont socicon-tiktok socicon"></span>
              </a>
            </div>
            <div class="navbar-buttons mbr-section-btn">
                <a class="btn btn-sm btn-white-outline display-4" href="https://wa.me/50663833317?text=Hola%2C%20me%20interesa%20reservar%20en%20Monta%C3%B1a%20Encantada">
                    RESERVAR
                </a>
            </div>
      </div>
    </nav>'''

INJECT_POINT = '<script src="assets/web/assets/jquery/jquery.min.js"></script>'

def fix(filename, block):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'pannellum' in html:
        print(f"  {filename}: already has 3D viewer, skipping")
        return
    if INJECT_POINT not in html:
        print(f"  {filename}: inject point not found!")
        return
    html = html.replace(INJECT_POINT, block + '\n' + INJECT_POINT)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {filename}: 3D viewer injected ✓")

print("Fixing 3D viewers...")
fix('domo.html', PANNELLUM_DOMO)
fix('cabana.html', PANNELLUM_CABANA)

# Fix menu in domo.html and cabana.html
def fix_menu(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'dropdown-submenu' in html and 'socicon-whatsapp' in html:
        print(f"  {filename}: menu already fixed, skipping")
        return
    import re
    pattern = r'<nav class="navbar[^>]*>.*?</nav>'
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        print(f"  {filename}: nav not found!")
        return
    html = html[:match.start()] + MENU_FIX + html[match.end():]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {filename}: menu fixed ✓")

fix_menu('domo.html')
fix_menu('cabana.html')

# Fix footer position in domo.html and cabana.html (move to end)
def fix_footer(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    import re
    footer_match = re.search(r'<section class="footer2[^>]*>.*?</section>', html, re.DOTALL)
    if not footer_match:
        print(f"  {filename}: footer not found, skipping")
        return
    footer_html = footer_match.group(0)
    # Check if footer is already at the end (before scripts)
    after_footer = html[footer_match.end():].strip()
    if after_footer.startswith('<section class="gallery') or after_footer.startswith('<section class="mbr-section"'):
        # Footer is not at the end, move it
        html_without_footer = html[:footer_match.start()] + html[footer_match.end():]
        # Insert before closing </body> or before final scripts
        insert_point = '</body>'
        if insert_point in html_without_footer:
            html_without_footer = html_without_footer.replace(insert_point, footer_html + '\n' + insert_point)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_without_footer)
            print(f"  {filename}: footer moved to bottom ✓")
        else:
            print(f"  {filename}: </body> not found!")
    else:
        print(f"  {filename}: footer already at bottom, skipping")

fix_footer('domo.html')
fix_footer('cabana.html')

# Fix guests counter in index.html
def fix_guests(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'count < max' in html:
        print(f"  {filename}: guests fix already applied, skipping")
        return
    marker = '</body>'
    if marker not in html:
        print(f"  {filename}: </body> not found!")
        return
    html = html.replace(marker, GUESTS_FIX + marker)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {filename}: guests counter fixed ✓")

fix_guests('index.html')
print("Done!")
