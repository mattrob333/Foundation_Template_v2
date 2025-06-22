---
description: intelligence_source_discovery
---

# intelligence_source_discovery
Identify and document ongoing intelligence sources for Foundation maintenance

## Prerequisites
- Completed `two_classification` (know industry and archetype)
- Understanding of company's ecosystem
- 30-45 minutes for thorough discovery

## Workflow Execution

### Step 1: Load Company Context (2 min)
```
Read from:
- shared_context/company_overview.md → {{COMPANY_NAME}}, {{INDUSTRY}}
- shared_context/business_classification.md → {{ARCHETYPE}}, {{FOCUS_AREAS}}

Extract:
- Company name and variations
- Industry and sub-sectors
- Competitive set
- Technology focus areas
- Geographic markets
```

### Step 2: Identify Industry Intelligence Sources (10 min)

#### Publications & Media
```
@web search "{{INDUSTRY}} industry publications trade media"
@web search "{{INDUSTRY}} news sites blogs RSS feeds"
@web search "{{INDUSTRY}} newsletters substacks"

Look for:
- Top 3-5 industry publications
- Relevant trade journals
- Industry-specific news aggregators
- Quality blogs with RSS feeds
- Email newsletters worth subscribing
```

#### Thought Leaders & Analysts
```
@web search "{{INDUSTRY}} thought leaders LinkedIn influencers"
@web search "{{INDUSTRY}} industry analysts Gartner Forrester"
@web search "{{INDUSTRY}} YouTube channels podcasts"

Identify:
- Top 5-10 industry influencers
- Analyst firms covering the space
- Popular YouTube channels
- Relevant podcasts
- Twitter/LinkedIn voices
```

#### Communities & Forums
```
@web search "{{INDUSTRY}} Reddit communities forums"
@web search "{{INDUSTRY}} Slack communities Discord"
@web search "{{INDUSTRY}} LinkedIn groups discussions"

Find:
- Active subreddits
- Industry-specific forums
- Professional Slack/Discord communities
- LinkedIn groups with engagement
- Stack Overflow tags (if tech)
```

### Step 3: Map Company-Specific Sources (8 min)

#### Official Channels
```
@web search "{{COMPANY_NAME}} blog RSS feed"
@web search "{{COMPANY_NAME}} YouTube channel"
@web search "{{COMPANY_NAME}} podcast"
@web search "{{COMPANY_NAME}} developer blog engineering"

Document:
- Company blog/newsroom (+ RSS)
- YouTube channel
- Podcast (if any)
- Engineering/tech blog
- Investor relations page
- Social media handles
```

#### Leadership Tracking
```
@web search "{{COMPANY_NAME}} CEO LinkedIn Twitter"
@web search "{{COMPANY_NAME}} executives social media"
@web search "{{COMPANY_NAME}} leadership team"

Find profiles for:
- CEO/Founder
- CTO/VP Engineering
- CMO/VP Marketing
- Other key executives
- Board members (if relevant)
```

#### Employee Insights
```
@web search "{{COMPANY_NAME}} employees LinkedIn"
@web search "{{COMPANY_NAME}} Glassdoor Blind"
@web search "{{COMPANY_NAME}} engineering blog posts"

Identify:
- Active employee bloggers
- Technical team members who post
- Glassdoor page
- Blind company channel
- Team tech talks/presentations
```

### Step 4: Competitive Intelligence Network (8 min)

#### Direct Competitors
```
For each top 3 competitor:
@web search "{{COMPETITOR}} blog news RSS"
@web search "{{COMPETITOR}} product updates changelog"
@web search "{{COMPETITOR}} leadership LinkedIn"

Capture:
- Competitor blogs/newsrooms
- Product update feeds
- Key executive profiles
- Developer documentation
- Pricing pages to monitor
```

#### Market Intelligence
```
@web search "{{INDUSTRY}} market research reports free"
@web search "{{INDUSTRY}} statistics data sources"
@web search "{{INDUSTRY}} benchmarks KPIs"

Find:
- Industry associations with data
- Government/regulatory sources
- Free research report sources
- Benchmark providers
- Statistical databases
```

### Step 5: Technology & Innovation Sources (5 min)

Based on {{ARCHETYPE}}:

#### For Tech Companies
```
- GitHub trending in relevant languages
- Hacker News keywords
- Product Hunt categories
- Dev.to tags
- TechCrunch tags
- ArXiv categories (if applicable)
```

#### For Traditional Industries
```
- Industry 4.0 sources
- Digital transformation blogs
- Automation news sources
- Industry-specific tech publications
```

### Step 6: Create Monitoring Setup (5 min)

#### Google Alerts Configuration
Create alerts for:
```
"{{COMPANY_NAME}}"
"{{COMPANY_NAME}}" AND (announcement OR news)
"{{INDUSTRY}}" AND (trends OR future)
"{{COMPETITOR_1}}" OR "{{COMPETITOR_2}}"
"{{KEY_TECHNOLOGY}}" AND "{{INDUSTRY}}"
```

#### RSS Feed Bundle
Compile RSS URLs for:
- Company blogs
- Industry publications  
- Competitor newsrooms
- Key influencer blogs
- YouTube channels (via RSS)

### Step 7: Document Intelligence Sources (5 min)

Create/Update: `shared_context/intelligence_sources.md`

Use the template structure to organize all discovered sources with:
- Source name and type
- URL/profile link
- RSS feed (if available)
- Update frequency
- Intelligence value
- Specific monitoring focus

### Step 8: Create Collection Schedule (3 min)

Organize sources by collection frequency:

**Daily Monitoring**
- Twitter/X feeds
- Reddit communities
- Google Alerts
- Company blogs

**Weekly Review**
- Industry publications
- LinkedIn updates
- YouTube channels
- Podcast releases

**Monthly Deep Dive**
- Research reports
- Glassdoor/Blind
- GitHub activity
- Market data

### Step 9: Validate Sources (5 min)

Test discovered sources:
```
For each major source:
1. Check if actively updated
2. Verify RSS feed works
3. Assess content quality
4. Note typical update frequency
5. Test accessibility (free vs paid)
```

### Step 10: Complete
```
✓ Industry sources identified
✓ Company channels mapped
✓ Leadership profiles found
✓ Competitive intel network built
✓ Monitoring system designed
✓ Sources documented
✓ Collection schedule created

Next: Use these sources during five_research_population
and ongoing maintenance
```

## Using Intelligence Sources

### During Research Population
Reference `intelligence_sources.md` when updating:
- Check RSS feeds for latest content
- Search specific communities for discussions
- Review influencer recent posts
- Monitor competitor updates

### For Ongoing Maintenance
Weekly routine:
1. Check daily sources for major news
2. Review RSS feeds for updates
3. Scan communities for sentiment
4. Update files with new intelligence

### For Calibration
When calibrating agents:
- Review sources for strategic shifts
- Check leadership social for vision changes
- Monitor communities for culture shifts
- Track competitor moves

## Success Metrics

Good intelligence source discovery yields:
- 20-30 high-quality sources
- 10+ RSS feeds for automation
- 5-10 key people to follow
- 3-5 active communities
- Clear monitoring system

## Pro Tips

1. **Quality over Quantity**: Better to deeply monitor 10 great sources than skim 50
2. **Automate Collection**: Use RSS readers, alerts, and aggregators
3. **Community Focus**: Where practitioners discuss real challenges
4. **Executive Intel**: Leadership thoughts predict company direction
5. **Competitor Obsession**: Know their moves as well as your own

---

*This workflow should be run after initial Foundation setup and updated quarterly as sources change.*