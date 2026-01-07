"""
Simple example showing how to use the Manus Agent for a basic task.
"""
from manus_agent import ManusAgent


def simple_research(phase_name: str) -> str:
    """Simple research callback."""
    return f"Research conducted for: {phase_name}\n- Key findings documented\n- Resources identified"


def simple_work(phase_name: str) -> str:
    """Simple work callback."""
    return f"Work completed for: {phase_name}\n- Implementation done\n- Tests passed"


def main():
    """Run a simple example task."""
    # Create the agent
    agent = ManusAgent(output_dir="output")
    
    # Start a simple task
    agent.start_task("Build a simple web application")
    
    # Execute phases with callbacks
    agent.execute_phase(0, research_callback=simple_research)
    agent.execute_phase(1, research_callback=simple_research)
    agent.execute_phase(2, research_callback=simple_research)
    agent.execute_phase(3, work_callback=simple_work)
    agent.execute_phase(4, work_callback=simple_work)
    agent.execute_phase(5, work_callback=simple_work)
    
    # Generate deliverable
    agent.generate_deliverable()
    
    # Check status
    agent.print_status()
    
    print("\nTask completed! Check the output directory for results.")


if __name__ == "__main__":
    main()
