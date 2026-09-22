# miniSOAR
Building a complete SOAR framework in Python

---

```mermaid
flowchart TD
    %% Inputs
    B["Entra Logs"] --> n3["Log Parser"]
    n1["Process Creation Logs"] --> n3
    n3 --> C["SOAR Core Logic"]

    %% APIs
    C <--> D["Virustotal API"]
    C <--> E["AbuseIPDB API"]
    C <--> F["Microsoft Graph"]

    %% Playbooks & Decisions
    C -->|Logic| n4{"Security Playbook"}
    n4 --> n5["Isolate"]
    n4 --> n6["Manual Investigation"]
    n4 --> n7["Dismiss alert + Update logic"]

    %% Outputs & Logging
    n5 --> n8["Alert Staff + Log Incident"]
    n6 --> n8
    n7 --> n9["Log Incident + Update"]
