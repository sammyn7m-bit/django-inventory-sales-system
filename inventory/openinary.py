import os

import requests
from django.core.exceptions import ImproperlyConfigured

OPENINARY_API_HOST = "https://cdn.openinary.dev"


def create_upload_signature():
    api_key = os.getenv("OPENINARY_API_KEY")

    if not api_key:
        raise ImproperlyConfigured(
            "OPENINARY_API_KEY is not configured."
        )

    response = requests.post(
        f"{OPENINARY_API_HOST}/upload/sign",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "DjangoInventorySalesSystem/1.0",
        },
        json={
            "folder": "products",
            "expiresIn": 300,
        },
        timeout=15,
    )

    response.raise_for_status()

    data = response.json()

    if not data.get("success"):
        raise RuntimeError("Openinary could not sign the upload.")

    return {
        "signature": data["signature"],
        "expires": data["expires"],
        "folder": data["folder"],
    }
