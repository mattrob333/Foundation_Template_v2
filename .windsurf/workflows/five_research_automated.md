---
description: 5 - Automated Research Population
---

# five_research_automated
Populate comprehensive research data using APIs and MCP servers

## Prerequisites
- Completed workflows 1-4
- API keys configured (see research_automation_apis.md)
- Firecrawl MCP Server installed
- Client data form completed (if applicable)

## Time Estimate
- **Manual Process**: 60-90 minutes
- **Automated Process**: 5-10 minutes
- **Human Review**: 5 minutes

## Workflow Execution

### Step 1: Initialize Research Context (1 min)
```
Load existing data:
- company_overview.md (from Discovery)
- business_classification.md (from Classification)
- All agent context files

Extract key identifiers:
- Company domain: {{DOMAIN}}
- Company name: {{COMPANY_NAME}}
- Industry: {{INDUSTRY}}
- Employee range: {{EMPLOYEE_RANGE}}
```

### Step 2: Tier 1 - Basic Enrichment (2 min)
```
# AbstractAPI Company Enrichment
@api abstract_company_enrichment domain={{DOMAIN}}:

✅ COLLECT:
- Legal company name
- Year founded (verify against discovery)
- Employee count estimate
- Industry classification
- Company description
- Logo URL
- Social media profiles

⚠️ VALIDATE:
- Cross-check with discovery data
- Flag any conflicts for review
- Update confidence scores

OUTPUT → enrichment_basic.json
```

### Step 3: Tier 2 - Web Intelligence (3 min)
```
# Firecrawl MCP Deep Scraping
@mcp firecrawl_batch_scrape urls=[
  "{{DOMAIN}}",
  "{{DOMAIN}}/about",
  "{{DOMAIN}}/team",
  "{{DOMAIN}}/products",
  "{{DOMAIN}}/customers",
  "{{DOMAIN}}/careers"
]:

✅ EXTRACT:
- Mission/vision statements
- Product descriptions
- Customer testimonials
- Team size indicators
- Technology mentions
- Recent updates/news

⚠️ STRUCTURED EXTRACTION:
@mcp firecrawl_extract url={{DOMAIN}} schema={
  "products": ["name", "description", "pricing"],
  "leadership": ["name", "title", "bio"],
  "customers": ["name", "industry", "useCase"]
}

OUTPUT → web_intelligence.json
```

### Step 4: Tier 3 - Market Intelligence (2 min)
```
# News and Market Updates
@api newsapi query="{{COMPANY_NAME}}" last_6_months:

✅ COLLECT:
- Recent press releases
- Product launches
- Leadership changes
- Funding announcements
- Partnership news

# Competitive Intelligence
@mcp firecrawl_search query="{{COMPANY_NAME}} vs competitors":
- Direct competitors mentioned
- Market positioning claims
- Differentiation points

# Industry Trends
@api industry_reports sector={{INDUSTRY}}:
- Market size and growth
- Key trends
- Regulatory changes

OUTPUT → market_intelligence.json
```

### Step 5: Tier 4 - Deep Enrichment (2 min)
```
# Conditional Deep Data (if Growth/Enterprise)
IF classification IN ['Scale-up', 'Mid-Market', 'Enterprise']:
  
  # Funding Data (Crunchbase)
  @api crunchbase company={{COMPANY_NAME}}:
  - Total funding amount
  - Latest round details
  - Investor list
  - Valuation (if available)
  
  # Technology Stack (BuiltWith)
  @api builtwith domain={{DOMAIN}}:
  - Core technologies
  - Analytics tools
  - Marketing stack
  - Infrastructure

  # Business Intelligence (Clearbit)
  @api clearbit domain={{DOMAIN}}:
  - Detailed firmographics
  - Technology spend estimates
  - Growth indicators

OUTPUT → deep_enrichment.json
```

### Step 6: Data Synthesis & Validation (1 min)
```
# Compile all data sources
research_data = merge(
  enrichment_basic,
  web_intelligence,
  market_intelligence,
  deep_enrichment,
  client_provided_data
)

# Validation checks
FOR each data_point IN research_data:
  - Check source reliability
  - Verify data freshness (< 6 months)
  - Cross-validate between sources
  - Flag conflicts or gaps

# Confidence scoring
calculate_confidence_score():
  - High: Multiple sources agree
  - Medium: Single source or partial data
  - Low: Inferred or outdated data

# Generate research quality report
quality_metrics = {
  "completeness": "85%",
  "data_freshness": "< 30 days",
  "source_diversity": "6 sources",
  "conflicts_found": [],
  "client_data_needed": []
}
```

### Step 7: Populate Agent Research Files (1 min)
```
# Update each agent's research file
FOR agent IN [ATLAS, NAVIGATOR, MAESTRO, CATALYST]:
  
  file_path = f"agents/{agent}/research.md"
  
  # Filter relevant data for each agent
  agent_data = filter_by_agent_scope(research_data, agent)
  
  # Update research file with:
  - Market intelligence (ATLAS focus)
  - Operational metrics (NAVIGATOR focus)
  - Technology insights (MAESTRO focus)
  - Change indicators (CATALYST focus)
  
  # Add source citations
  add_citations(agent_data)
  
  # Flag any agent-specific gaps
  identify_research_gaps(agent)
```

### Step 8: Generate Research Summary (1 min)
Create: `shared_context/research_summary.md`

```markdown
# Research Population Summary

## Data Collection Metrics
- **Total Time**: {{ELAPSED_TIME}} minutes
- **Sources Used**: {{SOURCE_COUNT}}
- **API Calls**: {{API_CALLS}}
- **Data Points Collected**: {{DATA_POINTS}}
- **Confidence Level**: {{OVERALL_CONFIDENCE}}%

## Key Findings
### Company Insights
- {{TOP_3_INSIGHTS}}

### Market Position
- {{MARKET_SUMMARY}}

### Technology Profile
- {{TECH_SUMMARY}}

### Growth Indicators
- {{GROWTH_METRICS}}

## Data Quality Report
### Complete Data ({{COMPLETE_PERCENT}}%)
- ✅ Company basics
- ✅ Product information
- ✅ Market presence

### Partial Data ({{PARTIAL_PERCENT}}%)
- ⚠️ Financial metrics (client required)
- ⚠️ Customer details (limited public info)

### Missing Data ({{MISSING_PERCENT}}%)
- ❌ Internal metrics (client required)
- ❌ Strategic priorities (client required)

## Recommended Actions
1. Review and validate automated findings
2. Request client data for gaps
3. Set up monitoring for updates
```

### Step 9: Human Review & Approval (5 min)
```
Present to user for review:

1. **Data Accuracy Check**
   - [ ] Company information correct
   - [ ] No outdated information
   - [ ] Sources properly cited

2. **Completeness Review**
   - [ ] All agents have sufficient data
   - [ ] Critical gaps identified
   - [ ] Client data integrated

3. **Quality Assurance**
   - [ ] No fabricated data
   - [ ] Confidence levels appropriate
   - [ ] Conflicts resolved

4. **Final Approval**
   - [ ] Ready for activation
   - [ ] Schedule data refresh
   - [ ] Archive raw data
```

---

## Automation Configuration

### Required API Keys
```yaml
api_keys:
  abstract_api: ${ABSTRACT_API_KEY}
  newsapi: ${NEWS_API_KEY}
  crunchbase: ${CRUNCHBASE_API_KEY}  # Optional
  clearbit: ${CLEARBIT_API_KEY}      # Optional
  builtwith: ${BUILTWITH_API_KEY}    # Optional
```

### MCP Server Setup
```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["@mendable/firecrawl-mcp-server"],
      "env": {
        "FIRECRAWL_API_KEY": "${FIRECRAWL_API_KEY}"
      }
    }
  }
}
```

### Batch Processing Template
```python
# Process multiple companies efficiently
companies = load_company_list()

for batch in chunks(companies, size=10):
    results = await asyncio.gather(*[
        populate_research(company) 
        for company in batch
    ])
    save_results(results)
    await rate_limit_delay()
```

---

## Cost Management

### Per-Company Costs (Estimated)
- **Basic Research**: ~$0.50
  - AbstractAPI: $0.03
  - NewsAPI: Free
  - Firecrawl: $0.47

- **Deep Research**: ~$5.00
  - All basic sources
  - Clearbit: ~$3.00
  - Crunchbase: $1.00
  - BuiltWith: $1.00

### Optimization Rules
1. Cache all API responses for 30 days
2. Use basic tier first, upgrade only if needed
3. Batch similar requests together
4. Monitor API usage daily
5. Set spending alerts

---

## Error Handling

### API Failures
```python
try:
    data = await api_call()
except APIError as e:
    # Try fallback source
    data = await fallback_source()
    log_api_failure(e)
```

### Data Quality Issues
- Missing required fields → Flag for manual review
- Conflicting data → Present both, request clarification
- Outdated information → Mark with low confidence
- Rate limits hit → Queue for retry

### Recovery Procedures
1. Save partial progress automatically
2. Resume from last successful step
3. Manual override options available
4. Detailed error logs for debugging

---

## Success Metrics

### Efficiency Gains
- ⏱️ Time Saved: 50-80 minutes per company
- 💰 Cost Reduction: 70% vs manual research
- 📊 Data Coverage: 3x more data points
- ✅ Consistency: 100% standardized output

### Quality Improvements
- 🎯 Accuracy: Source verification for all data
- 🔄 Freshness: Real-time data vs static research
- 📈 Completeness: Systematic coverage of all areas
- 🔍 Traceability: Full audit trail for all data
