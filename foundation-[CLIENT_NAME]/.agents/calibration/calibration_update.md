# calibration_update
Systematic recalibration of Foundation agents

## Prerequisites
- Existing Foundation with populated files
- Identified need for calibration (via triggers or schedule)
- 1-2 hours depending on scope

## Workflow Execution

### Step 1: Calibration Assessment (10 min)
```
Review all calibration files:
1. Check .agents/calibration/ATLAS_calibration.md
2. Check .agents/calibration/CATALYST_calibration.md
3. Check .agents/calibration/MAESTRO_calibration.md
4. Check .agents/calibration/NAVIGATOR_calibration.md

For each, identify:
- Which triggers are active?
- When was last calibration?
- What metrics are off target?
```

### Step 2: Determine Calibration Scope (5 min)
```
Based on triggers, classify update needed:

MINOR (Parameters only):
- Metrics drift < 20%
- No leadership changes
- Same strategy/market
- Time: 30 minutes

MAJOR (Agent persona update):
- Significant metric shifts
- New leadership/strategy
- Market position change
- Time: 60 minutes

TRANSFORMATIONAL (Full rebuild):
- Company pivot
- M&A event
- Crisis response
- Time: 2+ hours
```

### Step 3: Gather Change Intelligence (15 min)

#### Internal Changes
```
Review recent updates:
- Board/investor presentations
- All-hands communications
- Strategy documents
- Organizational changes
- New initiatives
```

#### External Changes
```
@web search "[COMPANY_NAME] news since [LAST_CALIBRATION_DATE]"
@web search "[COMPANY_NAME] leadership changes announcements"
@web search "[INDUSTRY] market shifts [CURRENT_QUARTER]"
@web search "[COMPANY_NAME] employee sentiment Glassdoor recent"
```

### Step 4: Update Calibration Files (10 min)

For each agent needing calibration:

#### Update Current State
```markdown
## Current Calibration State
- Previous: [WHAT_IT_WAS]
- Current: [WHAT_IT_IS_NOW]
- Change Driver: [WHY_IT_CHANGED]
```

#### Update Parameters
Adjust based on changes:
- Strategic focus (ATLAS)
- Cultural profile (CATALYST)
- Tech maturity (MAESTRO)
- Operational state (NAVIGATOR)

#### Version the Change
```markdown
### Version [X.X] - [TODAY_DATE]
- Trigger: [WHAT_TRIGGERED_THIS]
- Updates: [WHAT_WAS_CHANGED]
- New Focus: [NEW_PRIORITIES]
- Expected Impact: [WHAT_SHOULD_IMPROVE]
```

### Step 5: Update Agent Personas (15 min for MAJOR only)

If MAJOR calibration needed:

#### For ATLAS
Update `.agents/ATLAS.md`:
- Adjust strategic horizon
- Modify risk tolerance
- Update industry language
- Revise key questions

#### For CATALYST
Update `.agents/CATALYST.md`:
- Adjust change velocity
- Modify communication style
- Update cultural references
- Revise engagement approach

#### For MAESTRO
Update `.agents/MAESTRO.md`:
- Adjust tech sophistication
- Modify innovation stance
- Update architecture preferences
- Revise build/buy bias

#### For NAVIGATOR
Update `.agents/NAVIGATOR.md`:
- Adjust optimization focus
- Modify metric priorities
- Update efficiency targets
- Revise process approach

### Step 6: Refresh Knowledge Files (20 min)

Based on calibration scope:

#### MINOR Updates (Top 3 files per agent)
```
ATLAS:
- Update market_landscape/key_trends.md
- Update competitors/competitive_position.md
- Update strategy/strategic_priorities.md

CATALYST:
- Update sentiment/employee_pulse.md
- Update change_assets/transformation_status.md
- Update culture/values_evolution.md

MAESTRO:
- Update tech_stack/current_state.md
- Update innovation/tech_priorities.md
- Update architecture/target_state.md

NAVIGATOR:
- Update metrics/kpi_dashboard.md
- Update operations/bottlenecks.md
- Update scaling/capacity_plan.md
```

#### MAJOR Updates (5-10 files per agent)
Expand to include secondary files based on change areas

### Step 7: Validation Testing (10 min)

Test each recalibrated agent:

#### Context Awareness Test
```
@[AGENT] "How does [RECENT_CHANGE] affect our approach?"
Expected: Agent acknowledges and incorporates change
```

#### Alignment Test
```
@[AGENT] "What are our top priorities given [NEW_DIRECTION]?"
Expected: Priorities reflect recalibration
```

#### Cross-Agent Coherence
```
@ATLAS @CATALYST @MAESTRO @NAVIGATOR 
"How should we respond to [MAJOR_CHANGE]?"
Expected: Coordinated, aligned responses
```

### Step 8: Document Calibration (5 min)

Create calibration record:

Update/Create: `shared_context/calibration_log.md`

```markdown
# Calibration Log

## Calibration Event - [DATE]

### Trigger
[What prompted this calibration]

### Scope
- Type: [MINOR/MAJOR/TRANSFORMATIONAL]
- Agents Affected: [LIST]
- Time Invested: [HOURS]

### Changes Made
1. [SPECIFIC_CHANGE_1]
2. [SPECIFIC_CHANGE_2]
3. [SPECIFIC_CHANGE_3]

### Files Updated
- [COUNT] calibration files
- [COUNT] agent personas
- [COUNT] knowledge files

### Validation Results
- ✅ [TEST_1]: [RESULT]
- ✅ [TEST_2]: [RESULT]
- ⚠️ [TEST_3]: [ISSUE_TO_MONITOR]

### Next Review
- ATLAS: [DATE]
- CATALYST: [DATE]
- MAESTRO: [DATE]
- NAVIGATOR: [DATE]

### Notes
[Lessons learned, things to watch, recommendations]
```

### Step 9: Set Next Review (5 min)
```
Update calendar with next review dates:
- NAVIGATOR: +30 days
- CATALYST: +60 days
- ATLAS: +90 days
- MAESTRO: +90 days

Set reminders 1 week before each date
```

### Step 10: Complete
```
✓ Calibration triggers assessed
✓ Changes documented
✓ Agents updated as needed
✓ Knowledge refreshed
✓ Validation complete
✓ Version recorded
✓ Next review scheduled

Calibration Status: COMPLETE
Foundation Version: [NEW_VERSION]
```

## Quick Reference

### When to Run This Workflow

**Scheduled**: Per calibration file review dates
**Triggered**: When triggers fire
**Proactive**: Before major initiatives

### Time Estimates
- **MINOR**: 30-45 minutes
- **MAJOR**: 60-90 minutes  
- **TRANSFORMATIONAL**: 2-4 hours

### Success Criteria
- Agents reflect current reality
- Recommendations are actionable
- Cross-agent alignment achieved
- Team notices improvement

---

*Remember: Regular calibration is preventive maintenance for your AI executives. Small, frequent updates prevent major overhauls.*