---
description: 2 - Enhanced Classification
---

# two_classification_enhanced
Intelligently analyze and classify the business using multiple factors

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
- Business Model: {{B2B/B2C/B2B2C}}
- Growth Indicators: {{RECENT_FUNDING/HIRING/EXPANSION}}
```

### Step 2: Multi-Factor Archetype Determination (3 min)
```
Calculate Classification Score based on multiple factors:

FACTOR 1: Company Size (40% weight)
- 1-10 employees → 1 point
- 11-50 employees → 2 points
- 51-200 employees → 3 points
- 201-500 employees → 4 points
- 500+ employees → 5 points

FACTOR 2: Revenue/Funding (30% weight)
- Pre-revenue → 1 point
- <$1M revenue or seed funding → 2 points
- $1M-$10M revenue or Series A → 3 points
- $10M-$50M revenue or Series B+ → 4 points
- $50M+ revenue or late stage → 5 points

FACTOR 3: Company Age (15% weight)
- <2 years → 1 point
- 2-5 years → 2 points
- 5-10 years → 3 points
- 10-20 years → 4 points
- 20+ years → 5 points

FACTOR 4: Growth Velocity (15% weight)
@web search "{{COMPANY_NAME}}" growth rate hiring expansion:
- Declining/flat → 1 point
- Slow growth (<20% YoY) → 2 points
- Moderate growth (20-50% YoY) → 3 points
- High growth (50-100% YoY) → 4 points
- Hyper growth (100%+ YoY) → 5 points

WEIGHTED SCORE = (Size*0.4) + (Revenue*0.3) + (Age*0.15) + (Growth*0.15)

Classification:
- 1.0-1.8 → EARLY_STARTUP
- 1.9-2.6 → GROWTH_STARTUP
- 2.7-3.4 → SCALE_UP
- 3.5-4.2 → MID_MARKET
- 4.3-5.0 → ENTERPRISE

SPECIAL CASES:
- If B2C with <50 employees but >$10M revenue → upgrade one level
- If services business → consider revenue more heavily
- If platform business → consider user base/network effects
- Allow manual override with justification

Set: {{ARCHETYPE}} with {{CONFIDENCE_LEVEL}}
```

### Step 3: Business Model Analysis (2 min)
```
Determine primary business model:

PRODUCT COMPANIES:
- SaaS (recurring revenue)
- Software (license/perpetual)
- Hardware (physical products)
- Consumer goods

SERVICE COMPANIES:
- Consulting/Professional services
- Managed services
- Agency/Creative services
- Implementation/Integration

MARKETPLACE/PLATFORM:
- Two-sided marketplace
- Platform ecosystem
- Network effects business

HYBRID MODELS:
- Product-led services
- Service-wrapped products
- Platform + services

Set: {{BUSINESS_MODEL_TYPE}}
This affects which files and metrics matter most
```

### Step 4: Industry Deep Dive (3 min)
```
Enhanced industry analysis with sub-verticals:

TECHNOLOGY:
Sub-verticals:
- Enterprise SaaS → Focus on ARR, churn, expansion
- Developer tools → Focus on adoption, community
- AI/ML → Focus on differentiation, data moats
- Cybersecurity → Focus on trust, compliance
- Infrastructure → Focus on reliability, scale

HEALTHCARE:
Sub-verticals:
- Digital health → Focus on outcomes, engagement
- Medical devices → Focus on regulatory, clinical
- Biotech/Pharma → Focus on pipeline, IP
- Healthcare IT → Focus on interoperability
- Care delivery → Focus on access, quality

FINANCIAL SERVICES:
Sub-verticals:
- Fintech → Focus on user acquisition, regulatory
- Banking → Focus on digital transformation
- Insurance → Focus on risk, customer experience
- Wealth management → Focus on AUM, client retention
- Payments → Focus on volume, take rate

MANUFACTURING:
Sub-verticals:
- Discrete manufacturing → Focus on customization
- Process manufacturing → Focus on efficiency
- Industrial IoT → Focus on data utilization
- Supply chain → Focus on resilience

Set: {{INDUSTRY_SUBVERTICAL}}
Set: {{INDUSTRY_SPECIFIC_FOCUS}}
```

### Step 5: Growth State Analysis (3 min)
```
@web search "{{COMPANY_NAME}}" momentum indicators challenges:

Analyze multiple growth dimensions:

MARKET POSITION:
- Market share trajectory
- Competitive wins/losses
- Brand recognition changes
- Customer sentiment trends

OPERATIONAL HEALTH:
- Hiring velocity and quality
- Product release cadence
- Customer retention metrics
- Operational efficiency trends

FINANCIAL MOMENTUM:
- Revenue growth rate
- Margin improvement
- Cash position changes
- Investment in R&D/growth

STRATEGIC INITIATIVES:
- New market entry
- M&A activity
- Partnership momentum
- Digital transformation progress

Classify growth state with nuance:
- STRUGGLING: Multiple negative indicators
- STABILIZING: Recovering from challenges
- STEADY: Consistent, sustainable growth
- ACCELERATING: Multiple positive catalysts
- TRANSFORMING: Major strategic pivot
- MARKET_LEADING: Dominant position

Set: {{GROWTH_STATE}} with {{KEY_DRIVERS}}
```

### Step 6: Define Contextual Next Level (4 min)
```
Based on {{ARCHETYPE}} + {{BUSINESS_MODEL}} + {{GROWTH_STATE}} + {{INDUSTRY}}:

Generate 3 potential "Next Level" goals:

OPTION 1: {{GOAL_1}}
- Current state: {{WHERE_NOW_1}}
- Future state: {{WHERE_GOING_1}}
- Why this matters: {{RATIONALE_1}}
- Success metrics: {{METRICS_1}}

OPTION 2: {{GOAL_2}}
- Current state: {{WHERE_NOW_2}}
- Future state: {{WHERE_GOING_2}}
- Why this matters: {{RATIONALE_2}}
- Success metrics: {{METRICS_2}}

OPTION 3: {{GOAL_3}}
- Current state: {{WHERE_NOW_3}}
- Future state: {{WHERE_GOING_3}}
- Why this matters: {{RATIONALE_3}}
- Success metrics: {{METRICS_3}}

RECOMMENDED: {{PRIMARY_GOAL}} because {{JUSTIFICATION}}

Allow override: User can select different option or define custom goal
```

### Step 7: Critical Success Factors (3 min)
```
For {{COMPANY_NAME}} achieving {{SELECTED_GOAL}}:

Must-win battles (prioritized):
1. {{BATTLE_1}} 
   - Why critical: {{REASON_1}}
   - How to win: {{APPROACH_1}}
   - Timeline: {{WHEN_1}}

2. {{BATTLE_2}}
   - Why critical: {{REASON_2}}
   - How to win: {{APPROACH_2}}
   - Timeline: {{WHEN_2}}

3. {{BATTLE_3}}
   - Why critical: {{REASON_3}}
   - How to win: {{APPROACH_3}}
   - Timeline: {{WHEN_3}}

Key risks to mitigate:
1. {{RISK_1}} 
   - Probability: {{HIGH/MEDIUM/LOW}}
   - Impact: {{HIGH/MEDIUM/LOW}}
   - Mitigation: {{APPROACH_1}}

2. {{RISK_2}}
   - Probability: {{HIGH/MEDIUM/LOW}}
   - Impact: {{HIGH/MEDIUM/LOW}}
   - Mitigation: {{APPROACH_2}}

Required capabilities:
- {{CAPABILITY_1}}: Current state → Target state
- {{CAPABILITY_2}}: Current state → Target state
- {{CAPABILITY_3}}: Current state → Target state
```

### Step 8: Update Enhanced Classification Report (3 min)
Update existing file: `shared_context/business_classification.md`

```markdown
---
title: "Business Classification - {{COMPANY_NAME}}"
created: "{{TODAY_DATE}}"
classification_version: "2.0"
confidence_level: "{{HIGH/MEDIUM/LOW}}"
---

# Business Classification Report

## Classification Summary
- **Archetype**: {{ARCHETYPE}} (Confidence: {{CONFIDENCE}}%)
- **Business Model**: {{BUSINESS_MODEL_TYPE}}
- **Industry**: {{INDUSTRY}} - {{SUBVERTICAL}}
- **Growth State**: {{GROWTH_STATE}}
- **Classification Method**: Multi-factor analysis v2.0

## Classification Rationale
### Scoring Breakdown
- Size Score: {{SIZE_SCORE}}/5 ({{EMPLOYEE_COUNT}} employees)
- Revenue Score: {{REVENUE_SCORE}}/5 ({{REVENUE_STAGE}})
- Maturity Score: {{AGE_SCORE}}/5 ({{YEARS_OLD}} years)
- Growth Score: {{GROWTH_SCORE}}/5 ({{GROWTH_RATE}}% YoY)
- **Weighted Total**: {{TOTAL_SCORE}}/5

### Special Considerations
{{ANY_SPECIAL_FACTORS_THAT_INFLUENCED_CLASSIFICATION}}

## Business Model Analysis
**Primary Model**: {{BUSINESS_MODEL_TYPE}}
- Revenue Structure: {{REVENUE_STRUCTURE}}
- Customer Type: {{B2B/B2C/B2B2C}}
- Delivery Method: {{DELIVERY_METHOD}}
- Competitive Moat: {{MOAT_TYPE}}

## Growth State Analysis
**Current State**: {{GROWTH_STATE}}

Key Indicators:
- Market Position: {{MARKET_POSITION_SUMMARY}}
- Operational Health: {{OPERATIONAL_SUMMARY}}
- Financial Momentum: {{FINANCIAL_SUMMARY}}
- Strategic Direction: {{STRATEGIC_SUMMARY}}

## Next Level Goals

### Selected Goal: {{PRIMARY_GOAL}}
**From**: {{CURRENT_STATE}}
**To**: {{FUTURE_STATE}}
**Timeline**: {{TIMELINE}}

### Why This Goal
{{DETAILED_JUSTIFICATION}}

### Alternative Goals Considered
1. {{ALT_GOAL_1}} - {{WHY_NOT_1}}
2. {{ALT_GOAL_2}} - {{WHY_NOT_2}}

## Agent Focus Areas

Based on this classification, each agent should prioritize:

**ATLAS** (Strategic Intelligence):
- {{ATLAS_PRIORITY_1}}
- {{ATLAS_PRIORITY_2}}
- {{ATLAS_PRIORITY_3}}

**NAVIGATOR** (Operations Excellence):
- {{NAVIGATOR_PRIORITY_1}}
- {{NAVIGATOR_PRIORITY_2}}
- {{NAVIGATOR_PRIORITY_3}}

**MAESTRO** (Technology Integration):
- {{MAESTRO_PRIORITY_1}}
- {{MAESTRO_PRIORITY_2}}
- {{MAESTRO_PRIORITY_3}}

**CATALYST** (Change & Adoption):
- {{CATALYST_PRIORITY_1}}
- {{CATALYST_PRIORITY_2}}
- {{CATALYST_PRIORITY_3}}
```

### Step 9: Validate & Document
```
✓ Multi-factor classification complete
✓ Business model identified
✓ Growth state analyzed
✓ Contextual goals defined
✓ Success factors documented
✓ Agent priorities customized

Classification Confidence: {{CONFIDENCE_LEVEL}}
Manual Review Needed: {{YES/NO}}

Next: Run three_structure_creation
Time: ~10 minutes
```

## Improvements in This Version

1. **Multi-Factor Scoring**: Uses size, revenue, age, and growth velocity
2. **Business Model Recognition**: Differentiates between product, service, and platform companies
3. **Industry Sub-Verticals**: More specific than generic "Healthcare" or "Technology"
4. **Growth State Nuance**: Six states instead of four, with specific indicators
5. **Goal Optionality**: Provides three goal options instead of one rigid choice
6. **Confidence Scoring**: Indicates how certain the classification is
7. **Manual Override**: Allows human judgment to override algorithmic classification
8. **Special Cases**: Handles edge cases like high-revenue small companies

## Quick Reference

### Classification Formula
```
Score = (Employees × 0.4) + (Revenue × 0.3) + (Age × 0.15) + (Growth × 0.15)
```

### When to Override
- Unusual business models (e.g., 10-person company with $50M revenue)
- Recent pivots or transformations
- Industry-specific considerations
- Merger or acquisition scenarios
