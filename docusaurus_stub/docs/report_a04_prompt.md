---
title: report_a04_prompt
---

# GenAI Utilization Strategy for A04

---

## Prompt Engineering Overview

<details>
<summary>Strategic Application of GenAI for Tracking System Analysis</summary>

---

- **Objective**: Use GenAI tools to analyze and document web/app tracking systems for task A04 efficiently.  
- **Tools used**: Claude for conceptual analysis, Cursor for code and diagram generation, Windsurf for prompt optimization.  
- **Scope**: Cover custom tracking design, AppsFlyer evaluation, event flow visualization, and implementation planning.  
- **Outcome**: A ctx_doc_style-compliant report guiding stakeholders on tracking solution choices.  

#### GenAI Role in Workflow

- **Claude**: Generate detailed comparisons between custom and third-party tracking systems.  
- **Cursor**: Produce JSON payloads, JavaScript SDK snippets, and Mermaid diagrams.  
- **Windsurf**: Refine prompts to ensure precise, context-specific GenAI outputs.  

---

#### Success Metrics

- **Efficiency**: Reduce analysis time by `25%` compared to manual research.  
- **Comprehensiveness**: Address all A04 requirements, including technical and business perspectives.  
- **Clarity**: Ensure documentation is accessible to engineers and non-technical stakeholders.  

---

</details>

---

## Prompt Design for System Analysis

<details>
<summary>Prompts for Custom Tracking and AppsFlyer Evaluation</summary>

---

- **Purpose**: Guide GenAI to analyze custom tracking systems and AppsFlyer’s capabilities.  
- **Key prompt example**:  
  ```text
  Analyze the design of a custom web/app tracking system for app installs, conversions, and user events. Compare it with AppsFlyer’s features, focusing on scalability, accuracy, privacy compliance, and maintenance. Provide technical details, challenges, and benefits in ctx_doc_style-compliant Markdown.
  ```  
- **Claude usage**:  
  - Generate technical breakdowns of tracking link mechanisms and attribution logic.  
  - Produce comparative analysis of custom vs. AppsFlyer solutions.  

#### Prompt Refinement

- **Windsurf optimization**:  
  - Original: "Compare custom tracking with AppsFlyer."  
  - Refined: "Provide a detailed comparison of a custom tracking system (SDK, API, database) vs. AppsFlyer, including scalability, error rates, and compliance challenges."  
- **Outcome**: Precise analysis addressing A04’s key questions (e.g., attribution, data collection).  

---

#### Validation Process

- **Accuracy check**: Use Claude to verify technical details (e.g., AppsFlyer’s `<1%` error rate).  
- **Stakeholder alignment**: Ensure content is clear for marketing teams and engineers.  

---

</details>

---

## Prompt Design for Event Flow Visualization

<details>
<summary>Prompts for Generating Tracking Flow Diagrams</summary>

---

- **Purpose**: Create Mermaid diagrams to visualize tracking data flows.  
- **Key prompt example**:  
  ```text
  Generate Mermaid flow diagrams showing the event flow for a custom tracking system and AppsFlyer. Include steps from user ad click to marketing report generation. Format diagrams in ctx_doc_style-compliant Markdown with 2-space indentation.
  ```  
- **Cursor usage**:  
  - Produce Mermaid syntax for custom and AppsFlyer event flows.  
  - Example output:  
    ```mermaid
    graph TD
      A[User Clicks Ad] --> B[Tracking Link]
      B --> C[App Install]
      C --> D[AppsFlyer SDK]
      D --> E[AppsFlyer API]
      E --> F[AppsFlyer Servers]
      F --> G[Dashboard/Analytics]
      G --> H[Marketing Report]
    ```  

#### Diagram Optimization

- **Clarity**: Ensure diagrams are simple, with `7-8` steps per flow.  
- **Compliance**: Indent Mermaid blocks `2` spaces per ctx_doc_style.  
- **Validation**: Cross-check flows with A04 requirements (e.g., SDK-to-API interaction).  

---

#### Stakeholder Accessibility

- **Technical detail**: Diagrams show component interactions for engineers.  
- **Business value**: Visuals clarify data flow for marketing teams.  

---

</details>

---

## Prompt Design for Code Snippets

<details>
<summary>Prompts for Generating SDK and API Examples</summary>

---

- **Purpose**: Produce code snippets for custom tracking and AppsFlyer integration.  
- **Key prompt example**:  
  ```text
  Generate a JavaScript snippet for AppsFlyer SDK initialization and a JSON payload for a custom tracking system’s install event. Format code blocks in ctx_doc_style-compliant Markdown with language specification and 2-space indentation.
  ```  
- **Cursor usage**:  
  - Generate AppsFlyer SDK initialization code.  
  - Create JSON event payload for custom tracking.  
  - Example output:  
    ```javascript
    import AppsFlyer from 'appsflyer-sdk';
    AppsFlyer.init({
      appId: 'com.example.app',
      devKey: 'your-dev-key'
    });
    ```  

#### Code Optimization

- **Functionality**: Ensure snippets are executable (e.g., valid AppsFlyer SDK syntax).  
- **Formatting**: Use `json` or `javascript` for code block language specification.  
- **Error checking**: Cursor validates syntax and suggests corrections.  

---

#### Validation Process

- **Syntax check**: Verify code runs without errors.  
- **Relevance**: Ensure snippets align with A04’s tracking scenarios.  

---

</details>

---

## Prompt Design for Documentation

<details>
<summary>Prompts for ctx_doc_style-Compliant Report Creation</summary>

---

- **Purpose**: Generate a structured, multi-audience report for A04.  
- **Key prompt example**:  
  ```text
  Create a Markdown report for task A04 (Web/App Tracking Analysis) following ctx_doc_style.md. Include sections for custom tracking, AppsFlyer evaluation, event flow visualization, and implementation planning. Use bullet points, details blocks with action-oriented summaries, and proper --- separators. Ensure clarity for engineers and stakeholders.
  ```  
- **Claude usage**:  
  - Generate report structure with correct ##, ###, and #### hierarchy.  
  - Populate sections with bullet-pointed content and descriptive summaries.  

#### Formatting Standards

- **Details blocks**: Start/end with `---`, use specific summaries (e.g., "Technical Design and Challenges").  
- **Bullet points**: Single-idea bullets for clarity (e.g., one challenge per bullet).  
- **Block indentation**: Code and Mermaid blocks indented `2` spaces.  

---

#### Stakeholder Accessibility

- **Technical clarity**: Use consistent terms (e.g., `SDK`, `attribution`) for engineers.  
- **Business alignment**: Highlight benefits (e.g., AppsFlyer’s `<1` week deployment) for stakeholders.  

---

</details>

---

## Quality Checklist

<details>
<summary>Compliance with Documentation Standards</summary>

---

- [x] YAML front matter present with `report_a04_prompt` title.  
- [x] Each subsection (###) contains one details block.  
- [x] Main sections (##) separated by `---`.  
- [x] No separators between ### sections.  
- [x] Details blocks start and end with `---`.  
- [x] Subsubsections (####) separated by `---`.  
- [x] Summary text is descriptive and specific.  
- [x] All content formatted as bullet points.  
- [x] Block elements (code, Mermaid) indented by `2` spaces.  
- [x] No numbered headings or bullet points.  
- [x] Technical symbols wrapped in backticks (e.g., `25%`).  
- [x] Code blocks include language specification (e.g., `mermaid`, `javascript`).  

---

</details>

---