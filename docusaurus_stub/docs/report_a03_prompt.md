---
title: report_a03_prompt
---

# GenAI Utilization Strategy for Metaflow ML Pipeline Platform

---

## Prompt Engineering Overview

<details>
<summary>Strategic Use of GenAI for ML Pipeline Platform Design</summary>

---

- **Objective**: Leverage GenAI tools to design and document a Metaflow ML pipeline platform for AWS Data Platform.
- **Tools used**: Claude for ML architecture design, Cursor for infrastructure automation, Windsurf for prompt refinement.
- **Scope**: Cover Metaflow deployment, AWS integration, user workflows, and pipeline templates.
- **Outcome**: A comprehensive ML platform supporting `20-30` data scientists with reproducible, scalable pipelines.

#### GenAI Role in Workflow

- **Claude**: Generate ML platform architecture and pipeline design patterns.
- **Cursor**: Produce Terraform configurations and Metaflow deployment automation.
- **Windsurf**: Optimize prompts for ML-specific requirements and best practices.

---

#### Success Metrics

- **Development velocity**: Reduce ML pipeline development time by `50%` with standardized templates.
- **Platform adoption**: `>90%` of ML team using Metaflow within `2` months of deployment.
- **Reproducibility**: `100%` pipeline reproducibility with versioned artifacts and environments.

---

</details>

---

## ML Architecture Design Prompts

<details>
<summary>Prompts for Metaflow Platform Architecture and AWS Integration</summary>

---

- **Purpose**: Design comprehensive ML platform architecture leveraging Netflix's Metaflow for workflow orchestration.
- **Key prompt example**:
  ```text
  Design a production-ready Metaflow ML platform architecture for AWS supporting 20-30 data scientists. Include Metaflow service deployment, PostgreSQL metadata store, S3 artifact storage, AWS Batch compute integration, and seamless scaling from local development to cloud execution. Integrate with existing A01 platform infrastructure including FreeIPA authentication and VPC networking.
  ```
- **Claude usage**:
  - Generate platform architecture with component relationships and scaling strategies.
  - Design ML workflow patterns and template structures for common use cases.

#### Architecture Optimization

- **Windsurf refinement**:
  - Original: "Design Metaflow platform for ML pipelines."
  - Refined: "Design AWS Metaflow platform with PostgreSQL metadata, S3 artifacts, Batch compute, local-to-cloud scaling, and A01 platform integration for 20-30 users."
- **Component integration**: Detailed interaction patterns between Metaflow service, storage, and compute layers.

---

#### ML Workflow Design

- **Pipeline templates**: GenAI-generated templates for classification, regression, time series, and NLP workflows.
- **Best practices**: Embedded data validation, model evaluation, and deployment patterns in templates.

---

</details>

---

## Infrastructure Automation Prompts

<details>
<summary>Prompts for Terraform and Metaflow Service Deployment</summary>

---

- **Purpose**: Generate Infrastructure as Code for automated Metaflow platform deployment.
- **Key prompt example**:
  ```text
  Generate Terraform configurations for Metaflow platform including RDS PostgreSQL for metadata, S3 buckets for artifacts, AWS Batch job queues, EC2 service instance, and VPC integration. Include Ansible playbooks for Metaflow service installation, database schema initialization, and user environment configuration. Use modular design with environment-specific variables.
  ```
- **Cursor usage**:
  - Generate HCL configurations for AWS services (RDS, S3, Batch, EC2).
  - Produce installation scripts and configuration management playbooks.

#### Service Configuration

- **Metaflow service deployment**:
  ```text
  Create Terraform module for Metaflow service deployment on EC2 with PostgreSQL metadata store, S3 artifact storage, and AWS Batch integration. Include security groups, IAM roles, and monitoring configuration.
  ```
- **Batch compute setup**:
  ```text
  Configure AWS Batch job queues for Metaflow pipeline execution with spot instance support, auto-scaling, and resource limits. Include job definitions for different ML workload types.
  ```

---

#### Database and Storage

- **Metadata store**: RDS PostgreSQL configuration with backup and monitoring.
- **Artifact storage**: S3 bucket with versioning, lifecycle policies, and access control.

---

</details>

---

## ML Pipeline Template Prompts

<details>
<summary>Prompts for Creating Standardized ML Workflow Templates</summary>

---

- **Purpose**: Design reusable ML pipeline templates for common data science use cases.
- **Key prompt example**:
  ```text
  Create Metaflow pipeline templates for classification, regression, time series forecasting, and NLP tasks. Include standardized steps for data ingestion, preprocessing, feature engineering, model training, evaluation, and artifact storage. Embed best practices for data validation, hyperparameter tuning, and model versioning.
  ```
- **Template categories**: Classification, regression, time series, NLP, computer vision workflows.

#### Template Structure Design

- **Classification template**:
  ```text
  Design Metaflow classification pipeline template with data loading, train/test split, feature engineering, model training with cross-validation, performance evaluation, and model artifact storage. Include parameter configuration and logging.
  ```
- **Modular components**: Reusable steps for common ML operations and transformations.

---

#### Best Practices Integration

- **Data validation**: Automated data quality checks and schema validation.
- **Model evaluation**: Standardized metrics calculation and performance comparison.
- **Artifact management**: Automatic model versioning and experiment tracking.

---

</details>

---

## User Workflow Integration Prompts

<details>
<summary>Prompts for Development Environment and User Experience Design</summary>

---

- **Purpose**: Design seamless user workflows from local development to cloud execution.
- **Key prompt example**:
  ```text
  Design Metaflow user workflow supporting local development, testing, and cloud execution scaling. Include workstation setup, Jupyter notebook integration, AWS credential management, and pipeline deployment procedures. Integrate with FreeIPA authentication and provide clear migration paths from local to cloud execution.
  ```
- **User experience focus**: Minimal friction transition between development and production environments.

#### Development Environment

- **Local setup**: Workstation configuration and dependency management.
- **IDE integration**: VS Code and Jupyter notebook support for pipeline development.
- **Credential management**: Secure AWS credential handling with FreeIPA integration.

---

#### Cloud Scaling

- **Execution transition**: Seamless scaling from local testing to cloud compute.
- **Resource management**: Automatic compute resource allocation and cost optimization.

---

</details>

---

## Monitoring and Operations Prompts

<details>
<summary>Prompts for Platform Monitoring and Operational Procedures</summary>

---

- **Purpose**: Design comprehensive monitoring and maintenance strategies for ML platform operations.
- **Key prompt example**:
  ```text
  Design monitoring and alerting strategy for Metaflow ML platform including pipeline execution tracking, resource utilization monitoring, error detection, and performance optimization. Include CloudWatch integration, custom metrics, dashboard creation, and operational procedures for maintenance and troubleshooting.
  ```
- **Operations scope**: Platform health, pipeline performance, and user activity monitoring.

#### Monitoring Configuration

- **Pipeline metrics**: Execution success rates, duration trends, resource consumption.
- **Platform health**: Service availability, database performance, storage utilization.
- **User activity**: Pipeline creation rates, compute usage patterns, error frequencies.

---

#### Operational Procedures

- **Maintenance workflows**: Regular updates, backup procedures, and performance tuning.
- **Troubleshooting guides**: Common issues resolution and debugging procedures.

---

</details>

---

## Documentation Generation Prompts

<details>
<summary>Prompts for Comprehensive ML Platform Documentation</summary>

---

- **Purpose**: Generate structured documentation following ctx_doc_style for ML platform implementation.
- **Key prompt example**:
  ```text
  Create comprehensive Metaflow platform documentation following ctx_doc_style.md formatting. Include architecture overview, user getting started guides, pipeline template documentation, operational procedures, and troubleshooting guides. Use bullet points, details blocks, and proper markdown formatting for technical and business audiences.
  ```
- **Documentation scope**: Technical implementation and user-facing guides.

#### Content Structure

- **Technical documentation**: Architecture details, deployment procedures, and configuration guides.
- **User documentation**: Getting started guides, template usage, and best practices.
- **Operational documentation**: Maintenance procedures and troubleshooting guides.

---

#### Multi-Audience Accessibility

- **Engineering focus**: Detailed technical implementation with code examples.
- **Data science focus**: User-friendly guides and template documentation.
- **Business alignment**: Platform benefits and ROI explanations for stakeholders.

---

</details>

---

## Quality Assurance Prompts

<details>
<summary>Prompts for ML Platform Validation and Best Practices Compliance</summary>

---

- **Purpose**: Ensure ML platform design follows industry best practices and meets A03 requirements.
- **Validation prompts**: Review generated architecture against ML platform best practices and AWS Well-Architected Framework.
- **Compliance checking**: Verify Metaflow configuration and integration patterns.

#### ML Best Practices

- **Reproducibility**: Pipeline versioning and environment consistency validation.
- **Scalability**: Compute resource scaling and cost optimization verification.
- **Security**: Access control and data protection compliance checking.

---

#### Platform Validation

- **Architecture review**: Component integration and scaling strategy assessment.
- **User experience**: Workflow simplicity and adoption barrier analysis.

---

</details>

---

## Quality Checklist

<details>
<summary>Compliance with Documentation Standards</summary>

---

- [x] YAML front matter present with `report_a03_prompt` title.
- [x] Each subsection (###) contains one details block.
- [x] Main sections (##) separated by `---`.
- [x] No separators between ### sections.
- [x] Details blocks start and end with `---`.
- [x] Subsubsections (####) separated by `---`.
- [x] Summary text is descriptive and specific.
- [x] All content formatted as bullet points.
- [x] Block elements (code, text) indented by `2` spaces.
- [x] No numbered headings or bullet points.
- [x] Technical symbols wrapped in backticks (e.g., `20-30`).
- [x] Code blocks include language specification (e.g., `text`, `hcl`).

---

</details>

---
