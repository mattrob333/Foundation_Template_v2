---
description: 1 - Discovery
---

# one_discovery
Gather comprehensive company intelligence

## Prerequisites
- Company URL or LinkedIn profile
- Empty `shared_context/company_overview.md` file

## Workflow Execution

### Step 1: Initial Input (1 min)
```
Ask user: "What's the company website URL or LinkedIn profile?"
Store as: {{COMPANY_URL}}

If no URL provided:
Ask: "What's the company name and what do they do?"
```

### Step 2: Core Company Research (5 min)
```
@web search "{{COMPANY_URL}}" comprehensive analysis:

Essential data to find:
- Official company name
- Year founded and founders
- Headquarters location
- Employee count (check LinkedIn)
- Industry and sub-industry
- Products/services offered
- Business model (B2B/B2C, SaaS/Services)
- Revenue or funding stage
- Recent news (last 12 months)
```

### Step 3: Leadership & Culture (3 min)
```
@web search "{{COMPANY_NAME}}" leadership team LinkedIn:

Find:
- CEO/Founder (name, background)
- C-suite executives (titles, tenure)
- Board members (if available)
- Company values/culture
- Management philosophy
```

### Step 4: Market Position (3 min)
```
@web search "{{COMPANY_NAME}}" market position competitors:

Identify:
- Main competitors (top 3-5)
- Market share (if available)
- Unique value proposition
- Customer base description
- Geographic presence
```

### Step 5: Technology Indicators (3 min)
```
@web search "{{COMPANY_NAME}}" job postings technology stack:

Look for:
- Technologies mentioned in jobs
- Digital maturity indicators
- Technical team size
- Innovation initiatives
- Tech partnerships
```

### Step 6: Update Company Overview (5 min)
Update existing file: `shared_context/company_overview.md`

```markdown
---
title: "Company Overview - {{COMPANY_NAME}}"
source: "Web research via @web"
owner: "intel@tier4.ai"
agent_scope: ["ATLAS", "NAVIGATOR", "MAESTRO", "CATALYST"]
created: "{{TODAY_DATE}}"
tags: ["company", "overview", "public"]
---

# {{COMPANY_NAME}} Overview

## Company Snapshot
- **Founded**: {{YEAR}}
- **Headquarters**: {{LOCATION}}
- **Employees**: {{COUNT}} ({{SOURCE}})
- **Industry**: {{INDUSTRY}}
- **Website**: {{URL}}
- **Stage**: {{FUNDING/REVENUE}}

## What They Do
{{BRIEF_DESCRIPTION}}

## Products & Services
1. **{{PRODUCT_1}}**: {{DESCRIPTION}}
2. **{{PRODUCT_2}}**: {{DESCRIPTION}}
3. **{{PRODUCT_3}}**: {{DESCRIPTION}}

## Value Proposition
"{{VALUE_PROP_IN_THEIR_WORDS}}"

## Market Position
- **Competitors**: {{LIST}}
- **Differentiators**: {{KEY_DIFFERENCES}}
- **Target Market**: {{CUSTOMER_DESCRIPTION}}

## Leadership Team
- **CEO**: {{NAME}} - {{BACKGROUND}}
- **{{ROLE}}**: {{NAME}} - {{BACKGRO# /01_discovery
Gather comprehensive company intelligence

## Prerequisites
- Company URL or LinkedIn profile
- Empty `shared_context/company_overview.md` file

## Workflow Execution

### Step 1: Initial Input (1 min)
```
Ask user: "What's the company website URL or LinkedIn profile?"
Store as: {{COMPANY_URL}}

If no URL provided:
Ask: "What's the company name and what do they do?"
```

### Step 2: Core Company Research (5 min)
```
@web search "{{COMPANY_URL}}" comprehensive analysis:

Essential data to find:
- Official company name
- Year founded and founders
- Headquarters location
- Employee count (check LinkedIn)
- Industry and sub-industry
- Products/services offered
- Business model (B2B/B2C, SaaS/Services)
- Revenue or funding stage
- Recent news (last 12 months)
```

### Step 3: Leadership & Culture (3 min)
```
@web search "{{COMPANY_NAME}}" leadership team LinkedIn:

Find:
- CEO/Founder (name, background)
- C-suite executives (titles, tenure)
- Board members (if available)
- Company values/culture
- Management philosophy
```

### Step 4: Market Position (3 min)
```
@web search "{{COMPANY_NAME}}" market position competitors:

Identify:
- Main competitors (top 3-5)
- Market share (if available)
- Unique value proposition
- Customer base description
- Geographic presence
```

### Step 5: Technology Indicators (3 min)
```
@web search "{{COMPANY_NAME}}" job postings technology stack:

Look for:
- Technologies mentioned in jobs
- Digital maturity indicators
- Technical team size
- Innovation initiatives
- Tech partnerships
```

### Step 6: Update Company Overview (5 min)
Update existing file: `shared_context/company_overview.md`

```markdown
---
title: "Company Overview - {{COMPANY_NAME}}"
source: "Web research via @web"
owner: "intel@tier4.ai"
agent_scope: ["ATLAS", "NAVIGATOR", "MAESTRO", "CATALYST"]
created: "{{TODAY_DATE}}"
tags: ["company", "overview", "public"]
---

# {{COMPANY_NAME}} Overview

## Company Snapshot
- **Founded**: {{YEAR}}
- **Headquarters**: {{LOCATION}}
- **Employees**: {{COUNT}} ({{SOURCE}})
- **Industry**: {{INDUSTRY}}
- **Website**: {{URL}}
- **Stage**: {{FUNDING/REVENUE}}

## What They Do
{{BRIEF_DESCRIPTION}}

## Products & Services
1. **{{PRODUCT_1}}**: {{DESCRIPTION}}
2. **{{PRODUCT_2}}**: {{DESCRIPTION}}
3. **{{PRODUCT_3}}**: {{DESCRIPTION}}

## Value Proposition
"{{VALUE_PROP_IN_THEIR_WORDS}}"

## Market Position
- **Competitors**: {{LIST}}
- **Differentiators**: {{KEY_DIFFERENCES}}
- **Target Market**: {{CUSTOMER_DESCRIPTION}}

## Leadership Team
- **CEO**: {{NAME}} - {{BACKGROUND}}
- **{{ROLE}}**: {{NAME}} - {{BACKGROUND}}
- **{{ROLE}}**: {{NAME}} - {{BACKGROUND}}

## Recent Developments
- **{{DATE}}**: {{NEWS_ITEM}}
- **{{DATE}}**: {{NEWS_ITEM}}
- **{{DATE}}**: {{NEWS_ITEM}}

## Technology Profile
- **Tech Stack Indicators**: {{TECHNOLOGIES}}
- **Digital Maturity**: {{ASSESSMENT}}
- **Innovation Focus**: {{AREAS}}

## Initial Observations
- **Strengths**: {{2-3_ITEMS}}
- **Challenges**: {{2-3_ITEMS}}
- **Opportunities**: {{2-3_ITEMS}}
```

### Step 7: Validate Completeness (1 min)
Check overview includes:
- [ ] Employee count (critical for classification)
- [ ] Industry (needed for customization)
- [ ] Business model (B2B/B2C)
- [ ] Founded date (company maturity)
- [ ] Recent news (current state)

If missing critical data, note as:
`[TO BE CONFIRMED: {{MISSING_ITEM}}]`

### Step 8: Save and Confirm
```
Update file: shared_context/company_overview.md
Verify: File saved with proper YAML header
Test: @ATLAS can you see the company overview?

Success: "I can see that {{COMPANY_NAME}} is a {{INDUSTRY}} company..."
```

### Step 9: Complete
```
✓ Company overview created
✓ All public data gathered
✓ File properly formatted
✓ Ready for classification

Next: Run /02_classification
Time: ~20 minutes
```

## Common Edge Cases

**Private Company**: Limited info available
- Use LinkedIn employee count
- Check job postings for insights
- Note limitations in overview

**New Startup**: <1 year old
- Focus on founder backgrounds
- Emphasize problem/solution
- Check AngelList, Crunchbase

**Subsidiary**: Part of larger company
- Note parent company
- Focus on division specifics
- Clarify scope of Foundation

**Non-English**: Primary presence in other language
- Translate key information
- Note primary market
- Keep original company name