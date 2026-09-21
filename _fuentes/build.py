#!/usr/bin/env python3
"""Genera las páginas del sitio de Koi Sushi & Teppanyaki.

Ejecutar desde esta carpeta:  python3 build.py
Escribe index.html, menu.html, experiencias.html y contacto.html en la carpeta padre.
El header, el menú desplegable, la banda de contacto y el footer se comparten.
Los datos del menú están en MENU (abajo). Precios en COP, tal como en la carta 2026.
"""
import html
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# ---------------------------------------------------------------- datos
WA_NUM = '573203853275'
WA_TXT = 'Hola, Koi. Quiero hacer un pedido, ¿me comparten el menú?'
WA = f'https://wa.me/{WA_NUM}?text=' + html.escape(
    'Hola,%20Koi.%20Quiero%20hacer%20un%20pedido%2C%20%C2%BFme%20comparten%20el%20men%C3%BA%3F')
WA_RESERVA = f'https://wa.me/{WA_NUM}?text=Hola%2C%20Koi.%20Quiero%20reservar%20una%20mesa.'
WA_CATERING = f'https://wa.me/{WA_NUM}?text=Hola%2C%20Koi.%20Quiero%20informaci%C3%B3n%20sobre%20catering%20y%20teppanyaki%20show.'
WA_CLASES = f'https://wa.me/{WA_NUM}?text=Hola%2C%20Koi.%20Quiero%20informaci%C3%B3n%20sobre%20las%20clases%20de%20sushi.'
IG = 'https://www.instagram.com/koisushiyteppan/'
TIKTOK = 'https://www.tiktok.com/@koisushiyteppan'
FB = 'https://www.facebook.com/Koicocinaoriental'
MAIL = 'koicocinaoriental@gmail.com'
ADDRESS = 'Calle 16 #83A-15, barrio El Ingenio'
CITY = 'Cali, Colombia'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Calle+16+%2383A-15%2C+Cali%2C+Colombia'
MAPS_EMBED = 'https://www.google.com/maps?q=Calle+16+%2383A-15%2C+Cali%2C+Colombia&output=embed'

ARROW = '<span class="ic"><svg viewBox="0 0 10 10" fill="none" stroke-width="1.4"><path d="M1 5h8M5.5 1.5 9 5l-3.5 3.5"/></svg></span>'
EXT = '<span class="ic"><svg viewBox="0 0 10 10" fill="none" stroke-width="1.4"><path d="M2 8 8 2M3 2h5v5"/></svg></span>'
EXT_SM = '<svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M2 8 8 2M3 2h5v5"/></svg>'
STAR = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m12 2 2.9 6.6 7.1.7-5.4 4.8 1.6 7L12 17.4 5.8 21l1.6-7L2 9.3l7.1-.7z"/></svg>'

# ---------------------------------------------------------------- menú
# Cada categoría: id, título, kanji, nota opcional, y una lista de bloques.
# Bloque = dict con 'items' (lista) y opcionalmente 'title', 'note', 'cols' (encabezado x5/x10).
# Item = (nombre, precio, descripción) — precio puede ser:
#   '25.000'                       precio único
#   ('25.000', '38.000')           x5 / x10
#   {'x10': '36.000'}              solo x10
#   {'was': '126.000', 'now': '102.000'}   combo con precio anterior tachado
#   [('Veggie', '17.500'), ...]    opciones con precio cada una
# Un nombre que termina en '*' se marca como plato ganador de festival.

MENU = [
    dict(id='entradas', title='Entradas', jp='エントリー', blocks=[dict(items=[
        ('Kani yaki', '15.500', 'Palmito de cangrejo japonés apanado en panko acompañado de salsa agridulce.'),
        ('Coctel de camarón', '30.500', 'Camarones salteados marinados en limón, cebolla morada, cilantro y picadillo de tomate y maicitos.'),
        ('Karaage', '20.500', 'Trocitos de pollo apanado en salsa de miel, jengibre y ajonjolí.'),
        ('Bonsai', '18.000', 'Vegetales en tempura: brócoli, zanahoria, calabacín y champiñones. Pídelo con salsa agridulce o miel mostaza.'),
        ('Ebi furai', '29.000', 'Camarones en panko acompañados por salsa agridulce.'),
        ('Ika yaki', '26.500', 'Anillos de calamar en panko acompañados de salsa agridulce.'),
        ('Mabushita ebi', '35.500', '4 langostinos con queso crema, apanados en panko, acompañados de salsa ponzu o miel mostaza.'),
        ('Tofu crocante', '17.000', 'Cubitos de tofu en panko, acompañados de salsa mayochile.'),
        ('Harumakis', [('Vegetarianos', '16.500'), ('Con pollo', '19.500'), ('Lomo', '20.500'), ('Tocineta', '20.500'), ('Camarón', '21.000')],
         'Dos rollitos crocantes con rellenos típicos de Japón.'),
        ('Dumplings', [('Veggie', '17.500'), ('Mixto (res y cerdo)', '19.500')],
         'Masa wanton rellena y al vapor, acompañada de salsa ponzu.'),
    ])]),

    dict(id='teppanyaki', title='Teppanyaki', jp='鉄板焼き',
         note='Se arma en dos pasos: escoge la preparación y luego la receta.',
         steps=[
             ('Yakimeshi', 'Arroz frito con zanahoria, cebolla, maíz, cebollín, tortilla de huevo, raíz china, ajonjolí y salsa soya, salteado al mejor estilo teppan.'),
             ('Yakisoba', 'Pasta crespa con zanahoria, cebolla cabezona, calabacín, hatsai, brócoli, cebollín y aceite de sésamo, en salsa otafuko.'),
             ('Yasaitame', 'Mix de zanahoria, cebolla cabezona, calabacín, hatsai, brócoli y cebollín salteados en salsa teriyaki.'),
         ],
         blocks=[dict(title='Paso 2 · La receta', items=[
             ('Fusion', '30.500', 'Trozos de lomo viche, pollo y jamón salteados al estilo japonés en salsa de soya.'),
             ('Mandarín', '35.500', 'Trocitos de pollo, lomo viche y cerdo marinado.'),
             ('Nipón', '36.500', 'Pollo, tocineta, camarón y plátano maduro salteados en salsa soya y mantequilla de jengibre y ajo.'),
             ('Samba', '37.500', 'Costilla ahumada, pollo, tocineta y plátano maduro salteados en salsa del chef.'),
             ('Mar y tierra', '41.000', 'Camarón, trozos de lomo viche y pollo salteados en mantequilla de jengibre y ajo.'),
             ('Mix mariscos', '41.000', 'Anillos de calamar, pescado blanco, calamar baby y palmito, salteados en salsa soya.'),
             ('Sayori', '42.000', 'Camarones salteados en salsa soya y mantequilla de jengibre.'),
         ])]),

    dict(id='especiales', title='Especiales', jp='特産品',
         note='Acompaña tu plato especial con 2 de estas opciones: yakimeshi, yasaitame o papas a la francesa. Los platos marcados con ★ fueron ganadores de festivales gastronómicos en 2020.',
         blocks=[dict(items=[
             ('Koi especial*', '45.000', 'Yakimeshi con pollo y camarón y 5 bocados de sushi filadelfia. Acompáñalo con harumakis veggie o kani yaki. Ganador del Festival del Mar.'),
             ('Koi mixto*', '55.000', 'Trocitos de pollo y lomo biche desglasados en vino tinto, teriyaki y ajonjolí, con 3 langostinos desglasados en mantequilla y limón. Ganador del Festival del Asado.'),
             ('Terramar*', '48.000', 'Yakimeshi con trocitos de pollo y camarón al estilo teppanyaki, coronado con trozos de lomo biche desglasados en vino tinto, terminados en teriyaki y ajonjolí. Ganador del Festival del Arroz.'),
             ('Toriyaki', '40.000', 'Trozos de pollo desglasados en vino blanco y salteados en salsa teriyaki.'),
             ('Tonkotsu especial', '40.000', 'Trozos de lomo de cerdo salteados en salsa teriyaki y vino tinto.'),
             ('Costillas del Valle', '43.000', 'Costillas teppan glaseadas en vino tinto y salsa BBQ oriental.'),
             ('Combinación', '45.000', 'Trozos de lomo viche y pollo salteados en salsa teriyaki y costilla ahumada en salsa BBQ.'),
             ('Sayori especial', '46.000', 'Camarones salteados en vino blanco, limón y soya.'),
             ('Teriyaki', '47.500', 'Trozos de lomo viche desglasados en vino tinto y salteados en salsa teriyaki y ajonjolí.'),
             ('Frutos del mar', '50.000', 'Camarón, calamar baby, filete de pescado, kanikama y anillos de calamar desglasados en vino blanco.'),
             ('Sayori mixto', '55.000', 'Yakimeshi con camarón, acompañado de trozos de lomo viche y pollo salteados en salsa teriyaki y costilla ahumada en salsa BBQ.'),
             ('Salmón', '65.000', 'Filete de salmón desglasado en vino tinto y salsa teriyaki.'),
             ('Salteado agridulce', [('De pollo', '38.500'), ('Cerdo', '40.000'), ('Lomo', '44.000'), ('Camarón', '47.000')],
              'Proteína apanada salteada con vegetales en salsa agridulce, acompañada de una porción de arroz frito.'),
         ])]),

    dict(id='ramen', title='Ramen', jp='ラーメン',
         note='Caldo asiático a base de vegetales, cebollín, cilantro y pasta, terminado con ajonjolí. Puedes pedirlo con huevo cocido.',
         blocks=[dict(items=[
             ('Tori', '29.000', 'Pollo.'),
             ('Niku', '33.500', 'Lomo viche.'),
             ('Tonkotsu', '33.500', 'Cerdo.'),
             ('Ebi', '34.000', 'Camarón.'),
             ('Sakura', '35.000', 'Tilapia, calamar baby y tubo.'),
         ])]),

    dict(id='nigiri-sashimi', title='Nigiri y sashimi', jp='握り寿司 · 刺身', blocks=[
        dict(title='Nigiri', note='Corte de pescado fresco servido sobre una base de arroz.', items=[
            ('Salmón', '21.500', ''), ('Kanikama', '21.500', ''), ('Atún', '22.500', ''), ('Zuzuki', '22.500', ''),
        ]),
        dict(title='Sashimi', note='Cortes muy finos de pescado fresco con guarnición de zanahoria, pepino y aguacate en salsa ponzu.', items=[
            ('Tilapia', '28.500', 'Braseada en salsa teriyaki.'),
            ('Atún fresco', '32.000', ''),
            ('Salmón fresco', '32.500', ''),
            ('Mixto', '55.000', 'Atún y salmón.'),
            ('Combinación', '65.000', 'Atún y salmón fresco, tilapia ahumada.'),
        ]),
    ]),

    dict(id='sushi-tradicional', title='Sushi tradicional', jp='寿司ロール', blocks=[
        dict(cols=True, items=[
            ('Sake maki', ('25.000', '38.000'), 'Roll relleno de salmón fresco al estilo maki.'),
            ('Tuna maki', ('24.000', '36.000'), 'Roll relleno de atún fresco al estilo maki.'),
            ('Crab maki', ('25.000', '37.000'), 'Roll relleno de kanikama y masago al estilo maki.'),
            ('Zuzuki maki', ('24.000', '35.000'), 'Roll relleno de pescado blanco al estilo maki.'),
            ('Ebi tempura maki', ('27.000', '39.000'), 'Roll relleno de langostino en panko, aguacate y mayonesa japonesa al estilo maki.'),
            ('Rainbow roll', ('29.000', '43.000'), 'Kanikama y aguacate, terminado con topping de masago, salmón, tilapia y atún.'),
        ]),
        dict(title='Combos', items=[
            ('Combo x30', {'was': '126.000', 'now': '102.000'}, 'Tuna maki x10, sake maki x10, crab maki x5 y ebi tempura x5.'),
            ('Combo x40', {'was': '191.000', 'now': '153.000'}, 'Tuna maki x10, sake maki x10, crab maki x5, ebi tempura x5, zuzuki x5 y rainbow x5.'),
            ('Combo x60', {'was': '228.000', 'now': '185.000'}, 'Tuna maki x10, sake maki x10, crab maki x10, ebi tempura x10, zuzuki x10 y rainbow x10.'),
        ]),
        dict(title='Barcos · Sushi appetizer', items=[
            ('Sushihana', '45.000', '5 bocados de maki (sake maki o tuna maki) y 4 bocados de nigiri (atún, salmón, kanikama y zuzuki).'),
            ('Benihana · Flor roja', '145.000', 'Maki: tuna x5, sake x5, crab x5 y ebi tempura x5. Nigiri: 1 atún, 1 salmón, 1 kanikama y 1 tilapia. Temaki: 1 salmón y 1 kanikama. Sashimi mixto (atún y salmón). Gunkan de masago x1.'),
            ('Hatsuhana · Flor de primavera', '237.500', 'Maki: tuna x10, sake x10, crab x10 y ebi tempura x10. Nigiri: 2 atún, 2 salmón, 2 kanikama y 2 tilapia. Temaki: 1 salmón, 1 kanikama y 1 atún. Sashimi mixto (atún, salmón y tilapia). Gunkan de masago x2.'),
        ]),
    ]),

    dict(id='sushi-sencillo', title='Sushi sencillo', jp='寿司ロール', blocks=[
        dict(cols=True, items=[
            ('Sayori', ('20.000', '33.500'), 'Roll en panko relleno de tilapia fresca, aguacate y queso crema.'),
            ('Crunchy tuna', ('22.500', '35.000'), 'Atún en panko, skin de salmón, aguacate y queso crema, con topping de aguacate y ajonjolí.'),
            ('Miyaki', ('22.500', '34.500'), 'Palmito de cangrejo en panko, queso crema y mango, terminado con topping de plátano guayabo y salsa de maracuyá.'),
            ('Filadelfia', ('23.000', '34.000'), 'Salmón fresco, aguacate y queso crema.'),
            ('Tropical roll', ('24.000', '35.000'), 'Salmón fresco, queso crema y mango, con topping de maduro y salsa de maracuyá.'),
            ('Spicy tuna', ('24.000', '36.000'), 'Atún fresco en salsa spicy, cebollín y aguacate, terminado al estilo maki.'),
            ('Alaska roll', ('24.000', '35.000'), 'Roll en panko relleno de salmón, queso crema y plátano maduro.'),
            ('California', ('24.000', '37.000'), 'Kanikama, aguacate y pepino, con topping de masago y ajonjolí.'),
            ('Torimaki', {'x10': '36.000'}, 'Pollo apanado, queso crema y aguacate con topping de plátano maduro, tocineta y salsa teriyaki.'),
            ('Teriyaki roll', {'x10': '38.000'}, 'Lomito a la plancha, queso crema y cebollín con topping de aguacate, tocineta y salsa teriyaki.'),
        ]),
        dict(title='Combos', items=[
            ('Combo x30', {'was': '127.000', 'now': '102.000'}, 'Filadelfia x5, alaska x5, sayori x10, miyaki x5 y spicy tuna x5.'),
            ('Combo x40', {'was': '162.000', 'now': '130.000'}, 'Filadelfia x5, alaska x5, sayori x10, miyaki x5, spicy tuna x5 y crunchy tuna x10.'),
            ('Combo x60', {'was': '222.000', 'now': '178.000'}, 'Filadelfia x5, alaska x5, sayori x10, miyaki x10, spicy tuna x10, crunchy tuna x10 y torimaki x10.'),
        ]),
    ]),

    dict(id='sushi-especial', title='Sushi especial', jp='寿司ロール', blocks=[
        dict(cols=True, items=[
            ('Dragón Koi', ('30.000', '44.000'), 'Langostino marinado en vino blanco y apanado en panko, queso crema y aguacate. Terminado con salmón flameado, topping de salsa dinamita y crunchy tempura.'),
            ('Ebi ichi ban', ('27.000', '40.000'), 'Langostino tempura, kanikama y aguacate. Terminado con topping de masago, ajonjolí y un toque de salsa dinamita.'),
            ('Ika maki', ('26.000', '41.000'), 'Calamares apanados, aguacate, queso crema y masago, terminado con tartar de atún, salmón y cebollín.'),
            ('Sumo roll', ('27.000', '39.000'), 'Pescado blanco, camarones apanados, queso crema y plátano maduro; terminado con palmito en salsa de queso. Panko opcional.'),
            ('Ojo de tigre', ('29.000', '42.000'), 'Atún, salmón y kanikama tempurados con aguacate, masago y ajonjolí, terminado con un dip de dinamita.'),
            ('Dragón roll', ('27.000', '40.000'), 'Langostino tempura, aguacate y queso crema. Terminado con topping de salmón fresco y salsa de maracuyá.'),
            ('Koi sushi roll', ('28.000', '39.000'), 'Salmón fresco, atún, cebollín y queso crema, con topping de salsa dinamita, kanikama, masago y ajonjolí.'),
            ('Valluno maki', ('28.000', '43.000'), 'Camarones apanados, queso crema y aguacate con topping de plátano maduro, terminado con salsa de queso caliente y teriyaki.'),
            ('Taimaki', ('27.000', '40.000'), 'Calamar apanado, queso crema y aguacate, con topping de pescado blanco flameado y salsa dinamita.'),
            ('Osaka roll', ('30.000', '42.000'), 'Roll apanado de camarón, queso crema, plátano maduro y aguacate. Topping de salsa dinamita, kanikama, masago, cebollín y ajonjolí.'),
            ('Sake special', ('29.000', '41.000'), 'Piel de salmón crocante, queso crema y aguacate. Terminado con topping de salmón fresco y salsa de maracuyá.'),
            ('Rock and roll', ('29.000', '41.000'), 'Roll relleno de salmón apanado y aguacate, con topping de queso y kanikama, acompañado de salsa agridulce.'),
            ('Shiretoko', ('29.000', '41.000'), 'Roll tempura relleno de palmito apanado, mango y aguacate, con topping de camarones en salsa de queso y anguila.'),
            ('Ebi tuna', {'x10': '45.000'}, 'x5 de tilapia apanada, queso crema y aguacate con topping de camarones en panko y salsa agridulce · x5 de langostino en panko, kanikama y aguacate con topping de atún flameado, mayo dulce y cebollín.'),
        ]),
        dict(title='Combos', items=[
            ('Combo x30 rolls', {'was': '126.000', 'now': '115.000'}, 'Sake special x10, valluno x10 y ojo de tigre x10.'),
            ('Combo x40 rolls', {'was': '161.000', 'now': '145.000'}, 'Sake special x10, valluno x10, ojo de tigre x10 y rock and roll x10.'),
            ('Combo x50 rolls', {'was': '202.000', 'now': '175.000'}, 'Sake special x10, valluno x10, ojo de tigre x10, rock and roll x10 y shiretoko x10.'),
            ('Combo x60 rolls', {'was': '242.000', 'now': '194.500'}, 'Sake special x10, valluno x10, ojo de tigre x10, rock and roll x10, shiretoko x10 y taimaki x10.'),
            ('Combo x80 rolls', {'was': '327.000', 'now': '263.500'}, 'Sake special x10, valluno x10, ojo de tigre x10, rock and roll x10, shiretoko x10, taimaki x10, osaka x10 y dragón koi x10.'),
        ]),
    ]),

    dict(id='vegetariano', title='Vegetariano', jp='ベジタリアン', blocks=[
        dict(cols=True, items=[
            ('Veggie crunchy', ('17.000', '28.000'), 'Roll apanado en panko relleno de pepino, aguacate, zanahoria y mango.'),
            ('Yasai roll', ('17.000', '28.000'), 'Vegetales tempura y aguacate, terminado en salsa teriyaki.'),
            ('Tropical veggie', ('17.000', '28.000'), 'Roll relleno de queso crema, mango y crunchy de zanahoria, con topping de plátano maduro y salsa de maracuyá.'),
            ('Tofu roll', ('20.000', '32.000'), 'Roll relleno de aguacate y tofu apanado, con topping de champiñones salteados y ajonjolí.'),
        ]),
        dict(items=[
            ('Ramen veggie', '26.000', 'Pasta con vegetales salteados, maíz dulce, raíz china y champiñón. Pídelo con o sin huevo.'),
            ('Natsu', '29.000', 'Frutos secos y champiñones salteados en salsa teriyaki. Pídelo en yakimeshi, yasaitame o yakisoba.'),
            ('Natsu especial', '31.500', 'Frutos secos, champiñones y tofu salteados en salsa teriyaki. Pídelo en yakimeshi, yasaitame o yakisoba.'),
            ('Koi especial veggie', '35.000', 'Yakimeshi con frutos secos, 2 harumakis veggie y 5 bocados de tropical veggie.'),
            ('Tofu especial', '35.500', 'Tofu apanado salteado con vegetales y champiñones en salsa agridulce, acompañado de una porción de arroz frito (ligeramente picante).'),
            ('Combo x30 veggie', '67.500', 'Veggie crunchy x10, yasai roll x10 y tropical veggie x10.'),
        ]),
    ]),

    dict(id='infantil', title='Menú infantil', jp='キッズメニュー', blocks=[dict(items=[
        ('Nuggets de pollo', '25.000', 'Trozos de pollo apanados acompañados de papas a la francesa y una copa de helado.'),
        ('Pasta con pollo o tocineta', '25.000', 'Pasta ramen con crema de leche, acompañada de una copa de helado.'),
        ('Yakimeshi con pollo o tocineta', '25.000', 'Arroz con la proteína de tu elección, acompañado de una copa de helado.'),
    ])]),

    dict(id='postres', title='Postres', jp='デザート', blocks=[dict(items=[
        ('Amagyozas', '16.000', 'Empanadas rellenas de arequipe y queso mozzarella, acompañadas de una bola de helado de vainilla y salsa de frutas.'),
        ('Helado frito', '14.000', 'Helado apanado en panko acompañado de salsa del chef.'),
        ('Brownie con helado', '13.500', 'Brownie caliente con helado de vainilla.'),
    ])]),

    dict(id='bebidas', title='Bebidas', jp='飲み物', blocks=[
        dict(title='Jugos', items=[
            ('Jugos en agua', [('Mango, mora, fresa o lulo', '9.500'), ('Maracuyá', '10.500')], ''),
            ('Jugos en leche', [('Mango, mora, fresa o lulo', '12.500'), ('Maracuyá', '13.500')], ''),
        ]),
        dict(title='Limonadas', items=[
            ('Natural', '8.500', ''), ('De hierbabuena', '10.000', ''), ('Cerezada', '13.000', ''), ('Con coco', '13.000', ''),
            ('De sandía', '15.000', ''), ('De lychees', '15.000', ''), ('Mango viche', '16.000', ''), ('De vino', '21.000', ''), ('De tequila', '24.000', ''),
        ]),
        dict(title='Sodas italianas', items=[
            ('Sandía limón', '18.500', ''), ('Frutos rojos', '18.500', ''), ('Frutos amarillos', '18.500', ''), ('Lychees limón', '18.500', ''),
        ]),
        dict(title='Café', items=[
            ('Espresso', '4.350', ''), ('Americano', '5.400', ''), ('Capuccino', '6.500', ''), ('Café latte', '6.500', ''),
            ('Capuccino vainilla', '8.650', ''), ('Mocaccino', '9.750', ''), ('Capuccino de licor', '16.200', ''),
        ]),
        dict(title='Gaseosas y agua', items=[
            ('Gaseosas Postobón', '6.500', ''), ('Canada Dry', '6.500', ''), ('Bretaña', '6.500', ''),
            ('Agua Hatsu', '6.500', ''), ('Agua con gas Hatsu', '6.500', ''), ('Té Hatsu', '9.000', ''),
        ]),
        dict(title='Cervezas', note='Sujetas a disponibilidad.', items=[
            ('Andina', '8.500', ''), ('Club Colombia', '9.000', ''), ('Águila Light', '9.000', ''), ('Coronita', '10.000', ''),
            ('Heineken', '11.000', ''), ('Corona', '12.000', ''), ('Stella Artois', '12.000', ''),
            ('Tres Cordilleras', '15.000', 'Artesanal.'), ('BBC', '16.000', 'Artesanal.'),
            ('Michelado', '2.000', ''), ('Zumo de limón', '2.000', ''),
        ]),
        dict(title='Cocteles', note='Frutas: mango viche, fresa, maracuyá y sandía. 2 x 1 de lunes a jueves de 6:00 a 9:00 pm; viernes a domingo 2 x 50.000 (mismo sabor).', items=[
            ('Mojito tradicional', '32.000', ''), ('Margarita', '33.000', ''), ('Daiquiri de frutas', '34.000', ''),
            ('Mojito de frutas', '36.000', ''), ('Margarita de frutas', '37.000', ''), ('Orgasmo', '38.000', ''),
        ]),
    ]),

    dict(id='adiciones', title='Adiciones', jp='追加', blocks=[
        dict(title='Proteína', items=[
            ('Jamón · 80 g', '8.000', ''), ('Champiñones · 100 g', '8.000', ''), ('Pescado blanco · 100 g', '9.000', ''),
            ('Cerdo · 100 g', '10.000', ''), ('Pollo · 100 g', '12.000', ''), ('Tocineta · 80 g', '13.000', ''),
            ('Lomo biche · 100 g', '14.000', ''), ('Costilla ahumada · 80 g', '14.000', ''), ('Camarón · 50 g (5 und)', '16.000', ''),
        ]),
        dict(title='Otras adiciones', items=[
            ('Ajonjolí', '2.000', ''), ('Plátano maduro', '3.000', ''), ('Aguacate', '3.000', ''), ('Queso crema', '3.000', ''),
            ('Panko', '3.000', ''), ('Salsa de maracuyá', '3.500', ''), ('Salsa de queso', '4.500', ''), ('Salsa agridulce', '4.500', ''),
            ('Mayonesa picante', '4.500', ''), ('Salsa dinamita', '6.500', ''), ('Papas a la francesa', '8.500', ''),
            ('Yasaitame', '10.000', ''), ('Yakimeshi', '12.000', ''),
        ]),
    ]),
]

# ---------------------------------------------------------------- helpers
def price_html(p):
    if isinstance(p, str):
        return f'<span class="menu-item__price">{p}</span>'
    if isinstance(p, tuple):
        return f'<span class="menu-item__price"><small>x5</small>{p[0]} &nbsp; <small>x10</small>{p[1]}</span>'
    if isinstance(p, dict) and 'x10' in p:
        return f'<span class="menu-item__price"><small>x10</small>{p["x10"]}</span>'
    if isinstance(p, dict) and 'was' in p:
        return f'<span class="menu-item__price"><span class="was">{p["was"]}</span>{p["now"]}</span>'
    return '<span class="menu-item__price"></span>'


def item_html(name, price, desc):
    star = ''
    if name.endswith('*'):
        name = name[:-1]
        star = '<span class="star" title="Ganador de festival">★</span>'
    out = f'<div class="menu-item"><span class="menu-item__name">{html.escape(name)}{star}</span>'
    if isinstance(price, list):
        out += '<span class="menu-item__price"></span>'
        if desc:
            out += f'<p class="menu-item__desc">{html.escape(desc)}</p>'
        out += '<div class="menu-item__opts">' + ''.join(
            f'<span>{html.escape(n)}</span><span>{v}</span>' for n, v in price) + '</div>'
    else:
        out += price_html(price)
        if desc:
            out += f'<p class="menu-item__desc">{html.escape(desc)}</p>'
    return out + '</div>'


def block_html(b):
    out = '<div class="menu-sub">'
    if b.get('title'):
        note = f'<span class="menu-sub__note">{html.escape(b["note"])}</span>' if b.get('note') else ''
        out += f'<h4 class="label menu-sub__title">{html.escape(b["title"])}{note}</h4>'
    elif b.get('note'):
        out += f'<p class="menu-cat__note">{html.escape(b["note"])}</p>'
    if b.get('cols'):
        out += '<div class="menu-cols-head"><span>Roll</span><span>x5 &nbsp;·&nbsp; x10 bocados</span></div>'
    out += ''.join(item_html(*it) for it in b['items'])
    return out + '</div>'


def cat_html(c):
    note = f'<p class="menu-cat__note">{html.escape(c["note"])}</p>' if c.get('note') else ''
    out = f'<section class="menu-cat" id="{c["id"]}">'
    out += f'<div class="menu-cat__head"><h2 class="menu-cat__title">{html.escape(c["title"])}<span class="jp">{c["jp"]}</span></h2>{note}</div>'
    if c.get('steps'):
        out += '<h4 class="label menu-sub__title">Paso 1 · La preparación</h4><div class="menu-steps">'
        for n, t in c['steps']:
            out += f'<div class="menu-step"><p class="menu-step__name">{html.escape(n)}</p><p class="menu-step__text">{html.escape(t)}</p></div>'
        out += '</div>'
    blocks = c['blocks']
    if len(blocks) > 1 and c['id'] in ('bebidas', 'adiciones', 'nigiri-sashimi'):
        out += '<div class="menu-cat__cols">' + ''.join(block_html(b) for b in blocks) + '</div>'
    else:
        out += ''.join(block_html(b) for b in blocks)
    return out + '</section>'


# ---------------------------------------------------------------- plantilla
def head(title, desc, og_img, body_class, preload=None):
    preload_tags = ''
    if preload:
        preload_tags = '\n  ' + '\n  '.join(preload)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="theme-color" content="#0E0F12">
  <link rel="icon" type="image/png" href="img/favicon.png">
  <link rel="apple-touch-icon" href="img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{preload_tags}
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@110,400;110,500;125,400;125,500&family=Bodoni+Moda:wght@400&family=DM+Sans:wght@300;400;500&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@110,400;110,500;125,400;125,500&family=Bodoni+Moda:wght@400&family=DM+Sans:wght@300;400;500&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@110,400;110,500;125,400;125,500&family=Bodoni+Moda:wght@400&family=DM+Sans:wght@300;400;500&display=swap"></noscript>
  <link rel="stylesheet" href="css/style.css">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:image" content="img/{og_img}">
  <meta property="og:type" content="website">
</head>
<body class="{body_class}">'''


HEADER = f'''
  <header class="header">
    <div class="header__bar">
      <a class="btn-outline header__cta" href="{WA}" target="_blank" rel="noopener"><span class="full">Pedir a domicilio</span><span class="short">Pedir</span></a>
      <a class="header__logo" href="index.html" aria-label="Koi Sushi &amp; Teppanyaki, inicio">
        <img class="light" src="img/marca-blanca.png" alt="Koi" width="700" height="369">
        <img class="dark" src="img/marca-color.png" alt="" width="700" height="369">
      </a>
      <button class="header__burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav"><span></span></button>
    </div>
  </header>
  <div class="nav__scrim"></div>
  <nav class="nav" id="nav" aria-label="Principal">
    <div class="nav__panel">
      <div class="nav__links">
        <a href="index.html">Inicio</a>
        <a href="menu.html">Menú</a>
        <a href="experiencias.html">Experiencias</a>
        <a href="contacto.html">Contacto</a>
      </div>
      <div class="nav__ext">
        <a class="arrow-link ext" href="{IG}" target="_blank" rel="noopener">Instagram {EXT}</a>
        <a class="arrow-link ext" href="{TIKTOK}" target="_blank" rel="noopener">TikTok {EXT}</a>
        <a class="arrow-link ext" href="{WA}" target="_blank" rel="noopener">WhatsApp {EXT}</a>
      </div>
      <div class="nav__media">
        <picture>
          <source type="image/webp" media="(max-width: 767px)" srcset="img/barco-sushi-m.webp">
          <source type="image/webp" srcset="img/barco-sushi.webp">
          <source media="(max-width: 767px)" srcset="img/barco-sushi-m.jpg">
          <img src="img/barco-sushi.jpg" alt="Barco de sushi de Koi" loading="lazy" decoding="async">
        </picture>
        <div class="cap"><span class="label">Sushi · Ramen · Teppanyaki</span><img src="img/logo-blanco.png" alt=""><span class="label">El Ingenio · Cali</span></div>
      </div>
    </div>
  </nav>
'''

CONTACT_BAND = f'''
  <section class="contact-band">
    <div class="grid">
      <div class="contact-band__title reveal">
        <p class="label">Contacto y ubicación</p>
        <h2>Te esperamos en El Ingenio</h2>
      </div>
      <div class="contact-band__info reveal reveal-d1">
        <p>WhatsApp <a href="{WA}" target="_blank" rel="noopener">+57 320 385 3275</a><br>Correo <a href="mailto:{MAIL}">{MAIL}</a></p>
        <p><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}<br>{CITY}</a></p>
        <p>Domicilios en Cali, Buga, Palmira y Rozo</p>
      </div>
    </div>
  </section>
'''

FOOTER = f'''
  <footer class="footer">
    <div class="footer__top">
      <div class="footer__brand reveal">
        <picture>
          <source type="image/webp" srcset="img/fachada-m.webp">
          <img src="img/fachada-m.jpg" alt="Fachada del restaurante Koi en el barrio El Ingenio" loading="lazy" decoding="async" width="150" height="200">
        </picture>
        <div>
          <p>Sushi, ramen y teppanyaki con el sabor de la cocina oriental, en el barrio El Ingenio de Cali.</p>
          <a class="arrow-link on-light" href="experiencias.html">Experiencias Koi {ARROW}</a>
        </div>
      </div>
      <div class="footer__nav reveal reveal-d1">
        <p class="label footer__col-title">Navegación</p>
        <ul>
          <li><a href="index.html">Inicio</a></li>
          <li><a href="menu.html">Menú</a></li>
          <li><a href="experiencias.html">Experiencias</a></li>
          <li><a href="contacto.html">Contacto</a></li>
        </ul>
        <ul>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram {EXT_SM}</a></li>
          <li><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok {EXT_SM}</a></li>
          <li><a href="{FB}" target="_blank" rel="noopener">Facebook {EXT_SM}</a></li>
        </ul>
      </div>
      <div class="footer__order reveal reveal-d2">
        <p class="label footer__col-title">Domicilios</p>
        <p>Pide por WhatsApp y te lo llevamos a la casa en Cali, Buga, Palmira y Rozo.</p>
        <a class="btn-solid" href="{WA}" target="_blank" rel="noopener">Pedir por WhatsApp</a>
        <a class="tel" href="tel:+573203853275">+57 320 385 3275</a>
      </div>
    </div>
    <div class="footer__wordmark" aria-hidden="true">Koi Sushi<span class="jp">鯉寿司と鉄板</span></div>
    <div class="footer__legal">
      <span>Koi Sushi &amp; Teppanyaki · Cocina oriental © 2026 · Todos los derechos reservados</span>
      <span>{CITY}</span>
    </div>
  </footer>
  <a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg></a>
  <script src="js/main.js" defer></script>
</body>
</html>
'''


def card(img, title, price, text, badge=''):
    b = f'<span class="card__badge">{STAR} {badge}</span>' if badge else ''
    webp = img.replace('.jpg', '.webp')
    return f'''        <article class="card">
          <picture>
            <source type="image/webp" srcset="img/{webp}">
            <img src="img/{img}" alt="{html.escape(title)}" loading="lazy" decoding="async">
          </picture>
          <div class="card__head">{b}<h3 class="h3 card__title">{html.escape(title)}</h3><span class="card__price">{price}</span></div>
          <div>
            <p class="card__text">{html.escape(text)}</p>
            <a class="arrow-link on-dark" href="{WA}" target="_blank" rel="noopener">Pedir {ARROW}</a>
          </div>
        </article>
'''


# ---------------------------------------------------------------- páginas
def page_index():
    return head('Koi Sushi & Teppanyaki · Cocina oriental en Cali',
                'Sushi, ramen y teppanyaki en el barrio El Ingenio, Cali. Rolls, barcos de sushi, ramen, platos especiales ganadores de festivales, catering y domicilios.',
                'sushi-especial-m.jpg', 'page-inicio',
                preload=[
                    '<link rel="preload" as="image" href="img/sushi-especial-m.webp" type="image/webp" media="(max-width: 767px)">',
                    '<link rel="preload" as="image" href="img/sushi-especial.webp" type="image/webp" media="(min-width: 768px)">'
                ]) + '''
  <div class="preloader" aria-hidden="true"><p>Sushi, ramen y teppanyaki.<br><em>Cocina oriental</em> en Cali.</p></div>''' + HEADER + f'''
  <main>
    <section class="hero">
      <div class="hero__media">
        <picture>
          <source type="image/webp" media="(max-width: 767px)" srcset="img/sushi-especial-m.webp">
          <source type="image/webp" srcset="img/sushi-especial.webp">
          <source media="(max-width: 767px)" srcset="img/sushi-especial-m.jpg">
          <img src="img/sushi-especial.jpg" alt="Rolls de sushi especial de Koi" fetchpriority="high" decoding="async">
        </picture>
      </div>
      <p class="label hero__label reveal">Sushi · Ramen · Teppanyaki <span class="jp">鯉寿司と鉄板</span></p>
      <h1 class="hero__title reveal reveal-d1">Cocina oriental en Cali</h1>
      <div class="hero__foot reveal reveal-d2">
        <div>
          <p class="lede">Rolls, barcos de sushi, ramen y teppanyaki al mejor estilo japonés, en el barrio El Ingenio y a domicilio.</p>
          <a class="arrow-link on-dark" href="menu.html">Ver menú {ARROW}</a>
        </div>
      </div>
    </section>

    <section class="split">
      <div class="split__media">
        <picture>
          <source type="image/webp" media="(max-width: 767px)" srcset="img/teppanyaki-m.webp">
          <source type="image/webp" srcset="img/teppanyaki.webp">
          <source media="(max-width: 767px)" srcset="img/teppanyaki-m.jpg">
          <img src="img/teppanyaki.jpg" alt="Platos de teppanyaki recién salteados" loading="lazy" decoding="async">
        </picture>
      </div>
      <div class="split__panel">
        <div>
          <p class="label reveal">Teppanyaki <span class="jp">鉄板焼き</span></p>
          <h2 class="reveal reveal-d1">Salteado a la plancha, a tu manera</h2>
        </div>
        <div class="split__foot reveal reveal-d2">
          <p class="lede">Escoge la base —yakimeshi, yakisoba o yasaitame— y luego la receta: pollo, lomo, cerdo, camarón o mariscos, salteados al mejor estilo teppan.</p>
          <a class="arrow-link on-dark" href="menu.html#teppanyaki">Armar mi teppanyaki {ARROW}</a>
        </div>
      </div>
    </section>

    <section class="full-image">
      <picture>
        <source type="image/webp" media="(max-width: 767px)" srcset="img/tabla-sushi-m.webp">
        <source type="image/webp" srcset="img/tabla-sushi.webp">
        <source media="(max-width: 767px)" srcset="img/tabla-sushi-m.jpg">
        <img src="img/tabla-sushi.jpg" alt="Tabla de sushi con rolls variados" loading="lazy" decoding="async">
      </picture>
    </section>

    <section class="intro on-sand">
      <div class="grid">
        <p class="label intro__label reveal">Bienvenidos a Koi</p>
        <div class="intro__body">
          <h2 class="reveal">Sushi, ramen y teppanyaki con sabor propio</h2>
          <p class="lede reveal reveal-d1">Koi es cocina oriental hecha en Cali: pescado fresco, rolls apanados en panko, caldos de ramen y platos salteados a la plancha que han ganado festivales gastronómicos. Ven al restaurante o pide a domicilio.</p>
          <a class="arrow-link on-light reveal reveal-d2" href="menu.html">Ver el menú completo {ARROW}</a>
        </div>
      </div>
    </section>

    <section class="cards on-sand">
      <div class="cards__head reveal">
        <p class="label">Platos destacados</p>
        <a class="arrow-link on-light" href="menu.html">Menú completo {ARROW}</a>
      </div>
      <div class="cards__track reveal reveal-d1">
{card('card-koi-especial.jpg', 'Koi especial', '$45.000', 'Yakimeshi con pollo y camarón y 5 bocados de sushi filadelfia. Acompáñalo con harumakis veggie o kani yaki.', 'Festival del Mar 2020')}{card('card-terramar.jpg', 'Terramar', '$48.000', 'Yakimeshi con pollo y camarón al estilo teppanyaki, coronado con lomo biche desglasado en vino tinto, teriyaki y ajonjolí.', 'Festival del Arroz 2020')}{card('card-dragon-koi.jpg', 'Dragón Koi', '$44.000 x10', 'Langostino en panko, queso crema y aguacate, terminado con salmón flameado, salsa dinamita y crunchy tempura.')}{card('card-tonkotsu.jpg', 'Ramen tonkotsu', '$33.500', 'Caldo asiático de vegetales con pasta, cerdo, cebollín y cilantro, terminado con ajonjolí. Pídelo con huevo cocido.')}{card('card-sushi-especial.jpg', 'Ojo de tigre', '$42.000 x10', 'Atún, salmón y kanikama tempurados con aguacate, masago y ajonjolí, terminado con un dip de dinamita.')}      </div>
      <div class="cards__nav">
        <button data-prev aria-label="Anterior"><svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M11 6H1M5 1.5 1 6l4 4.5"/></svg></button>
        <div class="cards__bar"><i></i></div>
        <button data-next aria-label="Siguiente"><svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M1 6h10M7 1.5 11 6l-4 4.5"/></svg></button>
      </div>
    </section>

    <section class="exp on-cream">
      <div class="exp__head reveal">
        <div>
          <p class="label">Experiencias Koi</p>
          <h2>Llevamos el sabor a donde estés</h2>
        </div>
        <a class="arrow-link on-light" href="experiencias.html">Ver experiencias {ARROW}</a>
      </div>
      <div class="exp__grid">
        <article class="exp-item reveal">
          <picture>
            <source type="image/webp" srcset="img/chef-teppanyaki.webp">
            <img src="img/chef-teppanyaki.jpg" alt="Chef de Koi en un show de teppanyaki" loading="lazy" decoding="async">
          </picture>
          <div class="exp-item__body">
            <h3 class="exp-item__title">Teppanyaki show</h3>
            <span class="label exp-item__sub">Live show</span>
            <p class="exp-item__text">El mejor espectáculo de cocina en vivo para todas las ocasiones: cumpleaños, eventos y reuniones.</p>
            <a class="arrow-link on-light" href="{WA_CATERING}" target="_blank" rel="noopener">Cotizar {ARROW}</a>
          </div>
        </article>
        <article class="exp-item reveal reveal-d1">
          <picture>
            <source type="image/webp" srcset="img/sushi-en-casa.webp">
            <img src="img/sushi-en-casa.jpg" alt="Barco de sushi para catering" loading="lazy" decoding="async">
          </picture>
          <div class="exp-item__body">
            <h3 class="exp-item__title">Sushi at home</h3>
            <span class="label exp-item__sub">Sushi catering</span>
            <p class="exp-item__text">Deléitate con nuestro catering de sushi y sorprende a tus invitados con barcos y tablas para compartir.</p>
            <a class="arrow-link on-light" href="{WA_CATERING}" target="_blank" rel="noopener">Cotizar {ARROW}</a>
          </div>
        </article>
        <article class="exp-item reveal reveal-d2">
          <picture>
            <source type="image/webp" srcset="img/clases-sushi.webp">
            <img src="img/clases-sushi.jpg" alt="Clase de sushi en Koi" loading="lazy" decoding="async">
          </picture>
          <div class="exp-item__body">
            <h3 class="exp-item__title">Clases de sushi</h3>
            <span class="label exp-item__sub">Aprende con Koi</span>
            <p class="exp-item__text">Aprende a hacer sushi de forma recreativa. Invita a tu familia y amigos a probar este arte japonés preparado por ti.</p>
            <a class="arrow-link on-light" href="{WA_CLASES}" target="_blank" rel="noopener">Reservar clase {ARROW}</a>
          </div>
        </article>
      </div>
    </section>

    <section class="about on-mist">
      <div class="grid">
        <p class="label about__label reveal">Domicilios</p>
        <div class="about__media reveal reveal-d1">
          <picture>
            <source type="image/webp" media="(max-width: 767px)" srcset="img/koi-especial-m.webp">
            <source type="image/webp" srcset="img/koi-especial.webp">
            <source media="(max-width: 767px)" srcset="img/koi-especial-m.jpg">
            <img src="img/koi-especial.jpg" alt="Koi especial: yakimeshi, harumakis y sushi filadelfia" loading="lazy" decoding="async">
          </picture>
        </div>
        <div class="about__body">
          <h2 class="reveal">Koi hasta la puerta de tu casa</h2>
          <p class="lede reveal reveal-d1">Pide por WhatsApp y recibe tu sushi, ramen o teppanyaki donde estés. Cubrimos Cali y también Buga, Palmira y Rozo. El restaurante es pet friendly.</p>
          <ul class="pill-list reveal reveal-d2">
            <li>Cali</li><li>Buga</li><li>Palmira</li><li>Rozo</li><li>Pet friendly</li>
          </ul>
          <a class="arrow-link on-light reveal reveal-d2" href="{WA}" target="_blank" rel="noopener">Pedir por WhatsApp {ARROW}</a>
        </div>
      </div>
    </section>
  </main>''' + CONTACT_BAND + FOOTER


def page_menu():
    nav = ''.join(f'<a href="#{c["id"]}">{html.escape(c["title"])}</a>' for c in MENU)
    cats = ''.join(cat_html(c) for c in MENU)
    return head('Menú · Koi Sushi & Teppanyaki, Cali',
                'Menú completo de Koi: entradas, teppanyaki, especiales, ramen, nigiri, sashimi, sushi tradicional, sencillo y especial, vegetariano, postres y bebidas. Precios en pesos colombianos.',
                'nigiri-m.jpg', 'page-menu',
                preload=[
                    '<link rel="preload" as="image" href="img/nigiri-m.webp" type="image/webp" media="(max-width: 767px)">',
                    '<link rel="preload" as="image" href="img/nigiri.webp" type="image/webp" media="(min-width: 768px)">'
                ]) + HEADER + f'''
  <main>
    <section class="hero hero--short">
      <div class="hero__media">
        <picture>
          <source type="image/webp" media="(max-width: 767px)" srcset="img/nigiri-m.webp">
          <source type="image/webp" srcset="img/nigiri.webp">
          <source media="(max-width: 767px)" srcset="img/nigiri-m.jpg">
          <img src="img/nigiri.jpg" alt="Nigiri de salmón, atún y kanikama sobre tabla de madera" fetchpriority="high" decoding="async">
        </picture>
      </div>
      <p class="label hero__label reveal">Koi Sushi &amp; Teppanyaki <span class="jp">メニュー</span></p>
      <h1 class="hero__title reveal reveal-d1">Nuestro menú</h1>
      <div class="hero__foot reveal reveal-d2">
        <div>
          <p class="lede">Pescado fresco, rolls en panko, caldos de ramen y salteados a la plancha. Precios en pesos colombianos.</p>
          <div class="hero__actions">
            <a class="arrow-link on-dark" href="{WA}" target="_blank" rel="noopener">Pedir a domicilio {ARROW}</a>
            <a class="arrow-link on-dark" href="{WA_RESERVA}" target="_blank" rel="noopener">Reservar mesa {ARROW}</a>
          </div>
        </div>
      </div>
    </section>

    <nav class="menu-nav" aria-label="Categorías del menú"><div class="menu-nav__track">{nav}</div></nav>

    <section class="menu-page on-cream">
      <div class="menu-page__intro">
        <h2 class="reveal">Entradas, teppanyaki, ramen y más de treinta rolls de sushi</h2>
        <p class="lede reveal reveal-d1">Los rolls se piden por 5 o por 10 bocados. Los platos marcados con ★ ganaron festivales gastronómicos en 2020.</p>
      </div>
      {cats}
      <div class="menu-band reveal">
        <div>
          <h3>¿Listo para pedir?</h3>
          <p>Escríbenos por WhatsApp con tu pedido y te confirmamos el tiempo de entrega. Domicilios en Cali, Buga, Palmira y Rozo.</p>
        </div>
        <div class="menu-band__actions">
          <a class="btn-outline" href="{WA}" target="_blank" rel="noopener">Pedir a domicilio</a>
          <a class="btn-outline" href="{WA_RESERVA}" target="_blank" rel="noopener">Reservar mesa</a>
        </div>
      </div>
      <p class="menu-note">Precios en pesos colombianos (COP), según la carta 2026; pueden cambiar sin previo aviso. Cervezas sujetas a disponibilidad. Pide a domicilio por WhatsApp al +57 320 385 3275.</p>
    </section>
  </main>''' + CONTACT_BAND + FOOTER


def page_experiencias():
    return head('Experiencias · Teppanyaki show, catering y clases de sushi · Koi Cali',
                'Teppanyaki en vivo, catering de sushi a domicilio y clases de sushi en Cali. Koi lleva la cocina oriental a tus eventos.',
                'chef-teppanyaki.jpg', 'page-experiencias',
                preload=[
                    '<link rel="preload" as="image" href="img/chef-teppanyaki.webp" type="image/webp">'
                ]) + HEADER + f'''
  <main>
    <section class="hero hero--short">
      <div class="hero__media">
        <picture>
          <source type="image/webp" srcset="img/chef-teppanyaki.webp">
          <img src="img/chef-teppanyaki.jpg" alt="Chef de Koi durante un show de teppanyaki" fetchpriority="high" decoding="async" style="object-position: 30% 50%">
        </picture>
      </div>
      <p class="label hero__label reveal">Catering service <span class="jp">ケータリング</span></p>
      <h1 class="hero__title reveal reveal-d1">Experiencias Koi</h1>
      <div class="hero__foot reveal reveal-d2">
        <div>
          <p class="lede">Teppanyaki en vivo, sushi para tus eventos y clases para aprender a hacerlo tú.</p>
          <div class="hero__actions">
            <a class="arrow-link on-dark" href="{WA_CATERING}" target="_blank" rel="noopener">Cotizar por WhatsApp {ARROW}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="feature on-cream">
      <div class="grid">
        <div class="feature__media reveal">
          <picture>
            <source type="image/webp" srcset="img/chef-teppanyaki.webp">
            <img src="img/chef-teppanyaki.jpg" alt="Show de teppanyaki de Koi en la noche" loading="lazy" decoding="async">
          </picture>
        </div>
        <div class="feature__body">
          <p class="label reveal">Teppanyaki <span class="jp">鉄板焼き</span></p>
          <h2 class="reveal reveal-d1">Teppanyaki live show</h2>
          <p class="lede reveal reveal-d2">¡El mejor espectáculo de cocina en vivo para todas las ocasiones! Nuestro chef lleva la plancha a tu evento y prepara el teppanyaki frente a tus invitados.</p>
          <ul class="feature__list reveal reveal-d2">
            <li>Cumpleaños, reuniones familiares y eventos de empresa</li>
            <li>Yakimeshi, yakisoba o yasaitame con la proteína que prefieras</li>
            <li>Cotización según número de personas</li>
          </ul>
          <a class="btn-solid reveal reveal-d3" href="{WA_CATERING}" target="_blank" rel="noopener">Cotizar teppanyaki show</a>
        </div>
      </div>
    </section>

    <section class="feature feature--reverse on-stone">
      <div class="grid">
        <div class="feature__media reveal">
          <picture>
            <source type="image/webp" srcset="img/sushi-en-casa.webp">
            <img src="img/sushi-en-casa.jpg" alt="Barco de sushi de Koi listo para un evento" loading="lazy" decoding="async">
          </picture>
        </div>
        <div class="feature__body">
          <p class="label reveal">Sushi catering <span class="jp">寿司</span></p>
          <h2 class="reveal reveal-d1">Sushi at home</h2>
          <p class="lede reveal reveal-d2">Deléitate con nuestro catering de sushi y sorprende a tus invitados. Barcos, tablas y combos de rolls para compartir, entregados donde los necesites.</p>
          <ul class="feature__list reveal reveal-d2">
            <li>Barcos Sushihana, Benihana y Hatsuhana</li>
            <li>Combos de 30 a 80 bocados de rolls tradicionales, sencillos o especiales</li>
            <li>Opciones vegetarianas</li>
          </ul>
          <a class="btn-solid reveal reveal-d3" href="{WA_CATERING}" target="_blank" rel="noopener">Cotizar sushi catering</a>
        </div>
      </div>
    </section>

    <section class="feature on-cream">
      <div class="grid">
        <div class="feature__media reveal">
          <picture>
            <source type="image/webp" srcset="img/clases-sushi.webp">
            <img src="img/clases-sushi.jpg" alt="Personas preparando rolls en una clase de sushi de Koi" loading="lazy" decoding="async">
          </picture>
        </div>
        <div class="feature__body">
          <p class="label reveal">Aprende con Koi <span class="jp">教室</span></p>
          <h2 class="reveal reveal-d1">Clases de sushi</h2>
          <p class="lede reveal reveal-d2">Aprende a hacer sushi de forma recreativa. Invita a tu familia y amigos a probar este arte japonés preparado por ti, con la guía de nuestro equipo.</p>
          <ul class="feature__list reveal reveal-d2">
            <li>Ingredientes, tabla y utensilios incluidos</li>
            <li>Ideal para planes en pareja, con amigos o en familia</li>
            <li>Al final te comes lo que preparaste</li>
          </ul>
          <a class="btn-solid reveal reveal-d3" href="{WA_CLASES}" target="_blank" rel="noopener">Reservar una clase</a>
        </div>
      </div>
    </section>
  </main>''' + CONTACT_BAND + FOOTER


def page_contacto():
    return head('Contacto · Koi Sushi & Teppanyaki, Cali',
                'Escríbenos por WhatsApp al +57 320 385 3275 o visítanos en la Calle 16 #83A-15, barrio El Ingenio, Cali. Domicilios en Cali, Buga, Palmira y Rozo.',
                'fachada-m.jpg', 'page-contacto',
                preload=[
                    '<link rel="preload" as="image" href="img/fachada-m.webp" type="image/webp" media="(max-width: 767px)">',
                    '<link rel="preload" as="image" href="img/fachada.webp" type="image/webp" media="(min-width: 768px)">'
                ]) + HEADER + f'''
  <main>
    <section class="hero hero--short">
      <div class="hero__media">
        <picture>
          <source type="image/webp" media="(max-width: 767px)" srcset="img/fachada-m.webp">
          <source type="image/webp" srcset="img/fachada.webp">
          <source media="(max-width: 767px)" srcset="img/fachada-m.jpg">
          <img src="img/fachada.jpg" alt="Fachada del restaurante Koi" fetchpriority="high" decoding="async">
        </picture>
      </div>
      <p class="label hero__label reveal">Koi Sushi &amp; Teppanyaki <span class="jp">連絡先</span></p>
      <h1 class="hero__title reveal reveal-d1">Hablemos</h1>
      <div class="hero__foot reveal reveal-d2">
        <div>
          <p class="lede">Pedidos, reservas, catering o cualquier pregunta: por WhatsApp respondemos más rápido.</p>
          <div class="hero__actions">
            <a class="arrow-link on-dark" href="{WA}" target="_blank" rel="noopener">Escribir por WhatsApp {ARROW}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="contact on-cream">
      <div class="grid">
        <div class="contact__aside">
          <p class="label reveal">Contacto</p>
          <h2 class="reveal reveal-d1">Estamos en El Ingenio</h2>
          <p class="lede reveal reveal-d2">Ven al restaurante o pide a domicilio. Somos pet friendly.</p>
          <dl class="reveal reveal-d2">
            <div><dt>Dirección</dt><dd><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}<br>{CITY}</a></dd></div>
            <div><dt>WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">+57 320 385 3275</a></dd></div>
            <div><dt>Correo</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
            <div><dt>Domicilios</dt><dd>Cali, Buga, Palmira y Rozo</dd></div>
            <div><dt>Redes</dt><dd><a href="{IG}" target="_blank" rel="noopener">Instagram @koisushiyteppan</a><br><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok @koisushiyteppan</a><br><a href="{FB}" target="_blank" rel="noopener">Facebook @Koicocinaoriental</a></dd></div>
          </dl>
        </div>
        <form class="contact__form reveal reveal-d1" id="contact-form">
          <div class="form-row">
            <div class="field"><label for="f-nombre">Nombre</label><input id="f-nombre" name="nombre" type="text" autocomplete="name" required></div>
            <div class="field"><label for="f-tel">Teléfono</label><input id="f-tel" name="telefono" type="tel" autocomplete="tel" inputmode="tel" required></div>
          </div>
          <div class="field">
            <label for="f-motivo">Motivo</label>
            <select id="f-motivo" name="motivo">
              <option>Pedido a domicilio</option>
              <option>Reserva de mesa</option>
              <option>Teppanyaki show / catering</option>
              <option>Clases de sushi</option>
              <option>Otro</option>
            </select>
          </div>
          <div class="field"><label for="f-msg">Mensaje</label><textarea id="f-msg" name="mensaje" required placeholder="Cuéntanos qué necesitas: fecha, número de personas, dirección de entrega…"></textarea></div>
          <button class="btn-solid btn-solid--koi" type="submit">Enviar por WhatsApp</button>
          <p class="form-hint">Al enviar se abre WhatsApp con tu mensaje listo para que lo envíes desde tu número.</p>
        </form>
      </div>
      <div class="map reveal"><iframe src="{MAPS_EMBED}" title="Mapa: Koi Sushi &amp; Teppanyaki, Calle 16 #83A-15, Cali" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    </section>
  </main>''' + CONTACT_BAND + FOOTER


PAGES = {
    'index.html': page_index,
    'menu.html': page_menu,
    'experiencias.html': page_experiencias,
    'contacto.html': page_contacto,
}

if __name__ == '__main__':
    for name, fn in PAGES.items():
        path = os.path.join(OUT, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fn())
        print('escrito', os.path.relpath(path, OUT))
