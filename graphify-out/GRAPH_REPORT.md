# Graph Report - support-service  (2026-11-12)

## Corpus Check
- В структурный анализ включено файлов исходного кода: 6. Сторонние зависимости, документация и файлы окружения исключены.

## Summary
- 48 nodes · 74 edges · 9 communities (1 shown, 8 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- schemas.py
- main.py
- settings.py
- models.py
- create_ticket
- run_async_migrations
- run_migrations_online
- run_migrations_offline

## God Nodes (most connected - your core abstractions)
1. `TicketStatus` - 6 edges
2. `Base` - 6 edges
3. `create_ticket()` - 6 edges
4. `TicketResponse` - 5 edges
5. `Ticket` - 5 edges
6. `TicketCreate` - 4 edges
7. `get_my_tickets()` - 4 edges
8. `run_async_migrations()` - 4 edges
9. `run_migrations_online()` - 4 edges
10. `Settings` - 3 edges

## Surprising Connections (you probably didn't know these)
- `create_ticket()` --uses--> `TicketStatus`  [INFERRED]
  main.py → models.py
- `create_ticket()` --uses--> `TicketCreate`  [INFERRED]
  main.py → schemas.py
- `startup()` --uses--> `Base`  [INFERRED]
  main.py → models.py
- `create_ticket()` --uses--> `Ticket`  [INFERRED]
  main.py → models.py
- `get_my_tickets()` --uses--> `Ticket`  [INFERRED]
  main.py → models.py

## Import Cycles
- None detected.

## Communities (9 total, 8 thin omitted)

### Community 0 - "schemas.py"
Cohesion: 0.28
Nodes (4): TicketStatus, TicketCreate, TicketResponse, Config

## Knowledge Gaps
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Base` connect `models.py` to `main.py`, `env.py`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `TicketStatus` (e.g. with `create_ticket()` and `TicketResponse`) actually correct?**
  _`TicketStatus` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Why does `create_ticket()` connect `create_ticket` to `schemas.py`, `main.py`, `models.py`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `create_ticket()` (e.g. with `Ticket` and `TicketStatus`) actually correct?**
  _`create_ticket()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Ticket` (e.g. with `create_ticket()` and `get_my_tickets()`) actually correct?**
  _`Ticket` has 2 INFERRED edges - model-reasoned connections that need verification._