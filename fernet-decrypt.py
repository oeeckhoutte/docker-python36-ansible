import json
import sys
import click
from cryptography.fernet import Fernet


@click.command("foreach", context_settings=dict(ignore_unknown_options=True))
@click.option(
    "--encrypted_string", "-s", help="your fernet key to decrypt the encrypted str"
)
@click.option("--key", help="your fernet key to decrypt the encrypted str")
def main(encrypted_string, key):
    if not encrypted_string or not key:
        print("Please specify --encrypted_string and --key args")
        sys.exit(1)
    f = Fernet(key)
    encrypted_value = str.encode(encrypted_string)
    decrypted_value = f.decrypt(encrypted_value)
    decrypted_value = json.loads(decrypted_value)
    s = json.dumps(decrypted_value, indent=4, sort_keys=True)
    print(s)


if __name__ == "__main__":
    main()
