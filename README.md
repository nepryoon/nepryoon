# Luca Lillo

**AI Architect & Generative AI Engineer | Ontology & Knowledge Graph Architecture | Governed AI Agents**  
*Psychology-informed modelling and governance · Evidence-led evaluation*

I design AI systems that keep AI decisions explainable, testable and accountable, and I build their core components. In these systems, AI agents work on structured knowledge under explicit rules: they reach data only through typed, policy-filtered queries and tools, with human oversight built in from the start.

I have almost 20 years of experience, 18 of them at Enel Group, and I have led teams since 2007. From June to September 2026 I was Chief Technology Officer and Head of Research and Innovation at Sistemi & Automazione. Today I run Neuromorphic Inference Lab, my independent software research initiative. At the University of Liverpool I hold a Postgraduate Certificate in Data Science and Artificial Intelligence, and I am studying for an MSc in Artificial Intelligence.

I am looking for AI Architect, Generative AI Engineer and Ontology or Knowledge Graph Architect roles.  
**Based in Rome, Italy · Italian (EU) citizen · available immediately · open to relocation and to remote roles**

## Track record

- **Machine learning in production (Enel Group, 2017–2023).** In a six-person Agile team, I co-built and maintained for six years a machine learning platform in production on AWS for predictive maintenance and investment targeting, from requirements to production, adoption and ongoing operation. I selected Databricks, personally developed the platform's entire ETL layer (Apache Spark, SQL, Python) and did the modelling: feature selection, XGBoost training and evaluation, and thresholds for operational use. The platform contributed to reducing average customer interruption minutes by up to 30% in some territories (internal before-and-after measure).
- **RAG system in production, built as CTO (2026).** I designed from scratch, deployed into production and maintained an internal retrieval-augmented generation (RAG) system for the development team: it indexed all the code the company managed, and developers used it to ask how about 500 components worked and depended on each other.
- **Platforms in production, managed as CTO (2026).** I managed two platforms in production: a graph-analysis platform with a multi-agent tool that users could query about the graph data, and a due-diligence platform with about 60 connectors to different data sources. I handled their production issues end to end. Both platforms existed before I joined.
- **AI governance (2026).** As CTO, I authored the company AI policy (EU AI Act, GDPR and Italian Law 132/2025, prepared with a view to ISO/IEC 42001 certification): risk-based classification of AI use, human oversight and graduated autonomy levels for AI agents. I also authored the guidelines for AI-assisted software development, with controls for requirements, testing, traceability and validation, and led their adoption with HR.
- **Multi-agent architecture (2026, design stage).** I defined the architecture of a cloud-native graph-intelligence platform: AI agents under human supervision, EU AI Act, GDPR and data-sovereignty requirements, and a verification plan set before development.
- **Teams and capability.** As CTO, I established the technology function (5 direct and 15 functional reports). At Enel, I created the unit that trains a technical organisation of 1,500 people; at the end of 2025 it ranked first of the 12 training units in Italy for training hours per person.

## Selected public work

### [OCOR](https://github.com/nepryoon/ocor)

In development: a runnable implementation on a synthetic scenario; qualification in progress. OCOR (Operational Causal Ontology Runtime) is a vendor-neutral semantic core. It connects ontology definitions, evidence, governed decisions and controlled actions, so that software and AI agents work against explicit contracts and authority limits.

- **Designed:** an ontology-as-code metamodel, with modules and imports pinned by version and digest, typed objects and interfaces, n-ary links with named roles, constraints, bitemporal data, security markings, and contracts for named queries, functions, actions, events and MCP tools; a provenance model that extends W3C PROV-O.
- **Built:** the ontology compiler. It type-checks YAML or JSON ontology sources, rejects unresolved or cyclic references, and turns each ontology version into a deterministic, content-addressed canonical model with a semantic diff and a compatibility class; a breaking change is rejected without a migration plan.
- **Built:** governed access for agents: a named-query gateway that checks policy before any read, and an agent kernel with typed tools, budgets and a kill switch. In role-based multi-agent runs, dissent is recorded and the coordinator cannot suppress it.
- **Built:** governed agent memory (working, episodic, semantic and procedural kinds) with structured, full-text, vector and hybrid retrieval, consolidation that keeps conflicting claims apart, and scoped deletion.
- **Built:** a causal scenario runtime on structural causal models that estimates intervention effects and abstains when an effect is not identifiable.
- **Prototyped:** the W3C boundary on Apache Jena / Fuseki: RDF and JSON-LD publication with SHACL Core validation, and a SPARQL adapter.

**Scope boundary:** this is an implementation in development, not a production system. The repository's own records state that qualification is in progress and that runtime conformance and production readiness are not established.

### [Enterprise Code Intelligence](https://github.com/nepryoon/eci)

Runnable proof of concept. Graph-RAG over a codebase, with event-driven updates and vector, full-text and graph retrieval. Services in Python, Go and Rust; Neo4j, Qdrant, OpenSearch, Kafka and Debezium, PostgreSQL, Redis.

**Scope boundary:** this is a runnable proof of concept, not a production service.

### [Enterprise Sovereign AI Decision Matrix](https://github.com/nepryoon/enterprise-sovereign-ai-matrix)

Proof of concept with a [live demo](https://matrix.neuromorphicinference.com/) on synthetic data and one real routed model call. A governed AI workflow that routes the model call to a provider by data-sovereignty rules, requires human approval, records every decision and tracks latency, token use and cost. Next.js, FastAPI, LangGraph, PostgreSQL.

**Scope boundary:** this is a fixed, typed workflow with governed model invocation. It is not a general-purpose multi-agent runtime, a restart-safe distributed executor or a multi-tenant production platform.

### [IADF Platform](https://github.com/nepryoon/iadf-platform)

Runnable architecture proof of concept. The core of a policy-governed, AI-assisted software factory: contract-first schemas, an explicit state machine, PostgreSQL leasing, data-residency and cost-aware model routing, and fail-closed controls. Its four-role agent engine (architect, implementer, adversarial reviewer, diagnostician) takes coding agents from specification to tested code.

**Scope boundary:** this is an inspectable governed core and architecture proof of concept, not a complete production software factory.

### Agent demos: [HR onboarding orchestrator](https://github.com/nepryoon/hr-onboarding-orchestrator), [hiring panel](https://github.com/nepryoon/hr-hiring-panel), [innovation board](https://github.com/nepryoon/innovation-board)

Live demos on simulated data. In the onboarding orchestrator, an agent runs an onboarding workflow across simulated systems through tool calls. In the hiring panel and the innovation board, six agents assess a case from different perspectives. In all three, code validates the agents' output and a person decides.

### [MV Grid Fault Risk](https://github.com/nepryoon/mv-grid-fault-risk)

An open-source ML application: fault-risk scoring for medium-voltage lines, with time-based validation, reproducible training and evaluation, MLflow artefacts, Docker packaging and GitHub automation.

**Scope boundary:** the separate live FastAPI demonstration endpoint is rule-based. This is an independent project, not an Enel system, and not evidence of continuous trained-model serving.

### Preprint: *Can LLM Agents Care About the World?* (2026)

A formal control framework in which an LLM agent judges improvement or deterioration from an external, auditable indicator. Theoretical preprint with public [simulation code](https://github.com/nepryoon/ehd-simulations); not peer reviewed. [ResearchGate, DOI 10.13140/RG.2.2.25820.55685](https://doi.org/10.13140/RG.2.2.25820.55685)

## Research direction: Neuromorphic Inference

"Neuromorphic Inference" is the name of my lab and of a research direction: brain-inspired principles for how AI systems activate, connect and update structured knowledge, starting with context-dependent activation and relevance propagation over knowledge graphs. It is software research: no spiking neural networks and no neuromorphic hardware. These mechanisms are not implemented yet; OCOR builds the components they would act on.

## Psychology + AI: an engineering lens for ontologies and multi-agent systems

Formal training in Psychological Sciences shapes two parts of my work.

**Ontologies.** An ontology is a model of how people divide a domain into concepts. Psychology helps me with the human side of that model: how people form categories, why two teams give different meanings to the same word, and how to check that different people apply a definition in the same way.

**Multi-agent systems.** Psychology gives me a complementary, non-anthropomorphic lens on authority bias, conformity, groupthink, social loafing and confidence dominance. I do not assume that LLM agents have human motives. I translate these concepts into observable failure hypotheses, structural controls and evaluation designs.

The designs I have proposed, all testable, cover:

- separating procedural from epistemic authority;
- structured dissent, falsifiable objections, blind review and external verification;
- role permutation, agent ablation and adversarial-leader testing;
- compute-equivalent single-agent baselines;
- measures of task correctness, dissent robustness, cascading error, traceability and cost.

This work currently supports conceptual architecture and evaluation design. Proposed controls and measures stay labelled as proposals until they have been implemented and benchmarked.

## Practice and stack

- **Ontology engineering:** ontology-as-code, property-graph data modelling, provenance modelling, and the ontology as a governance layer for data, queries and actions.
- **Knowledge graphs and W3C standards:** Neo4j with Cypher (Enterprise Code Intelligence); Apache Jena / Fuseki with RDF, JSON-LD, SHACL Core and SPARQL (OCOR's W3C boundary, prototype); W3C PROV-O (OCOR provenance model, designed).
- **Architecture:** governed integration, model routing, retrieval, APIs, event-driven data flows and human oversight.
- **Agentic governance:** roles, permissions, explicit state, structured dissent, external evidence, traceability and fail-closed controls.
- **Evaluation:** explicit assumptions, success and failure criteria set in advance, telemetry, and validation against observed results.
- **Stack:** Python, SQL, TypeScript; FastAPI; LangGraph, LangChain, MCP; Qdrant, OpenSearch; PostgreSQL, Redis, Kafka and Debezium; Databricks, Apache Spark, MLflow, DVC, Weights & Biases; Docker, Kubernetes, Terraform, AWS, GitHub Actions; Claude and Codex as daily coding agents.

## Research-led method

**Question → literature review → explicit assumptions → success and failure criteria → instrumentation → validation.** I separate evidence, inference and hypothesis, then revise architectural decisions against observed results and documented limitations.

## Background

- **Chief Technology Officer & Head of Research and Innovation**, Sistemi & Automazione S.p.A., Rome — June 2026 – September 2026.
- **E-Distribuzione S.p.A. (Enel Group)** — May 2008 – June 2026: Head of Training Unit & Trainer; Senior Project Manager & Digital Transformation Lead (monitored Grid Blue Sky, Enel Grids' global digitalisation programme); Innovation & Agile Ambassador | Senior System Designer; Technical Project Manager.
- **Junior Production Manager**, VRM — April 2007 – April 2008: production of aluminium chassis and engine components for motorcycles and cars; configuration of CNC machines and robots; night-shift supervisor on alternate weeks.
- **MSc Artificial Intelligence**, University of Liverpool — in progress, expected August 2027; current average in the Distinction band.
- **Postgraduate Certificate in Data Science and Artificial Intelligence**, University of Liverpool — awarded.
- **MSc Management and Innovation (LM-77)**, Universitas Mercatorum.
- **BSc Psychological Sciences and Techniques**, Universitas Mercatorum.

## Transparency

Neuromorphic Inference Lab is my independent software research initiative. Its repositories are public; only some of them carry an open-source licence. I define architectures and specifications, direct AI-assisted implementation with coding agents (Claude, Codex), read and review the code and tests, and remain accountable for validation, limitations and deployment decisions. The repositories demonstrate inspectable patterns, bounded proofs of concept and one implementation in development (OCOR). They are not presented as customer production platforms, validated research frameworks or evidence of years operating autonomous multi-agent runtimes at scale.

## Connect

- [LinkedIn](https://www.linkedin.com/in/nepryoon)
- [Website](https://www.neuromorphicinference.com)
- [ORCID](https://orcid.org/0009-0003-1290-1279)
- [Email](mailto:lilloluca@gmail.com)
