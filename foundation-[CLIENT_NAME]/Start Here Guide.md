# Foundation™ - Start Here Guide

## What is Foundation™?

Foundation™ is an AI-powered business intelligence system that creates four AI executives who understand a specific company. Think of it as building a virtual executive team that knows the business inside and out.

## Your AI Executive Team

- **🎯 ATLAS** - Strategic Intelligence Officer (market opportunities, competition, growth strategy)
- **📊 NAVIGATOR** - Operations Excellence Officer (metrics, processes, efficiency)
- **🔧 MAESTRO** - Technology Integration Officer (systems, automation, tech strategy)
- **🚀 CATALYST** - Change & Adoption Officer (culture, transformation, adoption)

## How It Works

1. **Discover** - Gather company intelligence from public sources
2. **Classify** - Understand the business type and growth stage
3. **Generate** - Create customized AI executives for their specific needs
4. **Structure** - Build the right file structure for their archetype
5. **Research** - Populate with targeted intelligence
6. **Activate** - Deploy and start using the AI executives

## Getting Started

### Prerequisites
- GitHub account (free at github.com)
- Windsurf or Cursor IDE installed
- 2-4 hours for initial setup
- Company website URL or LinkedIn profile

### Important Note: Template Files
The Foundation template comes with many empty files pre-created. The workflows will:
- **Update** existing files (like company_overview.md, agent files)
- **Create** new files (like research files, intelligence reports)

This allows you to re-run workflows to refine and improve your Foundation over time.

### Step 1: Get the Template
1. Download the Foundation template
2. Extract to a folder
3. Rename to `foundation-[company-name]`
4. Open in Windsurf/Cursor

### Step 2: Run the Setup Workflows

The workflows are designed to be run in order. Here's what each does:

#### `/01_discovery` (20 minutes)
Gathers initial company intelligence from web sources.
- Input: Company URL
- Output: Comprehensive company overview
- Updates: `shared_context/company_overview.md`

#### `/02_classification` (10 minutes) 
Analyzes the business type and defines transformation goals.
- Input: Company overview
- Output: Business classification and goals
- Updates: `shared_context/business_classification.md` and `next_level_goals.md`

#### `/03_agent_generation` (20 minutes)
Creates customized AI executive personas.
- Input: Company data + classification
- Output: Four AI agents calibrated for the business
- Updates: `.agents/ATLAS.md`, `NAVIGATOR.md`, `MAESTRO.md`, `CATALYST.md`
- Creates: `shared_context/industry_intelligence.md`, `enhanced_overview.md`

#### `/04_structure_creation` (10 minutes)
Builds the right file structure based on business type.
- Input: Business classification
- Output: Empty files ready for research
- Creates: 15-25 new files across all agent folders

#### `/05_research_population` (60+ minutes)
Fills all files with targeted intelligence.
- Input: File structure + web research
- Output: Fully populated Foundation
- Updates: All created files with real data

### Step 3: Test Your Foundation

After setup, test each agent:

```
@ATLAS What's the biggest opportunity for this company?
@NAVIGATOR What should we optimize first?
@MAESTRO What technology would give us an edge?
@CATALYST How do we get the team on board?
```

## Quick Reference

### File Structure
```
foundation-[company]/
├── .agents/           → AI executive prompts
├── shared_context/    → Company-wide data
├── ATLAS/            → Strategic intelligence
├── NAVIGATOR/        → Operational data
├── MAESTRO/          → Technology insights
├── CATALYST/         → Change readiness
└── README.md         → Documentation
```

### Key Files to Know
- `foundation.config.yaml` - Basic configuration (edit first!)
- `shared_context/company_overview.md` - Core company data
- `shared_context/business_classification.md` - Business type analysis
- `.agents/*.md` - The AI executive "brains"

### Common Commands
- Save file: `Ctrl+S` (PC) or `Cmd+S` (Mac)
- Run workflow: Type workflow name in chat
- Test agent: `@AGENTNAME [your question]`

## Troubleshooting

### "Agent can't see files"
- Check YAML header includes agent in `agent_scope`
- Ensure file is saved
- Close and reopen file

### "Web search not working"
- Use `@web` exactly as shown in prompts
- Break complex searches into parts
- Be specific with search terms

### "Overwhelmed by complexity"
- Follow workflows in order
- Take breaks between phases
- Remember: 80% complete is useful, 0% is not

## Business Types We Support

### Early Startup (1-10 employees)
Focus: Product-market fit, customer validation, runway

### Growth Startup (11-50 employees)  
Focus: Scalable processes, unit economics, talent

### Scale-Up (51-200 employees)
Focus: Market expansion, operational excellence, platform

### Mid-Market (201-500 employees)
Focus: Digital transformation, competitive differentiation, efficiency

### Enterprise (500+ employees)
Focus: Innovation, disruption defense, transformation

## Success Metrics

A successful Foundation has:
- ✅ 4 customized AI executives
- ✅ 15-25 populated intelligence files
- ✅ Agents that give specific, valuable advice
- ✅ Clear next steps for transformation
- ✅ Knowledge that updates over time

## Next Steps After Setup

1. **Daily**: Ask agents for insights on current challenges
2. **Weekly**: Update with new market intelligence
3. **Monthly**: Review and refine agent responses
4. **Quarterly**: Major update of all intelligence

## Getting Help

If stuck:
1. Note which workflow step you're on
2. Copy any error messages
3. Ask: "I'm on [workflow/step] and seeing [issue]"

Remember: The goal is a working Foundation that delivers value, not perfection. You can always improve it over time.

---

Ready to start? Begin with workflow `/01_discovery` and follow the sequence. In 2-4 hours, you'll have a complete AI executive team that knows the business!