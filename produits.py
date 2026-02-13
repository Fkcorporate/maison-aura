# produits.py - Base de données des parfums (version enrichie)
# Tous les détails produits pour un site ultra professionnel

parfums = {
    'rose-absolue': {
        'id': 'Bouquet-ABSOLU',
        'nom': 'Bouquet ABSOLU',
        'nom_complet': 'Bouquet ABSOLU · Édition Impériale',
        'prix': 35,  # VOTRE PRIX
        'prix_promo': 30,  # -15%
        'en_promo': True,
        'nouveau': False,
        'meilleure_vente': True,
        'coup_de_coeur': True,
        
        # Description complète
        'description_courte': 'Une rose bulgare capturée à la pleine floraison, réchauffée par un cœur de santal.',
        'description_longue': """
            Inspirée des jardins secrets de la Vallée des Roses en Bulgarie, cette création olfractive capture 
            l'essence même de la rose damascena au moment le plus intense de sa floraison. La récolte s'effectue 
            manuellement avant l'aube pour préserver toute la délicatesse des pétales. Le résultat est un absolu 
            d'une pureté exceptionnelle, que notre maître parfumeur a marié à des bois précieux et un cuir de 
            Russie pour lui donner une profondeur inattendue.
        """,
        
        # Caractéristiques techniques
        'famille': 'Florale · Cuirée · Boisée',
        'sous_famille': 'Rose orientale',
        'concentration': 'Extrait de parfum',
        'volume': '50 ml',
        'pourcentage': '30%',
        'tenue': '8-10 heures',
        'diffusion': 'Intense',
        'genre': 'Féminin',
        'saison': 'Automne · Hiver',
        'occasion': 'Soirée · Cérémonie',
        
        # Notes olfactives
        'notes': {
            'tete': ['Bergamote de Calabre', 'Pamplemousse rose', 'Aldéhydes'],
            'coeur': ['Rose bulgare', 'Absolue de jasmin', 'Géranium d\'Égypte'],
            'fond': ['Cuir de Russie', 'Santal de Mysore', 'Musc blanc', 'Benjoin']
        },
        
        # Informations créateur
        'nez': 'Mathilde Laurent',
        'annee_creation': 2024,
        'maison': 'Aura Parfums',
        'collection': 'Collection Impériale',
        'edition': 'Limitée',
        'numero_lot': 'AR-2024-001',
        
        # Images et médias
        'image_principale': 'rose-absolue.jpg',
        'image_secondaire': 'rose-absolue-2.jpg',
        'image_flacon': 'flacon-rose-absolue.jpg',
        'image_emballage': 'coffret-rose-absolue.jpg',
        'video_presentation': 'https://youtu.be/example',
        
        # Contenu marketing
        'accroche': "L'âme d'une rose, la force du cuir",
        'histoire': """
            Créé pour célébrer le centenaire de la maison, Rose Absolue incarne le savoir-faire 
            artisanal transmis depuis quatre générations. Chaque flacon est numéroté à la main 
            et signé par notre maître parfumeur.
        """,
        'rituel': "Appliquez sur les points de pulsation : poignets, creux du cou et derrière les oreilles.",
        'conseil': "Idéal en superposition avec notre huile corporelle non parfumée pour une tenue exceptionnelle.",
        
        # Ingrédients
        'ingredients': [
            'Alcool', 'Parfum', 'Aqua', 'Limonène', 'Linalool', 
            'Citronellol', 'Geraniol', 'Eugenol', 'Benzyl benzoate'
        ],
        'origine_ingredients': 'France, Bulgarie, Inde',
        'certification': 'Vegan · Cruelty-free',
        
        # Prix et stock
        'devise': 'EUR',
        'stock': 47,
        'collection_limitée': True,
        'exemplaires_totaux': 500,
        'exemplaires_restants': 47,
        
        # Avis clients (simulés)
        'notes_moyenne': 4.8,
        'nb_avis': 124,
        'avis': [
            {'auteur': 'Sophie M.', 'note': 5, 'commentaire': 'Mon parfum signature !', 'date': '2025-01-15'},
            {'auteur': 'Claire D.', 'note': 5, 'commentaire': 'Tenue exceptionnelle', 'date': '2025-01-10'},
            {'auteur': 'Marie L.', 'note': 4.5, 'commentaire': 'Très élégant', 'date': '2025-01-05'}
        ]
    },
    
    'cuir-russie': {
        'id': 'Tobacco-Vanille',
        'nom': 'Tobacco Vanille',
        'nom_complet': 'Tobacco Vanille · Heritage Collection',
        'prix': 35,  # VOTRE PRIX
        'prix_promo': 30,  # -10% (promo spéciale)
        'en_promo': True,
        'nouveau': True,
        'meilleure_vente': False,
        'coup_de_coeur': True,
        
        'description_courte': 'Un cuir noble et moderne, associé à des notes de tabac blond et de bouleau.',
        'description_longue': """
            Hommage aux routes de la soie et aux échanges entre l'Orient et l'Occident, Cuir de Russie 
            réinvente le classique des cuirs avec une modernité saisissante. Le bouleau russe, traditionnellement 
            utilisé dans le tannage, dialogue avec un tabac blond virginal et des épices rares.
        """,
        
        'famille': 'Cuirée · Boisée · Épicée',
        'sous_famille': 'Cuir russe moderne',
        'concentration': 'Eau de Parfum',
        'volume': '75 ml',
        'pourcentage': '20%',
        'tenue': '6-8 heures',
        'diffusion': 'Modérée',
        'genre': 'Masculin · Féminin',
        'saison': 'Toutes saisons',
        'occasion': 'Travail · Dîner',
        
        'notes': {
            'tete': ['Bergamote de Sicile', 'Genièvre', 'Cardamome'],
            'coeur': ['Bouleau de Russie', 'Cuir de Toscane', 'Iris'],
            'fond': ['Tabac blond', 'Ambre', 'Mousse de chêne', 'Fève tonka']
        },
        
        'nez': 'Jean-Claude Ellena',
        'annee_creation': 2025,
        'maison': 'Aura Parfums',
        'collection': 'Heritage Collection',
        'edition': 'Coffret prestige',
        'numero_lot': 'CR-2025-001',
        
        'image_principale': 'cuir-russie.jpg',
        'image_secondaire': 'cuir-russie-2.jpg',
        'image_flacon': 'flacon-cuir.jpg',
        
        'accroche': "L'élégance d'un cuir, la chaleur du tabac",
        
        'stock': 28,
        'collection_limitée': False,
        
        'notes_moyenne': 4.9,
        'nb_avis': 89,
        'avis': [
            {'auteur': 'Thomas B.', 'note': 5, 'commentaire': 'Magnifique cuir moderne', 'date': '2025-02-01'}
        ]
    },
    
    'bois-encens': {
        'id': 'bakara',
        'nom': "Bakara",
        'nom_complet': 'Bakara · Collection Sacrée',
        'prix': 35,  # VOTRE PRIX
        'prix_promo': 30,  # -15% (même si en_promo=False)
        'en_promo': False,
        'nouveau': False,
        'meilleure_vente': True,
        'coup_de_coeur': False,
        
        'description_courte': 'Un bois sacré et mystique, rehaussé par des notes d\'encens et de myrrhe.',
        'description_longue': """
            Voyage spirituel au cœur des forêts millénaires et des lieux de culte, Bois d'Encens 
            capture la sérénité des rituels anciens. L'encens d'Oman et la myrrhe de Somalie 
            se mêlent aux bois précieux pour une expérience méditative et sensorielle unique.
        """,
        
        'famille': 'Boisée · Résineuse · Spirituelle',
        'sous_famille': 'Bois sacré',
        'concentration': 'Extrait de parfum',
        'volume': '50 ml',
        'pourcentage': '25%',
        'tenue': '8-10 heures',
        'diffusion': 'Intense',
        'genre': 'Masculin',
        'saison': 'Hiver',
        'occasion': 'Méditation · Cérémonie',
        
        'notes': {
            'tete': ['Citron de Sicile', 'Cyprès', 'Baies roses'],
            'coeur': ['Encens d\'Oman', 'Myrrhe de Somalie', 'Ciste'],
            'fond': ['Cèdre de l\'Atlas', 'Vétiver', 'Patchouli', 'Labdanum']
        },
        
        'nez': 'Olivier Polge',
        'annee_creation': 2023,
        'maison': 'Aura Parfums',
        'collection': 'Collection Sacrée',
        'edition': 'Prestige',
        
        'image_principale': 'bois-encens.jpg',
        'image_2': 'bois-encens2.jpg',

        'accroche': "La spiritualité d'un bois, la pureté de l'encens",
        
        'stock': 15,
        'collection_limitée': False,
        
        'notes_moyenne': 4.7,
        'nb_avis': 156
    },
    
    'iris-poudre': {
        'id': 'Féroce-Intense',
        'nom': 'Féroce Intense',
        'nom_complet': 'Féroce Intense · Collection Féminine',
        'prix': 35,  # VOTRE PRIX
        'prix_promo': 30,  # -10%
        'en_promo': True,
        'nouveau': False,
        'meilleure_vente': False,
        'coup_de_coeur': True,
        
        'description_courte': 'Un iris raffiné et poudré, adouci par des notes de vanille et de musc.',
        'description_longue': """
            L'iris, racine précieuse entre toutes, dévoile ici sa facette la plus délicate et poudrée. 
            Cultivé en Toscane, récolté à la main et séché pendant trois ans, il livre un absolu d'une 
            finesse inégalée que nous avons enveloppé de vanille bourbon et de muscs blancs pour un 
            sillage irisé et réconfortant.
        """,
        
        'famille': 'Florale · Poudrée · Musquée',
        'sous_famille': 'Iris cosmétique',
        'concentration': 'Eau de Parfum',
        'volume': '100 ml',
        'pourcentage': '18%',
        'tenue': '6-8 heures',
        'diffusion': 'Douce',
        'genre': 'Féminin',
        'saison': 'Printemps · Été',
        'occasion': 'Quotidien · Bureau',
        
        'notes': {
            'tete': ['Aldéhydes', 'Néroli', 'Poivre rose'],
            'coeur': ['Iris de Toscane', 'Violette', 'Héliotrope'],
            'fond': ['Vanille de Madagascar', 'Musc blanc', 'Santal', 'Fève tonka']
        },
        
        'nez': 'Dominique Ropion',
        'annee_creation': 2024,
        'maison': 'Aura Parfums',
        'collection': 'Collection Féminine',
        
        'image_principale': 'iris-poudre.jpg',
        'image_2': 'iris-poudre2.jpg',

        'accroche': "La douceur d'un iris, la chaleur d'une étreinte",
        
        'stock': 62,
        'collection_limitée': False,
        
        'notes_moyenne': 4.6,
        'nb_avis': 203
    }
}

# Métadonnées supplémentaires
informations_boutique = {
    'nom': 'AURA · Parfums d\'exception',
    'slogan': 'L\'art de la parfumerie française',
    'description': 'Maison de parfumerie fondée en 1925, perpétuant un savoir-faire artisanal unique.',
    'adresse': '12 Rue de la Paix, 75002 Paris',
    'telephone': '+33 1 42 61 12 34',
    'whatsapp': '+33 7 52 71 77 01',
    'email': 'contact@aura-parfums.fr',
    'horaires': 'Lun-Sam 10h-19h',
    'siret': '824 567 890 00012',
    'tva': 'FR 12 824567890',
    
    'reseaux_sociaux': {
        'instagram': 'https://instagram.com/auraparfums',
        'facebook': 'https://facebook.com/auraparfums',
        'pinterest': 'https://pinterest.com/auraparfums'
    },
    
    'mentions_legales': {
        'editeur': 'Aura SAS',
        'capital': '150 000 €',
        'rcs': 'Paris B 824 567 890',
        'directeur_publication': 'Philippe Delacroix'
    }
}
