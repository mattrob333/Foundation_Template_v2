# Foundation™ Structure Creation Workflow
Create archetype-specific file structure

## Prerequisites
- Completed `shared_context/business_classification.md`

## Workflow Execution

### Step 1: Load Classification
```
Read: shared_context/business_classification.md
Extract: {{ARCHETYPE}}, {{FOCUS_AREAS}}
```

### Step 2: Determine File Count
```
EARLY_STARTUP → 12-15 files
GROWTH_STARTUP → 15-18 files
SCALE_UP → 18-22 files
MID_MARKET → 20-25 files
ENTERPRISE → 25-30 files
```

### Step 3: Create Directories
```
Ensure exist:
- CATALYST/{archetype_dirs}/
- ATLAS/{archetype_dirs}/
- NAVIGATOR/{archetype_dirs}/
- MAESTRO/{archetype_dirs}/
```

### Step 4: Generate File List
Based on archetype, use template from:
`.templates/archetype_templates/{{ARCHETYPE}}_files.md`

### Step 5: Create Files with Headers
For each file in list:
```yaml
---
title: "[Descriptive Title]"
source: "To be populated"
owner: "intel@tier4.ai"
agent_scope: ["RELEVANT_AGENT"]
created: "[TODAY]"
status: "empty"
---

# [Title]
*To be populated by research workflow*
```

### Step 6: Generate Structure Report
Create: `shared_context/file_structure_report.md`

Include:
- Total files: {{COUNT}}
- By agent: CATALYST (X), ATLAS (Y), etc.
- Priority order for population

### Step 7: Validate & Proceed
```
Structure ready:
- Files created: {{TOTAL}}
- Customized for: {{ARCHETYPE}}
- Ready for: /05_research_execution
```

## Time: 5 minutes