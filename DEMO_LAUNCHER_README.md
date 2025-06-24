# Foundation v3 Demo Launcher Guide

## Overview

The Foundation Demo Launcher allows you to run the complete Foundation workflow for any company without touching the template files. Perfect for:
- Team demonstrations
- Client presentations
- Testing improvements
- Training sessions

## Quick Start

### Option 1: Simple Batch File (Easiest)
```cmd
START_DEMO.bat
```
Then enter:
- Company name (e.g., "Stripe")
- Company URL (e.g., "https://stripe.com")

### Option 2: PowerShell Script (More Control)
```powershell
.\START_FOUNDATION_DEMO.ps1 -CompanyName "Stripe" -CompanyURL "https://stripe.com"
```

### Option 3: Custom Output Directory
```powershell
.\START_FOUNDATION_DEMO.ps1 -CompanyName "Stripe" -CompanyURL "https://stripe.com" -OutputDirectory "CLIENT_DEMO_STRIPE"
```

## What Happens

1. **Creates Demo Directory**: `DEMO_[timestamp]` or your custom name
2. **Generates Instructions**: `RUN_WORKFLOW.md` with step-by-step guide
3. **Tracks Progress**: `WORKFLOW_STATUS.md` to monitor completion

## Running the Workflow

After launching:

1. **Open Windsurf** in the new demo directory
2. **Open** `RUN_WORKFLOW.md`
3. **Tell Windsurf**: "Please execute this Foundation workflow"

## Expected Timeline

- **Phase 1: Discovery** - 3-5 minutes
- **Phase 2: Classification** - 1-2 minutes  
- **Phase 3: Structure** - 1 minute
- **Phase 4: Research** - 5-7 minutes
- **Phase 5: Validation** - 1 minute
- **Phase 6: AI Executives** - 5 minutes

**Total: ~15-20 minutes**

## Output Structure

```
DEMO_2025-06-24_19-00-00/
├── WORKFLOW_STATUS.md          # Progress tracker
├── RUN_WORKFLOW.md            # Instructions
├── 01_discovery_results.md    # Company basics
├── 02_classification_results.md # Multi-factor analysis
├── 03_structure_config.md     # Agent configuration
├── 04_research_data.md        # Detailed research
├── 05_validation_report.md    # Quality checks
└── AI_Executives/
    ├── ATLAS_strategic_vision.md
    ├── NAVIGATOR_operational_excellence.md
    ├── MAESTRO_innovation_technology.md
    ├── CATALYST_change_transformation.md
    └── EXECUTIVE_SUMMARY.md
```

## Demo Tips

### For Best Results:
- Choose companies with good web presence
- Public companies have more available data
- B2B SaaS companies work particularly well
- Avoid companies requiring login to view info

### Good Demo Companies:
- **Notion** - Productivity software
- **Stripe** - Payments infrastructure
- **Datadog** - Monitoring platform
- **Snowflake** - Data warehouse
- **HubSpot** - Marketing/CRM platform

### During the Demo:
1. Show the launcher creating the workspace
2. Open Windsurf and show the instructions
3. Let it run Phase 1-2 to show automation
4. Skip ahead to show AI Executives
5. Highlight the Executive Summary

## Customization

### Modify Instructions:
Edit the PowerShell script to:
- Change research focus areas
- Add industry-specific prompts
- Adjust time estimates
- Include custom templates

### Post-Demo:
- Save interesting results
- Delete routine demos
- Archive client demos
- Extract learnings

## Troubleshooting

### If Windsurf can't access URLs:
- Check if site requires login
- Try company's investor relations page
- Use LinkedIn company page as backup

### If data is limited:
- Focus on what's available
- Note gaps for client input
- Demonstrate the process anyway

### If errors occur:
- Check internet connection
- Verify Firecrawl MCP is active
- Try a different company

## Advanced Usage

### Batch Processing:
```powershell
$companies = @(
    @{Name="Stripe"; URL="https://stripe.com"},
    @{Name="Notion"; URL="https://notion.so"},
    @{Name="Datadog"; URL="https://datadoghq.com"}
)

foreach ($company in $companies) {
    .\START_FOUNDATION_DEMO.ps1 -CompanyName $company.Name -CompanyURL $company.URL
}
```

### Integration with Git:
```bash
# After demo completion
cd DEMO_2025-06-24_19-00-00
git init
git add .
git commit -m "Foundation analysis for [Company]"
git remote add origin [client-repo]
git push
```

## Best Practices

1. **Always test** before client demos
2. **Keep template clean** - never modify it
3. **Archive good examples** for reference
4. **Document learnings** from each run
5. **Update instructions** based on feedback

---

*The Foundation Demo Launcher is part of the Foundation v3 system by Tier 4 Intelligence*
