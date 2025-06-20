---
description: # Foundation™ Business Classification Workflow
---

Analyze and classify the business for targeted intelligence

## Prerequisites
- Completed `shared_context/company_overview.md`

## Workflow Execution

### Step 1: Load Company Data
```
Read from: shared_context/company_overview.md
Extract: Company Name, Employees, Industry, Funding Stage, Years Operating
```

### Step 2: Classify Archetype
```
Based on employee count:
- 1-10 → EARLY_STARTUP
- 11-50 → GROWTH_STARTUP
- 51-200 → SCALE_UP
- 201-500 → MID_MARKET
- 500+ → ENTERPRISE
```

### Step 3: Industry Overlay
```
Identify special focus based on industry:
- SaaS/Software → Add: metrics, PLG, platform scaling
- Manufacturing → Add: supply chain, automation, quality
- Healthcare → Add: compliance, outcomes, interop
- Financial → Add: regulation, risk, fintech
```

### Step 4: Growth Stage Analysis
```
@web search "{{COMPANY_NAME}}" growth signals hiring funding expansion

Classify stage: Searching / Building / Scaling / Optimizing / Transforming
```

### Step 5: Define Next Level (Critical)
```
Based on Archetype + Industry + Stage:

EARLY_STARTUP → "Achieve Product-Market Fit"
GROWTH_STARTUP → "Build Scalable Growth Engine"  
SCALE_UP → "Achieve Market Leadership"
MID_MARKET → "Digital Transformation Excellence"
ENTERPRISE → "Innovation-Driven Reinvention"
```

### Step 6: Populate Classification Report
Update existing file: `shared_context/business_classification.md`

Use template from: `.templates/classification_template.md`

Key sections:
- Primary Classification (archetype, industry, stage)
- Next Level Transformation (from → to)
- Focus Areas (must have / skip)
- Agent Priorities (what each should focus on)

### Step 7: Populate Next Level Goals
Update existing file: `shared_context/next_level_goals.md`

Simple format:
- Current State: {{WHERE_THEY_ARE}}
- Future State: {{WHERE_THEY_NEED_TO_BE}}
- Success Metrics: {{3-5_KEY_METRICS}}
- Timeline: 12-18 months

### Step 8: Validate & Proceed
```
Classification complete:
- Archetype: {{RESULT}}
- Next Level: {{GOAL}}
- Ready for: /03_agent_generation
```

## Time: 10 minutes