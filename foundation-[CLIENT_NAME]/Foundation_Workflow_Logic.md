# Foundation™ Workflow Logic & Design

## Why This Order Matters

The Foundation workflows follow a specific sequence designed to build upon each previous step:

### 1. Discovery → Classification → Structure → Agents → Research

This order ensures that:
- We understand the company before classifying it (one_discovery)
- We classify the company before building its structure (two_classification)
- We create the file structure before customizing agents (three_structure_creation)
- Agents know their files before we populate them (four_agent_generation)
- Everything is ready for intelligence gathering (five_research_population)

## The Logic Flow

### Step 1: Discovery (Know the Company)
**Purpose**: Gather all public intelligence about the company
**Output**: Comprehensive overview that feeds all other steps
**Why First**: Can't classify what we don't understand

### Step 2: Classification (Understand the Type)
**Purpose**: Determine archetype and transformation goals
**Output**: Blueprint for what kind of Foundation to build
**Why Second**: Structure depends on company type and goals

### Step 3: Structure Creation (Build the Framework)
**Purpose**: Create archetype-specific file structure
**Output**: Knowledge organization tailored to their needs
**Why Third**: Agents need to know what files they'll work with

### Step 4: Agent Generation (Customize the Executives)
**Purpose**: Create AI executives that understand their domain
**Output**: Agents calibrated for company AND file structure
**Why Fourth**: Agents must know their knowledge base layout

### Step 5: Research Population (Fill with Intelligence)
**Purpose**: Populate all files with targeted research
**Output**: Complete knowledge base for all agents
**Why Last**: Everything else must be ready first

## Key Design Principles

### 1. **Progressive Enhancement**
Each step adds a layer of customization:
- Generic template → Company-specific
- Company-specific → Archetype-optimized
- Archetype-optimized → File-aware
- File-aware → Intelligence-populated

### 2. **Dependency Management**
Each workflow explicitly states prerequisites:
- No classification without discovery
- No structure without classification
- No agents without structure
- No research without agents

### 3. **Rerunnable Workflows**
Design supports iterative improvement:
- "Update" existing files (not overwrite)
- "Create" new files (when needed)
- Can re-run to refine and improve
- No data loss on subsequent runs

### 4. **Archetype Templates**
Different company types need different structures:
- **Early Startup**: Focus on validation, minimal process
- **Growth Company**: Balance strategy and operations
- **Scale-Up**: Comprehensive coverage, market leadership
- **Mid-Market**: Digital transformation emphasis
- **Enterprise**: Innovation and disruption defense

### 5. **Agent File Awareness**
Agents know their knowledge structure:
```markdown
## My Knowledge Base Structure
I have access to strategic intelligence in:
- `/ATLAS/market_landscape/` - Market trends
- `/ATLAS/competitors/` - Competitive intelligence
- `/ATLAS/strategy/` - Strategic frameworks
```

This allows agents to:
- Reference specific files
- Guide research priorities
- Cross-reference between domains
- Provide file-specific insights

## Common Pitfalls Avoided

### ❌ Creating agents before structure
**Problem**: Agents don't know what files they'll have
**Solution**: Create structure first, then agents

### ❌ Populating files before agents exist
**Problem**: No guidance on what intelligence to gather
**Solution**: Agents guide research priorities

### ❌ One-size-fits-all structure
**Problem**: Startup needs ≠ Enterprise needs
**Solution**: Archetype-specific templates

### ❌ Static, unchangeable setup
**Problem**: Can't improve or update
**Solution**: Rerunnable workflows with update logic

## The Result

A Foundation that is:
- **Contextual**: Knows the specific company
- **Structured**: Organized for their archetype
- **Intelligent**: Agents understand their domain
- **Populated**: Full of relevant intelligence
- **Maintainable**: Can be updated and improved

## Visual Flow

```
Company URL
    ↓
[one_discovery] → Company Overview
    ↓
[two_classification] → Archetype + Goals
    ↓
[three_structure_creation] → File Framework
    ↓
[four_agent_generation] → Customized Executives
    ↓
[five_research_population] → Populated Intelligence
    ↓
Ready Foundation™
```

This logical flow ensures each component builds on the previous, creating a coherent, customized business intelligence system.