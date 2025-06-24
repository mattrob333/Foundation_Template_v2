# Foundation v3 Demo Launcher
# This script creates a complete Foundation workflow demonstration
# It preserves the template and creates everything in a separate directory

param(
    [Parameter(Mandatory=$true)]
    [string]$CompanyName,
    
    [Parameter(Mandatory=$true)]
    [string]$CompanyURL,
    
    [string]$OutputDirectory = "DEMO_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss')"
)

Write-Host "🚀 Foundation v3 Demo Launcher" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Create demo directory
$DemoPath = Join-Path $PSScriptRoot $OutputDirectory
Write-Host "📁 Creating demo directory: $OutputDirectory" -ForegroundColor Yellow
New-Item -ItemType Directory -Path $DemoPath -Force | Out-Null

# Create workflow status file
$StatusFile = Join-Path $DemoPath "WORKFLOW_STATUS.md"
@"
# Foundation Workflow Status

**Company**: $CompanyName
**URL**: $CompanyURL
**Started**: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

## Workflow Progress
- [ ] Phase 1: Discovery
- [ ] Phase 2: Classification  
- [ ] Phase 3: Structure & Agents
- [ ] Phase 4: Research Population
- [ ] Phase 5: Validation
- [ ] Phase 6: AI Executive Creation

## Notes
This is a live demonstration of the Foundation v3 system.
All data is sourced from public information.
"@ | Out-File -FilePath $StatusFile -Encoding UTF8

Write-Host "✅ Demo directory created" -ForegroundColor Green
Write-Host ""

# Create instruction file for Windsurf
$InstructionFile = Join-Path $DemoPath "RUN_WORKFLOW.md"
@"
# Foundation v3 Workflow Instructions

**Company**: $CompanyName  
**URL**: $CompanyURL  
**Output Directory**: $OutputDirectory

## Instructions for Windsurf AI

Please execute the complete Foundation workflow for $CompanyName using the following steps:

### Phase 1: Discovery (3-5 minutes)
1. Use Firecrawl to map the website: $CompanyURL
2. Search for company information:
   - Basic info (founding, HQ, employees)
   - Leadership team
   - Financial metrics (revenue, funding, valuation)
   - Market position
3. Create `01_discovery_results.md` with findings

### Phase 2: Classification (1-2 minutes)
1. Apply the enhanced multi-factor classification:
   - Company size (employees)
   - Revenue/funding level
   - Company age
   - Growth velocity
   - Business model
   - Industry/sub-vertical
2. Calculate composite score
3. Determine investment stage
4. Create `02_classification_results.md`

### Phase 3: Structure & Agents (1 minute)
1. Define the Foundation folder structure
2. Configure the 4 AI agents with focus areas:
   - ATLAS: Strategic vision
   - NAVIGATOR: Operations
   - MAESTRO: Technology
   - CATALYST: Change
3. Create `03_structure_config.md`

### Phase 4: Research Population (5-7 minutes)
1. Extract detailed leadership profiles
2. Gather financial metrics and pricing
3. Analyze product features
4. Research competitive landscape
5. Create `04_research_data.md`

### Phase 5: Validation (1 minute)
1. Run quality checks on all data
2. Calculate completeness scores
3. Verify source citations
4. Flag any missing data
5. Create `05_validation_report.md`

### Phase 6: AI Executive Creation (5 minutes)
1. Create the 4 AI executives in `AI_Executives/`:
   - `ATLAS_strategic_vision.md`
   - `NAVIGATOR_operational_excellence.md`
   - `MAESTRO_innovation_technology.md`
   - `CATALYST_change_transformation.md`
2. Create `EXECUTIVE_SUMMARY.md` synthesizing all perspectives

### Important Guidelines:
- Use only public, verifiable information
- Maintain source citations for all data
- Never fabricate information
- Flag data that requires client input
- Focus on investment-grade analysis

### Success Criteria:
- All 6 phases completed
- Data accuracy: 100% sourced
- Quality score: >90%
- Time: <20 minutes total

Please begin with Phase 1: Discovery using Firecrawl on $CompanyURL
"@ | Out-File -FilePath $InstructionFile -Encoding UTF8

Write-Host "📋 Workflow instructions created" -ForegroundColor Green
Write-Host ""
Write-Host "✨ Demo setup complete!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Open Windsurf in the demo directory: $DemoPath" -ForegroundColor White
Write-Host "2. Open the file: RUN_WORKFLOW.md" -ForegroundColor White
Write-Host "3. Ask Windsurf to execute the workflow" -ForegroundColor White
Write-Host ""
Write-Host "The entire workflow will run in ~15-20 minutes" -ForegroundColor Gray
Write-Host "All files will be created in: $OutputDirectory" -ForegroundColor Gray
Write-Host ""
