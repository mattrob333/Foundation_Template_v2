---
description: Structure_Creation
---

# three_structure_creation
Create optimized file structure based on business archetype

Prerequisites

Completed business classification
Access to .templates/archetype_templates/

Workflow Execution
Step 1: Load Configuration (1 min)
Read from: shared_context/business_classification.md
Extract:
- Archetype: {{ARCHETYPE}}
- Industry: {{INDUSTRY}}
- Focus Areas: {{MUST_HAVE_AREAS}}
- Skip Areas: {{SKIP_AREAS}}
Step 2: Select Archetype Template (2 min)
Based on {{ARCHETYPE}}, select template from:
.templates/archetype_templates/

- EARLY_STARTUP → early_startup_template/
- GROWTH_STARTUP → growth_startup_template/
- SCALE_UP → scale_up_template/
- MID_MARKET → mid_market_template/
- ENTERPRISE → enterprise_template/
Step 3: Copy Template Structure (3 min)
Copy the appropriate template structure to create:

For EARLY_STARTUP:
- Focus on validation and market fit
- Minimal process documentation
- Emphasis on customer discovery

For GROWTH_STARTUP:
- Balance of strategy and operations
- Scaling focus
- Talent and culture files

For SCALE_UP:
- Comprehensive coverage
- Market leadership focus
- Platform strategy

For MID_MARKET:
- Digital transformation emphasis
- Legacy modernization
- Efficiency optimization

For ENTERPRISE:
- Innovation framework
- Disruption defense
- New ventures focus
Step 4: Create Industry Overlay Files (3 min)
Based on {{INDUSTRY}}, add specialized files:

For SaaS/Technology:
Create new files:
- NAVIGATOR/metrics/saas_metrics.md
- MAESTRO/architecture/api_strategy.md
- ATLAS/strategy/platform_evolution.md

For Manufacturing:
Create new files:
- NAVIGATOR/operations/supply_chain.md
- MAESTRO/workflow_opportunities/automation_roadmap.md
- NAVIGATOR/metrics/quality_metrics.md

For Healthcare:
Create new files:
- NAVIGATOR/operations/compliance_tracking.md
- MAESTRO/architecture/interoperability.md
- CATALYST/change_assets/regulatory_readiness.md

For Financial Services:
Create new files:
- NAVIGATOR/operations/risk_management.md
- MAESTRO/architecture/security_framework.md
- ATLAS/strategy/fintech_threats.md
Step 5: Add Headers to All Files (3 min)
For each file (both from template and newly created):

Add/update YAML header:
---
title: "[Descriptive Title Based on Filename]"
source: "To be populated"
owner: "intel@tier4.ai" 
agent_scope: ["{{RELEVANT_AGENT}}"]
created: "{{TODAY_DATE}}"
status: "empty"
priority: "{{high/medium/low based on focus areas}}"
tags: ["{{archetype}}", "{{relevant}}", "{{tags}}"]
---

# {{Title}}

*This file will be populated by the research workflow.*

## Purpose
{{Brief description of what this file will contain}}

## Key Questions to Answer
- {{Question 1}}
- {{Question 2}}
- {{Question 3}}
Step 6: Create File Inventory (3 min)
Create new file: shared_context/file_inventory.md
Use the file inventory template to document:

All files created for each agent
File paths and purposes
Population priority order
Status tracking (Empty/Partial/Complete)
Maintenance schedule

markdownExample structure:
## 🚀 CATALYST Files
### /sentiment
| File | Path | Status | Priority | Purpose |
|------|------|--------|----------|---------|
| employee_pulse.md | CATALYST/sentiment/employee_pulse.md | Empty | High | Track employee sentiment |

[Continue for all files...]
The inventory serves as:

Master list for research population
Progress tracking during setup
Maintenance checklist post-launch
Documentation for handoffs

Step 7: Complete
✓ Archetype template applied
✓ Industry-specific files added
✓ All files have proper headers
✓ File inventory created
✓ {{COUNT}} files ready for agents

Next: Run four_agent_generation
Time: ~10 minutes
Notes
Why Templates Matter:

Consistency across Foundations
Best practices built-in
Faster setup time
Fewer missed files

Customization:

Templates are starting points
Add/remove files based on specific needs
Industry overlays add specialization
Keep focus on transformation goals
