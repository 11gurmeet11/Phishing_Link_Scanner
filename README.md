# Phishing_Link_Scanner

## Description  
This is a simple Python-based tool that scans URLs to detect potential phishing attempts. It uses heuristic checks such as keyword analysis, shortened URL detection, and suspicious domain structures to help identify malicious links.

---

## Features  
-  Checks for common phishing keywords in the URL  
-  Detects usage of known URL shorteners (e.g., bit.ly, t.co)  
-  Analyzes domain structure for suspicious patterns  
-  Resolves and displays redirection URLs  
-  Lightweight and command-line friendly

---

## How It Works  
The tool uses the following heuristics to flag a URL as suspicious:

1. **Phishing Keywords**: Checks if the URL contains terms like `login`, `verify`, `account`, `secure`, etc.  
2. **Shortened URLs**: Detects if the link is masked using a shortener like `bit.ly`, `t.co`, etc.  
3. **Suspicious Domain Structure**: Flags domains with an unusually high number of dots (e.g., `secure-login-update.freegift.com.info.biz`).  
4. **Redirections**: Follows redirects and alerts if the final destination differs from the input.

---

## Installation  
Make sure Python 3 and `requests` are installed on your system.

```bash
git clone https://github.com/11gurmeet11/phishing_link_scanner.git
cd phishing-link-scanner
pip install requests
```

----

## Usage
```bash
python3 phishing_scanner.py -u "http://example.com"
```

---

## Example
```bash
python3 phish-scanner.py -u "http://secure-login-update.freegift.com"                        

🔍 PHISHING LINK SCANNER
────────────────────────────
Scanning: http://secure-login-update.freegift.com

❌ URL contains phishing-related keywords: login, secure, update, gift, free
➡  Redirects to: http://secure-login-update.freegift.com/

⚠  This URL may be a **PHISHING ATTEMPT**.
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


