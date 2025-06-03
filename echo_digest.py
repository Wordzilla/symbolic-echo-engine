# Compresses echo structures into serialized digests

import json

def digest_echo_structure(echo_data, path="echo_digest.json"):
    with open(path, 'w') as f:
        json.dump(echo_data, f)
    return path
