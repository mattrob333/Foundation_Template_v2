---
description: 4 - Agent_Generation
---

# four_agent_generation
Create customized AI executive personas calibrated for their file structure

## Prerequisites
- Completed `shared_context/company_overview.md`
- Completed `shared_context/business_classification.md` 
- Completed `shared_context/next_level_goals.md`
- Completed `three_structure_creation` (file structure exists)# /04_agent_generation
Create customized AI executive personas calibrated for their file structure

## Prerequisites
- Completed `shared_context/company_overview.md`
- Completed `shared_context/business_classification.md` 
- Completed `shared_context/next_level_goals.md`
- Completed `/03_structure_creation` (file structure exists)

## Workflow Execution

### Step 1: Gather Context (2 min)
```
Load files:
1. shared_context/company_overview.md → {{COMPANY_DATA}}
2. shared_context/business_classification.md → {{CLASSIFICATION}}
3. shared_context/next_level_goals.md → {{GOALS}}
4. shared_context/file_inventory.md → {{FILE_STRUCTURE}}

Extract:
- Company: {{NAME}}
- Industry: {{INDUSTRY}}
- Stage: {{ARCHETYPE}}
- Next Level: {{TRANSFORMATION}}
- Files Created: {{FILE_LIST}}
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

### Step 3: Create Agent Calibration (5 min)
Create new file: `.agents/calibration_guide.md`

```markdown
# Agent Calibration for {{COMPANY_NAME}}

## File Structure Context
Each agent has access to these specific files:

### ATLAS Files ({{COUNT}})
{{LIST_ATLAS_FILES}}

### NAVIGATOR Files ({{COUNT}})
{{LIST_NAVIGATOR_FILES}}

### MAESTRO Files ({{COUNT}})
{{LIST_MAESTRO_FILES}}

### CATALYST Files ({{COUNT}})
{{LIST_CATALYST_FILES}}

## Calibration by Agent

### ATLAS Focus
With access to {{ATLAS_FILE_CATEGORIES}}, ATLAS should:
- Use market_landscape/ files for trend analysis
- Reference competitors/ files for positioning
- Leverage strategy/ files for recommendations
Key Question: "What move doubles our impact?"

### NAVIGATOR Focus  
With access to {{NAVIGATOR_FILE_CATEGORIES}}, NAVIGATOR should:
- Monitor metrics/ files for performance tracking
- Use operations/ files for efficiency gains
- Reference sales_marketing/ for growth insights
Key Question: "What's blocking our growth?"

### MAESTRO Focus
With access to {{MAESTRO_FILE_CATEGORIES}}, MAESTRO should:
- Assess tech_stack/ for modernization needs
- Use workflow_opportunities/ for automation
- Reference talent/ for capability building
Key Question: "What tech gives us an edge?"

### CATALYST Focus
With access to {{CATALYST_FILE_CATEGORIES}}, CATALYST should:
- Monitor sentiment/ for readiness signals
- Use change_assets/ for transformation
- Track performance/ for adoption metrics
Key Question: "How do we bring everyone along?"
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

### Step 6: Enhance Agent Knowledge Bases (3 min)
For each generated agent, add file-specific knowledge section:

**Add to ATLAS:**
```markdown
## My Knowledge Base Structure
I have access to comprehensive strategic intelligence in:
- `/ATLAS/market_landscape/` - Market trends and opportunities
- `/ATLAS/competitors/` - Competitive intelligence and positioning
- `/ATLAS/strategy/` - Strategic plans and frameworks
- `/ATLAS/finance/` - Financial analysis and projections

I can reference any file in these directories to provide insights.
```

**Add to NAVIGATOR:**
```markdown
## My Knowledge Base Structure
I have access to operational intelligence in:
- `/NAVIGATOR/metrics/` - KPIs and performance data
- `/NAVIGATOR/operations/` - Process documentation
- `/NAVIGATOR/sales_marketing/` - Go-to-market intelligence
- `/NAVIGATOR/scaling/` - Growth and scaling playbooks

I use these files to optimize operations and drive efficiency.
```

**Add to MAESTRO:**
```markdown
## My Knowledge Base Structure
I have access to technical intelligence in:
- `/MAESTRO/tech_stack/` - Current and future architecture
- `/MAESTRO/workflow_opportunities/` - Automation candidates
- `/MAESTRO/talent/` - Technical team and skills
- `/MAESTRO/innovation/` - Emerging technology opportunities

I leverage these files for technology strategy and implementation.
```

**Add to CATALYST:**
```markdown
## My Knowledge Base Structure
I have access to change intelligence in:
- `/CATALYST/sentiment/` - Culture and readiness data
- `/CATALYST/change_assets/` - Transformation resources
- `/CATALYST/performance/` - Adoption and success metrics
- `/CATALYST/transformation/` - Change frameworks

I use these resources to ensure successful transformation.
```

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

Expected: Spec