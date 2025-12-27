# 📖 Guide d'utilisation - API Uncensored.com

Guide simple pour utiliser ce dépôt et l'API Uncensored.com.

---

## 🎯 Ce dépôt, c'est quoi ?

C'est une **boîte à outils** pour utiliser l'API Uncensored.com facilement :
- 📚 Documentation complète des endpoints
- 🐍 Code Python prêt à l'emploi
- 💡 Exemples concrets et fonctionnels

---

## 🚀 Démarrage rapide (3 étapes)

### Étape 1 : Récupérer le code

```bash
# Cloner le dépôt
git clone https://github.com/taowill972/uncensored-ai-docs.git
cd uncensored-ai-docs
```

### Étape 2 : Installer les dépendances

```bash
# Installer Python (si pas déjà installé)
# Télécharger depuis python.org (version 3.11+)

# Installer les bibliothèques nécessaires
pip install -r examples/python/requirements.txt
```

### Étape 3 : Obtenir votre clé API

1. Aller sur [uncensored.com](https://uncensored.com)
2. Créer un compte (gratuit ou payant)
3. Copier votre clé API depuis le dashboard

---

## 💻 4 façons d'utiliser l'API

### **Option A : Depuis le terminal (le plus simple)**

```bash
# 1. Définir votre clé API
export UNCENSORED_API_KEY="votre_clé_ici"

# 2. Lancer l'exemple
python examples/python/chat_example.py
```

**Résultat :** Le script envoie un message à l'API et affiche la réponse.

---

### **Option B : Dans vos propres scripts Python**

Créez un fichier `mon_script.py` :

```python
from examples.python.chat_example import UncensoredClient

# Initialiser le client
client = UncensoredClient(api_key="votre_clé_api")

# Utilisation simple
reponse = client.chat("Bonjour, comment ça va ?")
print(reponse)

# Avec un modèle spécifique
reponse_gpt5 = client.chat(
    "Explique-moi la relativité",
    model="gpt-5-uncensored"
)
print(reponse_gpt5)
```

**Résultat :** Vous pouvez intégrer l'API dans vos propres projets.

---

### **Option C : Depuis n'importe quel terminal (cURL)**

```bash
curl -X POST https://api.uncensored.com/v1/chat \
  -H "Authorization: Bearer VOTRE_CLE_API" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "model-t",
    "messages": [{"role": "user", "content": "Bonjour!"}]
  }'
```

**Résultat :** Vous pouvez tester l'API sans écrire de code Python.

---

### **Option D : Dans une application web/mobile**

**JavaScript (Node.js) :**

```javascript
const fetch = require('node-fetch');

const API_KEY = 'votre_clé_api';
const BASE_URL = 'https://api.uncensored.com/v1';

async function chat(message) {
  const response = await fetch(`${BASE_URL}/chat`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'model-t',
      messages: [{ role: 'user', content: message }]
    })
  });

  const data = await response.json();
  return data.choices[0].message.content;
}

// Utilisation
chat("Bonjour!").then(console.log);
```

**Résultat :** Vous pouvez créer des chatbots, applications web, etc.

---

## 📚 Modèles disponibles

| Modèle | Utilisation | Tarif |
|--------|-------------|-------|
| `model-t` | Rapide et efficace | Vérifie sur uncensored.com |
| `gpt-5-uncensored` | Plus puissant, sans censure | Vérifie sur uncensored.com |
| `gemini-pro` | Google Gemini intégré | Vérifie sur uncensored.com |
| `grok-4` | Modèle xAI/Twitter | Vérifie sur uncensored.com |

⚠️ **Important :** Vérifiez les tarifs sur [uncensored.com/pricing](https://uncensored.com)

---

## 🔧 Endpoints disponibles

| Endpoint | Fonction | Exemple |
|----------|----------|---------|
| `/chat` | Conversations textuelles | Chatbot, assistant |
| `/vision` | Analyse d'images | Décrire une photo |
| `/image` | Génération d'images | Créer une illustration |
| `/video` | Génération vidéo | Créer une vidéo courte |
| `/speech` | Synthèse vocale | Texte → Audio |
| `/edit` | Modification de contenu | Corriger un texte |

---

## ❓ FAQ (Questions fréquentes)

### **Q : C'est gratuit ?**
R : Uncensored.com propose généralement un free tier avec limitations, puis des plans payants. Vérifiez sur leur site.

### **Q : Où trouver ma clé API ?**
R : Sur [uncensored.com](https://uncensored.com), allez dans votre dashboard → API Keys.

### **Q : Ça marche sur Windows/Mac/Linux ?**
R : Oui ! Python fonctionne partout. Installez Python puis suivez les étapes ci-dessus.

### **Q : Je peux utiliser ça commercialement ?**
R : Vérifiez les conditions d'utilisation d'Uncensored.com. Ce dépôt est sous licence MIT (libre d'utilisation).

### **Q : Comment contribuer à ce projet ?**
R : Lisez [CONTRIBUTING.md](CONTRIBUTING.md) pour les instructions détaillées.

---

## 🆘 Besoin d'aide ?

1. **Issues GitHub** : [Ouvrir une issue](https://github.com/taowill972/uncensored-ai-docs/issues)
2. **Documentation officielle** : [uncensored.com/docs](https://uncensored.com)
3. **Support Uncensored** : Contactez leur équipe sur leur site

---

## 📝 Exemple complet de A à Z

Imaginons que vous voulez créer un chatbot simple :

```bash
# 1. Cloner le repo
git clone https://github.com/taowill972/uncensored-ai-docs.git
cd uncensored-ai-docs

# 2. Installer
pip install -r examples/python/requirements.txt

# 3. Créer votre script
cat > mon_chatbot.py << 'EOF'
from examples.python.chat_example import UncensoredClient

client = UncensoredClient(api_key="votre_clé_api")

print("Chatbot démarré ! (tapez 'quit' pour quitter)")
while True:
    user_input = input("\nVous: ")
    if user_input.lower() == 'quit':
        break

    reponse = client.chat(user_input)
    print(f"Bot: {reponse}")
EOF

# 4. Lancer
python mon_chatbot.py
```

**Résultat :** Vous avez un chatbot fonctionnel en 4 commandes ! 🎉

---

## ✅ Checklist de démarrage

- [ ] Python installé (3.11+)
- [ ] Dépôt cloné
- [ ] Dépendances installées (`pip install -r ...`)
- [ ] Clé API obtenue sur uncensored.com
- [ ] Premier test réussi avec `chat_example.py`
- [ ] Prêt à créer vos propres projets !

---

Bonne exploration ! 🚀
