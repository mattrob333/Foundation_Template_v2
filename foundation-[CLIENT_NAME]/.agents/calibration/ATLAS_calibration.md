# ATLAS Strategic Intelligence Calibration

---
calibration_version: 1.0
last_calibrated: [DATE]
next_review: [DATE + 90 days]
agent: ATLAS
---

## Current Calibration State

### Company Context
- **Company**: [COMPANY_NAME]
- **Industry**: [INDUSTRY]
- **Archetype**: [EARLY_STARTUP | GROWTH_STARTUP | SCALE_UP | MID_MARKET | ENTERPRISE]
- **Strategic Focus**: [CURRENT_STRATEGIC_PRIORITY]
- **Market Position**: [LEADER | CHALLENGER | FOLLOWER | NICHE]

### Strategic Parameters
- **Planning Horizon**: [6 months | 12 months | 18 months | 3 years]
- **Risk Tolerance**: [Conservative | Moderate | Aggressive]
- **Growth Strategy**: [Organic | M&A | Platform | Geographic]
- **Innovation Approach**: [Fast Follower | Pioneer | Disruptor]

## Calibration Triggers

Monitor these signals for recalibration needs:

### 🚨 Immediate Recalibration Required
- [ ] Company pivot or major strategy shift
- [ ] Merger, acquisition, or divestiture
- [ ] New CEO or strategic leadership change
- [ ] Market disruption or black swan event
- [ ] Regulatory change affecting core business

### ⚠️ Quarterly Review Triggers
- [ ] Revenue growth rate change >20%
- [ ] Employee count change >30%
- [ ] New funding round or IPO
- [ ] Major competitor entry/exit
- [ ] Geographic expansion

### 📊 Monthly Monitoring
- [ ] Competitive landscape shifts
- [ ] Market share changes
- [ ] Strategic initiative progress
- [ ] Industry trend acceleration

## Data Sources for Recalibration

### Internal Sources
1. **Strategic Documents**
   - Location: `shared_context/strategic_plans/`
   - Update: Board decks, strategic planning docs
   - Frequency: Quarterly

2. **Financial Performance**
   - Location: `ATLAS/finance/`
   - Update: Revenue, growth rates, burn rate
   - Frequency: Monthly

3. **Leadership Communications**
   - Source: All-hands, investor updates
   - Extract: Strategic priorities, vision changes
   - Frequency: As released

### External Sources
1. **Market Intelligence**
   ```
   @web search "[COMPANY_NAME] strategy announcement"
   @web search "[INDUSTRY] market trends [CURRENT_YEAR]"
   @web search "[COMPANY_NAME] competitive positioning"
   ```

2. **Competitive Moves**
   ```
   @web search "[TOP_COMPETITORS] strategic initiatives"
   @web search "[INDUSTRY] M&A activity"
   @web search "[MARKET] disruption threats"
   ```

3. **Industry Analysis**
   - Sources: Gartner, Forrester, CB Insights
   - Focus: Market size, growth, trends
   - Frequency: Quarterly

## Recalibration Process

### Step 1: Assess Change Magnitude
```markdown
Change Assessment:
- Current State: [DESCRIBE]
- New State: [DESCRIBE]
- Impact Level: [Low | Medium | High | Transformational]
- Affected Areas: [List strategic areas]
```

### Step 2: Update Core Parameters
1. **Update company context** in this file
2. **Revise strategic focus** based on new reality
3. **Adjust planning horizon** if needed
4. **Modify risk tolerance** per new strategy

### Step 3: Update ATLAS Persona
Edit `.agents/ATLAS.md`:
- Adjust "My Mission" section
- Update "Key Questions I Always Ask"
- Revise strategic frameworks used
- Modify industry-specific language

### Step 4: Refresh Knowledge Base
Priority files to update:
1. `ATLAS/market_landscape/industry_analysis.md`
2. `ATLAS/competitors/competitive_landscape.md`
3. `ATLAS/strategy/strategic_options.md`
4. `ATLAS/finance/financial_projections.md`

### Step 5: Validate Calibration
Test queries:
```
@ATLAS "Given our new [CHANGE], what strategic opportunities emerge?"
@ATLAS "How does [CHANGE] affect our competitive position?"
@ATLAS "What are the top 3 strategic risks we now face?"
```

Expected: Responses reflect new strategic reality

## Version History

### Version 1.0 - [DATE]
- Initial calibration
- Company: [STAGE/SIZE]
- Focus: [STRATEGIC_PRIORITY]
- Key Challenge: [MAIN_CHALLENGE]

### Version X.X - [DATE]
- Trigger: [WHAT_CHANGED]
- Updates: [WHAT_WAS_MODIFIED]
- New Focus: [NEW_PRIORITY]
- Outcome: [RESULT]

## Calibration Metrics

Track these to measure calibration effectiveness:

| Metric | Target | Current | Status |
|--------|--------|---------|---------|
| Strategic Insight Relevance | >90% | [X]% | [🟢🟡🔴] |
| Prediction Accuracy | >70% | [X]% | [🟢🟡🔴] |
| Executive Alignment | >85% | [X]% | [🟢🟡🔴] |
| Actionability Score | >80% | [X]% | [🟢🟡🔴] |

## Next Steps

1. **Scheduled Review**: [DATE]
2. **Monitor**: [KEY_METRICS_TO_WATCH]
3. **Prepare**: [UPCOMING_STRATEGIC_DECISIONS]
4. **Update**: [FILES_NEEDING_REFRESH]

---

*Calibration Note: ATLAS becomes more valuable with each calibration cycle. Track what works and refine continuously.*