# ADR-001 -- Strict Layered Architecture Enforcement (v2 Extension)

Date: 2026-03-01 Status: Accepted

------------------------------------------------------------------------

## Extension -- Interface Layer Formalization

Frontend is formally recognized as part of the Interface Layer.

Constraints:

-   No business logic in frontend.
-   No consolidation or aggregation calculation in client.
-   All state mutations must occur through Application layer use cases.
-   API contracts must remain stable once Month 3 is locked.

Violation of these rules is a structural breach.
