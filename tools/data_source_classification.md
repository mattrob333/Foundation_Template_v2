# Data Source Classification Guide

## Critical Rule: NEVER Fabricate Unverifiable Information

**🚨 ABSOLUTE RULE**: If data cannot be found through public sources or APIs, it MUST be marked as "CLIENT_REQUIRED" and explicitly requested from the client. Never guess, estimate, or make up data.

## Data Categories

### 🌐 PUBLIC_VERIFIABLE (Can be automated)
Data available through web scraping, APIs, or public databases:

| Data Point | Sources | Reliability | APIs Available |
|------------|---------|-------------|----------------|
| Company Name | Website, LinkedIn, Crunchbase | HIGH | ✓ Crunchbase, LinkedIn |
| Website URL | Direct, Google Search | HIGH | ✓ Google Search |
| Industry Category | LinkedIn, Crunchbase, Website | HIGH | ✓ Multiple |
| Headquarters Location | LinkedIn, Website, Google | HIGH | ✓ Multiple |
| Year Founded | Crunchbase, LinkedIn, Website | HIGH | ✓ Crunchbase |
| Employee Count Range | LinkedIn, Glassdoor | MEDIUM | ✓ LinkedIn |
| Public Funding Rounds | Crunchbase, TechCrunch | HIGH | ✓ Crunchbase |
| Public Executive Names | LinkedIn, Company Website | HIGH | ✓ LinkedIn |
| Product Descriptions | Website, Product Hunt | HIGH | ✓ Various |
| Public Customer Logos | Website Case Studies | MEDIUM | ❌ Scraping |
| News & Press Releases | Google News, PR Sites | HIGH | ✓ News APIs |
| Job Postings | Indeed, LinkedIn, Company Site | HIGH | ✓ Indeed API |
| Social Media Presence | Twitter, LinkedIn | HIGH | ✓ Social APIs |
| Public Reviews | G2, Capterra, Glassdoor | MEDIUM | ✓ Some APIs |
| Tech Stack (partial) | BuiltWith, Job Postings | MEDIUM | ✓ BuiltWith |

### 🔒 CLIENT_REQUIRED (Must request from client)
Data that CANNOT be reliably obtained without client input:

| Data Point | Why Client-Only | How to Request |
|------------|----------------|----------------|
| Exact Revenue | Private companies don't disclose | "What was your revenue last fiscal year?" |
| Exact Employee Count | LinkedIn shows ranges only | "How many full-time employees do you have?" |
| Growth Rate | Requires historical data | "What's your YoY revenue growth rate?" |
| Burn Rate | Highly confidential | "What's your monthly burn rate?" |
| Customer Count | Rarely public | "How many active customers do you have?" |
| Churn Rate | Internal metric | "What's your annual customer churn rate?" |
| CAC/LTV | Internal metrics | "What's your CAC and LTV?" |
| Profit Margins | Private info | "What are your gross/net margins?" |
| Strategic Priorities | Internal planning | "What are your top 3 strategic priorities?" |
| Budget Allocations | Confidential | "How is your budget allocated?" |
| Internal Challenges | Not public | "What are your biggest internal challenges?" |
| Future Plans | Confidential | "What are your 12-month goals?" |
| Competitive Advantages | Strategic info | "What's your main competitive advantage?" |
| Customer Segments | Often confidential | "Who are your primary customer segments?" |
| Pricing Strategy | Often hidden | "What's your pricing model and average deal size?" |

### ⚠️ HYBRID_VERIFICATION (Partial public, needs confirmation)
Data where public sources provide clues but client confirmation is needed:

| Data Point | Public Indicators | Client Confirmation Needed |
|------------|------------------|---------------------------|
| Business Model | Website suggests, but may be incomplete | "Is your primary model B2B SaaS, or do you have other revenue streams?" |
| Target Market | Marketing materials hint at it | "Who exactly is your ideal customer profile?" |
| Company Stage | Funding suggests, but not definitive | "How would you describe your current stage?" |
| Market Position | Some public data, but subjective | "How do you see your market position?" |
| Technology Stack | Job posts show some, not all | "What's your complete technology stack?" |
| Geographic Presence | HQ is public, full presence isn't | "Which geographic markets do you operate in?" |

## Implementation in Workflows

### Modified Discovery Workflow Example

```markdown
### Step 2: Public Data Collection (5 min)
@web search "{{COMPANY_URL}}" comprehensive analysis:

✅ COLLECT (Public/Verifiable):
- Official company name
- Headquarters location  
- Website URL
- Industry category
- Year founded
- Employee count RANGE (e.g., "51-200")
- Public funding rounds
- Executive team names
- Product descriptions
- Recent news

⚠️ DO NOT FABRICATE:
- Exact employee count
- Revenue figures
- Growth rates
- Internal metrics
```

### Client Data Request Template

```markdown
## Data Request for {{COMPANY_NAME}}

To complete your Foundation accurately, we need the following information that isn't publicly available:

### Financial Metrics
- [ ] Annual revenue (last fiscal year): $______
- [ ] Year-over-year growth rate: ______%
- [ ] Gross margin: ______%

### Operational Metrics  
- [ ] Exact employee count: ______
- [ ] Customer count: ______
- [ ] Monthly/Annual churn rate: ______%

### Strategic Information
- [ ] Top 3 strategic priorities for next 12 months:
  1. ______________________
  2. ______________________
  3. ______________________

### Optional but Helpful
- [ ] Average deal size: $______
- [ ] Sales cycle length: ______ days
- [ ] Primary customer segment: ______
```

## Validation Rules

### When Processing Data:

1. **If found publicly**: Mark source and confidence level
   ```
   Employee Count: 51-200 (Source: LinkedIn, HIGH confidence)
   ```

2. **If not found publicly**: Mark as CLIENT_REQUIRED
   ```
   Revenue: CLIENT_REQUIRED - Not publicly disclosed
   ```

3. **If partially found**: Mark what's known and what's needed
   ```
   Business Model: B2B SaaS (Source: Website)
   Pricing Model: CLIENT_REQUIRED - Not publicly available
   ```

## Automated vs Manual Collection

### Can Be Automated 🤖
- LinkedIn API → Company basics, employee ranges
- Crunchbase API → Funding, investors, founding date
- News APIs → Recent developments, press
- BuiltWith API → Technology stack indicators
- Social Media APIs → Brand presence, engagement

### Requires Manual Review 👤
- Website scraping → Needs interpretation
- Review sites → Sentiment analysis
- Job postings → Tech stack and priorities inference
- Case studies → Customer types and use cases

### Always Requires Client 🤝
- Financial metrics (revenue, margins, burn)
- Internal metrics (churn, CAC, LTV)
- Strategic priorities and plans
- Competitive positioning details
- Future roadmap and goals

## Error Handling

### If Data Not Found:
```markdown
❌ WRONG: "The company has approximately $10M in revenue" (guessing)
✅ RIGHT: "Revenue: CLIENT_REQUIRED - Not publicly available"
```

### If Data Conflicting:
```markdown
❌ WRONG: Pick one source arbitrarily
✅ RIGHT: "Employee Count: 45-60 (LinkedIn shows 51-200, Glassdoor shows 45, needs client confirmation)"
```

### If Data Outdated:
```markdown
❌ WRONG: Use old data without notation
✅ RIGHT: "Last Funding: $15M Series A (2019 - may be outdated, request current status from client)"
```

## Quality Assurance Checklist

Before submitting any Foundation data:

- [ ] All PUBLIC_VERIFIABLE data has sources noted
- [ ] All CLIENT_REQUIRED data is clearly marked
- [ ] No data has been fabricated or guessed
- [ ] Confidence levels are indicated where appropriate
- [ ] Conflicting data sources are noted
- [ ] Outdated information is flagged
- [ ] Client data request form is complete
- [ ] Validation rules have been followed

## Integration with Classification System

The enhanced classification system should handle missing data gracefully:

```python
# Pseudo-code for handling missing data
if revenue_data == "CLIENT_REQUIRED":
    # Use only available factors
    classification_score = (size_score * 0.57) + (age_score * 0.21) + (growth_score * 0.21)
    confidence_level = "MEDIUM - Missing revenue data"
else:
    # Use all factors
    classification_score = calculate_full_score()
    confidence_level = "HIGH"
```

Remember: **It's better to have incomplete but accurate data than complete but fabricated data.**
