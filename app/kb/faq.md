# Luumen FAQ

## Getting Started / Account

**How do I get started?**
Download from https://www.luumen.ai/download, install on macOS/Windows/Linux, sign in with OAuth (Google or Microsoft), create a workspace, add your first host.

**Is there a free version?**
Yes. Free plan = $0/month: unlimited hosts, 1 user, 600 AI credits, vulnerability scan.

**What is an AI Credit?**
AI Credits are consumed when you use LuumenAI features (chat, skills, diagnostics). Free 600 / Pro 2,400 / Team 4,500 / Enterprise Unlimited per month.

**Can I use Luumen on Windows?**
Yes. macOS, Windows, and Linux supported.

**What Linux distros are supported?**
Any distro with glibc 2.28+: Debian 10+, Ubuntu 20.04+, Fedora 29+, RHEL 8+, OpenSUSE 15.3+. AppImage for x64 and ARM64.

## Pricing & Billing

**How is pricing structured?**
Free ($0), Pro ($16/mo/user), Team ($30/user/mo), Enterprise (custom). All billed annually. 20% discount vs. monthly.

**How do I upgrade my plan?**
Upgrade via account settings in the app, or email support@luumen.ai.

**Are refunds available?**
No. All payments final. Cancel before the next billing cycle to avoid future charges.

**How do I cancel my subscription?**
Cancel before the current billing cycle expires. Access remains until the period ends.

**Does Luumen store my payment info?**
No. Payment is processed and stored by Stripe. Apiphani never stores card details.

**Can I get Enterprise pricing?**
Yes. Book a demo at https://www.luumen.ai/contact or email support@luumen.ai.

## Features & Capabilities

**What is LuumenAI?**
Embedded AI engine that understands natural language, ingests SOPs/runbooks, and automates repetitive tasks. Full context of hosts, OS, packages, environments.

**Does LuumenAI execute commands automatically?**
By default every action requires human approval (human-in-the-loop). Optional auto-execution mode can be enabled — customer assumes full responsibility for outcomes.

**What are AI Skills?**
Reusable automated workflows built from natural-language instructions + SOPs. All plans have AI Skills; sharing AI Skills requires Team or Enterprise.

**Does Luumen support WinRM?**
Yes. WinRM is supported on all plans.

**Does Luumen support jump/bastion hosts?**
Yes. Jump Host and Bastion Host support is on all plans.

**How does vulnerability scanning work?**
Daily scans of environments, OS versions, and installed packages against NVD and SAP Security Notes. Flags CVEs with severity scores + remediation steps.

**Can I share credentials with my team?**
Only on Team and Enterprise. Free and Pro do not support credential sharing.

**Is SSO available?**
Enterprise only: SAML, OIDC, Active Directory + SCIM provisioning.

**Are cloud integrations available?**
AWS, Azure, GCP integrations are Enterprise only.

## Security & Privacy

**Is Luumen SOC 2 certified?**
Yes. SOC 2 Type 2 attested. Audit reports at https://trust.apiphani.com.

**How is my data encrypted?**
At rest: AES-256-GCM (cloud-provider managed). In transit: TLS 1.3 with ECDHE. Zero plaintext access.

**Does Luumen use my data to train AI?**
By default, Apiphani may use aggregated and anonymized customer data to improve the service. Opt-out available in account settings.

**Where is my data stored?**
Amazon Web Services (AWS). AWS GovCloud used for FedRAMP-bound environments.

**I found a security vulnerability. Who do I contact?**
Email security@luumen.ai. Reports acknowledged promptly. No legal action against good-faith researchers.

**Is my personal data shared with third parties?**
Only with authorized subprocessors needed to deliver the service (AWS, WorkOS, Stripe, Intercom, etc.). Full list at https://trust.apiphani.com or in privacy policy at https://www.luumen.ai/privacy.
