# tony-sandbox

Sandbox repository for **Tony AI** hands experimentation.

This is a minimal Python + Svelte project with trivial tests, used as a safe
"war zone" where Tony's autonomous Hands can experiment with code changes
without risk.

## Structure

```
tony-sandbox/
├── python/
│   ├── math_utils.py       # Simple math utilities
│   ├── string_utils.py     # String manipulation helpers
│   └── tests/
│       ├── test_math.py    # Math tests
│       └── test_string.py  # String tests
├── svelte/
│   ├── src/
│   │   └── Counter.svelte  # Basic counter component
│   └── tests/
│       └── counter.spec.ts
└── README.md
```

## Python Tests

```bash
cd python && python -m pytest tests/ -v
```

## Usage

This repo is monitored by Tony's Hand system. Issues labeled `tony-resolve` or
assigned to `tony-8-bot` will be automatically picked up and resolved via PR.
