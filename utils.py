"""Utility helpers."""

import json
import os


def load_config(path: str = "config.json") -> dict:
    """Read a JSON config, returning {} when absent."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)
