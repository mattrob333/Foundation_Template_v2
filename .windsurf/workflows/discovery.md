---
description: Foundation™ Discovery Workflow
---

Initial company intelligence gathering

## Prerequisites
- Empty Foundation template structure
- Company URL or LinkedIn profile

## Workflow Execution

### Step 1: Gather Initial Input
```
Welcome to Foundation™ Discovery. I'll gather comprehensive intelligence about the target company.

Please provide:
1. Company website URL or LinkedIn profile
2. Any additional context (optional)
```

Store response as: {{COMPANY_URL}}

### Step 2: Comprehensive Company Research
```
@web search "{{COMPANY_URL}}" comprehensive analysis including:
- Official company name and legal entity structure
- Founding date, founders, and origin story
- Current C-suite and leadership team with backgrounds
- Total employee count (verify on LinkedIn)
- Primary industry classification and sub-sectors
- Complete products and services portfolio
- Business model (B2B/B2C, SaaS/Services/Product/Hybrid)
- Revenue (if public) or funding history (amount, stage, investors)
- Recent milestones, news, and announcements (last 12 months)
- Technology indicators from job postings and website
- Company mission, vision, values, and culture
- Office locations and geographic presence
- Key customers or case studies (if available)
- Awards, certifications, or recognition
```

### Step 3: Leadership Deep Dive
```
@web search "{{COMPANY_NAME}}" leadership team LinkedIn profiles:
- CEO background and previous companies
- Other C-suite executives and their expertise
- Board members and advisors
- Notable investors or strategic partners
```

### Step 4: Recent Developments
```
@web search "{{COMPANY_NAME}}" news last 6 months:
- Product launches or updates
- Funding announcements
- Executive changes
- Partnerships or acquisitions
- Market expansion
- Any challenges or controversies
```

### Step 5: Format Company Overview
Create comprehensive overview with proper structure:

```markdown
---
title: "Company Overview - {{COMPANY_NAME}}"
source: "Web research via @web"
owner: "intel@tier4.ai"
agent_scope: ["ATLAS", "NAVIGATOR", "MAESTRO", "CATALYST"]
created: "{{TODAY_DATE}}"
updated: "{{TODAY_DATE}}"
tags: ["company", "overview", "foundation"]
---

# {{COMPANY_NAME}} Overview

## Company Snapshot
- **Legal Name**: {{FULL_LEGAL_NAME}}
- **Founded**: {{YEAR}} by {{FOUNDERS}}
- **Headquarters**: {{CITY}}, {{STATE/COUNTRY}}
- **CEO**: {{CEO_NAME}} ({{CEO_BACKGROUND}})
- **Employees**: {{COUNT}} ({{GROWTH_TREND}})
- **Industry**: {{PRIMARY_INDUSTRY}} > {{SUB_SECTOR}}
- **Website**: {{WEBSITE_URL}}
- **Business Model**: {{MODEL_TYPE}}

## Funding & Financial Status
- **Total Funding**: ${{AMOUNT}}
- **Latest Round**: {{STAGE}} - ${{AMOUNT}} ({{DATE}})
- **Key Investors**: {{INVESTOR_LIST}}
- **Revenue**: {{PUBLIC_OR_ESTIMATED}}
- **Valuation**: {{IF_AVAILABLE}}

## Mission & Vision
"{{MISSION_STATEMENT}}"

{{VISION_DESCRIPTION}}

## Products & Services

### Core Offerings
1. **{{PRODUCT_1}}**
   - Description: {{DESCRIPTION}}
   - Target Market: {{TARGET}}
   - Key Features: {{FEATURES}}

2. **{{PRODUCT_2}}**
   - Description: {{DESCRIPTION}}
   - Target Market: {{TARGET}}
   - Key Features: {{FEATURES}}

[Continue for all major products/services]

## Market Position
- **Value Proposition**: {{UNIQUE_VALUE}}
- **Target Customers**: {{CUSTOMER_PROFILE}}
- **Key Differentiators**: 
  - {{DIFFERENTIATOR_1}}
  - {{DIFFERENTIATOR_2}}
  - {{DIFFERENTIATOR_3}}

## Leadership Team
- **{{CEO_NAME}}** - Chief Executive Officer
  - Background: {{PREVIOUS_EXPERIENCE}}
  - Joined: {{DATE}}
  
- **{{CXO_NAME}}** - {{TITLE}}
  - Background: {{PREVIOUS_EXPERIENCE}}
  - Expertise: {{AREA}}

[Continue for key executives]

## Recent Milestones & News
- **{{DATE}}**: {{MILESTONE_1}}
- **{{DATE}}**: {{MILESTONE_2}}
- **{{DATE}}**: {{MILESTONE_3}}

## Technology Indicators
- **Tech Stack Signals**: {{IDENTIFIED_TECHNOLOGIES}}
- **Engineering Team Size**: {{ESTIMATE}}
- **Technical Focus Areas**: {{AREAS}}

## Company Culture & Values
- **Core Values**: {{VALUES_LIST}}
- **Culture Type**: {{CULTURE_DESCRIPTION}}
- **Employee Sentiment**: {{GLASSDOOR_RATING}}/5

## Geographic Presence
- **Headquarters**: {{HQ_LOCATION}}
- **Other Offices**: {{OFFICE_LIST}}
- **Remote Policy**: {{REMOTE_STANCE}}

## Growth Indicators
- **Employee Growth**: {{YOY_GROWTH}}%
- **Hiring Velocity**: {{OPEN_POSITIONS}} open roles
- **Expansion Signals**: {{GEOGRAPHIC_OR_PRODUCT}}

## Key Challenges & Opportunities
### Challenges
- {{CHALLENGE_1}}
- {{CHALLENGE_2}}

### Opportunities  
- {{OPPORTUNITY_1}}
- {{OPPORTUNITY_2}}

## Additional Context
{{ANY_OTHER_RELEVANT_INFORMATION}}
```

### Step 6: Save Company Overview
Update file: `shared_context/company_overview.md`
- Replace all placeholder content
- Ensure all {{VARIABLES}} are filled with actual data
- Remove any sections that don't apply

### Step 7: Initial Leadership & Culture Analysis
```
@web search "{{COMPANY_NAME}} {{CEO_NAME}}" leadership style culture:
- Management philosophy and approach
- Communication style (from interviews, blog posts)
- Company culture initiatives
- Employee reviews about leadership
```

Update file: `shared_context/leadership_culture.md`

```markdown
---
title: "Leadership & Culture - {{COMPANY_NAME}}"
source: "Web research"
owner: "intel@tier4.ai"
agent_scope: ["CATALYST", "NAVIGATOR"]
created: "{{TODAY_DATE}}"
---

# Leadership & Culture Analysis

## Leadership Style
- **CEO Leadership Type**: {{STYLE}}
- **Decision Making**: {{CENTRALIZED/DISTRIBUTED}}
- **Communication Culture**: {{FORMAL/CASUAL}}
- **Innovation Appetite**: {{CONSERVATIVE/AGGRESSIVE}}

## Cultural Indicators
- **Glassdoor Rating**: {{RATING}}/5
- **Key Themes from Reviews**:
  - Positive: {{THEMES}}
  - Negative: {{THEMES}}
- **Values in Action**: {{EXAMPLES}}

## Management Philosophy
{{DETAILED_DESCRIPTION}}
```

### Step 8: Validation Checklist
Before proceeding to classification:
- [ ] Company overview is complete with no placeholders
- [ ] All sections have real data (remove if not applicable)
- [ ] Employee count is verified (LinkedIn cross-check)
- [ ] Recent news is included (last 6 months)
- [ ] Leadership team has at least CEO + 2 other executives
- [ ] Industry classification is specific (not just "technology")
- [ ] Business model is clear (B2B SaaS, B2C marketplace, etc.)
- [ ] Funding or revenue information is included

### Step 9: Output Summary
```
Discovery Complete for {{COMPANY_NAME}}

Key Findings:
- Company Type: {{QUICK_CLASSIFICATION}}
- Employee Count: {{NUMBER}}
- Stage: {{STARTUP/GROWTH/ENTERPRISE}}
- Industry: {{SPECIFIC_INDUSTRY}}
- Key Challenge: {{MAIN_CHALLENGE}}

Files Updated:
✓ shared_context/company_overview.md
✓ shared_context/leadership_culture.md

Ready for Phase 2: Business Classification
Run: /classification
```

## Common Issues & Solutions

**Issue**: Limited information (private company)
**Solution**: 
- Check LinkedIn company page
- Search for press releases
- Look for case studies mentioning them
- Check job postings for insights
- Industry reports sometimes mention private companies

**Issue**: Multiple companies with same name
**Solution**: 
- Use location + company name
- Add founder name to search
- Use exact website URL
- Look for industry + company name

**Issue**: Very new company (<1 year old)
**Solution**:
- Focus on founder backgrounds
- Search for launch announcements
- Check ProductHunt, TechCrunch
- Look at investor announcements
- AngelList or Crunchbase profiles

## Time Estimate: 10-15 minutes