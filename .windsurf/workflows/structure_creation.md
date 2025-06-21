---
description: Structure_Creation
---

# /04_structure_creation
Create optimized file structure based on business type

## Prerequisites
- Completed business classification
- Agents already created

## Workflow Execution

### Step 1: Load Configuration (1 min)
```
Read from: shared_context/business_classification.md
Extract:
- Archetype: {{ARCHETYPE}}
- Industry: {{INDUSTRY}}
- Focus Areas: {{MUST_HAVE_AREAS}}
- Skip Areas: {{SKIP_AREAS}}
```

### Step 2: Verify Base Structure (1 min)
```
Confirm these directories exist (should be in template):
- shared_context/
- CATALYST/
- ATLAS/
- NAVIGATOR/
- MAESTRO/
- .agents/
- .templates/
```

### Step 3: Create Archetype-Specific Files (5 min)

Based on {{ARCHETYPE}}, create appropriate empty files:

#### For EARLY_STARTUP:
```
Create new files:
CATALYST/sentiment/market_validation.md
CATALYST/sentiment/customer_feedback.md
CATALYST/change_assets/founder_alignment.md

ATLAS/market_landscape/tam_sam_som.md
ATLAS/market_landscape/beachhead_strategy.md
ATLAS/competitors/early_competition.md
ATLAS/finance/runway_scenarios.md

NAVIGATOR/ops_metrics/burn_rate.md
NAVIGATOR/ops_metrics/unit_economics.md
NAVIGATOR/sales_marketing/customer_acquisition.md

MAESTRO/tech_stack/mvp_architecture.md
MAESTRO/tech_stack/build_vs_buy.md
MAESTRO/workflow_opportunities/quick_wins.md
```

#### For GROWTH_STARTUP:
```
Create new files:
CATALYST/sentiment/team_culture.md
CATALYST/change_assets/scaling_culture.md
CATALYST/performance/hiring_success.md

ATLAS/market_landscape/expansion_markets.md
ATLAS/competitors/competitive_matrix.md
ATLAS/finance/series_a_readiness.md
ATLAS/strategic_plans/growth_strategy.md

NAVIGATOR/ops_metrics/saas_metrics.md
NAVIGATOR/ops_metrics/cohort_analysis.md
NAVIGATOR/process_docs/playbook_library.md
NAVIGATOR/sales_marketing/sales_efficiency.md

MAESTRO/tech_stack/platform_scaling.md
MAESTRO/talent/tech_hiring_plan.md
MAESTRO/workflow_opportunities/automation_roadmap.md
```

#### For SCALE_UP:
```
Create new files:
CATALYST/sentiment/employee_engagement.md
CATALYST/change_assets/change_readiness.md
CATALYST/performance/adoption_tracking.md

ATLAS/market_landscape/market_leadership.md
ATLAS/competitors/moat_analysis.md
ATLAS/finance/growth_efficiency.md
ATLAS/strategic_plans/platform_strategy.md

NAVIGATOR/ops_metrics/operational_excellence.md
NAVIGATOR/process_docs/scaled_processes.md
NAVIGATOR/sales_marketing/market_penetration.md

MAESTRO/tech_stack/enterprise_architecture.md
MAESTRO/talent/tech_organization.md
MAESTRO/workflow_opportunities/platform_integration.md
```

#### For MID_MARKET:
```
Create new files:
CATALYST/sentiment/digital_readiness.md
CATALYST/change_assets/transformation_plan.md
CATALYST/performance/change_metrics.md

ATLAS/market_landscape/disruption_threats.md
ATLAS/competitors/digital_competitors.md
ATLAS/strategic_plans/transformation_roadmap.md

NAVIGATOR/ops_metrics/efficiency_benchmarks.md
NAVIGATOR/process_docs/process_optimization.md
NAVIGATOR/sales_marketing/omnichannel_strategy.md

MAESTRO/tech_stack/legacy_modernization.md
MAESTRO/tech_stack/integration_architecture.md
MAESTRO/workflow_opportunities/digital_transformation.md
```

#### For ENTERPRISE:
```
Create new files:
CATALYST/sentiment/innovation_culture.md
CATALYST/change_assets/innovation_framework.md
CATALYST/performance/transformation_metrics.md

ATLAS/market_landscape/disruption_defense.md
ATLAS/competitors/startup_threats.md
ATLAS/strategic_plans/innovation_portfolio.md
ATLAS/finance/new_ventures.md

NAVIGATOR/ops_metrics/enterprise_agility.md
NAVIGATOR/process_docs/agile_transformation.md
NAVIGATOR/sales_marketing/digital_channels.md

MAESTRO/tech_stack/modern_architecture.md
MAESTRO/talent/digital_skills_gap.md
MAESTRO/workflow_opportunities/innovation_labs.md
```

### Step 4: Add File Headers (3 min)
For each newly created file, add appropriate header:

```yaml
---
title: "[Descriptive Title Based on Filename]"
source: "To be populated"
owner: "intel@tier4.ai"
agent_scope: ["{{RELEVANT_AGENT}}"]
created: "{{TODAY_DATE}}"
status: "empty"
priority: "{{high/medium/low based on focus areas}}"
tags: ["{{relevant}}", "{{tags}}"]
---

# {{Title}}

*This file will be populated by the research workflow.*

## Purpose
{{Brief description of what this file will contain}}

## Key Questions to Answer
- {{Question 1}}
- {{Question 2}}
- {{Question 3}}
```

### Step 5: Create Structure Report (2 min)
Create new file: `shared_context/structure_report.md`

```markdown
---
title: "File Structure Report - {{COMPANY_NAME}}"
created: "{{TODAY_DATE}}"
---

# Foundation Structure Report

## Files Created
Total: {{COUNT}} files across 4 agents

### CATALYST ({{COUNT}} files)
- sentiment/{{FILE}}: {{PURPOSE}}
- change_assets/{{FILE}}: {{PURPOSE}}
- performance/{{FILE}}: {{PURPOSE}}

### ATLAS ({{COUNT}} files)
- market_landscape/{{FILE}}: {{PURPOSE}}
- competitors/{{FILE}}: {{PURPOSE}}
- finance/{{FILE}}: {{PURPOSE}}
- strategic_plans/{{FILE}}: {{PURPOSE}}

### NAVIGATOR ({{COUNT}} files)
- ops_metrics/{{FILE}}: {{PURPOSE}}
- process_docs/{{FILE}}: {{PURPOSE}}
- sales_marketing/{{FILE}}: {{PURPOSE}}

### MAESTRO ({{COUNT}} files)
- tech_stack/{{FILE}}: {{PURPOSE}}
- talent/{{FILE}}: {{PURPOSE}}
- workflow_opportunities/{{FILE}}: {{PURPOSE}}

## Priority Order for Population
Based on {{NEXT_LEVEL_GOAL}}:

High Priority:
1. {{FILE_PATH}} - Critical for {{REASON}}
2. {{FILE_PATH}} - Critical for {{REASON}}
3. {{FILE_PATH}} - Critical for {{REASON}}

Medium Priority:
4. {{FILE_PATH}} - Important for {{REASON}}
5. {{FILE_PATH}} - Important for {{REASON}}

Lower Priority:
[Remaining files...]
```

### Step 6: Validate Structure (1 min)
```
Check:
- [ ] All directories have relevant files
- [ ] File count matches archetype needs
- [ ] Headers include proper agent_scope
- [ ] Priority aligns with next level goals

Success: ~15-25 files created based on archetype
```

### Step 7: Complete
```
✓ File structure created
✓ {{COUNT}} files ready for research
✓ Priority order established
✓ All files have proper headers

Next: Run /05_research_population
Time: ~10 minutes
```

## Notes on File Creation

**Why these specific files:**
- Each archetype has different intelligence needs
- Early startups need validation data
- Growth companies need scaling intelligence
- Enterprises need transformation insights

**File count by archetype:**
- EARLY_STARTUP: ~15 files (focused)
- GROWTH_STARTUP: ~18 files (expanding)
- SCALE_UP: ~20 files (comprehensive)
- MID_MARKET: ~18 files (transformation)
- ENTERPRISE: ~22 files (innovation)