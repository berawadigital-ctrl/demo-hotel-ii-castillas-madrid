# Contenido de la demo Hotel II Castillas (Madrid) (es/ca/en/fr). Hechos de hoteldoscastillas-madrid.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación estándar','Descanso en el centro','Baño completo'],'ca':['Habitació estàndard','Descans al centre','Bany complet'],'en':['Standard room','Rest in the centre','Full bathroom'],'fr':['Chambre standard','Repos en plein centre','Salle de bain complète']}
RD={
'es':['Con aire acondicionado, TV, escritorio, caja fuerte gratuita, minibar de pago y wifi gratuito.','Sencilla, cómoda y funcional, con suelo de madera, ventanas insonorizadas y calefacción.','Ducha o bañera con ducha, bidet, secador de pelo y espejo de maquillaje.'],
'ca':['Amb aire condicionat, TV, escriptori, caixa forta gratuïta, minibar de pagament i wifi gratuït.','Senzilla, còmoda i funcional, amb terra de fusta, finestres insonoritzades i calefacció.','Dutxa o banyera amb dutxa, bidet, assecador de cabells i mirall de maquillatge.'],
'en':['With air conditioning, TV, desk, free safe, paid minibar and free wifi.','Simple, comfortable and functional, with wooden floors, soundproofed windows and heating.','Shower or bath with shower, bidet, hairdryer and make-up mirror.'],
'fr':['Avec climatisation, TV, bureau, coffre-fort gratuit, minibar payant et wifi gratuit.','Simple, confortable et fonctionnelle, avec parquet, fenêtres insonorisées et chauffage.','Douche ou baignoire avec douche, bidet, sèche-cheveux et miroir de maquillage.']}
ART={
'hero':('skyline',4101,['#2b3a55','#d9805a','#f6d09a','#2a3854','#1f2a40','#141c2c']),
'intro':('columns',4102,['#efe9e2','#f7f2ec','#b07a3a','#7a2e2e','#4a1c1c']),
'r1':('arches',4111,['#f1e8e0','#dcb9a2','#a8704f','#7a2e2e','#4a1c1c']),
'r2':('skyline',4112,['#33415e','#e08a5c','#f8d29c','#30405c','#232f46','#172031']),
'r3':('columns',4113,['#ece6df','#f5f0ea','#b8844a','#7a2e2e','#4a1c1c']),
'g1':('arches',4121,['#f0e7df','#d8b39b','#a46b4a','#7a2e2e','#4a1c1c']),
'g2':('columns',4122,['#eee8e1','#f6f1eb','#bd8a4e','#7e3030','#4c1d1d']),
'g3':('skyline',4123,['#2f3d5a','#de875b','#f7cf98','#2d3b57','#202b42','#151d2e']),
'g4':('hills',4124,['#e7e4cf','#f2e3c0','#f3cb86','#a7bf9b','#7e9e82','#567564']),
'g5':('arches',4125,['#efe6de','#d5ae96','#a06646','#7a2e2e','#4a1c1c']),
'g6':('columns',4126,['#ede7e0','#f5f0ea','#b98648','#7a2e2e','#4a1c1c'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel II Castillas · Hotel en pleno centro de Madrid, a pocos metros de la Puerta del Sol',see_rooms='Ver habitaciones',hero_k='Madrid · Puerta del Sol',hero_t='Descubre la ciudad desde un alojamiento acogedor',hero_s='En la calle Abada, a un minuto a pie de la Puerta del Sol y a tres de la Gran Vía.',
 intro_t='Trato cercano y profesional en una ubicación inmejorable',intro_p1='El Hotel II Castillas está en Abada, 7, en pleno centro, a escasos metros de las estaciones de metro de Sol, Gran Vía y Callao.',
 intro_p2='Habitaciones sencillas, cómodas y funcionales; desayuno buffet con productos fríos y calientes y opciones para celíacos; wifi gratuito y atención personalizada.',
 stats=['1 min a pie de Sol','Desayuno buffet','Opciones sin gluten','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Confort y descanso en el centro: así son sus habitaciones estándar.',
 svcs=['Desayuno buffet','Opciones para celíacos','Recepción y atención personalizada','Wifi gratuito','Aire acondicionado','Ventanas insonorizadas','Taberna dNorte en el edificio','Parking público cercano'],
 loc_p='Abada, 7 · 28013 Madrid, a pocos metros de la Puerta del Sol; Plaza Mayor a 5 minutos a pie y Palacio Real a 10.',
 chips=['¿Cómo son las habitaciones?','¿Hay desayuno?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Hotel II Castillas · Hotel al bell mig de Madrid, a pocs metres de la Puerta del Sol',see_rooms='Veure habitacions',hero_k='Madrid · Puerta del Sol',hero_t='Descobreix la ciutat des d\'un allotjament acollidor',hero_s='Al carrer Abada, a un minut a peu de la Puerta del Sol i a tres de la Gran Vía.',
 intro_t='Tracte proper i professional en una ubicació immillorable',intro_p1='L\'Hotel II Castillas és a Abada, 7, al bell mig del centre, a pocs metres de les estacions de metro de Sol, Gran Vía i Callao.',
 intro_p2='Habitacions senzilles, còmodes i funcionals; esmorzar bufet amb productes freds i calents i opcions per a celíacs; wifi gratuït i atenció personalitzada.',
 stats=['1 min a peu de Sol','Esmorzar bufet','Opcions sense gluten','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Confort i descans al centre: així són les seves habitacions estàndard.',
 svcs=['Esmorzar bufet','Opcions per a celíacs','Recepció i atenció personalitzada','Wifi gratuït','Aire condicionat','Finestres insonoritzades','Taberna dNorte a l\'edifici','Pàrquing públic a prop'],
 loc_p='Abada, 7 · 28013 Madrid, a pocs metres de la Puerta del Sol; Plaza Mayor a 5 minuts a peu i Palau Reial a 10.',
 chips=['Com són les habitacions?','Hi ha esmorzar?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Hotel II Castillas · Hotel in the heart of Madrid, a few metres from Puerta del Sol',see_rooms='See the rooms',hero_k='Madrid · Puerta del Sol',hero_t='Discover the city from a welcoming place to stay',hero_s='On Calle Abada, a one-minute walk from Puerta del Sol and three from the Gran Vía.',
 intro_t='Friendly, professional service in an unbeatable location',intro_p1='Hotel II Castillas is at Abada, 7, right in the centre, a few metres from Sol, Gran Vía and Callao metro stations.',
 intro_p2='Simple, comfortable and functional rooms; a buffet breakfast with hot and cold products and options for coeliacs; free wifi and personal attention.',
 stats=['1 min walk to Sol','Buffet breakfast','Gluten-free options','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Comfort and rest in the centre: this is what its standard rooms offer.',
 svcs=['Buffet breakfast','Options for coeliacs','Reception and personal attention','Free wifi','Air conditioning','Soundproofed windows','Taberna dNorte in the building','Public car park nearby'],
 loc_p='Abada, 7 · 28013 Madrid, a few metres from Puerta del Sol; Plaza Mayor a 5-minute walk and the Royal Palace 10.',
 chips=['What are the rooms like?','Is there breakfast?','Is there parking?','How do I book?']),
'fr':dict(title='Hotel II Castillas · Hôtel en plein centre de Madrid, à quelques mètres de la Puerta del Sol',see_rooms='Voir les chambres',hero_k='Madrid · Puerta del Sol',hero_t='Découvrez la ville depuis un hébergement accueillant',hero_s='Calle Abada, à une minute à pied de la Puerta del Sol et à trois de la Gran Vía.',
 intro_t='Un accueil proche et professionnel, un emplacement imbattable',intro_p1='L\'Hotel II Castillas se trouve Abada, 7, en plein centre, à quelques mètres des stations de métro Sol, Gran Vía et Callao.',
 intro_p2='Des chambres simples, confortables et fonctionnelles ; un petit-déjeuner buffet chaud et froid avec des options pour cœliaques ; wifi gratuit et accueil personnalisé.',
 stats=['1 min à pied de Sol','Petit-déjeuner buffet','Options sans gluten','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Confort et repos en centre-ville : voici ses chambres standard.',
 svcs=['Petit-déjeuner buffet','Options pour cœliaques','Réception et accueil personnalisé','Wifi gratuit','Climatisation','Fenêtres insonorisées','Taberna dNorte dans l\'immeuble','Parking public à proximité'],
 loc_p='Abada, 7 · 28013 Madrid, à quelques mètres de la Puerta del Sol ; Plaza Mayor à 5 minutes à pied et Palais royal à 10.',
 chips=['Comment sont les chambres ?','Y a-t-il un petit-déjeuner ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.hoteldoscastillas-madrid.com/bookingstep1/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Hotel II Castillas',ac='#7a2e2e',ac2='#b07a3a',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Abada, 7 · 28013 Madrid',phones=['+34 915 24 97 50'],emails=['reservas@hoteldoscastillas.com'],maps='Hotel II Castillas, Calle de la Abada 7, Madrid',t=T)
META=dict(repo='demo-hotel-ii-castillas-madrid',name='Hotel II Castillas',legal_name='López y Talavera Hoteles S.L.',registry_ids=['CIF B-83669705','Registro Mercantil de Madrid, hoja M-334451'],
 url='https://www.hoteldoscastillas-madrid.com/',domain='hoteldoscastillas-madrid.com',municipality='Madrid',province='Madrid',sector='hotel en el centro de Madrid',
 read_at='2026-10-29T10:47:00+01:00',created_at='2026-10-29T10:55:00+01:00',built_at='2026-10-29T10:55:00+01:00',audit_date='2026-10-29T10:45:00+01:00',
 rating=dict(value=4.4,coincide=['telefono','web'],date='2026-10-29T06:50:02+01:00',url='https://www.google.com/maps/place/Hotel+Madrid+II+Castillas/@40.4192202,-3.7043768,17z/data=!4m9!3m8!1s0xd42287dc0175d6b:0x6f438133e5ff563a!5m2!4m1!1i2!8m2!3d40.4192202!4d-3.7043768!16s%2Fg%2F11_qqn0l5'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (hoteldoscastillas-madrid.com/bookingstep1/, pagina del propio dominio que carga el componente de tarifas de Mirai del hotel, data-mirai-id 92443242; /booking/ redirige ahi); la demo no construye ningun motor. Titular contrastado con el Registro Mercantil de Madrid (hoja M-334451, la misma que cita su aviso legal).'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Cómo son las habitaciones?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay restaurante?','K04'),('¿Hay parking?','K05'),('¿Dónde está el hotel?','K06'),('¿Qué ver cerca?','K07'),('¿Qué servicios tiene?','K08'),('¿Qué ventajas tiene reservar en la web?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Com són les habitacions?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha restaurant?','K04'),('Hi ha pàrquing?','K05'),('On és l\'hotel?','K06'),('Què es pot veure a prop?','K07'),('Quins serveis té?','K08'),('Quins avantatges té reservar al web?','K09'),('Com reservo?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What are the rooms like?','K01'),('What equipment do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there a restaurant?','K04'),('Is there parking?','K05'),('Where is the hotel?','K06'),('What is there to see nearby?','K07'),('What services does it offer?','K08'),('What are the advantages of booking on the website?','K09'),('How do I book?','K10'),('What is the phone number?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Comment sont les chambres ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un restaurant ?','K04'),('Y a-t-il un parking ?','K05'),('Où est l\'hôtel ?','K06'),('Que voir à proximité ?','K07'),('Quels services propose-t-il ?','K08'),('Quels avantages à réserver sur le site ?','K09'),('Comment réserver ?','K10'),('Quel est le numéro de téléphone ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
