---
description: Agent_Generation
---

# /03_agent_generation
Create customized AI executive personas calibrated for transformation

## Prerequisites
- Completed `shared_context/company_overview.md`
- Completed `shared_context/business_classification.md` 
- Completed `shared_context/next_level_goals.md`

## Workflow Execution

### Step 1: Gather Context (2 min)
```
Load files:
1. shared_context/company_overview.md → {{COMPANY_DATA}}
2. shared_context/business_classification.md → {{CLASSIFICATION}}
3. shared_context/next_level_goals.md → {{GOALS}}

Extract:
- Company: {{NAME}}
- Industry: {{INDUSTRY}}
- Stage: {{ARCHETYPE}}
- Next Level: {{TRANSFORMATION}}
```

### Step 2: Industry Intelligence (5 min)
```
@web search "{{INDUSTRY}} {{ARCHETYPE}} executive priorities KPIs challenges"

Focus on:
- What metrics matter most at this stage
- Common strategic mistakes to avoid
- Technology adoption patterns
- Cultural success factors

Create new file: shared_context/industry_intelligence.md
```

### Step 3: Create Calibration Guide (5 min)
Create new file: `.agents/calibration_guide.md`

```markdown
# Agent Calibration for {{COMPANY_NAME}}

## Company Context
- Industry: {{INDUSTRY}}
- Stage: {{ARCHETYPE}} 
- Goal: {{TRANSFORMATION}}
- Timeline: 12-18 months

## ATLAS Focus
Strategic priorities for {{TRANSFORMATION}}:
- Market: {{MARKET_OPPORTUNITY}}
- Competition: {{COMPETITIVE_FOCUS}}
- Growth: {{GROWTH_STRATEGY}}
Key Question: "What move doubles our impact?"

## NAVIGATOR Focus  
Operational priorities for {{TRANSFORMATION}}:
- Metrics: {{KEY_METRICS}}
- Efficiency: {{OPTIMIZATION_TARGETS}}
- Scale: {{SCALING_NEEDS}}
Key Question: "What's blocking our growth?"

## MAESTRO Focus
Technology priorities for {{TRANSFORMATION}}:
- Platform: {{TECH_NEEDS}}
- Automation: {{AUTOMATION_TARGETS}}
- Innovation: {{TECH_DIFFERENTIATORS}}
Key Question: "What tech gives us an edge?"

## CATALYST Focus
Change priorities for {{TRANSFORMATION}}:
- Culture: {{CULTURE_SHIFTS}}
- Adoption: {{CHANGE_TARGETS}}
- Readiness: {{PREPARATION_NEEDS}}
Key Question: "How do we bring everyone along?"

## Success Metrics
- {{METRIC_1}}
- {{METRIC_2}}
- {{METRIC_3}}
```

### Step 4: Enhance Company Overview (3 min)
Create new file: `shared_context/enhanced_overview.md`

Combine:
- Original company overview
- Classification insights
- Next level goals
- Industry intelligence
- Key challenges and opportunities

This becomes the input for agent generation.

### Step 5: Generate Agents (5 min)
Use the meta-prompt creator with enhanced_overview.md

The meta-prompt will output 4 agent blocks. For each:
1. Verify company name is used (not placeholders)
2. Check industry-specific language
3. Confirm next-level focus
4. Ensure proper formatting

### Step 6: Customize Key Questions (3 min)
For each generated agent, enhance the "Key Questions I Always Ask" section using the calibration guide:

**ATLAS Questions:**
- Original questions from meta-prompt
- "What {{INDUSTRY}} trend creates our biggest opportunity?"
- "How do we achieve {{TRANSFORMATION}} faster than competitors?"
- Add calibration key question

**NAVIGATOR Questions:**
- Original questions from meta-prompt  
- "What's our path from {{CURRENT_METRIC}} to {{TARGET_METRIC}}?"
- "Which processes must scale for {{TRANSFORMATION}}?"
- Add calibration key question

**MAESTRO Questions:**
- Original questions from meta-prompt
- "What technology enables {{TRANSFORMATION}}?"
- "Build vs buy for {{CRITICAL_CAPABILITY}}?"
- Add calibration key question

**CATALYST Questions:**
- Original questions from meta-prompt
- "What cultural shifts enable {{TRANSFORMATION}}?"
- "Who are the key champions for change?"
- Add calibration key question

### Step 7: Save Final Agents (2 min)
Update existing files:
- `.agents/ATLAS.md` 
- `.agents/NAVIGATOR.md`
- `.agents/MAESTRO.md`
- `.agents/CATALYST.md`

Each file must have YAML header:
```yaml
---
agent: [AGENT_NAME]
role: [Agent Title]
company: {{COMPANY_NAME}}
version: 1.0
---
```

### Step 8: Quality Validation (3 min)
Test each agent with transformation-focused queries:

```
@ATLAS "What should {{COMPANY}} prioritize for {{TRANSFORMATION}}?"
@NAVIGATOR "How do we measure progress toward {{TRANSFORMATION}}?"
@MAESTRO "What tech investments enable {{TRANSFORMATION}}?"
@CATALYST "What change risks could derail {{TRANSFORMATION}}?"
```

Expected: Specific, actionable insights (not generic advice)

### Step 9: Create Summary (2 min)
Create new file: `.agents/AGENT_SUMMARY.md`

```markdown
# Your AI Executive Team for {{COMPANY_NAME}}

## Calibrated for: {{TRANSFORMATION}}

### ATLAS - Strategic Intelligence
**Focus**: {{ATLAS_FOCUS}}
**First Ask**: "{{ATLAS_KEY_QUESTION}}"

### NAVIGATOR - Operations Excellence  
**Focus**: {{NAVIGATOR_FOCUS}}
**First Ask**: "{{NAVIGATOR_KEY_QUESTION}}"

### MAESTRO - Technology Integration
**Focus**: {{MAESTRO_FOCUS}}
**First Ask**: "{{MAESTRO_KEY_QUESTION}}"

### CATALYST - Change & Adoption
**Focus**: {{CATALYST_FOCUS}}
**First Ask**: "{{CATALYST_KEY_QUESTION}}"

## They Work Together
- ATLAS sees opportunity → NAVIGATOR plans execution
- MAESTRO enables with tech → CATALYST ensures adoption

Ready to transform!
```

### Step 10: Complete
```
✓ Agents created and customized
✓ Focused on {{TRANSFORMATION}}
✓ Industry-specific language
✓ Quality validated

Next: Run /04_structure_creation
Time: ~20 minutes
```

## Quick Quality Checklist
Rate 1-10:
- [ ] Uses company specifics (not generic)
- [ ] Focused on transformation goal
- [ ] Industry-appropriate language
- [ ] Actionable insights
- [ ] Differentiated from generic AI

If any < 7, refine in Step 6.

## Common Customizations by Archetype

**EARLY_STARTUP**: Focus on validation, runway, first customers
**GROWTH_STARTUP**: Focus on scaling, metrics, product-market fit
**SCALE_UP**: Focus on efficiency, market expansion, platform
**MID_MARKET**: Focus on digital transformation, competitive edge
**ENTERPRISE**: Focus on innovation, disruption defense, agility