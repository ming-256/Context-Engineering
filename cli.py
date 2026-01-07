#!/usr/bin/env python3
"""
Command-line interface for the Manus Agent.
Usage: python cli.py --task "Your task description" [--output-dir output]
"""
import argparse
import sys
from manus_agent import ManusAgent


def default_research(phase_name: str) -> str:
    """Default research function."""
    return f"""
### Research for {phase_name}

- Analyzed requirements
- Explored options
- Documented findings
- Identified next steps
"""


def default_work(phase_name: str) -> str:
    """Default work function."""
    return f"""
### Work completed for {phase_name}

- Implementation done
- Testing completed
- Documentation updated
- Ready for next phase
"""


def main():
    """Run the CLI."""
    parser = argparse.ArgumentParser(
        description="Manus Agent - AI Orchestration Layer CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --task "Build a REST API"
  python cli.py --task "Create a web app" --output-dir my_project
  python cli.py --task "Design a system" --phases "Research" "Design" "Implement"
        """
    )
    
    parser.add_argument(
        "--task",
        required=True,
        help="Description of the task to execute"
    )
    
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory for output files (default: output)"
    )
    
    parser.add_argument(
        "--phases",
        nargs="+",
        help="Custom phases (space-separated)"
    )
    
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Automatically iterate through all phases"
    )
    
    parser.add_argument(
        "--no-callbacks",
        action="store_true",
        help="Skip research and work callbacks (just track phases)"
    )
    
    args = parser.parse_args()
    
    # Create agent
    print("\n" + "="*70)
    print("Manus Agent - Starting Task")
    print("="*70)
    print(f"Task: {args.task}")
    print(f"Output Directory: {args.output_dir}")
    print("="*70 + "\n")
    
    agent = ManusAgent(output_dir=args.output_dir)
    
    # Start task with custom or default phases
    agent.start_task(args.task, phases=args.phases)
    
    if args.auto:
        # Automatic iteration
        if args.no_callbacks:
            # No callbacks - just track phases
            agent.iterate()
        else:
            # With default callbacks
            num_phases = len(agent.phases)
            research_cbs = [default_research if i < num_phases // 2 else None 
                           for i in range(num_phases)]
            work_cbs = [None if i < num_phases // 2 else default_work 
                       for i in range(num_phases)]
            agent.iterate(research_cbs, work_cbs)
        
        # Generate deliverable
        agent.generate_deliverable()
        agent.print_status()
    else:
        # Manual mode - just create the plan
        print("\nPlan created successfully!")
        print("\nNext steps:")
        print("  1. Review plan.md in the output directory")
        print("  2. Use the Python API to execute phases manually")
        print("  3. Or run with --auto to execute all phases automatically")
        print("\nFor automatic execution, run:")
        print(f'  python cli.py --task "{args.task}" --auto')
    
    print("\n" + "="*70)
    print("Output files in:", args.output_dir)
    print("  - plan.md")
    if args.auto:
        print("  - notes.md")
        print("  - deliverable.md")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
