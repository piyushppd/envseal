"""envseal: misuse-resistant envelope encryption.

The public API will be exactly two calls:

    seal(plaintext: bytes, context: Mapping[str, str]) -> bytes
    unseal(blob: bytes, context: Mapping[str, str]) -> bytes

No algorithm, nonce or key arguments. Context (associated data) is mandatory.
Nothing is implemented yet; see THREATMODEL.md for the design intent.
"""

__all__ = ["__version__"]

__version__ = "0.0.1"
