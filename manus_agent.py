"""
Manus Agent - AI Orchestration Layer
Mimics Manus by creating plan.md, notes.md, and deliverable.md for complex tasks.
"""
from typing import Optional, Callable
from file_manager import FileManager
import time


class ManusAgent:
    """
    An AI orchestration agent that breaks down complex tasks into phases,
    tracks progress, conducts research, and produces deliverables.
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize the Manus Agent.
        
        Args:
            output_dir: Directory where output files will be stored
        """
        self.file_manager = FileManager(output_dir)
        self.current_phase = 0
        self.phases = []
        self.task = ""
    
    def start_task(self, task: str, phases: Optional[list[str]] = None) -> None:
        """
        Start a new task by creating the plan.md file.
        
        Args:
            task: Description of the task to complete
            phases: List of phases to complete (if None, will generate default phases)
        """
        self.task = task
        
        # Default phases if none provided
        if phases is None:
            phases = [
                "Understand the task and requirements",
                "Research and gather information",
                "Design the solution approach",
                "Implement the solution",
                "Review and refine",
                "Finalize deliverable"
            ]
        
        self.phases = phases
        self.current_phase = 0
        
        # Create the initial plan
        self.file_manager.create_plan(task, phases)
        print(f"✓ Plan created with {len(phases)} phases")
    
    def execute_phase(self, 
                     phase_index: int,
                     research_callback: Optional[Callable[[str], str]] = None,
                     work_callback: Optional[Callable[[str], str]] = None) -> None:
        """
        Execute a specific phase of the task.
        
        Args:
            phase_index: Index of the phase to execute (0-based)
            research_callback: Optional function to perform research for this phase
            work_callback: Optional function to perform work for this phase
        """
        if phase_index >= len(self.phases):
            raise ValueError(f"Phase index {phase_index} out of range")
        
        phase_name = self.phases[phase_index]
        print(f"\n→ Starting Phase {phase_index + 1}: {phase_name}")
        
        # Mark phase as in progress
        self.file_manager.update_plan(phase_index, "in_progress")
        
        # Research phase
        if research_callback:
            print(f"  Conducting research...")
            research_result = research_callback(phase_name)
            self.file_manager.add_notes(
                f"Phase {phase_index + 1}: {phase_name}",
                research_result
            )
            print(f"  ✓ Research notes saved")
        
        # Work phase
        if work_callback:
            print(f"  Performing work...")
            work_result = work_callback(phase_name)
            # Store work results in notes as well
            self.file_manager.add_notes(
                f"Phase {phase_index + 1} - Work Output",
                work_result
            )
            print(f"  ✓ Work completed")
        
        # Mark phase as completed
        self.file_manager.update_plan(phase_index, "completed")
        print(f"✓ Phase {phase_index + 1} completed")
        
        self.current_phase = phase_index + 1
    
    def iterate(self, 
               research_callbacks: Optional[list[Callable[[str], str]]] = None,
               work_callbacks: Optional[list[Callable[[str], str]]] = None) -> None:
        """
        Iterate through all phases automatically.
        
        Args:
            research_callbacks: List of research functions for each phase
            work_callbacks: List of work functions for each phase
        """
        print(f"\n{'='*60}")
        print(f"Starting Task: {self.task}")
        print(f"{'='*60}")
        
        for i in range(len(self.phases)):
            research_cb = research_callbacks[i] if research_callbacks and i < len(research_callbacks) else None
            work_cb = work_callbacks[i] if work_callbacks and i < len(work_callbacks) else None
            
            self.execute_phase(i, research_cb, work_cb)
            
            # Small delay to simulate processing
            time.sleep(0.5)
        
        print(f"\n{'='*60}")
        print(f"All phases completed!")
        print(f"{'='*60}\n")
    
    def generate_deliverable(self, 
                           title: Optional[str] = None,
                           content_generator: Optional[Callable[[], str]] = None) -> None:
        """
        Generate the final deliverable.
        
        Args:
            title: Title for the deliverable (defaults to task name)
            content_generator: Optional function to generate deliverable content
        """
        if title is None:
            title = f"Deliverable: {self.task}"
        
        print(f"\n→ Generating deliverable...")
        
        if content_generator:
            content = content_generator()
        else:
            # Default: Summarize from notes
            notes_content = self.file_manager.read_file('notes')
            content = f"""## Summary

This deliverable was generated from the task: {self.task}

## Phases Completed

"""
            for i, phase in enumerate(self.phases, 1):
                content += f"- {phase}\n"
            
            content += f"""
## Research Notes Summary

The detailed research and findings can be found in notes.md.

## Conclusion

All phases have been completed as outlined in plan.md.
"""
        
        self.file_manager.create_deliverable(title, content)
        print(f"✓ Deliverable created")
    
    def add_deliverable_section(self, section: str, content: str) -> None:
        """
        Add a section to the deliverable.
        
        Args:
            section: Section title
            content: Section content
        """
        self.file_manager.update_deliverable(section, content)
        print(f"✓ Added section '{section}' to deliverable")
    
    def get_status(self) -> dict:
        """
        Get the current status of the task.
        
        Returns:
            Dictionary with status information
        """
        return {
            'task': self.task,
            'total_phases': len(self.phases),
            'current_phase': self.current_phase,
            'completed_phases': self.current_phase,
            'remaining_phases': len(self.phases) - self.current_phase,
            'progress_percentage': (self.current_phase / len(self.phases) * 100) if self.phases else 0
        }
    
    def print_status(self) -> None:
        """Print the current status."""
        status = self.get_status()
        print(f"\n{'='*60}")
        print(f"Task Status")
        print(f"{'='*60}")
        print(f"Task: {status['task']}")
        print(f"Progress: {status['completed_phases']}/{status['total_phases']} phases completed")
        print(f"Percentage: {status['progress_percentage']:.1f}%")
        print(f"{'='*60}\n")
