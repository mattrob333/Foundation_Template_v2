# Foundation Template

A comprehensive template for building AI-powered business intelligence, research, and automation platforms. This repository provides a modular structure for rapid deployment, customization, and scaling of agent-based solutions.

## Overview

This template includes:
- **Agent Configurations**: Modular agent definitions for ATLAS, NAVIGATOR, MAESTRO, and CATALYST.
- **Shared Context**: Common business context and reusable knowledge assets.
- **Agent Knowledge Bases**: Domain-specific directories for each agent.
- **Workflows**: Predefined workflows for research, discovery, and automation.
- **Utility Scripts**: Python scripts for setup, reporting, and maintenance.
- **Document Templates**: Markdown templates for rapid report and knowledge base generation.

## Directory Structure

```
.foundation-[CLIENT_NAME]/
├── .agents/                # Agent definitions and calibration files
├── .github/                # GitHub workflows and configuration
├── .scripts/               # Utility and automation scripts
├── .templates/             # Document and archetype templates
├── .workflows/             # Workflow definitions
├── ATLAS/                  # Competitive intelligence agent knowledge base
├── CATALYST/               # Change management agent knowledge base
├── MAESTRO/                # Technology and talent agent knowledge base
├── NAVIGATOR/              # Operations and sales agent knowledge base
├── shared_context/         # Shared business context
├── foundation.config.yaml  # Main configuration file
├── README.md               # This file
└── TEMPLATE_STRUCTURE.md   # Template structure and usage
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mattrob333/Foundation_Template_v2.git
   cd Foundation_Template_v2
   ```
2. **Rename the directory:**
   Rename `foundation-[CLIENT_NAME]` to match your client or project name.
3. **Update configuration:**
   Edit `foundation.config.yaml` with your organization or client details.
4. **Review agent and context files:**
   Populate the required knowledge base and context files as needed.

## Usage

- Use the provided workflows to guide research, discovery, and automation.
- Populate agent directories with relevant data and insights.
- Leverage utility scripts for automating data collection and reporting.
- Follow the structure in `TEMPLATE_STRUCTURE.md` for best practices.

## Customization

- Add or remove agents by editing the `.agents/` directory and config.
- Extend workflows in `.workflows/` to match your business processes.
- Modify document templates in `.templates/` for custom reporting needs.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License.
