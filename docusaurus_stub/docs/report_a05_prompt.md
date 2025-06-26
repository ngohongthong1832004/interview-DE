---
title: report_a05_prompt
---

# GenAI Utilization Strategy for Real-Time Streaming Pipeline

---

## Prompt Engineering Overview

<details>
<summary>Strategic Use of GenAI for Streaming Data Architecture Design</summary>

---

- **Objective**: Leverage GenAI tools to design and document a real-time streaming data pipeline from AppsFlyer to business dashboards.
- **Tools used**: Claude for streaming architecture design, Cursor for infrastructure automation, Windsurf for prompt optimization.
- **Scope**: Cover data ingestion, stream processing, aggregation layers, and dashboard integration.
- **Outcome**: A production-ready streaming pipeline with `&lt;5` second latency and `&gt;1M` events per hour capacity.

#### GenAI Role in Workflow

- **Claude**: Generate streaming architecture patterns and real-time processing strategies.
- **Cursor**: Produce Terraform configurations for AWS streaming services and Flink applications.
- **Windsurf**: Refine prompts for stream processing optimization and performance tuning.

---

#### Success Metrics

- **Latency optimization**: Achieve `&lt;5` second end-to-end data latency through GenAI-optimized architecture.
- **Throughput maximization**: Handle `&gt;1M` events per hour with auto-scaling recommendations.
- **Reliability design**: `99.9%` pipeline uptime with GenAI-designed fault tolerance patterns.

---

</details>

---

## Streaming Architecture Design Prompts

<details>
<summary>Prompts for End-to-End Real-Time Data Pipeline Architecture</summary>

---

- **Purpose**: Design comprehensive streaming data architecture for AppsFlyer event processing and business analytics.
- **Key prompt example**:
  ```text
  Design a production-ready real-time streaming data pipeline for AppsFlyer events with `&lt;5` second latency and `&gt;1M` events/hour capacity. Include Kinesis Data Streams for ingestion, Apache Flink for stream processing, S3 data lake for storage, multi-level aggregations (hourly/daily), and QuickSight dashboard integration. Design Lambda architecture with fault tolerance and auto-scaling.
  ```
- **Claude usage**:
  - Generate Lambda architecture with stream and batch processing layers.
  - Design data flow patterns and real-time aggregation strategies.

#### Architecture Optimization

- **Windsurf refinement**:
  - Original: "Design streaming pipeline for real-time data."
  - Refined: "Design AWS Lambda architecture streaming pipeline: Kinesis ingestion → Flink processing → S3 storage → Multi-level aggregations → QuickSight dashboards with `&lt;5` second latency and `&gt;1M` events/hour."
- **Performance focus**: Latency optimization and throughput maximization strategies.

---

#### Data Flow Design

- **Stream processing patterns**: Event-driven architecture with real-time transformations.
- **Storage strategy**: Hot, warm, and cold data tiers for cost-effective analytics.

---

</details>

---

## Stream Processing Engine Prompts

<details>
<summary>Prompts for Apache Flink Application Design and Optimization</summary>

---

- **Purpose**: Design high-performance Flink applications for real-time event processing and aggregations.
- **Key prompt example**:
  ```text
  Design Apache Flink streaming application for AppsFlyer event processing including data enrichment, validation, real-time aggregations with time windows, and state management. Include parallelism configuration for `&gt;1M` events/hour, checkpointing strategy, and error handling. Optimize for low latency and high throughput with resource allocation recommendations.
  ```
- **Flink optimization**: Parallelism, state management, and performance tuning strategies.

#### Processing Logic Design

- **Event processing pipeline**:
  ```text
  Create Flink job structure for AppsFlyer events: ingestion → enrichment → validation → time-windowed aggregations → multi-sink output (S3 + Redis). Include parallelism configuration and state backend optimization.
  ```
- **Aggregation strategies**: Tumbling windows, sliding windows, and session windows for different business metrics.

---

#### Performance Optimization

- **Resource allocation**: CPU, memory, and parallelism recommendations for high throughput.
- **State management**: RocksDB configuration and checkpointing strategies.

---

</details>

---

## Data Ingestion Infrastructure Prompts

<details>
<summary>Prompts for Kinesis and API Gateway Configuration</summary>

---

- **Purpose**: Design scalable data ingestion infrastructure for AppsFlyer webhook and API integration.
- **Key prompt example**:
  ```text
  Design AWS data ingestion infrastructure for AppsFlyer events using Kinesis Data Streams with auto-scaling, API Gateway for webhook endpoints, Lambda for data validation, and error handling with dead letter queues. Include shard management, backpressure handling, and monitoring configuration for `&gt;100K` events/minute capacity.
  ```
- **Ingestion optimization**: Throughput maximization and error handling strategies.

#### Kinesis Configuration

- **Stream specifications**:
  ```text
  Configure Kinesis Data Streams for AppsFlyer events with optimal shard count, retention period, and monitoring. Include auto-scaling policies based on incoming record rate and consumer lag metrics.
  ```
- **Producer optimization**: Batch processing and compression strategies for high throughput.

---

#### API Integration

- **Webhook handling**: Secure API Gateway endpoints with authentication and rate limiting.
- **Data validation**: Lambda-based schema validation and quality checks.

---

</details>

---

## Aggregation Layer Design Prompts

<details>
<summary>Prompts for Multi-Level Data Aggregation Implementation</summary>

---

- **Purpose**: Design efficient hourly and daily aggregation strategies for business analytics.
- **Key prompt example**:
  ```text
  Design multi-level data aggregation strategy for AppsFlyer events including real-time hourly aggregations for operational dashboards and daily aggregations for business intelligence. Include aggregation logic for install counts, conversion rates, revenue metrics, and user segmentation. Optimize storage partitioning and query performance.
  ```
- **Aggregation optimization**: Time-window strategies and storage optimization.

#### Aggregation Logic

- **Hourly aggregations**:
  ```text
  Design Flink hourly aggregation logic for AppsFlyer events: install counts by campaign/country, conversion rates, revenue per channel, and user acquisition costs. Include late data handling and exactly-once processing guarantees.
  ```
- **Daily aggregations**: Business intelligence metrics and cross-platform attribution analysis.

---

#### Storage Optimization

- **Partitioning strategy**: Time-based partitioning for efficient query performance.
- **Data formats**: Parquet optimization for analytics workloads.

---

</details>

---

## Dashboard Integration Prompts

<details>
<summary>Prompts for Real-Time Analytics Dashboard Implementation</summary>

---

- **Purpose**: Design business dashboard integration with real-time data refresh capabilities.
- **Key prompt example**:
  ```text
  Design QuickSight dashboard integration for real-time AppsFlyer analytics with `&lt;1` minute refresh intervals. Include executive dashboards for KPIs, operational dashboards for real-time monitoring, and detailed analytics for campaign performance. Design data connectivity with ElastiCache Redis for real-time metrics and S3 for historical analysis.
  ```
- **Dashboard optimization**: Real-time data connectivity and user experience design.

#### Dashboard Architecture

- **Real-time connectivity**: ElastiCache Redis integration for sub-minute dashboard updates.
- **Historical analysis**: S3-based datasets with optimized refresh strategies.

---

#### User Experience

- **Multi-tier dashboards**: Executive, operational, and analytical views for different user needs.
- **Mobile optimization**: Responsive design for tablet and mobile access.

---

</details>

---

## Monitoring and Performance Prompts

<details>
<summary>Prompts for Pipeline Monitoring and Performance Optimization</summary>

---

- **Purpose**: Design comprehensive monitoring and alerting for streaming pipeline operations.
- **Key prompt example**:
  ```text
  Design monitoring and alerting strategy for real-time streaming pipeline including data throughput tracking, processing latency measurement, error rate monitoring, and resource utilization analysis. Include CloudWatch custom metrics, Grafana dashboards, and multi-level alerting with escalation procedures for technical and business stakeholders.
  ```
- **Monitoring scope**: Technical performance and business KPI tracking.

#### Performance Metrics

- **Technical monitoring**: Latency, throughput, error rates, and resource utilization.
- **Business monitoring**: Data quality, dashboard freshness, and user engagement metrics.

---

#### Alerting Strategy

- **Multi-level alerts**: Technical alerts for engineering teams and business alerts for stakeholders.
- **Escalation procedures**: Automated escalation for critical pipeline failures.

---

</details>

---

## Cost Optimization Prompts

<details>
<summary>Prompts for Streaming Infrastructure Cost Management</summary>

---

- **Purpose**: Design cost-effective streaming architecture with automatic scaling and resource optimization.
- **Key prompt example**:
  ```text
  Design cost optimization strategy for real-time streaming pipeline including Kinesis shard auto-scaling, Flink resource right-sizing, S3 storage lifecycle policies, and reserved capacity planning. Include cost monitoring, budget alerts, and optimization recommendations for sustained operations.
  ```
- **Cost focus**: Pay-per-use optimization and reserved capacity planning.

#### Resource Optimization

- **Auto-scaling**: Dynamic resource allocation based on workload patterns.
- **Reserved capacity**: Cost optimization for predictable workloads.

---

#### Cost Monitoring

- **Budget controls**: Automated cost tracking and alert thresholds.
- **Optimization recommendations**: Regular cost review and right-sizing suggestions.

---

</details>

---

## Documentation Generation Prompts

<details>
<summary>Prompts for Streaming Pipeline Documentation Creation</summary>

---

- **Purpose**: Generate comprehensive technical documentation following ctx_doc_style standards.
- **Key prompt example**:
  ```text
  Create comprehensive real-time streaming pipeline documentation following ctx_doc_style.md formatting. Include architecture overview, data flow diagrams, deployment procedures, monitoring setup, and operational guides. Use bullet points, details blocks, and proper markdown formatting for technical and business audiences.
  ```
- **Documentation scope**: Technical implementation and operational procedures.

#### Content Structure

- **Architecture documentation**: Component relationships and data flow patterns.
- **Operational guides**: Deployment, monitoring, and troubleshooting procedures.
- **User documentation**: Dashboard usage and business metric explanations.

---

#### Multi-Audience Accessibility

- **Technical focus**: Detailed implementation guides with code examples.
- **Business focus**: KPI explanations and dashboard usage guides.

---

</details>

---

## Quality Checklist

<details>
<summary>Compliance with Documentation Standards</summary>

---

- [x] YAML front matter present with `report_a05_prompt` title.
- [x] Each subsection (###) contains one details block.
- [x] Main sections (##) separated by `---`.
- [x] No separators between ### sections.
- [x] Details blocks start and end with `---`.
- [x] Subsubsections (####) separated by `---`.
- [x] Summary text is descriptive and specific.
- [x] All content formatted as bullet points.
- [x] Block elements (code, text) indented by `2` spaces.
- [x] No numbered headings or bullet points.
- [x] Technical symbols wrapped in backticks (e.g., `&lt;5`).
- [x] Code blocks include language specification (e.g., `text`, `java`).

---

</details>

---
