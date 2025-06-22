---
description: 5 - Research_Population
---

# five_research_population
Populate all files with targeted intelligence

## Prerequisites
- All previous workflows completed
- Empty files created with headers
- Structure report available

## Workflow Execution

### Step 1: Load Research Plan (3 min)
```
Read from:
1. shared_context/file_inventory.md → {{FILE_LIST}}
2. shared_context/business_classification.md → {{FOCUS_AREAS}}
3. shared_context/next_level_goals.md → {{TRANSFORMATION}}
4. shared_context/intelligence_sources.md → {{DATA_SOURCES}} (if available)

Identify:
- High priority files to populate first
- Research themes based on transformation
- Industry-specific data needs
- Available RSS feeds and sources
```

### Step 2: CATALYST Research Phase (15 min)
Update CATALYST files with market intelligence:

**If intelligence_sources.md exists, prioritize:**
- RSS feeds for latest company news
- Glassdoor/employee review sites
- Industry forums for culture insights
- Leadership social media for vision

#### For sentiment files:
```
Update file: CATALYST/sentiment/{{FILENAME}}.md

@web search "{{COMPANY_NAME}}" customer reviews glassdoor culture:
- Customer sentiment and feedback
- Employee reviews and themes
- Cultural indicators
- Market perception
- Recent news sentiment

Format findings with:
- Positive indicators
- Negative indicators
- Trends over time
- Implications for change
```

#### For change_assets files:
```
Update file: CATALYST/change_assets/{{FILENAME}}.md

Research based on {{TRANSFORMATION}}:
- Change management best practices for {{INDUSTRY}}
- Common resistance points at {{ARCHETYPE}} stage
- Success factors for similar transformations
- Cultural requirements for success
```

#### For performance files:
```
Update file: CATALYST/performance/{{FILENAME}}.md

Create frameworks for:
- Measuring transformation progress
- Leading vs lagging indicators
- Adoption metrics
- Success benchmarks
```

### Step 3: ATLAS Research Phase (20 min)
Update ATLAS files with strategic intelligence:

#### For market_landscape files:
```
Update file: ATLAS/market_landscape/{{FILENAME}}.md

@web search "{{INDUSTRY}}" market size growth trends 2025:
- Market size and growth rate
- Key trends and disruptions
- Regulatory changes
- Technology impacts
- Strategic opportunities

Include:
- TAM/SAM/SOM calculations (if startup)
- Market share analysis (if scale-up)
- Disruption threats (if enterprise)
```

#### For competitors files:
```
Update file: ATLAS/competitors/{{FILENAME}}.md

@web search "{{COMPANY_NAME}}" competitors comparison:
- Direct competitors (3-5)
- Indirect/emerging threats
- Competitive positioning
- Differentiation opportunities
- Competitive intelligence

Format as:
- Competitor profiles
- Strength/weakness analysis
- Strategic implications
```

#### For strategic_plans files:
```
Update file: ATLAS/strategic_plans/{{FILENAME}}.md

Based on {{NEXT_LEVEL_GOAL}}:
- Strategic options available
- Resource requirements
- Risk/reward analysis
- Implementation timeline
- Success metrics
```

### Step 4: NAVIGATOR Research Phase (15 min)
Update NAVIGATOR files with operational intelligence:

#### For ops_metrics files:
```
Update file: NAVIGATOR/ops_metrics/{{FILENAME}}.md

@web search "{{INDUSTRY}}" KPIs benchmarks operational metrics:
- Industry-standard metrics
- Benchmark performance levels
- {{ARCHETYPE}}-appropriate KPIs
- Operational excellence indicators

Create dashboards showing:
- Current vs target state
- Industry comparisons
- Improvement opportunities
```

#### For process_docs files:
```
Update file: NAVIGATOR/process_docs/{{FILENAME}}.md

Research operational best practices:
- Core processes for {{INDUSTRY}}
- Automation opportunities
- Efficiency improvements
- Scalability considerations
```

#### For sales_marketing files:
```
Update file: NAVIGATOR/sales_marketing/{{FILENAME}}.md

@web search "{{INDUSTRY}}" sales benchmarks customer acquisition:
- CAC benchmarks
- Sales cycle data
- Conversion rates
- Growth strategies
- Channel effectiveness
```

### Step 5: MAESTRO Research Phase (15 min)
Update MAESTRO files with technology intelligence:

#### For tech_stack files:
```
Update file: MAESTRO/tech_stack/{{FILENAME}}.md

@web search "{{COMPANY_NAME}}" technology BuiltWith job posti