# envseal

[![CI](https://github.com/piyushppd/envseal/actions/workflows/ci.yml/badge.svg)](https://github.com/piyushppd/envseal/actions/workflows/ci.yml)

Misuse-resistant envelope encryption for sensitive records.

> **Status: pre-alpha. Nothing is implemented yet.** This repository currently
> holds the project skeleton, toolchain and CI. Do not use it to protect data.

## The idea

Most cryptographic failures in application code are not broken primitives. They
are callers making choices they should never have been offered: the algorithm,
the nonce, the key, whether to bind context. `envseal` offers none of them.

```python
blob = seal(plaintext, context={"tenant": "acme", "record": "42"})
plaintext = unseal(blob, context={"tenant": "acme", "record": "42"})
```

Planned properties:

- Two calls. No algorithm, nonce or key arguments.
- Context (associated data) is mandatory; a mismatch fails closed.
- Envelope encryption: a fresh data key per object, wrapped by a key-encrypting
  key held in a KMS or Vault transit; a local fake for tests.
- Key commitment: one ciphertext cannot decrypt under two keys.
- A version byte in the header, so rotation is a decrypt-old / encrypt-new
  migration, not a flag day.
- No hand-rolled primitives. Cryptography comes from
  [`cryptography`](https://cryptography.io).

See [THREATMODEL.md](THREATMODEL.md) for what it will and will not defend against.

## Development

Requires [uv](https://docs.astral.sh/uv/).

```sh
uv sync          # create .venv and install dev dependencies
uv run pytest    # tests + coverage
uv run ruff check . && uv run ruff format --check .
uv run mypy      # strict
```

## License

Apache-2.0
