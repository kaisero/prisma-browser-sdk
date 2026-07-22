# prisma-browser-sdk

Python SDK for the Palo Alto Networks Prisma Browser

`prisma-browser-sdk` is the Python SDK for Prisma Browser Management Console Public API. It exposes
every object as a typed `client.<object>` wrapper with clean, verb-named methods and
handles authentication, pagination, and retries for you.

```bash
pip install prisma-browser-sdk
```

```python
from prisma_browser.extras.facade import Client

client = Client.from_env()
```

## Where to go next

- **[Getting Started](getting-started.md)** — install, authenticate, make your first call.
- **[Architecture](architecture.md)** — how the client, resources, and components fit together.
- **[Authentication](guides/authentication.md)** — credentials and configuration.
- **[Pagination](guides/pagination.md)** — iterate large result sets.
- **[CRUD operations](guides/crud.md)** — create, read, update, and delete resources.
- **[API Reference](reference/)** — every resource, operation, and model.

