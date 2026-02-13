# app.py - Application Flask version luxe avec panier
from flask import Flask, render_template, send_from_directory, jsonify, request, session, redirect, url_for
from produits import parfums, informations_boutique
import os
import json
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aura-parfums-luxe-secret-key-2025'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SESSION_TYPE'] = 'filesystem'

# Configuration des promotions
PROMOTIONS = {
    'nouveaux_clients': {
        'code': 'BIENVENUE15',
        'reduction': 15,
        'message': '-15% sur votre première commande'
    },
    'newsletter': {
        'code': 'NEWSLETTER10',
        'reduction': 10,
        'message': '-10% en vous inscrivant à notre newsletter'
    }
}

@app.context_processor
def inject_globals():
    """Injecte des variables globales dans tous les templates"""
    # Calculer le nombre d'articles dans le panier
    cart_count = 0
    if 'panier' in session:
        cart_count = sum(item.get('quantite', 1) for item in session['panier'])
    
    return {
        'annee': datetime.now().year,
        'promo_actuelle': PROMOTIONS['nouveaux_clients'],
        'whatsapp_number': '0752717701',
        'whatsapp_link': 'https://wa.me/33752771701',
        'boutique': informations_boutique,
        'cart_count': cart_count
    }

@app.route('/')
def index():
    """Page d'accueil avec tous les produits"""
    return render_template('index.html', parfums=parfums)

@app.route('/parfum/<nom_parfum>')
def fiche_produit(nom_parfum):
    """Page détaillée d'un parfum"""
    if nom_parfum in parfums:
        # Produits similaires (aléatoires)
        autres = [p for p in parfums.keys() if p != nom_parfum]
        similaires = {k: parfums[k] for k in autres[:3] if k in parfums}
        
        return render_template('produit.html', 
                             parfum=parfums[nom_parfum],
                             similaires=similaires,
                             page_titre=parfums[nom_parfum]['nom'])
    return render_template('404.html'), 404

@app.route('/collection')
def collection():
    """Tous les parfums"""
    return render_template('collection.html', parfums=parfums)

@app.route('/histoire')
def histoire():
    """Page histoire de la marque"""
    return render_template('histoire.html')

@app.route('/contact')
def contact():
    """Page contact"""
    return render_template('contact.html')

@app.route('/panier')
def panier():
    """Page du panier"""
    panier = session.get('panier', [])
    total = 0
    
    # Calculer le total
    for item in panier:
        produit_id = item['id']
        quantite = item.get('quantite', 1)
        if produit_id in parfums:
            prix = parfums[produit_id]['prix_promo'] if parfums[produit_id]['en_promo'] else parfums[produit_id]['prix']
            item['prix'] = prix
            item['nom'] = parfums[produit_id]['nom']
            item['image'] = parfums[produit_id]['image_principale']
            total += prix * quantite
    
    return render_template('panier.html', panier=panier, total=total, parfums=parfums)

@app.route('/ajouter-au-panier', methods=['POST'])
def ajouter_au_panier():
    """Ajoute un produit au panier"""
    data = request.json
    produit_id = data.get('id')
    quantite = int(data.get('quantite', 1))
    
    if produit_id not in parfums:
        return jsonify({'success': False, 'message': 'Produit non trouvé'}), 404
    
    # Initialiser le panier si nécessaire
    if 'panier' not in session:
        session['panier'] = []
    
    # Vérifier si le produit est déjà dans le panier
    panier = session['panier']
    for item in panier:
        if item['id'] == produit_id:
            item['quantite'] = item.get('quantite', 1) + quantite
            session.modified = True
            return jsonify({
                'success': True, 
                'message': 'Quantité mise à jour dans le panier',
                'cart_count': sum(i.get('quantite', 1) for i in panier)
            })
    
    # Ajouter le nouveau produit
    panier.append({
        'id': produit_id,
        'quantite': quantite
    })
    session.modified = True
    
    return jsonify({
        'success': True, 
        'message': 'Produit ajouté au panier',
        'cart_count': sum(i.get('quantite', 1) for i in panier)
    })

@app.route('/mettre-a-jour-panier', methods=['POST'])
def mettre_a_jour_panier():
    """Met à jour la quantité d'un produit dans le panier"""
    data = request.json
    produit_id = data.get('id')
    quantite = int(data.get('quantite', 1))
    
    if 'panier' not in session:
        return jsonify({'success': False, 'message': 'Panier vide'}), 404
    
    panier = session['panier']
    for item in panier:
        if item['id'] == produit_id:
            if quantite <= 0:
                panier.remove(item)
            else:
                item['quantite'] = quantite
            session.modified = True
            break
    
    # Recalculer le total
    total = 0
    for item in panier:
        if item['id'] in parfums:
            prix = parfums[item['id']]['prix_promo'] if parfums[item['id']]['en_promo'] else parfums[item['id']]['prix']
            total += prix * item.get('quantite', 1)
    
    return jsonify({
        'success': True,
        'cart_count': sum(i.get('quantite', 1) for i in panier),
        'total': total
    })

@app.route('/supprimer-du-panier', methods=['POST'])
def supprimer_du_panier():
    """Supprime un produit du panier"""
    data = request.json
    produit_id = data.get('id')
    
    if 'panier' in session:
        panier = session['panier']
        session['panier'] = [item for item in panier if item['id'] != produit_id]
        session.modified = True
    
    return jsonify({'success': True, 'cart_count': sum(i.get('quantite', 1) for i in session.get('panier', []))})

@app.route('/valider-commande', methods=['POST'])
def valider_commande():
    """Valide la commande et génère le message WhatsApp"""
    data = request.json
    nom = data.get('nom')
    email = data.get('email')
    telephone = data.get('telephone', '')
    adresse = data.get('adresse')
    notes = data.get('notes', '')
    
    panier = session.get('panier', [])
    if not panier:
        return jsonify({'success': False, 'message': 'Panier vide'}), 400
    
    # Construire le message WhatsApp
    message = "🛍️ *NOUVELLE COMMANDE AURA*\n\n"
    message += f"👤 *Client:* {nom}\n"
    message += f"📧 *Email:* {email}\n"
    if telephone:
        message += f"📱 *Téléphone:* {telephone}\n"
    message += f"📍 *Adresse:* {adresse}\n\n"
    
    message += "📦 *ARTICLES COMMANDÉS:*\n"
    total = 0
    for item in panier:
        produit_id = item['id']
        quantite = item.get('quantite', 1)
        if produit_id in parfums:
            produit = parfums[produit_id]
            prix = produit['prix_promo'] if produit['en_promo'] else produit['prix']
            sous_total = prix * quantite
            total += sous_total
            message += f"• {produit['nom']} x{quantite} - {sous_total}€\n"
    
    message += f"\n💰 *TOTAL: {total}€*\n"
    
    if notes:
        message += f"\n📝 *Notes:* {notes}\n"
    
    message += "\n⏰ *Date de commande:* " + datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Vider le panier après validation
    session['panier'] = []
    session.modified = True
    
    # Encoder le message pour URL
    from urllib.parse import quote
    message_encoded = quote(message)
    
    whatsapp_url = f"https://wa.me/33752771701?text={message_encoded}"
    
    return jsonify({
        'success': True,
        'whatsapp_url': whatsapp_url,
        'message': 'Commande validée'
    })

@app.route('/vider-panier', methods=['POST'])
def vider_panier():
    """Vide complètement le panier"""
    session['panier'] = []
    session.modified = True
    return jsonify({'success': True})

@app.route('/newsletter', methods=['POST'])
def newsletter():
    """Inscription newsletter"""
    email = request.form.get('email')
    if email:
        return jsonify({'success': True, 'message': 'Inscription réussie !'})
    return jsonify({'success': False, 'message': 'Email invalide'}), 400

@app.route('/api/produits')
def api_produits():
    """API pour récupérer tous les produits (format JSON)"""
    return jsonify(parfums)

@app.route('/api/produit/<nom_parfum>')
def api_produit(nom_parfum):
    """API pour un produit spécifique"""
    if nom_parfum in parfums:
        return jsonify(parfums[nom_parfum])
    return jsonify({'error': 'Produit non trouvé'}), 404

@app.route('/appliquer-promo', methods=['POST'])
def appliquer_promo():
    """Applique un code promo en session"""
    code = request.json.get('code', '').upper()
    
    for promo_key, promo_data in PROMOTIONS.items():
        if promo_data['code'] == code:
            session['code_promo'] = code
            session['reduction'] = promo_data['reduction']
            return jsonify({
                'success': True, 
                'message': f'Code {code} appliqué ! {promo_data["message"]}',
                'reduction': promo_data['reduction']
            })
    
    return jsonify({'success': False, 'message': 'Code promo invalide'}), 400

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.errorhandler(404)
def page_non_trouvee(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def erreur_serveur(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Création des dossiers nécessaires
    for dossier in ['static', 'static/images', 'templates']:
        if not os.path.exists(dossier):
            os.makedirs(dossier)
            print(f"📁 Dossier '{dossier}' créé.")
    
    print("\n" + "="*50)
    print("✨ AURA PARFUMS - Site de Luxe avec Panier ✨")
    print("="*50)
    print("🌐 Accédez au site: http://127.0.0.1:5000")
    print("📱 WhatsApp: 07 52 71 77 01")
    print("🛒 Système de panier activé")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
