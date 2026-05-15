# Luumen Features

## LuumenAI
AI engine at the heart of Luumen. Accepts natural-language instructions and SOPs to build automated workflows. Has full context on hosts, OS versions, installed packages, environments. Every action requires explicit human-in-the-loop approval by default.

- Natural-language command interface embedded in terminal
- Ingests SOPs, runbooks, docs to create AI Skills
- AI Skills can be shared across team (Team & Enterprise)
- AI Knowledge Ingestion: Pro and above
- Auto-execution mode available (requires explicit user enablement; customer assumes all risks)

## AI-Assisted Triage (Incident Investigation)
Triage incidents in the terminal. LuumenAI uses context from current SSH sessions, IT tickets, telemetry, and SOPs to provide resolution steps. Enterprise tier includes AI Incident Investigation with cross-team knowledge sharing.

- Surfaces how other teams solved similar incidents
- Full context: org SOPs, telemetry, tickets
- Basic on all tiers; **AI Incident Investigation: Enterprise only**

## One-Click Host Access
Centralized workspace to connect to any server. Hundreds of hosts across clients, environments, cloud providers.

- SSH protocol
- WinRM (Windows Remote Management)
- Jump Host / Bastion Host
- Host Groups
- Snippets (reusable commands)
- Hosts stored securely in cloud

## Real-Time Monitoring
Integrates with monitoring tools for real-time metrics, resource trends, telemetry.

- CPU, memory, disk, network metrics
- Observability tool integrations (Enterprise)
- AWS, Azure, Google Cloud (Enterprise)

## Vulnerability & Security Scanning
Daily scans of environments, OS versions, installed packages against NVD and SAP Security Notes.

- CVE flagging with severity (CRITICAL, HIGH, MEDIUM, LOW)
- Actionable remediation steps
- Basic vulnerability scan: Free and above
- Session logs: all plans
- Monitoring Agent Scan: Enterprise only
- Automated Compliance Scan: Enterprise only

## Automated Compliance Scans (Enterprise)
Customizable checks for OS, configurations, security baselines, resource thresholds. Drift detection + proactive performance management.

## SAP Tools (Enterprise Only)
- Luumen SAP Agent
- SAP Security Note Scans
- SAP HotNews Analysis
- SAP Observability Integration

## Integrations
- ITSM Integrations: Enterprise (coming soon to lower tiers)
- SOP Ingestion Integrations: Enterprise (coming soon to lower tiers)
- Observability Integrations: Enterprise
- AWS / Azure / GCP: Enterprise
- SCIM provisioning for directory sync: Enterprise
