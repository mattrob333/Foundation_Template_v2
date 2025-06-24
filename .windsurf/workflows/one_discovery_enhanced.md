---
description: 1 - Enhanced Discovery with Data Integrity
---

# one_discovery_enhanced
Gather comprehensive company intelligence with clear data source tracking

## Prerequisites
- Company URL or LinkedIn profile
- Empty `shared_context/company_overview.md` file
- Client Data Collection Form ready (if needed)

## Critical Rules
🚨 **NEVER FABRICATE DATA**: If information cannot be found through public sources, mark it as CLIENT_REQUIRED
🚨 **ALWAYS CITE SOURCES**: Every data point must have a source and confidence level
🚨 **FLAG CONFLICTS**: When sources disagree, note all versions and request clarification

## Workflow Execution

### Step 1: Initial Input & Validation (2 min)
```
Ask user: "What's the company website URL or LinkedIn profile?"
Store as: {{COMPANY_URL}}

Validate URL:
- Check if URL is accessible
- Confirm it's the official company site
- Note any redirects or multiple domains

If no URL provided:
Ask: "What's the company name? We'll search for public information."
```

### Step 2: Core Company Research - PUBLIC DATA (5 min)
```
@web search "{{COMPANY_URL}}" comprehensive analysis:

✅ PUBLIC/VERIFIABLE - Collect these:
- Official company name (Source: Website)
- Headquarters location (Source: Website/LinkedIn)
- Year founded (Source: Crunchbase/LinkedIn/Website)
- Employee count RANGE (Source: LinkedIn shows ranges like "51-200")
- Industry classification (Source: LinkedIn/Crunchbase)
- Product/service descriptions (Source: Website)
- Public funding rounds (Source: Crunchbase/News)
- Website URL (Source: Direct)
- Social media handles (Source: Website/Search)

⚠️ CLIENT_REQUIRED - Mark these for later:
- Exact employee count (LinkedIn only shows ranges)
- Annual revenue (Private companies rarely disclose)
- Growth rate (Requires historical data)
- Profit margins (Confidential information)
- Customer count (Rarely public)

❌ DO NOT GUESS OR FABRICATE
```

### Step 3: Leadership & Culture - MIXED DATA (3 min)
```
@web search "{{COMPANY_NAME}}" leadership team LinkedIn:

✅ PUBLIC/VERIFIABLE:
- CEO/Founder name and LinkedIn (Source: LinkedIn/Website)
- C-suite executives names and titles (Source: LinkedIn/Website)
- Board members if public (Source: Website/News)
- Publicly stated values (Source: Website careers page)
- Glassdoor rating if available (Source: Glassdoor)

⚠️ PARTIAL/NEEDS CONFIRMATION:
- Leadership tenure (LinkedIn may be outdated)
- Team size by department (Job postings give hints)
- Culture descriptions (Marketing vs reality)

❌ CLIENT_REQUIRED:
- Internal culture assessment
- Leadership priorities
- Organizational structure details
```

### Step 4: Market Position - INFERENCE DATA (3 min)
```
@web search "{{COMPANY_NAME}}" competitors market position:

✅ PUBLIC/VERIFIABLE:
- Named competitors (Source: G2/Capterra comparisons)
- Industry reports mentioning company (Source: Gartner/Forrester)
- Customer logos if displayed (Source: Website)
- Geographic presence (Source: Office locations)
- Partnership announcements (Source: Press releases)

⚠️ INFERENCE (Note as estimates):
- Market share (Unless in public reports)
- Competitive positioning (Based on marketing)
- Customer segment focus (Based on case studies)

❌ CLIENT_REQUIRED:
- Actual market share data
- Win/loss rates
- Customer segmentation data
- Revenue by geography
```

### Step 5: Technology Indicators - PARTIAL DATA (3 min)
```
@web search "{{COMPANY_NAME}}" job postings technology stack:

✅ PUBLIC/VERIFIABLE:
- Technologies in job posts (Source: Indeed/LinkedIn jobs)
- BuiltWith profile (Source: BuiltWith.com)
- Public API documentation (Source: Developer docs)
- Tech partnerships announced (Source: Press releases)
- Open source contributions (Source: GitHub)

⚠️ INFERENCE:
- Tech stack priorities (Based on hiring)
- Digital maturity (Based on web presence)
- Innovation focus (Based on job posts)

❌ CLIENT_REQUIRED:
- Complete technology stack
- Internal tools and systems
- Technology roadmap
- Technical debt assessment
```

### Step 6: Data Validation & Gap Analysis (2 min)
```
Create data quality report:

COMPLETE DATA (High confidence):
- Company name: {{VALUE}} ✓
- Founded: {{VALUE}} ✓
- Industry: {{VALUE}} ✓

PARTIAL DATA (Medium confidence):
- Employees: {{RANGE}} (LinkedIn estimate)
- Funding: {{AMOUNT}} (last public round)

MISSING DATA (Client required):
- Revenue: CLIENT_REQUIRED
- Growth rate: CLIENT_REQUIRED
- Exact employees: CLIENT_REQUIRED

CONFLICTING DATA (Needs verification):
- Example: Employee count
  - LinkedIn: 51-200
  - Glassdoor: 75 employees
  - ACTION: Request exact count from client
```

### Step 7: Update Company Overview with Source Tracking (5 min)
Update existing file: `shared_context/company_overview.md`

```markdown
---
title: "Company Overview - {{COMPANY_NAME}}"
data_quality: "{{COMPLETE/PARTIAL/NEEDS_CLIENT_INPUT}}"
last_verified: "{{TODAY_DATE}}"
owner: "intel@tier4.ai"
agent_scope: ["ATLAS", "NAVIGATOR", "MAESTRO", "CATALYST"]
created: "{{TODAY_DATE}}"
tags: ["company", "overview", "public"]
---

# {{COMPANY_NAME}} Overview

## Data Quality Notice
- **Public Data Completeness**: {{PERCENTAGE}}%
- **Client Data Needed**: {{YES/NO}}
- **Confidence Level**: {{HIGH/MEDIUM/LOW}}

## Company Snapshot
- **Founded**: {{YEAR}} (Source: {{SOURCE}})
- **Headquarters**: {{LOCATION}} (Source: {{SOURCE}})
- **Employees**: {{RANGE}} (Source: LinkedIn, CLIENT_REQUIRED for exact)
- **Industry**: {{INDUSTRY}} (Source: {{SOURCE}})
- **Website**: {{URL}} (Verified: {{DATE}})
- **Revenue**: CLIENT_REQUIRED - Not publicly disclosed
- **Growth Rate**: CLIENT_REQUIRED - Not publicly available

## What They Do
{{BRIEF_DESCRIPTION}} (Source: Company website)

### Products/Services
1. **{{PRODUCT_1}}**: {{DESCRIPTION}} (Source: Website)
2. **{{PRODUCT_2}}**: {{DESCRIPTION}} (Source: Website)

## Leadership Team
**CEO/Founder**: {{NAME}} (Source: LinkedIn, verified {{DATE}})
- Background: {{BACKGROUND}}
- Tenure: {{TENURE}} (Note: Based on LinkedIn, may need verification)

**Other Executives**:
{{LIST_WITH_SOURCES}}

## Market Position
### Known Competitors (Source: Public comparisons)
1. {{COMPETITOR_1}} - {{HOW_THEY_COMPARE}}
2. {{COMPETITOR_2}} - {{HOW_THEY_COMPARE}}

### Market Share
CLIENT_REQUIRED - Not publicly available

## Technology Profile
### Confirmed Technologies (Source: Job postings, BuiltWith)
- {{TECH_1}}
- {{TECH_2}}

### Full Stack Details
CLIENT_REQUIRED - Partial visibility only

## Recent Developments
{{NEWS_WITH_SOURCES_AND_DATES}}

## Data Gaps Requiring Client Input
The following information could not be found through public sources:
1. Annual revenue and growth rate
2. Exact employee count
3. Customer metrics (count, churn, CAC/LTV)
4. Detailed market share data
5. Complete technology stack
6. Strategic priorities and roadmap

Please complete the Client Data Collection Form for accurate classification.

---
*Data Collection Method: Public web research with source verification*
*Last Updated: {{DATE}}*
```

### Step 8: Generate Client Request if Needed (2 min)
If data gaps exist, create: `shared_context/client_data_request.md`

```markdown
# Data Request for {{COMPANY_NAME}}

Based on our public research, we need the following information to complete your Foundation:

## Critical for Classification (Required)
- [ ] Annual revenue: $______
- [ ] Exact employee count: ______
- [ ] Year-over-year growth rate: ______%

## Important for AI Executive Calibration (Recommended)
- [ ] Customer count: ______
- [ ] Primary customer segment: ______
- [ ] Top 3 strategic priorities

## Helpful for Comprehensive Intelligence (Optional)
- [ ] Complete tech stack
- [ ] Competitive win rate
- [ ] Geographic revenue split

Please use the Client Data Collection Form or provide this information directly.
```

### Step 9: Quality Check & Complete
```
✓ All public data has sources
✓ All missing data is marked CLIENT_REQUIRED
✓ No fabricated information
✓ Confidence levels noted
✓ Data gaps documented
✓ Client request generated if needed

Next: Run two_classification_enhanced
Note: Classification confidence will be lower without client data
Time: ~10 minutes
```

## Key Improvements in This Version

1. **Clear Data Categories**: PUBLIC_VERIFIABLE vs CLIENT_REQUIRED
2. **Source Tracking**: Every data point has a source
3. **No Fabrication**: Missing data is explicitly marked
4. **Confidence Levels**: Indicates data quality
5. **Conflict Resolution**: Notes when sources disagree
6. **Client Request**: Automatically generates data request
7. **Partial Data Handling**: Can proceed with available data
8. **Quality Metrics**: Tracks completeness percentage

## Handling Missing Data in Next Steps

When client data is missing, subsequent workflows should:
1. Use only available data for classification
2. Note reduced confidence levels
3. Flag decisions that would change with complete data
4. Prioritize getting client data for critical gaps
