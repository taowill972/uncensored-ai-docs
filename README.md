# uncensored-ai-docs

Documentation complète de l'API Uncensored.com - Endpoints, modèles, exemples Python/cURL, intégration Dataset AI, et guide de fine-tuning.

## Description

Ce dépôt centralise la documentation technique pour l'API d'[Uncensored.com](https://uncensored.com), une plateforme d'IA générative offrant des modèles sans restrictions. L'objectif est de fournir des guides pratiques et des exemples de code pour intégrer cette API dans vos projets.

**Objectifs du projet :**
- Documenter tous les endpoints disponibles
- Fournir des exemples de code prêts à l'emploi
- Créer des guides de fine-tuning personnalisé
- Centraliser les bonnes pratiques d'intégration

## Modèles disponibles

| Modèle | Description |
|--------|-------------|
| **Model-T** | Modèle intelligent et efficace |
| **GPT-5 Uncensored** | Version sans restrictions de GPT-5 |
| **Gemini-pro** | Modèle Google Gemini intégré |
| **Grok-4** | Modèle xAI/Twitter |
| **Sora-2** | Génération vidéo |
| **Flagship** | Modèle phare multimodal |

## Endpoints API

| Endpoint | Fonction |
|----------|----------|
| `/chat` | Conversations textuelles |
| `/code` | Génération et analyse de code |
| `/vision` | Analyse d'images |
| `/edit` | Modification de contenu |
| `/media` | Génération multimédia |
| `/speech` | Synthèse vocale |
| `/image` | Génération d'images |
| `/video` | Génération vidéo |

## Fonctionnalités

- **Sans restrictions** : Réponses non censurées
- **Multimodal** : Texte, image, vidéo, audio
- **Recherche web** : Accès à internet en temps réel
- **Anonymisation** : Options de confidentialité
- **Fallback** : Routage automatique entre modèles

## Manuel d'utilisation

### Prérequis
- Compte Uncensored.com (gratuit ou premium)
- Clé API (obtenue dans le dashboard)

### Installation Python

```bash
pip install requests
```

### Exemple : Chat simple

```python
import requests

API_KEY = "votre_cle_api"
BASE_URL = "https://api.uncensored.com/v1"

response = requests.post(
    f"{BASE_URL}/chat",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "model-t",
        "messages": [
            {"role": "user", "content": "Bonjour, comment ça va?"}
        ]
    }
)

print(response.json()["choices"][0]["message"]["content"])
```

### Exemple : cURL

```bash
curl -X POST https://api.uncensored.com/v1/chat \
  -H "Authorization: Bearer VOTRE_CLE_API" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "model-t",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### Exemple : Génération d'image

```python
response = requests.post(
    f"{BASE_URL}/image",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "prompt": "Un paysage futuriste avec des néons",
        "size": "1024x1024"
    }
)

image_url = response.json()["data"][0]["url"]
print(f"Image générée: {image_url}")
```

## Structure prévue

```
uncensored-ai-docs/
├── README.md           # Ce fichier
├── LICENSE             # Licence MIT
├── docs/
│   ├── getting-started.md
│   ├── authentication.md
│   ├── endpoints/
│   │   ├── chat.md
│   │   ├── vision.md
│   │   ├── image.md
│   │   └── video.md
│   └── fine-tuning.md
├── examples/
│   ├── python/
│   ├── javascript/
│   └── curl/
└── datasets/
    └── README.md
```

## Ressources

- **Site officiel** : [uncensored.com](https://uncensored.com)
- **Playground** : Test API en ligne
- **Apps** : iOS et Android disponibles

## Contribution

Les contributions sont bienvenues ! Ouvrez une issue ou une PR pour :
- Ajouter des exemples de code
- Corriger la documentation
- Proposer de nouveaux guides

## Licence

MIT License
