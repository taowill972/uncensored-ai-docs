"""
Exemple d'utilisation de l'API Uncensored.com pour le chat
Documentation: https://github.com/taowill972/uncensored-ai-docs
"""

import requests
import os
from typing import Optional

class UncensoredClient:
    """Client simple pour l'API Uncensored.com"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialise le client API

        Args:
            api_key: Clé API (ou utilise la variable d'environnement UNCENSORED_API_KEY)
        """
        self.api_key = api_key or os.getenv("UNCENSORED_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set UNCENSORED_API_KEY env var or pass api_key parameter")

        self.base_url = "https://api.uncensored.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, message: str, model: str = "model-t") -> str:
        """
        Envoie un message au modèle de chat

        Args:
            message: Le message à envoyer
            model: Le modèle à utiliser (défaut: model-t)

        Returns:
            La réponse du modèle
        """
        response = requests.post(
            f"{self.base_url}/chat",
            headers=self.headers,
            json={
                "model": model,
                "messages": [{"role": "user", "content": message}]
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]


def main():
    """Exemple d'utilisation"""
    # Initialiser le client
    client = UncensoredClient()

    # Envoyer un message
    response = client.chat("Bonjour! Comment ça va?")
    print(f"Réponse: {response}")

    # Utiliser un modèle différent
    response_gpt5 = client.chat("Explique-moi la théorie de la relativité", model="gpt-5-uncensored")
    print(f"\nRéponse GPT-5: {response_gpt5}")


if __name__ == "__main__":
    main()
