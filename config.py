PORT = 33333

# name -> secret (32 hex chars)
USERS = {
    "tg":  "e601e300d8e3fb8bfcec8828f9cf0834",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.cloudflare.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "f52147af89f63098ba6022d882c04602"
