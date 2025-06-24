# Research Automation APIs & MCP Servers

## Overview
This document outlines the best APIs and MCP servers for automating the Foundation system's research population phase, reducing the 60+ minute manual process to under 10 minutes.

---

## 🏆 Recommended API Stack

### Tier 1: Core Business Data APIs

#### 1. **AbstractAPI Company Enrichment** ⭐ BEST VALUE
- **What it provides**: Company basics, industry, employee count, year founded
- **Coverage**: 175+ countries
- **Pricing**: Free tier available, $9-399/month
- **Integration**: REST API with JSON responses
- **Best for**: Basic company information at scale
```bash
GET https://companyenrichment.abstractapi.com/v1/
?api_key=YOUR_KEY&domain=example.com
```

#### 2. **Clearbit Enrichment API** ⭐ MOST COMPREHENSIVE
- **What it provides**: 100+ data points including tech stack, funding, social profiles
- **Coverage**: Global with ML-powered accuracy
- **Pricing**: Custom enterprise pricing
- **Integration**: REST API with official SDKs (Python, Node, Ruby)
- **Best for**: Deep company intelligence
```python
import clearbit
clearbit.key = 'YOUR_KEY'
company = clearbit.Company.find(domain='example.com')
```

#### 3. **Crunchbase API** ⭐ BEST FOR FUNDING DATA
- **What it provides**: Funding rounds, investors, acquisitions, leadership
- **Coverage**: Startups and tech companies globally
- **Pricing**: Starts at $99/month
- **Integration**: REST API
- **Best for**: Investment and growth data
- **Documentation**: https://data.crunchbase.com/docs

### Tier 2: Specialized Data Sources

#### 4. **LinkedIn Sales Navigator API** (via RapidAPI)
- **What it provides**: Employee counts, company updates, industry trends
- **Limitations**: Official API restricted, third-party alternatives available
- **Alternative**: Proxycurl API for LinkedIn data

#### 5. **BuiltWith API**
- **What it provides**: Technology stack, analytics tools, frameworks
- **Pricing**: From $295/month
- **Best for**: Technical profiling

#### 6. **Google News API** (via NewsAPI)
- **What it provides**: Recent news, press releases, market updates
- **Pricing**: Free tier (100 requests/day), paid from $449/month
- **Best for**: Current events and PR tracking

---

## 🚀 MCP Server Integration

### 1. **Firecrawl MCP Server** ⭐ RECOMMENDED
The most powerful MCP server for web scraping and data extraction.

**Features**:
- Advanced web scraping with JavaScript rendering
- Batch processing for multiple URLs
- Content extraction with AI-powered parsing
- Rate limiting and retry logic built-in
- Deep research capabilities

**Installation**:
```bash
# For Windsurf
npm install -g @mendable/firecrawl-mcp-server

# Configure in Windsurf settings
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["@mendable/firecrawl-mcp-server"],
      "env": {
        "FIRECRAWL_API_KEY": "your-api-key"
      }
    }
  }
}
```

**Key Tools**:
- `firecrawl_scrape`: Single page extraction
- `firecrawl_batch_scrape`: Multiple URLs at once
- `firecrawl_map`: Discover all pages on a site
- `firecrawl_search`: Search within scraped content
- `firecrawl_extract`: Structured data extraction
- `firecrawl_deep_research`: Comprehensive analysis

### 2. **Web Search MCP Server**
For general web searches and discovery.

### 3. **Database MCP Servers**
For storing and retrieving enriched data.

---

## 📋 Implementation Strategy

### Phase 1: Basic Automation (Week 1)
1. **Set up Firecrawl MCP Server** for web scraping
2. **Integrate AbstractAPI** for basic company data
3. **Add NewsAPI** for recent developments
4. **Create batch processing templates**

### Phase 2: Enhanced Data (Week 2)
1. **Add Clearbit or similar** for deep enrichment
2. **Integrate Crunchbase** for funding data
3. **Set up technology detection** (BuiltWith/Wappalyzer)
4. **Build validation workflows**

### Phase 3: Full Automation (Week 3)
1. **Create orchestration layer** to coordinate APIs
2. **Implement caching** to reduce API costs
3. **Add quality scoring** for data confidence
4. **Build fallback chains** for missing data

---

## 💰 Cost Optimization

### Estimated Monthly Costs (per 100 companies)
- **Basic Tier**: ~$50/month
  - AbstractAPI: $9
  - NewsAPI: Free tier
  - Firecrawl: $49

- **Professional Tier**: ~$500/month
  - Clearbit: ~$300
  - Crunchbase: $99
  - BuiltWith: $295
  - Firecrawl: $49

### Cost-Saving Strategies
1. **Cache everything**: Store API responses for 30 days
2. **Batch requests**: Process multiple companies together
3. **Tiered approach**: Use expensive APIs only when needed
4. **Fallback chains**: Try free sources first

---

## 🔧 Sample Automation Workflow

```python
# Pseudo-code for automated research population
async def populate_research(company_domain):
    # Step 1: Basic enrichment (fast & cheap)
    basic_data = await abstract_api.enrich(company_domain)
    
    # Step 2: Web scraping for current info
    website_data = await firecrawl.scrape(company_domain)
    about_page = await firecrawl.scrape(f"{company_domain}/about")
    
    # Step 3: News and updates
    news = await news_api.search(basic_data.company_name)
    
    # Step 4: Deep enrichment (if needed)
    if needs_deep_data(basic_data):
        deep_data = await clearbit.enrich(company_domain)
        funding = await crunchbase.search(basic_data.company_name)
    
    # Step 5: Technology detection
    tech_stack = await builtwith.lookup(company_domain)
    
    # Step 6: Compile and validate
    return compile_research_data(
        basic_data, website_data, news, 
        deep_data, funding, tech_stack
    )
```

---

## 🎯 Expected Outcomes

### Before Automation
- **Time**: 60+ minutes per company
- **Data Quality**: Variable, depends on researcher
- **Coverage**: Limited by manual effort
- **Cost**: High labor cost

### After Automation
- **Time**: 5-10 minutes per company
- **Data Quality**: Consistent and validated
- **Coverage**: Comprehensive across all sources
- **Cost**: Predictable API costs, minimal labor

---

## 🚦 Next Steps

1. **Get API Keys**:
   - [ ] AbstractAPI (free tier)
   - [ ] NewsAPI (free tier)
   - [ ] Firecrawl (trial key)

2. **Install MCP Servers**:
   - [ ] Firecrawl MCP Server
   - [ ] Configure in Windsurf

3. **Create Templates**:
   - [ ] Research batch template
   - [ ] Data validation checklist
   - [ ] Output formatting

4. **Test & Iterate**:
   - [ ] Run on 5 test companies
   - [ ] Compare with manual research
   - [ ] Adjust data sources as needed
