"""
make_english_only.py
Run this script inside ZerynBot-main to remove all non-English languages
and convert the bot into a streamlined English-only system.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 1. Non-English locale files to delete
LOCALE_FILES_TO_REMOVE = [
    "locales/es.json",
    "locales/fr.json",
    "locales/pt.json",
    "locales/vi.json",
    "locales/zh.json",
]

# 2. i18n audit/migration scripts that are no longer needed
UNUSED_SCRIPTS = [
    "scripts/i18n_audit.py",
    "scripts/i18n_migrate.py",
    "scripts/_i18n_pending.json",
    "tests/test_i18n.py",
    "tests/test_i18n_no_hardcoded.py",
    "tests/i18n_budget.json",
    "bot/cogs/lang.py",
]

print(">>> [1/3] Removing non-English locale files...")
for rel_path in LOCALE_FILES_TO_REMOVE:
    p = BASE_DIR / rel_path
    if p.exists():
        p.unlink()
        print(f"  [x] Deleted: {rel_path}")
    else:
        print(f"  [-] Not found (already deleted): {rel_path}")

print("\n>>> [2/3] Removing unused language scripts & cogs...")
for rel_path in UNUSED_SCRIPTS:
    p = BASE_DIR / rel_path
    if p.exists():
        p.unlink()
        print(f"  [x] Deleted: {rel_path}")

print("\n>>> [3/3] Replacing i18n.py with streamlined English-only loader...")
new_i18n_code = '''"""
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
    """Load English translations into memory."""
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
    else:
        logger.warning("locales/en.json not found!")

# Initialize on module import
load_translations()

def t(key: str, **kwargs) -> str:
    """
    Retrieve an English string by dot-notated key.
    Example: t("moderation.ban_success", user="Alex")
    """
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

# Backwards compatibility alias
def get_text(key: str, guild_id: int = None, **kwargs) -> str:
    return t(key, **kwargs)
'''

i18n_path = BASE_DIR / "i18n.py"
with open(i18n_path, "w", encoding="utf-8") as f:
    f.write(new_i18n_code)
print("  [✓] Updated i18n.py to English-only mode.")

print("\nAll non-English languages successfully removed! Bot is now English-only.")