# Luumen Security & Compliance

Apiphani operates under SOC 2 Type 2 attestation, ISO 27001 certification, and CSA STAR accreditation.

## Certifications & Attestations
- **SOC 2 Type II** — Independently audited controls for security, availability, confidentiality.
- **ISO 27001** — Certified information security management across all operations.
- **CSA STAR Accreditation** — Certified by the Cyber Security Trust Alliance.

## Encryption
- **At rest**: AES-256-GCM, cloud-provider managed encryption for all sensitive datastores.
- **In transit**: TLS 1.3 with ECDHE key exchange and AES-256-GCM cipher.
- Zero plaintext access.
- Privileged access to encryption keys restricted to authorized personnel.

## Data Protection
- Formal classification & retention policy for confidential data.
- Customer data is purged when a customer leaves the service.

## Access & Identity
- Unique credentials required for all production access; password policies enforced.
- Enterprise SSO (SAML, OIDC, Active Directory) and SCIM provisioning available for Enterprise tier.
- Workspace-level roles and permissions limit visibility/actions.
- Privileged system and admin actions captured in audit logs.

## Monitoring & Incident Response
- Production access requires authenticated encrypted connections; firewalls reviewed annually.
- Continuous network monitoring for security events.
- Continuous vulnerability scanning of dependencies and infrastructure against NVD.
- Incidents logged, tracked, resolved, and communicated to affected parties per documented policy.

## Third-Party Subprocessors

| Category | Subprocessor | Purpose |
|----------|--------------|---------|
| Hosting & Infrastructure | Amazon Web Services | App hosting, infra, storage, LLM inference (Bedrock). AWS GovCloud for FedRAMP. |
| AI & Product Analytics | LangSmith | LLM trace and prompt monitoring for LuumenAI |
| AI & Product Analytics | PostHog | Product analytics on the Luumen application |
| Identity & Auth | Microsoft Azure | Identity/IAM for MS365, Sign in with Outlook |
| Identity & Auth | Google Cloud Platform | Sign in with Google (OAuth) |
| Identity & Auth | WorkOS | OAuth, Enterprise SSO (SAML/OIDC), directory sync (SCIM) |
| Observability | Dynatrace | APM and infrastructure observability |
| Observability | Better Stack | Application log aggregation |
| Customer Engagement | Stripe | Self-service billing and payment processing |
| Customer Engagement | Intercom | Customer support conversations |
| Customer Engagement | Frill | Customer feedback and feature requests |

## Trust Resources
- Full compliance reports: https://trust.apiphani.com (request access)
- Responsible disclosure: security@luumen.ai — no legal action against good-faith researchers
- System status: https://status.luumen.ai
