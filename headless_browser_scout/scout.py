from dataclasses import dataclass
import re

@dataclass
class BrowserScoutConfig:
    port: int = 9222
    host: str = "127.0.0.1"
    timeout: float = 30.0
    stealth_mode: bool = True

def extract_clean_dom(raw_html: str) -> str:
    """Removes scripts, styles, SVGs, and iframe tags to extract core readable text/DOM."""
    cleaned = re.sub(r"(?is)<(script|style|svg|noscript|iframe).*?>.*?</>", "", raw_html)
    cleaned = re.sub(r"<!--.*?-->", "", cleaned)
    return cleaned.strip()
