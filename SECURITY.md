# Security Policy

## Scope

This repository contains documentation, taxonomy data, and visualization code. There is no production service, authentication system, or user data.

Security concerns relevant to this project:

1. **Taxonomy integrity** — If you discover that a threat entry, CTSS score, or mitigation mapping has been altered in a way that materially degrades the framework's defensive value, report it.
2. **Command Center vulnerabilities** — The HTML5 Command Center is a static visualization tool. If you identify a client-side vulnerability (XSS, data injection) in the visualization code, report it.
3. **Supply chain** — If you identify a dependency in this repository that has been compromised, report it immediately.

## Reporting

Report security issues by opening a **private security advisory** through GitHub's Security tab. Do not open a public issue for security vulnerabilities.

Include:
- Description of the concern
- Steps to reproduce (for code vulnerabilities)
- Affected files and taxonomy IDs (for taxonomy integrity issues)
- Proposed remediation if known

We will respond within 72 hours and coordinate disclosure with you.

## Out of Scope

- Social engineering of CSI staff
- Physical security
- Denial of service against GitHub infrastructure
