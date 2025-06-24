# Foundation™ for Investment Due Diligence - Quick Adaptation Guide

## Overview
How to rapidly configure the Foundation system for different investment evaluation scenarios.

---

## 🎯 Investment Type Configurations

### Seed/Early Stage VC
**Focus Areas**: Team (40%), Market (35%), Product (25%)

**Discovery Priorities**:
- Founder backgrounds and track records
- Problem validation and customer pain
- Early traction signals
- Competitive landscape

**Classification Adjustments**:
- Weight company age less (many are <2 years)
- Focus on growth potential vs current size
- Consider pivot likelihood

**Agent Calibration**:
- ATLAS: Vision and market opportunity
- NAVIGATOR: Burn rate and runway
- MAESTRO: MVP and technical feasibility
- CATALYST: Founder coachability

---

### Growth Equity / Series B-D
**Focus Areas**: Metrics (35%), Market (25%), Team (25%), Operations (15%)

**Discovery Priorities**:
- Unit economics and growth metrics
- Market share and competitive position
- Management team depth
- Operational scalability

**Classification Adjustments**:
- Revenue becomes primary factor
- Growth rate critical
- Path to profitability

**Agent Calibration**:
- ATLAS: Expansion strategy and TAM
- NAVIGATOR: Operational efficiency
- MAESTRO: Technical scalability
- CATALYST: Organizational readiness

---

### Private Equity Buyout
**Focus Areas**: Financials (40%), Operations (30%), Market (20%), Team (10%)

**Discovery Priorities**:
- Historical financials and EBITDA
- Customer concentration
- Operational inefficiencies
- Management retention

**Classification Adjustments**:
- EBITDA margins primary
- Debt capacity consideration
- Value creation opportunities

**Agent Calibration**:
- ATLAS: Roll-up opportunities
- NAVIGATOR: Cost optimization
- MAESTRO: Systems modernization
- CATALYST: Cultural transformation

---

### Distressed/Turnaround
**Focus Areas**: Problems (40%), Solutions (30%), Assets (20%), Team (10%)

**Discovery Priorities**:
- Root cause analysis
- Asset quality and value
- Liquidity position
- Turnaround feasibility

**Classification Adjustments**:
- Focus on fixable vs structural issues
- Timeline to stability
- Capital requirements

**Agent Calibration**:
- ATLAS: Strategic alternatives
- NAVIGATOR: Crisis management
- MAESTRO: Quick wins
- CATALYST: Stakeholder alignment

---

## 📊 Key Metrics by Stage

### Pre-Revenue (Seed)
```python
key_metrics = {
    "team_quality": "critical",
    "market_size": "must be >$1B",
    "product_validation": "customer interviews",
    "burn_rate": "18+ month runway",
    "competition": "differentiation clear"
}
```

### Early Revenue (Series A)
```python
key_metrics = {
    "mrr_growth": ">15% monthly",
    "unit_economics": "CAC < 12mo LTV",
    "logo_retention": ">90%",
    "sales_efficiency": "improving",
    "product_market_fit": "demonstrated"
}
```

### Growth Stage (Series B+)
```python
key_metrics = {
    "arr_growth": ">100% YoY",
    "net_retention": ">110%",
    "gross_margins": ">70%",
    "sales_efficiency": ">0.8x",
    "market_share": "growing"
}
```

### Mature (PE)
```python
key_metrics = {
    "ebitda_margins": ">20%",
    "revenue_growth": ">15%",
    "customer_concentration": "<20%",
    "working_capital": "optimized",
    "debt_capacity": ">3x"
}
```

---

## 🔄 Workflow Modifications

### 1. Discovery Phase Adjustments

**For VC/Seed**:
```markdown
PRIORITIZE:
- LinkedIn profiles of all founders
- AngelList/Crunchbase profiles
- Twitter/social media presence
- Published content/thought leadership
- Previous startup experience
```

**For PE/Buyout**:
```markdown
PRIORITIZE:
- Detailed financials (request immediately)
- Competitor financial benchmarks
- Industry reports and multiples
- Management incentive structures
- Customer contract details
```

### 2. Classification Enhancements

**Add Investment-Specific Scores**:
```python
# VC Scoring
vc_score = (
    founder_score * 0.4 +
    market_score * 0.3 +
    product_score * 0.2 +
    traction_score * 0.1
)

# PE Scoring  
pe_score = (
    financial_score * 0.4 +
    operational_score * 0.3 +
    market_score * 0.2 +
    management_score * 0.1
)
```

### 3. Research Automation Focus

**VC Research Queries**:
```bash
# Founder research
@web search "founder_name previous companies"
@web search "founder_name linkedin accomplishments"

# Market validation
@mcp firecrawl_deep_research query="market_name growth trends 2024"
@web search "competitor recent funding rounds"

# Product research
@mcp firecrawl_scrape url="product_hunt_page"
@web search "product_name user reviews"
```

**PE Research Queries**:
```bash
# Financial research
@web search "company_name revenue employees linkedin"
@mcp firecrawl_extract url="investor_relations" schema={financial_metrics}

# Operational research
@web search "company_name glassdoor reviews"
@mcp firecrawl_map url="careers_page"

# Market research
@web search "industry_name M&A transactions 2024"
@mcp firecrawl_deep_research query="industry consolidation trends"
```

---

## 📋 Investment-Specific Checklists

### VC Checklist Additions
```markdown
FOUNDER ASSESSMENT
- [ ] Previous exit experience
- [ ] Domain expertise (years)
- [ ] Technical capability
- [ ] Fundraising track record
- [ ] Advisory board quality

MARKET VALIDATION  
- [ ] Customer interviews (min 10)
- [ ] Competitor funding mapped
- [ ] Market timing factors
- [ ] Regulatory considerations
```

### PE Checklist Additions
```markdown
FINANCIAL DILIGENCE
- [ ] QoE adjustments identified
- [ ] Working capital normalized
- [ ] Customer concentration <20%
- [ ] Recurring revenue %
- [ ] EBITDA quality score

OPERATIONAL REVIEW
- [ ] Management depth chart
- [ ] Systems assessment
- [ ] Integration readiness
- [ ] Cost reduction opportunities
```

---

## 🚀 Quick Start Commands

### For Any Investment Evaluation
```bash
# 1. Start with company discovery
@mcp firecrawl_map url="company.com"

# 2. Get recent news and updates
@web search "company_name news 2024"
@web search "company_name funding"

# 3. Competitive intelligence
@web search "company_name competitors"
@mcp firecrawl_batch_scrape urls=[competitor_sites]

# 4. Deep dive on specific areas
@mcp firecrawl_deep_research query="company_name business model"

# 5. Extract structured data
@mcp firecrawl_extract urls=["team_page"] schema={leadership_schema}
```

---

## 📊 Output Templates

### Investment Memo Structure
1. **Executive Summary** (1 page)
2. **Investment Thesis** (2 pages)
3. **Due Diligence Findings** (5-10 pages)
4. **Financial Analysis** (3-5 pages)
5. **Risk Assessment** (2 pages)
6. **Recommendation** (1 page)

### Dashboard Metrics
- Investment score (0-100)
- Risk rating (Low/Med/High)
- Timeline to decision
- Key milestones
- Red flags count

---

## 💡 Pro Tips

1. **Start Classification Early**: Don't wait for all data
2. **Use Confidence Scores**: Be transparent about data gaps
3. **Automate First**: Only manual research after automation
4. **Track Everything**: Use validation checklists religiously
5. **Client Data Fast**: Request non-public data immediately

---

This guide enables rapid adaptation of Foundation for any investment scenario while maintaining quality and consistency.
