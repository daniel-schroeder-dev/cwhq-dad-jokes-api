# Overview

This section should contain an overview of the data provided and the API purpose. 

## Note

This is a simpler version of the original (now defunct) API which can be referenced here: [https://github.com/KegenGuyll/DadJokes_API#getting-started](https://github.com/KegenGuyll/DadJokes_API#getting-started). This version only provides a single endpoint (`/random/jokes`).

## Getting Started

The current version of the API lives at [https://projects.flask.cwhq-apps.com/dad-joke-api/](https://projects.flask.cwhq-apps.com/dad-joke-api/)

### Endpoints

| Endpoint                                                  |                                   What it does                                   |
| --------------------------------------------------------- | :------------------------------------------------------------------------------: |
| `GET` [`/random/jokes`](#random/jokes)                     |   Returns a joke object that contains a `setup` and `punchline`    |


## API calls

This API supports a data response in JSON format.

### /random/jokes

```json
{
    "punchline": "Ground-breaking",
    "setup": "I guess you could say that the invention of the shovel was really...."
}
```

