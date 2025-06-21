# Foundation™ Quick Reference Card

## File Operations Cheat Sheet

### Creating vs Updating Files

**Files that ALREADY EXIST in template (Update):**
```
shared_context/company_overview.md
shared_context/business_classification.md  
shared_context/next_level_goals.md
.agents/ATLAS.md
.agents/NAVIGATOR.md
.agents/MAESTRO.md
.agents/CATALYST.md
foundation.config.yaml
README.md
```

**Files you CREATE NEW during workflows:**
```
shared_context/industry_intelligence.md
shared_context/enhanced_overview.md
shared_context/file_inventory.md
shared_context/research_summary.md
.agents/calibration_guide.md
.agents/AGENT_SUMMARY.md
```

**Files from archetype templates (Copy/Create):**
```
ATLAS/[various files based on archetype]
NAVIGATOR/[various files based on archetype]
MAESTRO/[various files based on archetype]
CATALYST/[various files based on archetype]
```

## Workflow Order & Time

1. `one_discovery` → 20 min → Updates company_overview.md
2. `two_classification` → 10 min → Updates classification.md & goals.md
3. `three_structure_creation` → 10 min → Creates 15-25 archetype-specific files
4. `four_agent_generation` → 20 min → Updates agents with file knowledge
5. `five_research_population` → 60 min → Populates all files with intelligence

**Total: 2-3 hours**

## Common Commands

### File Operations
- Save file: `Ctrl+S` (PC) or `Cmd+S` (Mac)
- Save all: `Ctrl+K S` (PC) or `Cmd+K S` (Mac)
- Close file: `Ctrl+W` (PC) or `Cmd+W` (Mac)

### Testing Agents
```
@ATLAS [question]
@NAVIGATOR [question]
@MAESTRO [question]
@CATALYST [question]
```

### Web Search Format
```
@web search "[search terms]"
```

## Quick Validation Tests

### After Discovery:
```
@ATLAS Can you see the company overview?
```

### After Classification:
```
@ATLAS What's our next level transformation goal?
```

### After Structure Creation:
```
Check: Do all agent folders have archetype-specific files?
Look for: shared_context/file_inventory.md
```

### After Agent Generation:
```
@[ANY_AGENT] What files do you have access to?
@[ANY_AGENT] What should {{company}} focus on?
```

### After Research:
```
@ATLAS @NAVIGATOR @MAESTRO @CATALYST What's your #1 insight?
```

## Archetype Quick Guide

| Employees | Archetype | Focus | Files |
|-----------|-----------|-------|-------|
| 1-10 | EARLY_STARTUP | Product-Market Fit | ~15 |
| 11-50 | GROWTH_STARTUP | Scalable Growth | ~18 |
| 51-200 | SCALE_UP | Market Leadership | ~20 |
| 201-500 | MID_MARKET | Digital Transform | ~18 |
| 500+ | ENTERPRISE | Innovation | ~22 |

## File Header Template
```yaml
---
title: "[Descriptive Title]"
source: "[Where data came from]"
owner: "intel@tier4.ai"
agent_scope: ["AGENT_NAME"]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
tags: ["tag1", "tag2"]
---
```

## Troubleshooting Quick Fixes

**"Agent can't see file"**
- Check `agent_scope` includes agent name
- Ensure file is saved
- Close and reopen file

**"Web search failed"**
- Simplify search terms
- Remove special characters
- Try without quotes

**"File not found"**
- Check exact path/spelling
- Ensure directory exists
- Look for .gitkeep files

**"Placeholder text remains"**
- Search for: [[ or {{ or TODO
- Check YAML headers
- Review company name usage

## Emergency Recovery

If something goes wrong:
1. Save all open files
2. Note last successful step
3. Close and reopen IDE
4. Resume from last checkpoint

## Success Indicators

✅ No [PLACEHOLDER] text anywhere
✅ Agents give specific answers
✅ Files have real data (not templates)
✅ Cross-agent collaboration works
✅ Clear next steps identified

---

**Remember:** The goal is a useful Foundation, not a perfect one. You can always refine and improve over time!