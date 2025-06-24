# Validation Checklist Templates

## Quick Reference Guide
Use these templates at each workflow stage to ensure quality and completeness.

---

## 🔍 Discovery Validation (Workflow 1)

```markdown
### Discovery Checklist - {{COMPANY_NAME}}
Date: _________ Reviewer: _________

**REQUIRED (Must have all)**
- [ ] Company legal name with source
- [ ] Official website verified
- [ ] Headquarters location confirmed
- [ ] Industry classification (NAICS/SIC)
- [ ] Employee range from LinkedIn

**DATA QUALITY**
- [ ] All sources cited
- [ ] Sources < 6 months old
- [ ] No fabricated data
- [ ] CLIENT_REQUIRED items marked

**Score: ___/10** (8+ to proceed)

**Issues:** _________________________
```

---

## 🎯 Classification Validation (Workflow 2)

```markdown
### Classification Checklist - {{COMPANY_NAME}}
Date: _________ Reviewer: _________

**SCORING FACTORS**
- [ ] Size score calculated (40%)
- [ ] Revenue data or CLIENT_REQUIRED (30%)
- [ ] Company age verified (15%)
- [ ] Growth indicators (15%)

**CLASSIFICATION OUTPUT**
- [ ] Archetype selected with confidence %
- [ ] Business model identified
- [ ] 3 goal options provided
- [ ] Success metrics defined

**Score: ___/10** (8.5+ to proceed)

**Manual Override?** [ ] Yes - Reason: _______
```

---

## 🏗️ Structure Validation (Workflow 3)

```markdown
### Structure Checklist - {{COMPANY_NAME}}
Date: _________ Reviewer: _________

**FOUNDATION STRUCTURE**
- [ ] All 4 agent folders created
- [ ] Context files initialized
- [ ] Metadata tags correct
- [ ] File permissions set

**CUSTOMIZATION**
- [ ] Industry overlay applied
- [ ] Agent roles customized
- [ ] Interaction patterns defined

**Score: ___/10** (7+ to proceed)
```

---

## 🤖 Agent Validation (Workflow 4)

```markdown
### Agent Checklist - {{COMPANY_NAME}}
Date: _________ Reviewer: _________

**AGENT CONFIGURATION**
- [ ] ATLAS calibrated for strategy
- [ ] NAVIGATOR operational focus set
- [ ] MAESTRO tech stack aligned
- [ ] CATALYST change readiness assessed

**KNOWLEDGE BASE**
- [ ] Core knowledge populated
- [ ] Industry context added
- [ ] Company specifics integrated

**Score: ___/10** (8+ to proceed)
```

---

## 📚 Research Validation (Workflow 5)

```markdown
### Research Checklist - {{COMPANY_NAME}}
Date: _________ Reviewer: _________

**DATA COLLECTION**
- [ ] Automated research completed
- [ ] Manual gaps identified
- [ ] Client data integrated
- [ ] Sources verified

**COVERAGE BY AGENT**
- [ ] ATLAS: Market/competitive data
- [ ] NAVIGATOR: Operational metrics
- [ ] MAESTRO: Technology insights
- [ ] CATALYST: Culture/change data

**QUALITY METRICS**
- Data completeness: ___%
- Source freshness: ___ days
- Confidence level: ___%

**Score: ___/10** (7.5+ to proceed)
```

---

## ✅ Final Activation Validation

```markdown
### Activation Checklist - {{COMPANY_NAME}}
Date: _________ Reviewer: _________

**PRE-ACTIVATION**
- [ ] All workflows complete
- [ ] Quality scores > minimum
- [ ] Client data integrated
- [ ] No blocking issues

**SYSTEM CHECK**
- [ ] Agents responding correctly
- [ ] Knowledge accessible
- [ ] Interactions working
- [ ] Performance acceptable

**CLIENT READINESS**
- [ ] Preview completed
- [ ] Feedback incorporated
- [ ] Training scheduled
- [ ] Support documented

**FINAL APPROVAL**
Approved by: _________ Date: _________
Client Sign-off: _________ Date: _________
```

---

## 📊 Quick Scoring Guide

### Scoring Rubric (1-10)
- **10**: Exceptional, exceeds all requirements
- **9**: Excellent, all requirements met perfectly
- **8**: Good, minor gaps acceptable
- **7**: Adequate, some improvements needed
- **6**: Below standard, significant gaps
- **5 or below**: Do not proceed

### Minimum Scores by Stage
1. Discovery: 8.0
2. Classification: 8.5
3. Structure: 7.0
4. Agents: 8.0
5. Research: 7.5
6. Activation: 9.0

### Red Flags (Automatic Fail)
- 🔴 No source citations
- 🔴 Fabricated data
- 🔴 Client data missing > 7 days
- 🔴 Confidence < 70%
- 🔴 Quality score < minimum
