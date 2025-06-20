# Foundation™ Repository Structure v2.0

```
foundation-[CLIENT_NAME]/
│
├── README.md                        # Foundation overview & quick start guide
├── .gitignore                       # Ignore sensitive files
├── foundation.config.yaml           # Client configuration
├── FOUNDATION_STATUS.md             # Progress tracking and completion status
│
├── .agents/                         # Agent System Prompts & Calibration
│   ├── ATLAS.md                    # Strategic Intelligence Officer prompt
│   ├── NAVIGATOR.md                # Operations Excellence Officer prompt
│   ├── MAESTRO.md                  # Technology Integration Officer prompt
│   ├── CATALYST.md                 # Change & Adoption Officer prompt
│   │
│   └── calibration/                # Pre-generation calibration files
│       ├── ATLAS_calibration.md    # Strategic focus for this company
│       ├── NAVIGATOR_calibration.md # Operational priorities
│       ├── MAESTRO_calibration.md  # Technology priorities
│       └── CATALYST_calibration.md # Change management approach
│
├── shared_context/                  # Company-wide intelligence
│   ├── company_overview.md         # [✓] Core company information
│   ├── business_classification.md  # [✓] Archetype & stage analysis
│   ├── next_level_goals.md        # [✓] 12-18 month transformation goals
│   ├── leadership_culture.md       # [✓] Leadership style & culture
│   ├── industry_intelligence.md    # [✓] Industry-specific context
│   ├── tech_landscape.md          # [✓] Technology context
│   ├── enhanced_overview.md        # [✓] Combined insights for agents
│   │
│   ├── org_chart.md               # [ ] Organizational structure
│   ├── product_portfolio.md       # [ ] Products/services detail
│   ├── core_processes.md          # [ ] Internal processes
│   └── revenue_breakdown.md       # [ ] Financial structure
│
├── ATLAS/                          # Strategic Intelligence
│   ├── market_landscape/
│   │   ├── industry_analysis.md   # [✓] Market size, growth, segments
│   │   ├── key_trends_2025.md     # [✓] Future trends & disruptions
│   │   ├── regulation_watchlist.md # [✓] Compliance & regulatory
│   │   └── tam_sam_som.md         # [ ] Market opportunity sizing
│   │
│   ├── competitors/
│   │   ├── competitive_landscape.md # [✓] Top competitors overview
│   │   ├── feature_benchmarks.md   # [✓] Feature comparisons
│   │   ├── market_positioning.md   # [ ] Positioning analysis
│   │   └── disruption_threats.md   # [ ] Potential disruptors
│   │
│   ├── strategy/
│   │   ├── strategic_opportunities.md # [✓] Growth opportunities
│   │   ├── risk_assessment.md      # [ ] Strategic risks
│   │   ├── ma_targets.md           # [ ] Acquisition opportunities
│   │   └── partnership_strategy.md # [ ] Partnership opportunities
│   │
│   └── finance/
│       ├── funding_landscape.md    # [ ] For startups
│       ├── investor_intelligence.md # [ ] Investor analysis
│       └── financial_benchmarks.md # [ ] Industry financial metrics
│
├── NAVIGATOR/                      # Operational Excellence
│   ├── metrics/
│   │   ├── kpi_dashboard.md       # [✓] Key performance indicators
│   │   ├── operational_benchmarks.md # [✓] Industry benchmarks
│   │   ├── growth_metrics.md      # [ ] Growth tracking
│   │   └── efficiency_analysis.md # [ ] Operational efficiency
│   │
│   ├── sales_marketing/
│   │   ├── gtm_strategy.md        # [✓] Go-to-market approach
│   │   ├── pricing_analysis.md    # [✓] Pricing model & strategy
│   │   ├── customer_acquisition.md # [ ] CAC & channels
│   │   └── revenue_operations.md  # [ ] RevOps analysis
│   │
│   ├── operations/
│   │   ├── process_optimization.md # [ ] Process improvements
│   │   ├── resource_allocation.md # [ ] Resource optimization
│   │   ├── supply_chain.md        # [ ] For physical products
│   │   └── quality_metrics.md     # [ ] Quality management
│   │
│   └── scaling/
│       ├── growth_bottlenecks.md  # [ ] Scaling challenges
│       ├── operational_roadmap.md # [ ] Operations plan
│       └── cost_optimization.md   # [ ] Cost reduction
│
├── MAESTRO/                        # Technology Integration
│   ├── current_state/
│   │   ├── tech_stack_audit.md    # [✓] Current technology
│   │   ├── technical_debt.md      # [ ] Debt assessment
│   │   ├── integration_map.md     # [ ] System integrations
│   │   └── data_architecture.md   # [ ] Data infrastructure
│   │
│   ├── talent/
│   │   ├── team_assessment.md     # [✓] Current capabilities
│   │   ├── skill_gaps.md          # [✓] Missing skills
│   │   ├── hiring_roadmap.md      # [ ] Talent acquisition
│   │   └── training_needs.md      # [ ] Upskilling plans
│   │
│   ├── innovation/
│   │   ├── automation_opportunities.md # [✓] Automation targets
│   │   ├── ai_ml_use_cases.md    # [ ] AI/ML applications
│   │   ├── digital_transformation.md # [ ] DX roadmap
│   │   └── innovation_pipeline.md # [ ] Future tech bets
│   │
│   └── architecture/
│       ├── target_architecture.md # [ ] Future state design
│       ├── migration_strategy.md  # [ ] Migration plans
│       ├── build_vs_buy.md       # [ ] Decision framework
│       └── vendor_analysis.md     # [ ] Vendor selection
│
├── CATALYST/                       # Change & Adoption
│   ├── sentiment/
│   │   ├── internal_sentiment.md  # [✓] Employee perception
│   │   ├── external_perception.md # [✓] Market perception
│   │   ├── news_analysis.md       # [✓] Media coverage
│   │   └── social_listening.md    # [ ] Social media sentiment
│   │
│   ├── readiness/
│   │   ├── change_readiness.md    # [✓] Organization readiness
│   │   ├── stakeholder_map.md     # [ ] Key stakeholders
│   │   ├── resistance_points.md   # [ ] Change barriers
│   │   └── champion_network.md    # [ ] Change champions
│   │
│   ├── transformation/
│   │   ├── change_strategy.md     # [ ] Change approach
│   │   ├── communication_plan.md  # [ ] Comms strategy
│   │   ├── training_program.md    # [ ] Training needs
│   │   └── adoption_metrics.md    # [ ] Success metrics
│   │
│   └── culture/
│       ├── culture_assessment.md  # [ ] Current culture
│       ├── culture_evolution.md   # [ ] Target culture
│       ├── values_alignment.md    # [ ] Values assessment
│       └── innovation_culture.md  # [ ] Innovation readiness
│
├── .templates/                     # Document templates
│   ├── archetype_templates/       # Templates by company type
│   │   ├── startup_template.md    # 1-50 employees
│   │   ├── growth_template.md     # 50-200 employees
│   │   ├── midmarket_template.md  # 200-500 employees
│   │   └── enterprise_template.md # 500+ employees
│   │
│   ├── industry_templates/        # Industry-specific templates
│   │   ├── saas_template.md       # SaaS companies
│   │   ├── manufacturing_template.md # Manufacturing
│   │   ├── healthcare_template.md # Healthcare
│   │   └── financial_template.md  # Financial services
│   │
│   └── document_templates/        # Standard documents
│       ├── company_overview_template.md
│       ├── competitor_analysis_template.md
│       ├── kpi_dashboard_template.md
│       └── agent_prompt_template.md
│
├── .workflows/                     # Windsurf workflow definitions
│   ├── 01_discovery.md            # Initial company discovery
│   ├── 02_classification.md       # Business classification
│   ├── 03_agent_generation.md     # Agent persona creation
│   ├── 04_structure_creation.md   # File structure setup
│   ├── 05_research_execution.md   # Research population
│   │
│   ├── master_workflows/          # Orchestration workflows
│   │   ├── complete_pipeline.md   # Full 90-minute process
│   │   ├── quick_demo.md          # 30-minute version
│   │   └── deep_dive.md           # 2-hour comprehensive
│   │
│   └── utility_workflows/         # Supporting workflows
│       ├── validate_agents.md     # Test agent quality
│       ├── update_research.md     # Refresh data
│       └── quality_check.md       # Validate completion
│
├── .scripts/                       # Automation scripts
│   ├── initialization/            # Setup scripts
│   │   ├── create_structure.py    # Create file structure
│   │   ├── classify_business.py   # Auto-classification
│   │   └── generate_agents.py     # Agent generation
│   │
│   ├── research/                  # Research automation
│   │   ├── collect_public_data.py # Web scraping
│   │   ├── analyze_competitors.py # Competitive intel
│   │   └── market_research.py     # Market analysis
│   │
│   ├── maintenance/               # Ongoing updates
│   │   ├── update_market_data.py  # Market updates
│   │   ├── refresh_metrics.py     # Metric updates
│   │   └── monitor_news.py        # News monitoring
│   │
│   └── reporting/                 # Report generation
│       ├── generate_summary.py    # Executive summary
│       ├── agent_insights.py      # Agent recommendations
│       └── weekly_update.py       # Weekly reports
│
└── .github/                       # GitHub automation
    └── workflows/
        ├── daily_update.yml       # Daily data refresh
        ├── weekly_report.yml      # Weekly summaries
        ├── quality_check.yml      # Quality validation
        └── client_delivery.yml    # Delivery preparation
```

## Key Improvements in v2.0

### 1. **Discovery & Classification Phase**
- Added `business_classification.md` for archetype analysis
- Added `next_level_goals.md` for transformation objectives
- Added calibration files for agent customization

### 2. **Enhanced Shared Context**
- Leadership and culture analysis
- Industry-specific intelligence
- Technology landscape assessment
- Enhanced overview for agent generation

### 3. **Archetype-Specific Templates**
- Startup vs Growth vs Enterprise templates
- Industry-specific overlays (SaaS, Manufacturing, etc.)
- Customizable file structures

### 4. **Modular Workflow System**
- Sequential workflows for each phase
- Master orchestration workflows
- Utility workflows for testing and validation

### 5. **Better Organization**
- Clearer directory structure
- Grouped related files
- Status tracking with checkmarks
- Progress monitoring

### 6. **Automation Ready**
- Python scripts for each phase
- GitHub Actions for maintenance
- Reporting and monitoring tools

## File Population Priority

### Phase 1: Foundation (Required)
1. `shared_context/company_overview.md`
2. `shared_context/business_classification.md`
3. `shared_context/next_level_goals.md`
4. All agent files in `.agents/`

### Phase 2: Core Intelligence (Priority)
1. `ATLAS/market_landscape/industry_analysis.md`
2. `ATLAS/competitors/competitive_landscape.md`
3. `NAVIGATOR/metrics/kpi_dashboard.md`
4. `MAESTRO/current_state/tech_stack_audit.md`
5. `CATALYST/sentiment/internal_sentiment.md`

### Phase 3: Deep Insights (Enhancement)
- Strategy documents
- Detailed operational analysis
- Innovation roadmaps
- Transformation plans

## Usage Instructions

1. **Clone Template**: Copy for new client
2. **Run Discovery**: Execute `/foundation-discovery` workflow
3. **Classify Business**: Execute `/foundation-classify` workflow
4. **Generate Agents**: Execute `/foundation-agents` workflow
5. **Create Structure**: Execute `/foundation-structure` workflow
6. **Populate Data**: Execute `/foundation-research` workflow
7. **Validate**: Run quality checks and agent tests

## Success Metrics

- All required files populated: ✓
- Agents respond with specific insights: ✓
- No generic/placeholder content: ✓
- Cross-references working: ✓
- Client-ready in < 90 minutes: ✓