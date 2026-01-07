"""
Main entry point for the Manus Agent.
Demonstrates how to use the AI orchestration layer.
"""
from manus_agent import ManusAgent


def example_research_phase_1(phase_name: str) -> str:
    """Research for understanding the task."""
    return """
### Initial Analysis

- Reviewed the task requirements
- Identified key components needed
- Listed potential challenges
- Defined success criteria
"""


def example_research_phase_2(phase_name: str) -> str:
    """Research for gathering information."""
    return """
### Information Gathered

- Reviewed relevant documentation
- Explored similar solutions
- Identified best practices
- Noted potential pitfalls
"""


def example_research_phase_3(phase_name: str) -> str:
    """Research for solution design."""
    return """
### Design Considerations

- Architecture patterns evaluated
- Technology stack selected
- API design drafted
- Data flow mapped
"""


def example_work_phase_4(phase_name: str) -> str:
    """Work for implementation."""
    return """
### Implementation Progress

- Core modules created
- Key functions implemented
- Integration points established
- Initial testing completed
"""


def example_work_phase_5(phase_name: str) -> str:
    """Work for review and refinement."""
    return """
### Review Findings

- Code review completed
- Edge cases handled
- Performance optimized
- Documentation updated
"""


def generate_final_deliverable() -> str:
    """Generate the final deliverable content."""
    return """
## Executive Summary

This project successfully implements an AI orchestration layer inspired by Manus.

## Key Features

1. **Plan Management**: Tracks phases and progress through plan.md
2. **Research Documentation**: Stores findings and research in notes.md
3. **Deliverable Generation**: Produces final output in deliverable.md
4. **Iterative Workflow**: Supports plan → research → update → deliver cycle

## Architecture

The system consists of two main components:

- **FileManager**: Handles creation and updates of the three core files
- **ManusAgent**: Orchestrates the workflow and manages task execution

## Implementation Details

### FileManager
- Manages plan.md, notes.md, and deliverable.md
- Provides methods for creation, updates, and reading
- Timestamps all operations for auditability

### ManusAgent
- Breaks down complex tasks into manageable phases
- Executes phases with research and work callbacks
- Supports both manual and automated iteration
- Generates comprehensive deliverables

## Usage

The agent can be used in two ways:

1. **Manual Phase Execution**: Execute phases one at a time with custom callbacks
2. **Automatic Iteration**: Process all phases automatically with provided callbacks

## Outcomes

- Structured approach to complex tasks
- Clear documentation of progress
- Comprehensive research tracking
- Professional deliverables

## Future Enhancements

- Integration with AI APIs for automated research
- Support for subtasks and nested phases
- Collaborative features for team workflows
- Template system for common task types

## Conclusion

The Manus-inspired orchestration layer provides a robust framework for managing complex tasks through structured planning, research, and deliverable generation.
"""


def main():
    """Main function to demonstrate the Manus Agent."""
    
    # Example 1: Using the agent with automatic iteration
    print("\n" + "="*60)
    print("Manus Agent - AI Orchestration Layer Demo")
    print("="*60 + "\n")
    
    # Create an agent instance
    agent = ManusAgent(output_dir="output")
    
    # Define the task
    task = "Create an AI orchestration layer inspired by Manus"
    
    # Define custom phases
    phases = [
        "Understand the task and requirements",
        "Research AI orchestration patterns",
        "Design the system architecture",
        "Implement core modules",
        "Review and refine the implementation",
        "Generate final deliverable"
    ]
    
    # Start the task
    agent.start_task(task, phases)
    
    # Define callbacks for research and work
    research_callbacks = [
        example_research_phase_1,
        example_research_phase_2,
        example_research_phase_3,
        None,  # No research for phase 4
        None,  # No research for phase 5
        None   # No research for phase 6
    ]
    
    work_callbacks = [
        None,  # No work for phase 1
        None,  # No work for phase 2
        None,  # No work for phase 3
        example_work_phase_4,
        example_work_phase_5,
        None   # Deliverable generation happens separately
    ]
    
    # Iterate through all phases
    agent.iterate(research_callbacks, work_callbacks)
    
    # Generate the final deliverable
    agent.generate_deliverable(
        title="AI Orchestration Layer - Final Deliverable",
        content_generator=generate_final_deliverable
    )
    
    # Print final status
    agent.print_status()
    
    print("\n" + "="*60)
    print("Output files created in the 'output' directory:")
    print("  - plan.md: Task phases and progress tracking")
    print("  - notes.md: Research findings and work outputs")
    print("  - deliverable.md: Final deliverable document")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
