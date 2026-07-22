# Authentication

`prisma-browser-sdk` authenticates with credentials supplied via the environment or
passed explicitly.

## Required credentials

| Variable | Required | Secret |
|----------|----------|--------|
| `CLIENT_ID` | yes | no |
| `CLIENT_SECRET` | yes | yes |
| `SCOPE` | yes | no |
| `PRISMA_SASE_BASE_URL` | no | no |


## From the environment

```python
from prisma_browser.extras.facade import Client

client = Client.from_env()
```

## Passing credentials explicitly

```python
from prisma_browser.extras.facade import Client

client = Client.from_credentials(
    client_id="…",
    client_secret="…",
    scope="…",
)
```

Store secrets in a secrets manager or environment variables — never hard-code them.

