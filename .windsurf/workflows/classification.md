---
description: # Foundation™ Business Classification Workflow
---

# /02_classification
Analyze and classify the business for targeted intelligence

## Prerequisites
- Completed `shared_context/company_overview.md`

## Workflow Execution

### Step 1: Load Company Data (1 min)
```
Read from: shared_context/company_overview.md
Extract key variables:
- Company Name: {{COMPANY_NAME}}
- Employees: {{EMPLOYEE_COUNT}}
- Industry: {{INDUSTRY}}
- Founded: {{YEAR}}
- Stage: {{FUNDING_OR_REVENUE}}
```

### Step 2: Determine Archetype (1 min)
```
Based on employee count:
- 1-10 → EARLY_STARTUP
- 11-50 → GROWTH_STARTUP  
- 51-200 → SCALE_UP
- 201-500 → MID_MARKET
- 500+ → ENTERPRISE

Set: {{ARCHETYPE}}
```

### Step 3: Industry Overlay (2 min)
```
Analyze industry for special considerations:

Technology/SaaS:
- Add: Metrics focus (ARR, CAC, LTV)
- Add: Platform scaling considerations
- Add: Developer/API strategy

Manufacturing/Industrial:
- Add: Supply chain optimization
- Add: Automation opportunities
- Add: Quality/safety systems

Healthcare/Medical:
- Add: Compliance requirements
- Add: Patient outcome focus
- Add: Interoperability needs

Financial Services:
- Add: Regulatory compliance
- Add: Risk management
- Add: Fintech disruption

Professional Services:
- Add: Talent leverage
- Add: Knowledge management
- Add: Client success metrics

Set: {{INDUSTRY_FOCUS}}
```

### Step 4: Growth Signals (3 min)
```
@web search "{{COMPANY_NAME}}" recent growth signals:

Look for:
- Recent funding (amount, stage, investors)
- Hiring velocity (job postings, LinkedIn growth)
- Product launches (new offerings, markets)
- Geographic expansion (new offices, markets)
- Strategic partnerships (key relationships)
- Awards/recognition (industry validation)

Classify momentum:
- Stagnant (no major changes)
- Steady (organic growth)
- Accelerating (multiple growth signals)
- Transforming (major strategic shift)

Set: {{GROWTH_STATE}}
```

### Step 5: Define Next Level (2 min)
```
Based on {{ARCHETYPE}} + {{INDUSTRY}} + {{GROWTH_STATE}}:

EARLY_STARTUP + Any Industry:
Next Level: "Achieve Product-Market Fit"
- From: Idea/prototype stage
- To: Repeatable sales, clear value prop
- Success: First 10 happy customers

GROWTH_STARTUP + Technology:
Next Level: "Build Scalable Growth Engine"
- From: Manual processes, founder-led sales
- To: Repeatable playbooks, team-driven growth
- Success: $1M → $10M ARR

SCALE_UP + Any Industry:
Next Level: "Achieve Market Leadership"
- From: Regional player, single product
- To: Category leader, platform approach
- Success: Top 3 market position

MID_MARKET + Traditional Industry:
Next Level: "Digital Transformation Excellence"
- From: Legacy systems, manual processes
- To: Digital-first, data-driven operations
- Success: 30%+ efficiency gain

ENTERPRISE + Any Industry:
Next Level: "Innovation-Driven Reinvention"
- From: Market incumbent, slow innovation
- To: Agile innovator, new ventures
- Success: New revenue streams launched

Set: {{NEXT_LEVEL_GOAL}}
```

### Step 6: Identify Critical Success Factors (2 min)
```
For {{ARCHETYPE}} achieving {{NEXT_LEVEL_GOAL}}:

What must they get right:
1. {{CRITICAL_FACTOR_1}} - Why: {{REASON}}
2. {{CRITICAL_FACTOR_2}} - Why: {{REASON}}
3. {{CRITICAL_FACTOR_3}} - Why: {{REASON}}

What could derail them:
1. {{RISK_1}} - Mitigation: {{APPROACH}}
2. {{RISK_2}} - Mitigation: {{APPROACH}}
3. {{RISK_3}} - Mitigation: {{APPROACH}}
```

### Step 7: Update Classification Report (3 min)
Update existing file: `shared_context/business_classification.md`

```markdown
---
title: "Business Classification - {{COMPANY_NAME}}"
created: "{{TODAY_DATE}}"
classification_version: "1.0"
---

# Business Classification

## Primary Classification
- **Archetype**: {{ARCHETYPE}}
- **Industry**: {{INDUSTRY}} ({{INDUSTRY_FOCUS}})
- **Growth State**: {{GROWTH_STATE}}
- **Employee Range**: {{EMPLOYEE_COUNT}}

## Next Level Transformation
**Current State**: {{CURRENT_DESCRIPTION}}
**Future State**: {{FUTURE_DESCRIPTION}}
**Timeline**: 12-18 months
**Success Metrics**:
- {{METRIC_1}}
- {{METRIC_2}}
- {{METRIC_3}}

## Critical Success Factors
1. **{{FACTOR_1}}**: {{EXPLANATION}}
2. **{{FACTOR_2}}**: {{EXPLANATION}}
3. **{{FACTOR_3}}**: {{EXPLANATION}}

## Foundation Focus Areas

### Must Have (Core)
- {{AREA_1}}: Essential for {{REASON}}
- {{AREA_2}}: Essential for {{REASON}}
- {{AREA_3}}: Essential for {{REASON}}
- {{AREA_4}}: Essential for {{REASON}}
- {{AREA_5}}: Essential for {{REASON}}

### Should Have (Important)
- {{AREA_6}}: Important for {{REASON}}
- {{AREA_7}}: Important for {{REASON}}
- {{AREA_8}}: Important for {{REASON}}

### Skip (Not Now)
- {{SKIP_1}}: Not relevant because {{REASON}}
- {{SKIP_2}}: Not relevant because {{REASON}}

## Agent Priorities

**ATLAS** should focus on:
- {{ATLAS_PRIORITY_1}}
- {{ATLAS_PRIORITY_2}}

**NAVIGATOR** should focus on:
- {{NAVIGATOR_PRIORITY_1}}
- {{NAVIGATOR_PRIORITY_2}}

**MAESTRO** should focus on:
- {{MAESTRO_PRIORITY_1}}
- {{MAESTRO_PRIORITY_2}}

**CATALYST** should focus on:
- {{CATALYST_PRIORITY_1}}
- {{CATALYST_PRIORITY_2}}
```

### Step 8: Update Next Level Goals (2 min)
Update existing file: `shared_context/next_level_goals.md`

```markdown
---
title: "Next Level Goals - {{COMPANY_NAME}}"
created: "{{TODAY_DATE}}"
priority: "critical"
---

# Next Level Definition

## Current State
{{COMPANY_NAME}} is currently:
- Stage: {{ARCHETYPE}}
- Position: {{MARKET_POSITION}}
- Constraint: {{MAIN_CONSTRAINT}}

## Future State (12-18 months)
{{COMPANY_NAME}} will be:
- Stage: {{TARGET_STAGE}}
- Position: {{TARGET_POSITION}}
- Capability: {{NEW_CAPABILITY}}

## Success Looks Like
- {{SUCCESS_INDICATOR_1}}
- {{SUCCESS_INDICATOR_2}}
- {{SUCCESS_INDICATOR_3}}

## Key Milestones
- Q1: {{MILESTONE_1}}
- Q2: {{MILESTONE_2}}
- Q3: {{MILESTONE_3}}
- Q4: {{MILESTONE_4}}
```

### Step 9: Validate & Complete
```
✓ Classification complete
✓ Next level defined
✓ Success metrics clear
✓ Agent priorities set

Next: Run /03_agent_generation
Time: ~10 minutes
```

## Quick Reference by Archetype

**EARLY_STARTUP**: Focus on validation, survival, first revenue
**GROWTH_STARTUP**: Focus on efficiency, talent, repeatable growth
**SCALE_UP**: Focus on market dominance, platform, operations
**MID_MARKET**: Focus on modernization, efficiency, differentiation
**ENTERPRISE**: Focus on innovation, agility, new business models