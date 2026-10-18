"""
ZerynBot Internationalization Engine - English Only
"""
import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger("i18n")

_TRANSLATIONS: Dict[str, Any] = {}
_LOCALES_DIR = Path(__file__).resolve().parent / "locales"

def load_translations():
    global _TRANSLATIONS
    en_file = _LOCALES_DIR / "en.json"
    if en_file.exists():
        try:
            with open(en_file, "r", encoding="utf-8") as f:
                _TRANSLATIONS = json.load(f)
            logger.info("Loaded English translations successfully.")
        except Exception as e:
            logger.error(f"Failed to load en.json: {e}")
            _TRANSLATIONS = {}

load_translations()

def t(key: str, **kwargs) -> str:
    parts = key.split(".")
    data = _TRANSLATIONS
    for part in parts:
        if isinstance(data, dict):
            data = data.get(part, key)
        else:
            return str(data)

    if isinstance(data, str):
        try:
            return data.format(**kwargs) if kwargs else data
        except Exception:
            return data
    return key

def get_text(key: str, guild_id: int = None, **kwargs) -> str:
    return t(key, **kwargs)
def tr(guild_settings_or_lang, key: str, **kwargs) -> str:
    if isinstance(guild_settings_or_lang, dict):
        lang = guild_settings_or_lang.get("language", DEFAULT_LANG)
    elif isinstance(guild_settings_or_lang, str):
        lang = guild_settings_or_lang
    else:
        lang = DEFAULT_LANG
    return i18n.translate(lang, key, **kwargs)
