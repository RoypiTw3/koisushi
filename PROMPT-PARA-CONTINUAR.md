# Prompt para continuar con otro modelo

Copia y pega esto tal cual (ajusta la parte de "Lo que necesito ahora"):

---

Voy a continuar un proyecto web que ya está avanzado. Antes de hacer nada, lee estos dos archivos y confirma que entendiste el estado:

- `/Volumes/Tw3/Proyecto Claude/koi/CONTEXTO.md` (resumen del proyecto, decisiones tomadas y pendientes)
- `/Volumes/Tw3/Proyecto Claude/koi/README.md` (dónde se edita cada cosa)

Contexto rápido: es el sitio del restaurante Koi Sushi & Teppanyaki (cocina oriental, barrio El Ingenio, Cali, Colombia; Instagram @koisushiyteppan). Está hecho con el mismo estilo del sitio de Perú Peñón. Son cuatro páginas estáticas en HTML/CSS/JS (`index.html`, `menu.html`, `experiencias.html`, `contacto.html`), sin framework, en `/Volumes/Tw3/Proyecto Claude/koi/`. Las páginas se generan con `_fuentes/build.py` (ahí están los datos del menú y los textos).

Reglas para trabajar:

1. Respeta el sistema de diseño: colores y tipografía están como variables al inicio de `css/style.css` (crema #F5F0E8, negro #0E0F12, rojo Koi #D11016, matcha #5F715F; Archivo ancha para títulos, DM Sans para texto, Bodoni Moda para el wordmark). No introduzcas otros colores ni fuentes.
2. Para cambiar textos, menú o precios edita `_fuentes/build.py` y ejecuta `python3 build.py` desde `_fuentes/`. No edites los `.html` a mano si vas a volver a usar el generador.
3. No inventes datos del negocio. Verificados: WhatsApp +57 320 385 3275, Calle 16 #83A-15 barrio El Ingenio (Cali), correo koicocinaoriental@gmail.com, Instagram/TikTok @koisushiyteppan, Facebook @Koicocinaoriental, domicilios en Cali, Buga, Palmira y Rozo. NO hay horarios de atención confirmados; si los necesitas, pregúntame.
4. Escríbeme en español de Colombia, sin voseo.
5. Después de cada cambio, abre el sitio en local (`python3 -m http.server 8080` dentro de la carpeta) y revisa en móvil (375 px) y escritorio antes de darlo por terminado. El menú (`menu.html`) es lo más importante en celular.
6. La carpeta `_fuentes/originales/` es material de trabajo; no la incluyas al publicar.

Lo que necesito ahora:

[describe aquí el cambio: por ejemplo "agregar los horarios lunes a domingo X–Y en el pie y en contacto", "subir el precio del Dragón Koi a 32.000 / 46.000", "publicar en GitHub Pages como perupenon", etc.]

---
