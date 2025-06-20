#!/usr/bin/env python3
"""
Foundation™ Structure Creation Script
Creates archetype-specific file structure
"""

import os
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class StructureCreator:
    """Creates customized Foundation file structure based on classification"""
    
    def __init__(self, foundation_path: Path):
        self.foundation_path = Path(foundation_path)
        self.shared_context = self.foundation_path / "shared_context"
        
        # Define file structures by archetype
        self.structures = {
            "EARLY_STARTUP": {
                "CATALYST": [
                    "sentiment/market_validation.md",
                    "readiness/founder_alignment.md",
                    "culture/startup_culture.md"
                ],
                "ATLAS": [
                    "market_landscape/tam_sam_som.md",
                    "market_landscape/beachhead_strategy.md",
                    "competitors/competitive_differentiation.md",
                    "strategy/funding_strategy.md"
                ],
                "NAVIGATOR": [
                    "metrics/burn_runway.md",
                    "metrics/early_kpis.md",
                    "sales_marketing/customer_acquisition.md"
                ],
                "MAESTRO": [
                    "current_state/mvp_architecture.md",
                    "innovation/build_vs_buy.md",
                    "talent/technical_hiring.md"
                ]
            },
            "GROWTH_STARTUP": {
                "CATALYST": [
                    "sentiment/employee_sentiment.md",
                    "sentiment/customer_satisfaction.md",
                    "readiness/scaling_readiness.md",
                    "culture/culture_evolution.md",
                    "culture/talent_retention.md"
                ],
                "ATLAS": [
                    "market_landscape/market_expansion.md",
                    "market_landscape/category_creation.md",
                    "competitors/competitive_intelligence.md",
                    "competitors/moat_building.md",
                    "strategy/series_c_positioning.md"
                ],
                "NAVIGATOR": [
                    "metrics/unit_economics.md",
                    "metrics/growth_efficiency.md",
                    "metrics/operational_kpis.md",
                    "sales_marketing/sales_velocity.md",
                    "sales_marketing/market_segmentation.md",
                    "sales_marketing/revenue_retention.md"
                ],
                "MAESTRO": [
                    "current_state/platform_architecture.md",
                    "current_state/technical_debt_audit.md",
                    "innovation/automation_roadmap.md",
                    "innovation/data_strategy.md",
                    "talent/engineering_scaling.md",
                    "talent/skill_development.md"
                ]
            },
            "ENTERPRISE": {
                "CATALYST": [
                    "sentiment/change_resistance_map.md",
                    "sentiment/leadership_alignment.md",
                    "sentiment/employee_readiness.md",
                    "readiness/transformation_capability.md",
                    "readiness/stakeholder_analysis.md",
                    "transformation/communication_strategy.md",
                    "transformation/innovation_culture.md"
                ],
                "ATLAS": [
                    "market_landscape/disruption_threats.md",
                    "market_landscape/ecosystem_evolution.md",
                    "market_landscape/regulatory_horizon.md",
                    "competitors/digital_natives.md",
                    "competitors/incumbent_strategies.md",
                    "strategy/innovation_portfolio.md",
                    "strategy/venture_opportunities.md"
                ],
                "NAVIGATOR": [
                    "metrics/transformation_kpis.md",
                    "metrics/efficiency_targets.md",
                    "metrics/innovation_metrics.md",
                    "operations/process_modernization.md",
                    "operations/global_coordination.md",
                    "operations/supply_chain_digital.md",
                    "performance/business_unit_analysis.md",
                    "performance/portfolio_optimization.md"
                ],
                "MAESTRO": [
                    "current_state/legacy_assessment.md",
                    "current_state/integration_landscape.md",
                    "current_state/data_architecture.md",
                    "transformation/cloud_migration.md",
                    "transformation/api_strategy.md",
                    "transformation/security_architecture.md",
                    "innovation/emerging_tech_radar.md",
                    "innovation/innovation_lab_strategy.md"
                ]
            }
        }
        
        # Default to scale-up if not specified
        self.structures["SCALE_UP"] = self.structures["GROWTH_STARTUP"]
        self.structures["MID_MARKET"] = self.structures["GROWTH_STARTUP"]
    
    def load_classification(self) -> Dict[str, str]:
        """Load business classification to determine structure"""
        classification_path = self.shared_context / "business_classification.md"
        
        if not classification_path.exists():
            raise FileNotFoundError("Classification not found. Run classification workflow first.")
            
        with open(classification_path, 'r') as f:
            content = f.read()
            
        # Extract archetype
        import re
        archetype_match = re.search(r'### Archetype:\s*(\w+)', content)
        if archetype_match:
            archetype = archetype_match.group(1)
        else:
            archetype = "GROWTH_STARTUP"  # Default
            
        # Extract company name
        company_match = re.search(r'\*\*Company\*\*:\s*(.+)', content)
        company_name = company_match.group(1) if company_match else "Unknown Company"
        
        return {
            "archetype": archetype,
            "company_name": company_name
        }
    
    def create_file_with_header(self, file_path: Path, agent: str, title: str):
        """Create a file with proper YAML header"""
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        header = f"""---
title: "{title}"
source: "To be populated"
owner: "intel@tier4.ai"
agent_scope: ["{agent}"]
created: "{datetime.now().strftime('%Y-%m-%d')}"
status: "empty"
tags: ["{agent.lower()}", "intelligence", "foundation"]
---

# {title}

*This file will be populated by the research workflow.*

## Purpose
{self.get_file_purpose(file_path.name)}

## Research Questions
{self.get_research_questions(file_path.name)}

---
*Placeholder content - to be replaced with actual research*
"""
        
        with open(file_path, 'w') as f:
            f.write(header)
    
    def get_file_purpose(self, filename: str) -> str:
        """Get purpose description based on filename"""
        purposes = {
            "market_validation.md": "Validate market demand and customer feedback",
            "tam_sam_som.md": "Define total addressable market and opportunity size",
            "burn_runway.md": "Track financial health and runway calculations",
            "mvp_architecture.md": "Document current technical architecture and decisions",
            "competitive_differentiation.md": "Identify unique value propositions",
            "unit_economics.md": "Analyze CAC, LTV, and other key metrics",
            "disruption_threats.md": "Monitor startups and new business models",
            "transformation_kpis.md": "Track digital transformation progress"
        }
        return purposes.get(filename, "Strategic intelligence for decision making")
    
    def get_research_questions(self, filename: str) -> str:
        """Get research questions based on filename"""
        questions = {
            "market_validation.md": """- What evidence of product-market fit exists?
- What are customers saying about the problem?
- How urgent is the need?""",
            "competitive_differentiation.md": """- What makes us unique?
- Where do we win vs competitors?
- What's our defensible moat?""",
            "unit_economics.md": """- What's our CAC and LTV?
- How long is payback period?
- Are we improving efficiency?"""
        }
        return questions.get(filename, """- What intelligence is needed?
- What decisions will this inform?
- What actions should result?""")
    
    def create_structure(self, archetype: str, company_name: str) -> Dict[str, int]:
        """Create the file structure for given archetype"""
        if archetype not in self.structures:
            print(f"Warning: Unknown archetype {archetype}, using GROWTH_STARTUP")
            archetype = "GROWTH_STARTUP"
            
        structure = self.structures[archetype]
        file_count = {"total": 0}
        
        for agent, files in structure.items():
            agent_path = self.foundation_path / agent
            file_count[agent] = 0
            
            for file_path_str in files:
                file_path = agent_path / file_path_str
                
                # Generate title from path
                title_parts = file_path_str.split('/')
                title = title_parts[-1].replace('.md', '').replace('_', ' ').title()
                title = f"{title} - {company_name}"
                
                self.create_file_with_header(file_path, agent, title)
                file_count[agent] += 1
                file_count["total"] += 1
                
                print(f"✓ Created: {agent}/{file_path_str}")
        
        return file_count
    
    def generate_structure_report(self, archetype: str, company_name: str, file_count: Dict[str, int]):
        """Generate structure report"""
        report = f"""---
title: "File Structure Report - {company_name}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
archetype: "{archetype}"
---

# Foundation™ File Structure Report

## Structure Created
- **Company**: {company_name}
- **Archetype**: {archetype}
- **Total Files**: {file_count['total']}

## Files by Agent
- **CATALYST**: {file_count.get('CATALYST', 0)} files - Change readiness and culture
- **ATLAS**: {file_count.get('ATLAS', 0)} files - Strategic intelligence  
- **NAVIGATOR**: {file_count.get('NAVIGATOR', 0)} files - Operational metrics
- **MAESTRO**: {file_count.get('MAESTRO', 0)} files - Technology strategy

## Population Priority Order
1. **Quick Wins** (Essential for demo):
   - CATALYST/sentiment/market_validation.md
   - ATLAS/market_landscape/tam_sam_som.md
   - NAVIGATOR/metrics/burn_runway.md or unit_economics.md
   - MAESTRO/current_state/mvp_architecture.md or platform_architecture.md

2. **Core Intelligence** (Next priority):
   - Competitive analysis files
   - Key metrics dashboards
   - Technology assessments

3. **Deep Insights** (Time permitting):
   - Transformation strategies
   - Innovation opportunities
   - Detailed roadmaps

## Research Time Estimate
- Quick Demo (5 files): 20 minutes
- Standard (50% of files): 45 minutes  
- Comprehensive (all files): 90 minutes

## Next Step
Run: /05_research_execution
"""
        
        report_path = self.shared_context / "file_structure_report.md"
        with open(report_path, 'w') as f:
            f.write(report)
        
        print(f"\n✓ Structure report saved to: {report_path}")
    
    def run(self):
        """Execute structure creation"""
        print("Foundation™ Structure Creator")
        print("=" * 50)
        
        try:
            # Load classification
            print("Loading business classification...")
            classification = self.load_classification()
            archetype = classification["archetype"]
            company_name = classification["company_name"]
            
            print(f"✓ Creating structure for: {company_name}")
            print(f"✓ Archetype: {archetype}")
            
            # Create structure
            print("\nCreating file structure...")
            file_count = self.create_structure(archetype, company_name)
            
            # Generate report
            print("\nGenerating structure report...")
            self.generate_structure_report(archetype, company_name, file_count)
            
            print(f"\n✓ Structure creation complete!")
            print(f"  Total files created: {file_count['total']}")
            print("\nNext step: Run research workflow to populate files")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return 1
            
        return 0

if __name__ == "__main__":
    import sys
    
    # Get foundation path from command line or use current directory
    if len(sys.argv) > 1:
        foundation_path = sys.argv[1]
    else:
        foundation_path = "."
        
    creator = StructureCreator(foundation_path)
    sys.exit(creator.run())