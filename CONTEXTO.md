# Contexto del proyecto — Koi Sushi & Teppanyaki

Resumen para continuar el trabajo con otra persona u otro modelo. Fecha: 20 de septiembre de 2026.

## Objetivo

El restaurante **Koi Sushi & Teppanyaki · Cocina oriental** (Cali) no tenía página web. Se construyó una con el mismo estilo del sitio de Perú Peñón (`/Volumes/Tw3/Proyecto Claude/perupenon`, publicado en https://roypitw3.github.io/perupenon/), tomando el menú de la carta en PDF (`MENU KOI 2026.pdf`) y los datos de contacto del Instagram @koisushiyteppan. Prioridad: que se vea bien en celular, con el menú en una página aparte y solo unos pocos platos destacados en el inicio.

## Estado actual

Sitio estático (HTML/CSS/JS, sin framework ni build), verificado en 375 px (móvil) y 1440 px sin errores de consola. Falta publicarlo.

```
koi/
├── index.html            Inicio: hero, bloque teppanyaki, foto, intro, 5 platos destacados, experiencias, domicilios
├── menu.html             Menú completo (13 categorías) con barra de categorías fija (sticky) y resaltado automático
├── experiencias.html     Teppanyaki live show · Sushi at home (catering) · Clases de sushi
├── contacto.html         Datos, formulario que abre WhatsApp, mapa de Google embebido
├── css/style.css         Tokens y estilos
├── js/main.js            Interacción
├── img/                  Fotos y logos (ver abajo)
└── _fuentes/
    ├── build.py          Generador. Tiene los datos del menú (lista MENU) y los textos. `python3 build.py` desde _fuentes/
    └── originales/       Fotos extraídas del PDF sin optimizar (no se suben al hosting; está en .gitignore)
```

## Sistema de diseño

- Misma base que Perú Peñón (a su vez de ballenacabo.com): header flotante centrado (botón "Pedir a domicilio" izquierda, marca centro, hamburguesa derecha), menú que cae desde la barra, preloader negro con frase (solo la primera vez por sesión), hero a sangre, bloque partido foto + panel de color, imagen completa, intro, tarjetas con carrusel, banda de contacto, footer con wordmark gigante.
- Paleta: crema `#F5F0E8`, negro `#0E0F12`, rojo Koi `#D11016` (medido del logo), arena `#B9B2A4`, niebla `#C7C9C1`, piedra `#DAD4C8`, matcha `#5F715F` (banda de contacto). El panel del bloque partido es rojo Koi.
- Tipografía: Archivo ancha (`wdth 125`) para títulos, DM Sans para texto, Bodoni Moda para el wordmark "KOI SUSHI" del pie. Los subtítulos en japonés (鉄板焼き, 寿司ロール…) salen de la carta y usan la fuente japonesa del sistema (`--font-jp`).
- Logo: se extrajo del PDF (los peces y "KOI" eran vectoriales; el círculo rojo y el subtítulo eran raster) y se compuso con transparencia. Versiones en `img/`: `logo-color.png`, `logo-blanco.png` (círculo rojo + trazos crema, para fondos oscuros), `logo-negro.png`; y la marca compacta sin subtítulo `marca-color.png`, `marca-blanca.png`, `marca-negra.png` (la del header). `favicon.png`.
- Fotos: todas vienen de los fondos de la carta PDF (se extrajeron las imágenes originales, sin los textos superpuestos). No hay fotos propias del restaurante fuera de esas. En `img/` quedan también fotos que hoy no se usan en ninguna página (entradas, vegetariano, postres, café, bebidas, cocteles, especiales, ramen, sushi-sencillo, dragon-koi) por si se quieren agregar secciones; se pueden borrar si se quiere aligerar el hosting.

## Datos del negocio (verificados en la carta y en Instagram)

- WhatsApp: **+57 320 385 3275** (`573203853275`). Instagram también publica el enlace wa.me/message/63DSFM2246NTC1.
- Dirección: **Calle 16 #83A-15, barrio El Ingenio, Cali** (Google Maps la ubica correctamente).
- Correo: koicocinaoriental@gmail.com
- Redes: Instagram y TikTok @koisushiyteppan · Facebook @Koicocinaoriental
- Domicilios: Cali, Buga, Palmira y Rozo (bio de Instagram). Pet friendly (historia destacada de Instagram).
- Platos ganadores de festivales 2020 (según la carta): Koi Especial (Festival del Mar), Koi Mixto (Festival del Asado), Terramar (Festival del Arroz). Se marcan con ★.
- Servicios: teppanyaki live show, sushi catering ("Sushi at home") y clases de sushi (página 21 de la carta).
- Precios: los de la carta 2026, en COP. Rolls por 5 y 10 bocados. Los combos muestran el precio anterior tachado tal como en la carta.
- **No se encontraron horarios de atención** en la carta ni en Instagram. No se inventaron; el sitio no los muestra.

## Decisiones tomadas

1. La sección "Promociones" de la carta (lunes promo fest, martes 3x2, etc.) está marcada en el PDF como "TEMPORALMENTE NO DISPONIBLE", así que no se incluyó. Sí se dejó el 2x1 en cocteles porque aparece también en la página de cocteles.
2. No se inventaron testimonios ni historia del restaurante: en lugar de "Quiénes somos" (como en Perú Peñón) la cuarta página es "Experiencias" con los servicios reales.
3. Se corrigieron erratas de la carta ("calabachín", "champiñlones", "mostoza", "pezcado", "Nipón"…).
4. "Reservar mesa", "Pedir" y "Cotizar" abren WhatsApp con un mensaje listo. El formulario de contacto no tiene backend.
5. La página de menú no usa el efecto de aparición al hacer scroll (`reveal`) para que al saltar a una categoría el contenido esté visible de inmediato.
6. No se enlazó el PDF de la carta porque pesa 15 MB.

## Pendientes / preguntas para el cliente

- Horarios de atención (para el pie, contacto y menú).
- Confirmar si las promociones semanales volvieron.
- ¿Precios y disponibilidad vigentes? (la carta es de 2026 pero puede haber cambios).
- Fotos propias del local y del equipo si quieren reemplazar las de la carta.
- Publicación: Repositorio en GitHub https://github.com/RoypiTw3/koisushi y publicado en GitHub Pages https://roypitw3.github.io/koisushi/

## Cómo ver en local

```bash
cd "/Volumes/Tw3/Proyecto Claude/koi" && python3 -m http.server 8080
```

y abrir http://localhost:8080
