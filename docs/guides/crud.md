# CRUD operations

End-to-end create, read, update, and delete via the `client.application` wrapper.
Browse the full operation list in the **[API Reference](../reference/)**.

```python
from prisma_browser.extras.facade import Client

client = Client.from_env()
```


## Create

```python
created = client.application.create(
    type="custom",
    body=CustomApplicationInput(
        name="Acme Wiki",
        type="custom",
        urls=[UrlInput(url="https://wiki.acme.com/*")],
    ),
)

```


## Read

```python
fetched = client.application.get(
    id="<id>",
)
```


## Update

```python
updated = client.application.update(
    type="custom",
    id="<id>",
    body=PatchAppInput(CustomPatchApplicationInput(
            type="custom",
        )),
)
```


## Delete

```python
client.application.delete(
    id="<id>",
)
```


