# Luca Lillo

**Applied AI Engineer & Solution Architect | LLM Agents, RAG and Knowledge Graphs | AI Governance**  
*Psychology-informed governance · Evidence-led evaluation*

I design and build AI systems where decisions must stay explainable, testable and accountable: LLM agents, retrieval-augmented generation (RAG) and knowledge graphs, with human oversight built in from the start.

I have almost 20 years of experience, 18 of them at Enel Group in electricity distribution, a regulated critical infrastructure. From June to September 2026 I was Chief Technology Officer and Head of Research and Innovation at Sistemi & Automazione. Today I run Neuromorphic Inference Lab, my independent open-source initiative, and I am studying for an MSc in Artificial Intelligence at the University of Liverpool.

I am looking for Applied AI Engineer, AI Solution Architect and AI deployment roles.  
**Based in Rome, Italy · Italian (EU) citizen · available immediately · open to relocation within the EU**

## Track record

- **Machine learning in production (Enel Group, 2017–2023).** In a six-person Agile team, I co-built a machine learning platform for predictive maintenance and investment targeting, from requirements to production and adoption. I selected Databricks and personally developed the platform's entire ETL layer (Apache Spark, SQL, Python). The platform contributed to reducing average customer interruption minutes by up to 30% in some territories (internal before-and-after measure).
- **AI governance (2026).** As CTO, I authored the company AI policy (EU AI Act, GDPR and Italian Law 132/2025, prepared with a view to ISO/IEC 42001 certification): risk-based classification of AI use, human oversight and graduated autonomy levels for AI agents. I also authored the guidelines for AI-assisted software development, translating recent academic literature into controls for requirements, testing, traceability and validation.
- **Multi-agent architecture (2026, design stage).** I defined the architecture of a cloud-native graph-intelligence platform: multi-agent AI over an ontology layer and knowledge graph, agents under human supervision, EU AI Act, GDPR and data-sovereignty requirements, and a verification plan set before development.
- **Teams and capability.** As CTO, I established the technology function (5 direct and 15 functional reports). At Enel, I created the unit that trains a technical organisation of 1,500 people; at the end of 2025 it ranked first of the 12 training units in Italy for training hours per person.

## Selected open-source work

### [Enterprise Sovereign AI Decision Matrix](https://github.com/nepryoon/enterprise-sovereign-ai-matrix)

Proof of concept with a [live demo](https://matrix.neuromorphicinference.com/) on synthetic data and one real routed model call. A governed AI workflow that routes the model call to a provider by data-sovereignty rules, requires human approval, records every decision and tracks latency, token use and cost. Next.js, FastAPI, LangGraph, PostgreSQL.

**Scope boundary:** this is a fixed, typed workflow with governed model invocation. It is not a general-purpose multi-agent runtime, a restart-safe distributed executor or a multi-tenant production platform.

### [Enterprise Code Intelligence](https://github.com/nepryoon/eci)

Runnable proof of concept. Graph-RAG over a codebase, with event-driven updates and vector, full-text and graph retrieval. Services in Python, Go and Rust; Neo4j, Qdrant, OpenSearch, Kafka and Debezium, PostgreSQL, Redis.

**Scope boundary:** this is a runnable proof of concept, not a production service.

### [IADF Platform](https://github.com/nepryoon/iadf-platform)

Runnable architecture proof of concept. The core of a policy-governed, AI-assisted software factory: contract-first schemas, an explicit state machine, PostgreSQL leasing, data-residency and cost-aware model routing, and fail-closed controls. Its four-role agent engine (architect, implementer, adversarial reviewer, diagnostician) takes coding agents from specification to tested code.

**Scope boundary:** this is an inspectable governed core and architecture proof of concept, not a complete production software factory.

### Agent demos: [HR onboarding orchestrator](https://github.com/nepryoon/hr-onboarding-orchestrator), [hiring panel](https://github.com/nepryoon/hr-hiring-panel), [innovation board](https://github.com/nepryoon/innovation-board)

Live demos on simulated data. In the onboarding orchestrator, an agent runs an onboarding workflow across simulated systems through tool calls. In the hiring panel and the innovation board, six agents assess a case from different perspectives. In all three, code validates the agents' output and a person decides.

### [MV Grid Fault Risk](https://github.com/nepryoon/mv-grid-fault-risk)

An open-source ML application that connects electricity-distribution domain knowledge with time-based validation, reproducible training and evaluation, MLflow artefacts, Docker packaging and GitHub automation.

**Scope boundary:** the separate live FastAPI demonstration endpoint is rule-based. This is an independent project, not an Enel system, and not evidence of continuous trained-model serving.

### Preprint: *Can LLM Agents Care About the World?* (2026)

A formal control framework in which an LLM agent judges improvement or deterioration from an external, auditable indicator. Theoretical preprint with public simulation code; not peer reviewed. [ResearchGate, DOI 10.13140/RG.2.2.25820.55685](https://doi.org/10.13140/RG.2.2.25820.55685)

## Psychology + AI: an engineering lens for multi-agent systems

Formal training in Psychological Sciences gives me a complementary, non-anthropomorphic lens on authority bias, conformity, groupthink, social loafing and confidence dominance. I do not assume that LLM agents have human motives. I translate these concepts into observable failure hypotheses, structural controls and evaluation designs.

The designs I have proposed, all testable, cover:

- separating procedural from epistemic authority;
- structured dissent, falsifiable objections, blind review and external verification;
- role permutation, agent ablation and adversarial-leader testing;
- compute-equivalent single-agent baselines;
- measures of task correctness, dissent robustness, cascading error, traceability and cost.

This work currently supports conceptual architecture and evaluation design. Proposed controls and measures stay labelled as proposals until they have been implemented and benchmarked.

## Practice and stack

- **Architecture:** governed integration, model routing, retrieval, APIs, event-driven data flows and human oversight.
- **Agentic governance:** roles, permissions, explicit state, structured dissent, external evidence, traceability and fail-closed controls.
- **Evaluation:** explicit assumptions, success and failure criteria set in advance, telemetry, and validation against observed results.
- **Stack:** Python, SQL, TypeScript; FastAPI; LangGraph, LangChain, MCP; Qdrant, OpenSearch, Neo4j; PostgreSQL, Redis, Kafka and Debezium; Databricks, Apache Spark, MLflow; Docker, Kubernetes, Terraform, AWS, GitHub Actions; Claude and Codex as daily coding agents.

## Research-led method

**Question → literature review → explicit assumptions → success and failure criteria → instrumentation → validation.** I separate evidence, inference and hypothesis, then revise architectural decisions against observed results and documented limitations.

## Background

- **Chief Technology Officer & Head of Research and Innovation**, Sistemi & Automazione S.p.A., Rome — June 2026 – September 2026.
- **E-Distribuzione S.p.A. (Enel Group)** — May 2008 – June 2026: Head of Training Unit; Senior Project Manager | Digital Transformation Lead (monitored Grid Blue Sky, Enel Grids' global digitalisation programme); Innovation & Agile Ambassador | Senior System Designer; Project Manager.
- **MSc Artificial Intelligence**, University of Liverpool — in progress, expected August 2027; current average in the Distinction band.
- **Postgraduate Certificate in Data Science and Artificial Intelligence**, University of Liverpool — academic requirements completed; formal award pending.
- **MSc Management and Innovation (LM-77)**, Universitas Mercatorum.
- **BSc Psychological Sciences and Techniques**, Universitas Mercatorum.

## Transparency

Neuromorphic Inference Lab is an independent open-source initiative. I define architectures and specifications, direct AI-assisted implementation with coding agents (Claude, Codex), review code and tests, and remain accountable for validation, limitations and deployment decisions. The repositories demonstrate inspectable patterns and bounded proofs of concept. They are not presented as customer production platforms, validated research frameworks or evidence of years operating autonomous multi-agent runtimes at scale.

## Connect

- [LinkedIn](https://www.linkedin.com/in/nepryoon)
- [Website](https://www.neuromorphicinference.com)
- [ORCID](https://orcid.org/0009-0003-1290-1279)
- [Email](mailto:lilloluca@gmail.com)
