---
title: report_a02_prompt
---

# GenAI Utilization Strategy for Dask Cluster Design

---

## Prompt Engineering Overview

<details>
<summary>Strategic Use of GenAI for Distributed Computing Platform Design</summary>

---

- **Objective**: Leverage GenAI tools to design and document a Dask distributed computing cluster for AWS Data Platform.
- **Tools used**: Claude for architecture design, Cursor for infrastructure code, Windsurf for prompt optimization.
- **Scope**: Cover cluster architecture, resource management, monitoring, and integration with A01 platform.
- **Outcome**: A comprehensive technical plan for production-ready Dask cluster supporting `20-30` concurrent users.

#### GenAI Role in Workflow

- **Claude**: Generate cluster architecture designs and performance optimization strategies.
- **Cursor**: Produce Terraform and Ansible configurations for automated deployment.
- **Windsurf**: Refine prompts for specific Dask cluster requirements and AWS integration patterns.

---

#### Success Metrics

- **Efficiency**: Reduce cluster design time by `40%` compared to manual research and planning.
- **Accuracy**: Ensure `100%` compliance with A02 requirements and distributed computing best practices.
- **Integration**: Seamless connection with existing A01 platform infrastructure and services.

---

</details>

---

## Cluster Architecture Prompts

<details>
<summary>Prompts for Designing Scalable Dask Distributed Computing Infrastructure</summary>

---

- **Purpose**: Guide GenAI to design optimal Dask cluster topology for `20-30` concurrent users.
- **Key prompt example**:
  ```text
  Design a production-ready Dask cluster architecture for AWS that supports 20-30 concurrent data engineers. Include scheduler, worker nodes, auto-scaling configuration, and resource management. Integrate with existing AWS Data Platform (A01) including FreeIPA authentication and EFS storage. Provide detailed node specifications, network architecture, and performance optimization strategies.
  ```
- **Claude usage**:
  - Generate cluster topology with hub-and-spoke architecture recommendations.
  - Propose instance types and auto-scaling strategies for cost-effective operations.

#### Prompt Refinement

- **Windsurf optimization**:
  - Original: "Design a Dask cluster for multiple users."
  - Refined: "Design an AWS Dask cluster with scheduler-worker topology, auto-scaling, FreeIPA integration, and resource quotas for 20-30 concurrent data engineers."
- **Outcome**: Specific cluster architecture with detailed component interactions and scaling policies.

---

#### Architecture Validation

- **Cross-checking**: Use Claude to validate scheduler-worker communication patterns and resource allocation.
- **Performance analysis**: GenAI-generated recommendations for memory management and CPU optimization.

---

</details>

---

## Infrastructure as Code Prompts

<details>
<summary>Prompts for Terraform and Ansible Configuration Generation</summary>

---

- **Purpose**: Generate Infrastructure as Code configurations for automated Dask cluster deployment.
- **Key prompt example**:
  ```text
  Generate Terraform configurations for AWS Dask cluster including scheduler EC2 instance, auto-scaling worker group, security groups, and load balancer. Include Ansible playbooks for Dask software installation, FreeIPA integration, and EFS mounting. Use modular design with variables for environment-specific configurations.
  ```
- **Cursor usage**:
  - Generate HCL configurations for AWS resources (EC2, ASG, ALB, security groups).
  - Produce YAML playbooks for Dask installation and configuration management.

#### Code Generation Strategies

- **Modular approach**: Request separate modules for scheduler, workers, and networking components.
- **Error handling**: Include validation and retry logic in infrastructure configurations.
- **Example output refinement**:
  ```text
  Create Terraform auto-scaling group for Dask workers with launch template, scaling policies based on CPU utilization `>70%` scale up, `<30%` scale down, and integration with existing VPC from A01 platform.
  ```

---

#### Configuration Optimization

- **Best practices**: GenAI suggestions for security group rules, IAM policies, and resource tagging.
- **Cost optimization**: Automated recommendations for instance types and scaling thresholds.

---

</details>

---

## Performance Optimization Prompts

<details>
<summary>Prompts for Cluster Performance Tuning and Resource Management</summary>

---

- **Purpose**: Optimize Dask cluster performance for concurrent user workloads and resource efficiency.
- **Key prompt example**:
  ```text
  Provide Dask cluster performance optimization strategies for 20-30 concurrent users including memory management, thread allocation, scheduler tuning, and auto-scaling policies. Include specific configuration parameters for worker memory, CPU allocation, and queue management to prevent resource contention.
  ```
- **Claude usage**:
  - Generate performance tuning recommendations for scheduler and worker configurations.
  - Provide resource allocation strategies and user quota management approaches.

#### Resource Management Prompts

- **Memory optimization**:
  ```text
  Configure Dask worker memory settings for c5.large instances (4GB RAM) to maximize utilization while preventing OOM errors. Include garbage collection policies and memory monitoring recommendations.
  ```
- **Scaling strategy**:
  ```text
  Design auto-scaling policies for Dask worker nodes based on queue depth, CPU utilization, and user session count. Include cool-down periods and maximum cluster size constraints.
  ```

---

#### Monitoring Integration

- **CloudWatch metrics**: GenAI prompts for custom metric collection and dashboard creation.
- **Alerting configuration**: Automated alert rule generation for cluster health monitoring.

---

</details>

---

## User Integration Prompts

<details>
<summary>Prompts for Authentication and Resource Quota Implementation</summary>

---

- **Purpose**: Design user access management and resource allocation for multi-tenant Dask cluster.
- **Key prompt example**:
  ```text
  Design Dask cluster user authentication using FreeIPA LDAP integration with role-based access control. Include per-user resource quotas (4 cores, 8GB RAM maximum), session management, and JupyterHub integration for notebook-based cluster access. Provide configuration examples for Dask Gateway and user isolation.
  ```
- **Implementation focus**: Seamless integration with existing A01 platform authentication infrastructure.

#### Access Control Prompts

- **FreeIPA integration**:
  ```text
  Configure Dask Gateway to authenticate users against FreeIPA LDAP server with group-based permissions. Map data_engineers group to full cluster access and data_analysts group to limited resource quotas.
  ```
- **Resource quotas**:
  ```text
  Implement per-user resource limits in Dask cluster to prevent monopolization. Include maximum cores, memory, and session timeout configurations with fair sharing policies.
  ```

---

#### Session Management

- **JupyterHub integration**: Prompts for notebook-based cluster access with user isolation.
- **Queue management**: FIFO scheduling with priority levels based on user groups.

---

</details>

---

## Documentation Generation Prompts

<details>
<summary>Prompts for Creating Comprehensive Technical Documentation</summary>

---

- **Purpose**: Generate structured documentation following ctx_doc_style standards for Dask cluster implementation.
- **Key prompt example**:
  ```text
  Create comprehensive technical documentation for Dask cluster deployment following ctx_doc_style.md formatting. Include architecture diagrams, deployment procedures, user guides, and operational procedures. Use bullet points, details blocks, and proper markdown formatting for multi-audience accessibility.
  ```
- **Documentation scope**: Technical implementation details accessible to both engineers and business stakeholders.

#### Structure Generation

- **Architecture documentation**: Detailed component descriptions and interaction patterns.
- **Operational procedures**: Maintenance workflows, troubleshooting guides, and monitoring setup.
- **User documentation**: Getting started guides and best practices for cluster usage.

---

#### Stakeholder Communication

- **Technical clarity**: Engineering-focused implementation details with code examples.
- **Business alignment**: Performance benefits and resource utilization explanations for management.

---

</details>

---

## Quality Assurance Prompts

<details>
<summary>Prompts for Validation and Compliance Verification</summary>

---

- **Purpose**: Ensure all GenAI-generated content meets A02 requirements and documentation standards.
- **Validation prompts**: Cross-reference generated architecture with Dask best practices and AWS Well-Architected Framework.
- **Compliance checking**: Verify ctx_doc_style formatting rules and technical accuracy.

#### Review Process

- **Architecture validation**: GenAI review of cluster design for scalability and performance.
- **Code review**: Automated checking of Terraform and Ansible configurations for syntax and best practices.
- **Documentation review**: Compliance verification with style guidelines and technical accuracy.

---

#### Continuous Improvement

- **Feedback loops**: Iterative prompt refinement based on output quality assessment.
- **Template development**: Reusable prompt templates for similar infrastructure design tasks.

---

</details>

---

## Quality Checklist

<details>
<summary>Compliance with Documentation Standards</summary>

---

- [x] YAML front matter present with `report_a02_prompt` title.
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
