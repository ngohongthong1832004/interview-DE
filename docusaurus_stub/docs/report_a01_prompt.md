---
title: report_a01_prompt
---

# GenAI Utilization Strategy

---

## Prompt Engineering Overview

<details>
<summary>Strategic Use of GenAI for Technical Planning</summary>

---

- **Objective**: Leverage GenAI tools to design and document the AWS Data Platform for task A01 efficiently.  
- **Tools used**: Claude for architectural brainstorming, Cursor for code generation, Windsurf for prompt refinement.  
- **Scope**: Cover infrastructure design, automation strategies, and documentation creation.  
- **Outcome**: A comprehensive, actionable technical plan meeting ctx_doc_style standards.  

#### GenAI Role in Workflow

- **Claude**: Generate initial architecture drafts and validate component interactions.  
- **Cursor**: Produce Terraform and Ansible code snippets with error checking.  
- **Windsurf**: Optimize prompts for precise, context-aware GenAI responses.  

---

#### Success Metrics

- **Efficiency**: Reduce planning time by `30%` compared to manual design.  
- **Accuracy**: Ensure `100%` compliance with A01 requirements and ctx_doc_style.  
- **Clarity**: Produce documentation understandable by both engineers and stakeholders.  

---

</details>

---

## Prompt Design for Architecture

<details>
<summary>Prompts for Infrastructure Design and Component Selection</summary>

---

- **Purpose**: Guide GenAI to propose a scalable AWS architecture for `20-30` users.  
- **Key prompt example**:  
  ```text
  Design a production-ready AWS Data Platform for 20-30 data engineers. Include EC2, EFS, FreeIPA, and IAM with Terraform and Ansible automation. Provide a detailed architecture with component interactions, network design, and security measures. Ensure compliance with ctx_doc_style.md formatting.
  ```  
- **Claude usage**:  
  - Input prompt to generate VPC, EC2, and EFS configurations.  
  - Refine output to ensure private subnets and security group rules.  

#### Prompt Refinement

- **Windsurf optimization**:  
  - Original: "Design an AWS platform with EC2 and storage."  
  - Refined: "Design a secure AWS Data Platform with EC2, EFS, and FreeIPA, including network isolation and IaC."  
- **Outcome**: Specific, enterprise-level architecture with no manual AWS console usage.  

---

#### Validation Process

- **Cross-checking**: Use Claude to verify component compatibility (e.g., EFS with EC2).  
- **Stakeholder alignment**: Ensure architecture addresses both technical and business needs.  

---

</details>

---

## Prompt Design for IaC

<details>
<summary>Prompts for Terraform and Ansible Code Generation</summary>

---

- **Purpose**: Automate infrastructure provisioning and configuration using GenAI.  
- **Key prompt example**:  
  ```text
  Generate Terraform code for an AWS VPC with two private subnets, an EFS file system, and IAM roles for data engineers. Include modular design and ctx_doc_style-compliant formatting. Provide Ansible playbooks to configure FreeIPA and mount EFS on EC2 instances.
  ```  
- **Cursor usage**:  
  - Generate HCL code for Terraform modules (VPC, EFS, IAM).  
  - Produce YAML playbooks for Ansible tasks (FreeIPA setup, EFS mounting).  

#### Code Optimization

- **Error handling**: Cursor suggests validations (e.g., EFS encryption, IAM policy syntax).  
- **Modularity**: Split Terraform into reusable modules (e.g., `vpc`, `storage`).  
- **Example output**:  
  ```hcl
  module "efs" {
    source         = "./modules/efs"
    creation_token = "data-platform-efs"
    encrypted      = true
  }
  ```  

---

#### Validation Process

- **Syntax check**: Use Cursor to validate HCL and YAML code.  
- **Compliance**: Ensure code blocks are indented `2` spaces per ctx_doc_style.  

---

</details>

---

## Prompt Design for Documentation

<details>
<summary>Prompts for Creating ctx_doc_style-Compliant Reports</summary>

---

- **Purpose**: Produce structured, multi-audience documentation using GenAI.  
- **Key prompt example**:  
  ```text
  Create a Markdown report for AWS Data Platform (A01) following ctx_doc_style.md. Include sections for architecture, access control, IaC, deployment, and operations. Use bullet points, details blocks with descriptive summaries, and proper --- separators. Ensure all content is clear for engineers and stakeholders.
  ```  
- **Claude usage**:  
  - Generate initial report structure with correct header hierarchy.  
  - Populate details blocks with bullet-pointed content.  

#### Formatting Standards

- **Details blocks**: Start/end with `---`, use action-oriented summaries (e.g., "Detailed System Components").  
- **Bullet points**: Break content into single-idea bullets for clarity.  
- **Block indentation**: Code and YAML blocks indented `2` spaces.  

---

#### Stakeholder Accessibility

- **Technical clarity**: Use standardized terminology (e.g., `EC2`, `EFS`) for engineers.  
- **Business alignment**: Explain benefits (e.g., scalability, security) for non-technical readers.  

---

</details>

---

## Prompt Optimization Techniques

<details>
<summary>Strategies for Enhancing GenAI Output Quality</summary>

---

- **Context injection**: Include A01 requirements and ctx_doc_style rules in prompts.  
- **Iterative refinement**: Use Windsurf to rephrase vague prompts for specificity.  
- **Example-driven prompts**: Provide sample outputs (e.g., Terraform module) to guide GenAI.  
- **Feedback loops**: Review Claude/Cursor outputs, adjust prompts for missing details.  

#### Example Refinement

- **Initial prompt**: "Write a report for AWS platform."  
- **Refined prompt**:  
  ```text
  Generate a ctx_doc_style-compliant Markdown report for A01 AWS Data Platform. Include architecture diagrams, Terraform/Ansible plans, and a deployment timeline. Use details blocks, bullet points, and proper separators.
  ```  

---

#### Quality Assurance

- **Checklist validation**: Ensure all ctx_doc_style rules (e.g., no numbered lists, `---` usage) are met.  
- **Consistency**: Standardize terms (e.g., `FreeIPA`, `EFS`) across all GenAI outputs.  

---

</details>

---

## Quality Checklist

<details>
<summary>Compliance with Documentation Standards</summary>

---

- [x] YAML front matter present with `report_a01_prompt` title.  
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
- [x] Code blocks include language specification (e.g., `hcl`, `text`).  

---

</details>

---