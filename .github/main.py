DEFAULT_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/80.0.3987.163 "
    "Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.5",
}

from httpx import get
import json
import tldextract

calls = json.loads(open("provider.mov-cli").read())

for main, sub in dict(calls).items():
    print(f"Checking: {main}")
    if sub == "":
        continue
    try:
        check = get(sub, follow_redirects=True, headers=DEFAULT_HEADERS, timeout=10)
    except TimeoutError:
        continue
    if sub == str(check.url):
        pass
    else:
        calls[main] = str(check.url)
        print(f"Updated: {main} from {sub} to {check.url}")
open(f"provider.mov-cli", "w").write(json.dumps(calls))
