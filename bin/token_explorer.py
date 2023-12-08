# tokens_explorer.py

import tiktoken


def token_explorer_from_string(
    string: str, encoding_name: str, verbose: bool = False
) -> str:
    encoding = tiktoken.get_encoding(encoding_name)
    token_raw = encoding.encode(string)
    if verbose is True:
        print(token_raw)
    return token_raw
