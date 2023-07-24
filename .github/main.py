DEFAULT_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/80.0.3987.163 "
    "Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.5",
}

from httpx import get, ReadTimeout
import json
import tldextract
calls = json.loads(open("provider.mov-cli").read())
for main, sub in dict(calls).items():
    if sub == "":
        continue
    try:
        check = get(sub, follow_redirects=True, headers=DEFAULT_HEADERS, timeout=10)
    except:
        continue
    checkext = tldextract.extract(str(check.url))
    subext = tldextract.extract(sub)
    if checkext.registered_domain == subext.registered_domain:
        print(f"Checked: {main}")
    else:
        if checkext.subdomain:
            updatedurl = "https://" + checkext.subdomain + "." + checkext.registered_domain
        else:
            updatedurl = "https://" +  checkext.registered_domain
        calls[main] = updatedurl
        print(f"Updated: {main} from {sub} to {updatedurl}")
open(f"provider.mov-cli", "w").write(json.dumps(calls))
