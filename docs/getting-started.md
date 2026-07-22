# Getting Started

This guide takes you from zero to your first successful API call.

## Install

```bash
pip install prisma-browser-sdk
```

## Configure credentials

The client reads credentials from the environment. Set:

```bash
export CLIENT_ID="your-client_id"
export CLIENT_SECRET="…"
export SCOPE="your-scope"
```

See the [Authentication guide](guides/authentication.md) for every option and for passing
credentials explicitly.


## Your first call

```python
from prisma_browser.extras.facade import Client

client = Client.from_env()

# List application
page = client.application.list()
print(page)
```

You're set — continue to [CRUD operations](guides/crud.md).

