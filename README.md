# Context-Engineering

An AI orchestration layer from scratch, inspired by Manus. This project implements an agent that manages complex tasks by creating and maintaining three key files: `plan.md`, `notes.md`, and `deliverable.md`.

## Overview

This orchestration layer breaks down complex tasks into manageable phases, tracks progress, documents research findings, and produces comprehensive deliverables. It follows an iterative workflow:

**Plan → Research → Update Plan → Create Deliverable → Iterate**

## Features

- **Plan Management**: Automatically creates and updates `plan.md` with task phases and progress tracking
- **Research Documentation**: Stores findings and research in `notes.md` with timestamps
- **Deliverable Generation**: Produces final output in `deliverable.md`
- **Iterative Workflow**: Supports both manual and automated phase execution
- **Progress Tracking**: Real-time status updates and completion percentages
- **Flexible Callbacks**: Customize research and work for each phase

## Project Structure

```
.
├── file_manager.py      # Handles plan.md, notes.md, and deliverable.md
├── manus_agent.py       # Core orchestration agent
├── main.py              # Full example with custom callbacks
├── example_simple.py    # Simple usage example
├── requirements.txt     # Python dependencies (none required for basic usage)
└── output/             # Generated files (plan.md, notes.md, deliverable.md)
```

## Installation

No external dependencies are required! Just Python 3.8+.

```bash
git clone https://github.com/ming-256/Context-Engineering.git
cd Context-Engineering
```

## Quick Start

### Basic Usage

```python
from manus_agent import ManusAgent

# Create an agent
agent = ManusAgent(output_dir="output")

# Start a task
agent.start_task("Build a simple web application")

# Execute phases (with optional callbacks)
agent.execute_phase(0, research_callback=my_research_function)
agent.execute_phase(1, work_callback=my_work_function)

# Generate deliverable
agent.generate_deliverable()
```

### Run the Examples

```bash
# Full example with custom phases and callbacks
python main.py

# Simple example
python example_simple.py
```

Both examples will create an `output` directory with three files:
- `plan.md` - Task phases with progress tracking
- `notes.md` - Research findings and work outputs
- `deliverable.md` - Final deliverable document

## Core Components

### FileManager

Manages the three core markdown files:

```python
from file_manager import FileManager

fm = FileManager(output_dir="output")

# Create a plan
fm.create_plan("My task", ["Phase 1", "Phase 2", "Phase 3"])

# Update plan progress
fm.update_plan(0, status="completed", notes="Phase 1 done")

# Add research notes
fm.add_notes("Research Topic", "My findings here...")

# Create deliverable
fm.create_deliverable("Project Title", "Main content here...")
```

### ManusAgent

Orchestrates the entire workflow:

```python
from manus_agent import ManusAgent

agent = ManusAgent(output_dir="output")

# Define custom phases
phases = [
    "Understand requirements",
    "Research solutions", 
    "Design architecture",
    "Implement",
    "Test and refine"
]

# Start with custom phases
agent.start_task("My Complex Task", phases)

# Automatic iteration with callbacks
agent.iterate(
    research_callbacks=[callback1, callback2, None, None, None],
    work_callbacks=[None, None, callback3, callback4, callback5]
)

# Generate final deliverable
agent.generate_deliverable(content_generator=my_content_function)

# Check status
status = agent.get_status()
print(f"Progress: {status['progress_percentage']:.1f}%")
```

## Workflow

The agent follows a structured workflow:

1. **Create Plan** - Define the task and break it into phases
2. **Execute Phases** - For each phase:
   - Mark as in progress
   - Conduct research (optional callback)
   - Perform work (optional callback)
   - Save notes to `notes.md`
   - Mark as completed
   - Update `plan.md`
3. **Generate Deliverable** - Compile final output to `deliverable.md`
4. **Iterate** - Repeat as needed

## Example Output

### plan.md
```markdown
# Plan

**Task:** Create an AI orchestration layer
**Created:** 2026-01-07 20:30:00
**Status:** In Progress

## Phases

1. [x] Understand the task and requirements
2. [x] Research AI orchestration patterns
3. [~] Design the system architecture
4. [ ] Implement core modules
5. [ ] Review and refine
6. [ ] Generate final deliverable

## Progress Log

- 2026-01-07 20:32:15: Phase 3 in_progress
- 2026-01-07 20:31:45: Phase 2 completed
- 2026-01-07 20:31:00: Phase 1 completed
- 2026-01-07 20:30:00: Plan created with 6 phases
```

### notes.md
```markdown
# Research Notes

## Phase 1: Understand the task and requirements

**Timestamp:** 2026-01-07 20:30:15

### Initial Analysis

- Reviewed the task requirements
- Identified key components needed
- Listed potential challenges

---
```

### deliverable.md
```markdown
# AI Orchestration Layer - Final Deliverable

**Generated:** 2026-01-07 20:35:00

## Executive Summary

This project successfully implements an AI orchestration layer...

## Key Features

1. Plan Management
2. Research Documentation
3. Deliverable Generation

## Conclusion

All phases completed successfully.
```

## Customization

### Custom Phases

```python
agent = ManusAgent()
agent.start_task(
    "My Task",
    phases=[
        "Phase 1: Discovery",
        "Phase 2: Analysis", 
        "Phase 3: Implementation",
        "Phase 4: Validation"
    ]
)
```

### Custom Callbacks

```python
def my_research(phase_name: str) -> str:
    # Your research logic here
    return "Research findings..."

def my_work(phase_name: str) -> str:
    # Your work logic here
    return "Work output..."

agent.execute_phase(0, research_callback=my_research)
agent.execute_phase(1, work_callback=my_work)
```

### Custom Deliverable

```python
def generate_custom_deliverable() -> str:
    return """
    # My Custom Deliverable
    
    Content here...
    """

agent.generate_deliverable(
    title="Custom Title",
    content_generator=generate_custom_deliverable
)
```

## Future Enhancements

- Integration with AI APIs (OpenAI, Anthropic) for automated research
- Support for subtasks and nested phases
- Collaborative features for team workflows
- Template system for common task types
- Web interface for monitoring progress
- Export to different formats (PDF, HTML)

## Contributing

This is a learning project for documenting the creation of an AI orchestration layer from scratch. Contributions, ideas, and feedback are welcome!

## License

See LICENSE file for details.

## Acknowledgments

Inspired by Manus and the concept of structured AI-driven task management.

