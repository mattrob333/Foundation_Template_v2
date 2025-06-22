# Foundation™ Calibration System Guide

## Overview

The Foundation™ Calibration System ensures your AI executives stay relevant and valuable as your company evolves. Each agent has a calibration file that tracks changes, triggers updates, and guides recalibration.

## Why Calibration Matters

Companies change. They pivot, grow, acquire, transform. Your AI executives must evolve with these changes to remain valuable advisors. The calibration system:

- **Versions** your Foundation's intelligence
- **Triggers** updates based on business changes
- **Guides** the recalibration process
- **Tracks** effectiveness over time

## Calibration Files Structure

Each calibration file (in `.agents/calibration/`) contains:

1. **Current State**: Where the company/agent is now
2. **Triggers**: What changes require recalibration
3. **Data Sources**: Where to get updated information
4. **Process**: How to recalibrate
5. **Version History**: What changed and when
6. **Metrics**: How well calibration is working

## Calibration Schedule

### NAVIGATOR - Monthly Review
*Most frequent calibration due to operational dynamics*
- Operations change rapidly
- KPIs shift with business needs
- Process improvements are ongoing
- Weekly monitoring of key metrics

### CATALYST - Bi-Monthly Review
*Culture and change readiness fluctuate*
- Employee sentiment is volatile
- Change initiatives have phases
- Leadership impacts are immediate
- Monthly monitoring of culture health

### ATLAS & MAESTRO - Quarterly Review
*Strategic and technical changes are less frequent*
- Strategy evolves gradually
- Technology decisions have longer cycles
- Market positions shift slowly
- Monthly monitoring of key indicators

## Calibration Triggers

### 🚨 Immediate Calibration Required
Drop everything and recalibrate when:
- Leadership changes (C-suite)
- Major pivot or strategy shift
- Merger, acquisition, or sale
- Crisis event (breach, scandal, failure)
- Regulatory bombshell

### ⚠️ Scheduled Review Triggers
Regular calibration when:
- Metrics shift significantly
- New initiatives launch
- Growth stage changes
- Competitive landscape shifts
- Technology platform changes

### 📊 Monitoring Triggers
Watch for trends in:
- Performance metrics
- Employee sentiment
- Market dynamics
- Technical debt
- Customer feedback

## Calibration Process

### Step 1: Detect Change
Use calibration file triggers to identify what changed:
```
@ATLAS Check ATLAS_calibration.md triggers - which apply?
@NAVIGATOR Review operational metrics - what shifted?
@MAESTRO Assess tech stack changes - what's new?
@CATALYST Evaluate culture shifts - what's different?
```

### Step 2: Assess Impact
Determine calibration scope:
- **Minor**: Update parameters only
- **Major**: Revise agent persona
- **Transformational**: Rebuild knowledge base

### Step 3: Gather New Data
Use data sources from calibration files:
```
# Internal data
- Review new strategic documents
- Analyze updated metrics
- Interview key stakeholders

# External data
@web search "[COMPANY] latest news strategy"
@web search "[INDUSTRY] trends [CURRENT_YEAR]"
@web search "[COMPANY] employee sentiment"
```

### Step 4: Update Components
Based on impact assessment:

**Minor Updates**:
1. Update calibration file parameters
2. Refresh 2-3 key knowledge files
3. Test with validation queries

**Major Updates**:
1. Revise agent persona in `.agents/[AGENT].md`
2. Update 5-10 knowledge files
3. Adjust agent communication style
4. Comprehensive testing

**Transformational Updates**:
1. Re-run classification workflow
2. Adjust file structure if needed
3. Regenerate agent personas
4. Rebuild knowledge base
5. Full validation suite

### Step 5: Version & Document
Record in calibration file:
```markdown
### Version X.X - [DATE]
- Trigger: [What caused recalibration]
- Updates: [What was changed]
- New Focus: [Updated priorities]
- Results: [Measured outcomes]
```

## Using Calibration for Version Control

### Version Numbering
- **Major.Minor.Patch** (e.g., 2.1.3)
- **Major**: Transformational changes (pivot, M&A)
- **Minor**: Significant updates (new strategy, reorg)
- **Patch**: Regular maintenance updates

### Branching Strategy
For major calibrations:
```bash
# Create calibration branch
git checkout -b calibration-v2.0-series-b

# Make updates across files
# Test thoroughly
# Merge when validated

git checkout main
git merge calibration-v2.0-series-b
git tag -a v2.0 -m "Post-Series B calibration"
```

### Rollback Capability
If calibration causes issues:
```bash
# Revert to previous version
git checkout v1.9

# Or restore specific agent
git checkout v1.9 -- .agents/ATLAS.md
```

## Measuring Calibration Success

### Effectiveness Metrics

Each calibration file tracks:
- **Insight Relevance**: Are recommendations applicable?
- **Prediction Accuracy**: Do forecasts materialize?
- **Actionability**: Can you act on the advice?
- **Alignment**: Does it match company reality?

### Success Indicators

Good calibration shows:
- ✅ Agents reference recent changes naturally
- ✅ Recommendations align with new strategy
- ✅ Metrics match current priorities
- ✅ Language reflects cultural shifts
- ✅ Insights feel fresh and relevant

### Warning Signs

Recalibration needed when:
- ❌ Agents seem out of touch
- ❌ Recommendations feel stale
- ❌ Metrics don't match reality
- ❌ Cultural references are outdated
- ❌ Strategic advice misaligned

## Best Practices

### 1. Regular Reviews
- Set calendar reminders for reviews
- Don't wait for triggers - be proactive
- Quick checks better than perfect delays

### 2. Incremental Updates
- Small, frequent calibrations > major overhauls
- Update most relevant files first
- Test as you go

### 3. Team Involvement
- Interview stakeholders for changes
- Validate with subject matter experts
- Get feedback on calibration results

### 4. Documentation
- Always update version history
- Note what worked/didn't work
- Build calibration knowledge over time

### 5. Automation Opportunities
- Set up alerts for trigger metrics
- Automate data gathering where possible
- Create calibration templates

## Quick Calibration Checklist

When calibrating any agent:
- [ ] Review calibration file triggers
- [ ] Assess change magnitude
- [ ] Gather fresh data
- [ ] Update agent parameters
- [ ] Refresh relevant knowledge files
- [ ] Test with validation queries
- [ ] Document version changes
- [ ] Update next review date
- [ ] Communicate changes to team

## Conclusion

Calibration transforms Foundation™ from a static system to a living intelligence platform. Regular calibration ensures your AI executives grow with your company, providing increasingly valuable insights.

Remember: The best calibration is the one that happens. Don't aim for perfection - aim for continuous improvement.

---

*Start your first calibration by reviewing each agent's calibration file and setting review dates in your calendar.*