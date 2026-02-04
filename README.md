# My Agentic Project

This repository provides a lightweight Python scaffolding that mirrors the structure in the diagram.

## Structure

```
my-agentic-project/
├── app/
│   ├── api/
│   │   └── router.py
│   ├── agents/
│   │   ├── nodes.py
│   │   ├── state.py
│   │   ├── tools.py
│   │   ├── workflow.py
│   │   └── __init__.py
│   ├── utils/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── __init__.py
│   ├── dal/
│   │   ├── base.py
│   │   ├── dynamo_repo.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── agent_service.py
│   │   ├── tool_registry.py
│   │   └── __init__.py
│   └── __init__.py
├── entrypoints/
│   ├── agent_core/
│   │   └── cli_runner.py
│   ├── ecs/
│   │   ├── Dockerfile
│   │   └── main.py
│   └── lambda/
│       └── handler.py
├── tests/
│   └── test_workflow.py
├── pyproject.toml
└── README.md
```

## Quick start

```bash
python entrypoints/agent_core/cli_runner.py
```
