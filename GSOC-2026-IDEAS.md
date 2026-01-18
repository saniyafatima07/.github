# Google Summer of Code 2026 - Project Ideas

Welcome to the pointblank-club GSoC 2026 ideas page. This document consolidates project ideas across all our repositories for prospective GSoC contributors.

## About pointblank-club

pointblank-club is an organization focused on systems programming, security tools, and compiler optimization. Our projects span container runtimes, binary analysis, system hardening, and machine learning for compilers.

## How to Get Started

1. **Explore our repositories** - Familiarize yourself with the projects that interest you
2. **Read the documentation** - Each repository has a README and CONTRIBUTING.md
3. **Join the community** - Participate in GitHub Discussions and Issues
4. **Start small** - Look for `good first issue` labels to make initial contributions
5. **Reach out to mentors** - Discuss your ideas and get feedback early

# Project Ideas

---

## kettle: Add Container Lifecycle Management and Kubernetes Support

**Repository:** https://github.com/pointblank-club/kettle  
**Full proposal:** https://github.com/pointblank-club/kettle/blob/main/GSOC-2026.md

### Summary

Extend kettle with full container lifecycle management (create, start, stop, delete) and add Kubernetes integration to run and manage containers as pods.

### Description

This project evolves kettle from a minimal runtime engine into a usable container runtime with clear lifecycle primitives and basic Kubernetes compatibility. The work includes wiring lifecycle operations on top of low-level runtimes (runc/libcontainer), integrating OCI concepts, and adding a Kubernetes-facing layer to manage containers through standard tooling.

### Details

| Attribute | Value |
|---------|------|
| Skill level | Intermediate |
| Language | Go |
| Expected size | Medium |
| Mentors | Rahul K (rahul.u.india[at]gmail[.]com) |

### Relevant Links

- https://github.com/containerd/containerd  
- https://github.com/opencontainers/runc  

---

## vestigo: Automated Peripheral Modeling

**Repository:** https://github.com/pointblank-club/vestigo  
**Full proposal:** https://github.com/pointblank-club/vestigo/blob/main/GSOC-2026.md

### Summary

Extend Vestigo’s firmware analysis pipeline by improving format support, crypto-detection accuracy, and analysis extensibility.

### Description

Vestigo is a firmware analysis and cryptographic primitive detection pipeline. This project focuses on expanding supported firmware formats, improving ML-based crypto detection accuracy, integrating additional analysis backends (such as Ghidra or Binary Ninja), and optionally adding a web-based dashboard for analysis results.

### Details

| Attribute | Value |
|---------|------|
| Skill level | Intermediate |
| Language | Python |
| Expected size | Medium |
| Mentors | TBD |

### Relevant Links

- https://ghidra-sre.org/  
- https://binary.ninja/  

---

## oaas: Windows PE Binary-to-Binary Obfuscation Pipeline

**Repository:** https://github.com/pointblank-club/oaas  
**Full proposal:** https://github.com/pointblank-club/oaas/blob/main/GSOC-2026.md

### Summary

Implement a binary-to-binary obfuscation pipeline for Windows PE executables using LLVM-based lifting and recompilation.

### Description

Currently, oaas supports only source-to-binary obfuscation. This project enables obfuscating existing Windows PE binaries when source code is unavailable. The pipeline extracts control-flow graphs using Ghidra, lifts binaries to LLVM IR using McSema or RetDec, applies OLLVM obfuscation passes, and recompiles the result into a working obfuscated PE binary.

### Details

| Attribute | Value |
|---------|------|
| Skill level | Intermediate |
| Languages | Python, C++, Bash |
| Expected size | Medium (~175 hours) |
| Mentors | TBD |

### Relevant Links

- https://github.com/lifting-bits/mcsema  
- https://github.com/avast/retdec  
- https://ghidra-sre.org/  

---

## syshardn: Scheduled Compliance Scans and History

**Repository:** https://github.com/pointblank-club/syshardn  
**Full proposal:** https://github.com/pointblank-club/syshardn/blob/main/GSOC-2026.md

### Summary

Add scheduled compliance scans, persistent scan history, and artifact export to syshardn.

### Description

This project extends syshardn with the ability to run scans on a schedule and persist historical results. It includes integrating with native OS schedulers (cron, systemd timers, Windows Task Scheduler), storing scan history in a structured format, and exporting scan artifacts for auditing and compliance workflows.

### Details

| Attribute | Value |
|---------|------|
| Skill level | Intermediate |
| Language | Python |
| Expected size | Medium (~175 hours) |
| Mentors | TBD |

### Relevant Links

- https://www.freedesktop.org/software/systemd/man/systemd.timer.html  
- https://man7.org/linux/man-pages/man5/crontab.5.html  
- https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page  

---

## syshardn: macOS Platform Support

**Repository:** https://github.com/pointblank-club/syshardn  
**Full proposal:** https://github.com/pointblank-club/syshardn/blob/main/GSOC-2026.md

### Summary

Add native macOS platform support to syshardn with a dedicated executor and rule pack.

### Description

This project introduces macOS support to syshardn by implementing platform detection, a macOS-specific executor (check/apply/rollback), and a focused rule pack covering password policy, screen lock, firewall configuration, and FileVault.

### Details

| Attribute | Value |
|---------|------|
| Skill level | Intermediate |
| Language | Python |
| Expected size | Small (~90 hours) |
| Prerequisites | Access to macOS; familiarity with macOS security tooling |
| Mentors | TBD |

### Relevant Links

- https://www.cisecurity.org/benchmark/apple_os  

---

## IRis: GNN-Based Structure-Aware LLVM IR Analysis

**Repository:** https://github.com/pointblank-club/IRis  
**Full proposal:** https://github.com/pointblank-club/IRis/blob/main/GSOC-2026.md

### Summary

Integrate Graph Neural Networks (GNNs) into the IRis optimization pipeline for structure-aware LLVM IR analysis.

### Description

IRis currently relies on scalar feature vectors that discard structural information such as control flow and data dependencies. This project introduces graph-based representations of LLVM IR, constructs CFG and DFG graphs, and integrates a GNN encoder into the existing PassFormer pipeline to improve optimization prediction accuracy.

### Details

| Attribute | Value |
|---------|------|
| Skill level | Intermediate |
| Languages | Python, PyTorch, GNNs, LLVM IR |
| Expected size | Large (~350 hours) |
| Mentors | Shubhang, Inchara, Yash |

### Relevant Links

- https://llvm.org/  
- https://pytorch-geometric.readthedocs.io/  

---

## edgeFlow: Advanced IR Optimization Passes

**Repository:** https://github.com/pointblank-club/edgeFlow  
**Full proposal:** https://github.com/pointblank-club/edgeFlow/blob/main/GSOC-2026.md

### Summary

Implement advanced IR-level optimization passes and backend support for edge-deployed ML workloads.

### Description

edgeFlow is a DSL for optimizing machine-learning models for edge devices. This project focuses on implementing new optimization passes, expanding hardware backend support, improving quantization and pruning techniques, and integrating edgeFlow with popular ML frameworks.

### Details

| Attribute | Value |
|---------|------|
| Skill level | Intermediate |
| Language | Python / ML tooling |
| Expected size | Medium |
| Mentors | TBD |

### Relevant Links

- https://llvm.org/  

---

## General Information for Applicants

### Application Tips

- Start contributing early - familiarity with the codebase strengthens your application
- Propose realistic timelines based on the expected project size
- Demonstrate understanding of the technical challenges involved
- Show how your background prepares you for the project
- Be specific about deliverables and milestones

### Mentor Contact

For questions about specific projects, reach out via:
- Email: admin@pointblank.club
- GitHub Issues in the relevant repository
- GitHub Discussions (where available)
- Direct mentor contact (listed in project details)

---

## Contributing New Ideas

If you have a project idea that isn't listed here:

1. Open an issue in the relevant repository describing your idea
2. Include technical details, expected outcomes, and estimated scope
3. Discuss with maintainers to refine the proposal
4. If accepted, it may be added to this list

---

We look forward to working with GSoC 2026 contributors. Good luck with your applications!
