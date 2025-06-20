# Foundation™ Complete Pipeline
End-to-end workflow from URL to fully populated Foundation

## Overview
This master workflow orchestrates all phases of Foundation™ creation:
1. Discovery → 2. Classification → 3. Agent Generation → 4. Structure → 5. Research

Total Time: 60-90 minutes for comprehensive Foundation

## Prerequisites
- Clean Foundation template repository
- Access to all sub-workflows
- Company URL or LinkedIn profile

## Master Workflow Execution

### Phase 0: Initialize (2 minutes)
```
Welcome to Foundation™ Complete Pipeline!

This workflow will create a comprehensive AI intelligence system for your target company.

Please provide:
1. Company website URL or LinkedIn profile: {{COMPANY_URL}}
2. Any specific focus areas (optional): {{FOCUS_AREAS}}
3. Time preference:
   - Quick (30 min) - Essential files only
   - Standard (60 min) - Recommended
   - Comprehensive (90 min) - All files

Proceeding with: {{TIME_PREFERENCE}} approach
```

Create tracking file: `FOUNDATION_STATUS.md`
```markdown
# Foundation™ Creation Status

**Company**: {{COMPANY_NAME}}
**Started**: {{TIMESTAMP}}
**Target Completion**: {{TARGET_TIME}}

## Progress Tracker
- [ ] Phase 1: Discovery
- [ ] Phase 2: Classification  
- [ ] Phase 3: Agent Generation
- [ ] Phase 4: Structure Creation
- [ ] Phase 5: Research Population
- [ ] Phase 6: Validation

## Current Status
🔄 Phase 1 in progress...
```

### Phase 1: Discovery (10-15 minutes)
```
Starting Discovery Phase...
Executing: /01_discovery

[Follow all steps in 01_discovery.md workflow]
```

**Validation Checkpoint**:
- ✓ `shared_context/company_overview.md` exists
- ✓ No placeholder text remains
- ✓ Employee count identified
- ✓ Industry classified
- ✓ Recent news included

Update `FOUNDATION_STATUS.md`:
```
✓ Phase 1: Discovery - Complete
  - Company: {{COMPANY_NAME}}
  - Employees: {{COUNT}}
  - Industry: {{INDUSTRY}}
🔄 Phase 2 in progress...
```

### Phase 2: Classification (10 minutes)
```
Starting Classification Phase...
Executing: /02_classification

[Follow all steps in 02_classification.md workflow]
```

**Validation Checkpoint**:
- ✓ `shared_context/business_classification.md` exists
- ✓ Archetype determined
- ✓ Next level goals defined
- ✓ Focus areas identified

Update `FOUNDATION_STATUS.md`:
```
✓ Phase 2: Classification - Complete
  - Archetype: {{ARCHETYPE}}
  - Next Level: {{TRANSFORMATION}}
🔄 Phase 3 in progress...
```

### Phase 3: Agent Generation (20-30 minutes)
```
Starting Agent Generation Phase...
This is the most critical phase - taking extra care...

Executing: /03_agent_generation

[Follow all steps in 03_agent_generation.md workflow]
```

**Quality Gate** - Each agent must score ≥7/10 on:
- Specificity to company
- Relevance to goals
- Industry expertise
- Actionability
- Differentiation

If any agent scores <7, iterate until quality achieved.

Update `FOUNDATION_STATUS.md`:
```
✓ Phase 3: Agent Generation - Complete
  - ATLAS: {{SCORE}}/10
  - NAVIGATOR: {{SCORE}}/10
  - MAESTRO: {{SCORE}}/10
  - CATALYST: {{SCORE}}/10
🔄 Phase 4 in progress...
```

### Phase 4: Structure Creation (5 minutes)
```
Starting Structure Creation Phase...
Creating {{ARCHETYPE}}-specific file structure...

Based on classification:
- Archetype: {{ARCHETYPE}}
- Industry: {{INDUSTRY_OVERLAY}}
- Focus: {{FOCUS_AREAS}}

Creating targeted files:
```

#### For EARLY_STARTUP:
```
Creating startup-focused structure:
- CATALYST/market_validation/
- ATLAS/funding_strategy/
- NAVIGATOR/startup_metrics/
- MAESTRO/mvp_architecture/
Total: 15-18 files
```

#### For GROWTH_COMPANY:
```
Creating growth-focused structure:
- CATALYST/culture_scaling/
- ATLAS/expansion_strategy/
- NAVIGATOR/unit_economics/
- MAESTRO/platform_scaling/
Total: 18-22 files
```

#### For ENTERPRISE:
```
Creating transformation-focused structure:
- CATALYST/change_readiness/
- ATLAS/disruption_radar/
- NAVIGATOR/operational_excellence/
- MAESTRO/legacy_modernization/
Total: 22-28 files
```

Update `FOUNDATION_STATUS.md`:
```
✓ Phase 4: Structure Creation - Complete
  - Files created: {{COUNT}}
  - Customized for: {{ARCHETYPE}}
🔄 Phase 5 in progress...
```

### Phase 5: Research Population (20-40 minutes)

Based on time preference and archetype:

#### Quick Version (20 minutes):
```
Populating essential files only:

1. CATALYST Quick Intelligence (5 min)
   @web search "{{COMPANY_NAME}}" sentiment news reviews culture
   → Update: sentiment/internal_sentiment.md
   → Update: sentiment/external_perception.md

2. ATLAS Strategic Essentials (5 min)
   @web search "{{INDUSTRY}}" market size trends {{YEAR}}
   → Update: market_landscape/industry_analysis.md
   @web search "{{COMPANY_NAME}}" competitors
   → Update: competitors/competitive_landscape.md

3. NAVIGATOR Key Metrics (5 min)
   @web search "{{COMPANY_NAME}}" metrics KPIs performance
   → Update: metrics/kpi_dashboard.md

4. MAESTRO Tech Snapshot (5 min)
   @web search "{{COMPANY_NAME}}" technology stack BuiltWith
   → Update: current_state/tech_stack_audit.md
```

#### Standard Version (40 minutes):
```
[Full research as specified in archetype needs]
```

Update files with progress indicator:
```
Populating: {{CURRENT_FILE}}
Progress: {{X}}/{{TOTAL}} files complete
Time elapsed: {{MINUTES}} minutes
```

### Phase 6: Validation & Testing (5-10 minutes)

#### Agent Responsiveness Test:
```
Testing agent intelligence...

@ATLAS "What's the biggest opportunity for {{COMPANY_NAME}} to reach {{NEXT_LEVEL}}?"
Expected: Specific strategic insight
Result: {{PASS/FAIL}}

@NAVIGATOR "What should {{COMPANY_NAME}} measure to track progress?"
Expected: Relevant KPIs for their stage
Result: {{PASS/FAIL}}

@MAESTRO "What technology investment would give {{COMPANY_NAME}} the most leverage?"
Expected: Practical tech recommendation
Result: {{PASS/FAIL}}

@CATALYST "What's the biggest change risk for {{COMPANY_NAME}}?"
Expected: Culture/people insight
Result: {{PASS/FAIL}}
```

#### Cross-Agent Synthesis Test:
```
@ATLAS @NAVIGATOR @MAESTRO @CATALYST 
"If {{COMPANY_NAME}} could only focus on one initiative this quarter, what should it be?"

Expected: Coordinated response showing agent alignment
Result: {{PASS/FAIL}}
```

#### File Completeness Check:
```python
# Run validation script
python .scripts/reporting/validate_completion.py

Checking:
- [ ] All required files have content
- [ ] No placeholder text remains
- [ ] YAML headers are valid
- [ ] Agent scope permissions correct
- [ ] Cross-references working
```

### Phase 7: Final Deliverables

#### Generate Executive Summary:
Create: `EXECUTIVE_SUMMARY.md`

```markdown
# Foundation™ Executive Summary
## {{COMPANY_NAME}}

### AI Intelligence System Ready
Your Foundation™ is configured with four AI executives who understand:
- Your industry: {{INDUSTRY}}
- Your stage: {{ARCHETYPE}}
- Your goals: {{NEXT_LEVEL}}
- Your challenges: {{KEY_CHALLENGES}}

### Key Insights Discovered

#### Strategic (ATLAS)
- **Opportunity**: {{TOP_OPPORTUNITY}}
- **Threat**: {{TOP_THREAT}}
- **Recommendation**: {{STRATEGIC_REC}}

#### Operational (NAVIGATOR)
- **Bottleneck**: {{KEY_BOTTLENECK}}
- **Quick Win**: {{QUICK_WIN}}
- **Metric Focus**: {{KEY_METRIC}}

#### Technical (MAESTRO)
- **Priority**: {{TECH_PRIORITY}}
- **Investment**: {{TECH_INVEST}}
- **Risk**: {{TECH_RISK}}

#### Cultural (CATALYST)
- **Strength**: {{CULTURE_STRENGTH}}
- **Gap**: {{CULTURE_GAP}}
- **Action**: {{CULTURE_ACTION}}

### Recommended Next Steps
1. {{IMMEDIATE_ACTION_1}}
2. {{IMMEDIATE_ACTION_2}}
3. {{IMMEDIATE_ACTION_3}}

### How to Use Your Foundation™
- Ask any agent for specific guidance
- Update monthly with new intelligence
- Track progress against next-level goals
- Expand with internal data when ready

Created: {{DATE}}
Time to Complete: {{ACTUAL_TIME}}
Files Generated: {{FILE_COUNT}}
```

#### Update Foundation Status:
Final update to `FOUNDATION_STATUS.md`:

```markdown
# Foundation™ Creation Status

**Company**: {{COMPANY_NAME}}
**Started**: {{START_TIME}}
**Completed**: {{END_TIME}}
**Total Time**: {{DURATION}}

## Progress Tracker
- [x] Phase 1: Discovery - 12 min
- [x] Phase 2: Classification - 8 min
- [x] Phase 3: Agent Generation - 25 min
- [x] Phase 4: Structure Creation - 5 min
- [x] Phase 5: Research Population - 35 min
- [x] Phase 6: Validation - 5 min

## Final Statistics
- Files Created: {{TOTAL_FILES}}
- Research Queries: {{QUERY_COUNT}}
- Agent Quality Average: {{AVG_SCORE}}/10
- Actionable Insights: {{INSIGHT_COUNT}}

## Quality Metrics
- Company Specificity: ✓ High
- Industry Relevance: ✓ High
- Next-Level Focus: ✓ Aligned
- Actionability: ✓ Practical

## Delivery Ready
Foundation™ is complete and ready for use!
```

### Error Handling

#### If web search returns limited results:
```
Fallback search strategies:
1. Try company name + location
2. Search for founder/CEO name + company
3. Check industry reports mentioning company
4. Use competitor analysis to infer
5. Flag as "Limited public data" and continue
```

#### If classification is ambiguous:
```
Default classifications:
- Unknown size → Default to MID_MARKET
- Unknown industry → Use GENERAL_BUSINESS
- Mixed signals → Choose more mature archetype
- Note ambiguity in classification report
```

#### If agent generation fails quality check:
```
Recovery process:
1. Review calibration files
2. Enhance with more specific context
3. Regenerate with stricter prompts
4. Manual adjustment if needed
5. Document any manual changes
```

### Success Celebration 🎉

```
╔════════════════════════════════════════╗
║   Foundation™ Creation Complete!       ║
╠════════════════════════════════════════╣
║ Company: {{COMPANY_NAME}}              ║
║ Time: {{DURATION}}                     ║
║ Quality: {{QUALITY_SCORE}}/10          ║
╠════════════════════════════════════════╣
║ Your AI executives are ready to help   ║
║ {{COMPANY_NAME}} reach the next level! ║
╚════════════════════════════════════════╝

Next: Share EXECUTIVE_SUMMARY.md with client
```

## Workflow Variations

### `/complete_pipeline_quick` (30 minutes)
- Phases 1-3: Full (no shortcuts on agents)
- Phase 4: Minimal structure (10-12 files)
- Phase 5: Essential research only
- Best for: Demos, initial assessments

### `/complete_pipeline_deep` (2 hours)
- All phases extended
- Additional validation loops
- Comprehensive research
- Internal data integration prep
- Best for: Full client deployments

## This is the Way
Follow this pipeline for consistent, high-quality Foundation™ delivery every time!