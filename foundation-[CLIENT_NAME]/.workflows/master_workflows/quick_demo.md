# Foundation™ Quick Demo Workflow
30-minute version for demos and rapid prototypes

## Purpose
Create a working Foundation™ with essential files only

## Workflow Execution

### Phase 1: Rapid Discovery (5 min)
```
@web search "{{COMPANY_URL}}" quick overview:
- Company name, size, industry
- Products/services
- Recent news
- Leadership team

Populate: shared_context/company_overview.md (simplified)
```

### Phase 2: Quick Classification (2 min)
```
Determine:
- Archetype: Based on employee count
- Next Level: One-line transformation goal
- Focus: Top 3 priorities

Populate: shared_context/business_classification.md (essential sections only)
```

### Phase 3: Agent Generation (8 min)
```
Use simplified agent template
Focus on company-specific elements:
- Company name throughout
- Industry terminology
- Key challenge
- Next level goal

Populate: 4 agent files (keep under 50 lines each)
```

### Phase 4: Essential Files Only (15 min)

#### CATALYST (1 file)
```
@web search "{{COMPANY}}" sentiment culture
→ Populate: sentiment/quick_sentiment.md
```

#### ATLAS (2 files)
```
@web search "{{INDUSTRY}}" market trends
→ Populate: market_landscape/market_quick.md

@web search "{{COMPANY}}" competitors
→ Populate: competitors/competitor_quick.md
```

#### NAVIGATOR (1 file)
```
@web search "{{COMPANY}}" metrics performance
→ Populate: metrics/kpi_quick.md
```

#### MAESTRO (1 file)
```
@web search "{{COMPANY}}" technology stack
→ Populate: tech_stack/tech_quick.md
```

### Phase 5: Quick Test (2 min)
```
Ask each agent one question:
- @ATLAS "Biggest opportunity?"
- @NAVIGATOR "Key metric?"
- @MAESTRO "Tech priority?"
- @CATALYST "Main risk?"

If responses are specific → Success!
```

### Demo Script
```
"In just 30 minutes, we've created an AI intelligence system that understands {{COMPANY}}'s specific situation.

Each agent can now provide insights about:
- Market opportunities (ATLAS)
- Operational improvements (NAVIGATOR)
- Technology priorities (MAESTRO)
- Change challenges (CATALYST)

With more time, we expand to {{FULL_FILE_COUNT}} intelligence files for comprehensive coverage."
```

## Success Metrics
- Time: Under 30 minutes
- Files: 5-8 essential files
- Quality: Agents give specific answers
- Impact: Clear value demonstrated

## What to Skip
- Deep classification analysis
- Industry research
- Extensive file structure
- Multiple validation loops
- Enhancement passes

## Remember
This is for demos - show value quickly, expand later!