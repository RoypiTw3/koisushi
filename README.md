# Koi Sushi & Teppanyaki — sitio web

Sitio del restaurante **Koi Sushi & Teppanyaki · Cocina oriental** (Calle 16 #83A-15, barrio El Ingenio, Cali). Usa la misma estructura y sistema visual del sitio de Perú Peñón (header flotante, hero a sangre, bloques partidos, tipografía ancha en mayúsculas), con la paleta de Koi: crema, negro y el rojo del logo.

Sitio 100 % estático: no necesita instalación ni build. Se sube tal cual a cualquier hosting (GitHub Pages, Netlify, cPanel…).

## Estructura

```
index.html           Inicio
menu.html            Menú completo por categorías, con índice fijo para celular
experiencias.html    Teppanyaki show, sushi catering y clases de sushi
contacto.html        Datos, formulario (abre WhatsApp) y mapa
css/style.css        Estilos y tokens de diseño (colores, tipografía)
js/main.js           Preloader, menú, revelado al hacer scroll, carrusel, índice del menú, formulario
img/                 Fotos optimizadas (sacadas de la carta PDF), logo en varias versiones, favicon
_fuentes/build.py    Generador de las 4 páginas: aquí están los DATOS DEL MENÚ y los textos
```

## Cómo editar

- **Menú, precios y textos**: editar `_fuentes/build.py` (lista `MENU` y las funciones `page_*`) y luego ejecutar `python3 build.py` desde `_fuentes/`. Eso regenera los cuatro `.html`.
  También se pueden editar los `.html` directamente y olvidarse del generador (pero entonces no volver a ejecutarlo o se pierden los cambios).
- **WhatsApp**: buscar `573203853275` en `_fuentes/build.py` y en `js/main.js`.
- **Dirección, correo y redes**: variables `ADDRESS`, `MAIL`, `IG`, `TIKTOK`, `FB` al inicio de `_fuentes/build.py`.
- **Colores**: variables al inicio de `css/style.css` (`--cream`, `--ink`, `--koi`, `--sand`, `--mist`, `--matcha`).

## Ver en local

```bash
python3 -m http.server 8080
```

y abrir http://localhost:8080
