---
description: Research_Population
---

# /05_research_population
Populate all files with targeted intelligence

## Prerequisites
- All previous workflows completed
- Empty files created with headers
- Structure report available

## Workflow Execution

### Step 1: Load Research Plan (2 min)
```
Read from:
1. shared_context/structure_report.md → {{FILE_LIST}}
2. shared_context/business_classification.md → {{FOCUS_AREAS}}
3. shared_context/next_level_goals.md → {{TRANSFORMATION}}

Identify:
- High priority files to populate first
- Research themes based on transformation
- Industry-specific data needs
```

### Step 2: CATALYST Research Phase (15 min)
Update CATALYST files with market intelligence:

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

@web search "{{COMPANY_NAME}}" technology BuiltWith job postings:
- Current technology indicators
- Industry-standard platforms
- Technology gaps
- Modernization opportunities
- Integration needs

Include:
- Current state assessment
- Target architecture
- Migration path
- Cost/benefit analysis
```

#### For talent files:
```
Update file: MAESTRO/talent/{{FILENAME}}.md

@web search "{{INDUSTRY}}" technical skills hiring developer salaries:
- Required technical skills
- Talent availability
- Compensation benchmarks
- Skill gap analysis
- Hiring strategies
```

#### For workflow_opportunities files:
```
Update file: MAESTRO/workflow_opportunities/{{FILENAME}}.md

Identify automation/integration opportunities:
- High-impact automations
- ROI calculations
- Implementation complexity
- Quick wins vs long-term
- Platform recommendations
```

### Step 6: Cross-Reference Integration (10 min)
Update files with cross-references:

```
For each populated file:
1. Add "Related Intelligence" section
2. Link to relevant files in other agents
3. Note dependencies and connections
4. Highlight conflicts or gaps

Example:
## Related Intelligence
- See ATLAS/competitors/competitive_matrix.md for market context
- See NAVIGATOR/ops_metrics/efficiency_benchmarks.md for targets
- See CATALYST/change_assets/readiness_assessment.md for adoption
```

### Step 7: Quality Validation (5 min)
Run validation checks:

```
@ATLAS Can you access all market intelligence files?
Expected: "I can see {{COUNT}} files with market data including..."

@NAVIGATOR Can you see the operational metrics?
Expected: "Yes, I have access to KPIs showing..."

@MAESTRO Can you read the technology assessments?
Expected: "I can see the tech stack analysis..."

@CATALYST Can you access change readiness data?
Expected: "I have visibility into sentiment and readiness..."
```

### Step 8: Create Research Summary (3 min)
Create new file: `shared_context/research_summary.md`

```markdown
---
title: "Research Summary - {{COMPANY_NAME}}"
created: "{{TODAY_DATE}}"
---

# Foundation Research Summary

## Research Statistics
- Files populated: {{COUNT}}
- Research queries: {{QUERIES}}
- Data sources: {{SOURCES}}
- Time invested: {{TIME}}

## Key Insights Discovered

### Strategic (ATLAS)
1. {{KEY_INSIGHT_1}}
2. {{KEY_INSIGHT_2}}
3. {{KEY_INSIGHT_3}}

### Operational (NAVIGATOR)
1. {{KEY_INSIGHT_1}}
2. {{KEY_INSIGHT_2}}
3. {{KEY_INSIGHT_3}}

### Technical (MAESTRO)
1. {{KEY_INSIGHT_1}}
2. {{KEY_INSIGHT_2}}
3. {{KEY_INSIGHT_3}}

### Cultural (CATALYST)
1. {{KEY_INSIGHT_1}}
2. {{KEY_INSIGHT_2}}
3. {{KEY_INSIGHT_3}}

## Recommended Next Steps
Based on research findings:

Immediate (This Week):
1. {{ACTION_1}}
2. {{ACTION_2}}

Short-term (This Month):
3. {{ACTION_3}}
4. {{ACTION_4}}

Medium-term (This Quarter):
5. {{ACTION_5}}
6. {{ACTION_6}}

## Data Gaps Identified
Areas needing internal data:
- {{GAP_1}}
- {{GAP_2}}
- {{GAP_3}}

## Foundation Ready
✓ All agents have contextual knowledge
✓ Transformation path researched
✓ Industry intelligence gathered
✓ Ready for client activation
```

### Step 9: Complete
```
✓ All files populated with intelligence
✓ Cross-references added
✓ Agents validated
✓ Research summary created

Foundation Status: READY FOR DEPLOYMENT
Total Time: ~60 minutes
Files Updated: {{COUNT}}
```

## Research Tips

**Prioritize Quality over Quantity:**
- Better to have 15 well-researched files than 25 sparse ones
- Focus on transformation-critical intelligence
- Use specific, current data

**Industry-Specific Focus:**
- Tech companies: Focus on metrics, competition, talent
- Manufacturing: Focus on operations, automation, supply chain
- Services: Focus on talent, client success, efficiency

**Archetype-Specific Depth:**
- Startups: More validation, less process documentation
- Scale-ups: Balance of strategy and operations
- Enterprises: Deep transformation and innovation focus