import argparse
import requests
from urllib.parse import urlparse
import re

PHISHING_KEYWORDS = ['login', 'secure', 'update', 'verify', 'account', 'bank', 'gift', 'free', 'card', 'signin', 'password']
URL_SHORTENERS = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'is.gd', 'buff.ly', 'adf.ly', 'bit.do']

def is_shortened(url):
    parsed = urlparse(url)
    return parsed.netloc.lower() in URL_SHORTENERS

def contains_phishing_keywords(url):
    return [word for word in PHISHING_KEYWORDS if word in url.lower()]

def resolve_redirects(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.url
    except:
        return url

def scan_url(url):
    print("\n🔍 PHISHING LINK SCANNER")
    print("────────────────────────────")
    print(f"Scanning: {url}\n")

    original_url = url
    url = resolve_redirects(url)

    flags = []

    # Heuristic: phishing keywords
    keywords = contains_phishing_keywords(url)
    if keywords:
        flags.append(f"❌ URL contains phishing-related keywords: {', '.join(keywords)}")

    # Heuristic: shortened URL
    if is_shortened(original_url):
        flags.append(f"❌ URL uses a known shortener service ({urlparse(original_url).netloc})")

    # Heuristic: suspicious domain structure
    if url.count('.') > 3:
        flags.append("❌ URL has a suspicious domain structure (too many dots)")

    if url != original_url:
        flags.append(f"➡  Redirects to: {url}")

    if flags:
        for flag in flags:
            print(flag)
        print("\n⚠  This URL may be a **PHISHING ATTEMPT**.")
    else:
        print("✅ URL appears safe based on heuristic checks.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phishing URL Scanner")
    parser.add_argument("-u", "--url", required=True, help="URL to scan")
    args = parser.parse_args()
    scan_url(args.url)
