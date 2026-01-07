"""
File Manager module for handling plan.md, notes.md, and deliverable.md files.
"""
import os
from typing import Optional
from datetime import datetime


class FileManager:
    """Manages the three core files for the Manus-style agent."""
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize the FileManager.
        
        Args:
            output_dir: Directory where files will be stored
        """
        self.output_dir = output_dir
        self.plan_file = os.path.join(output_dir, "plan.md")
        self.notes_file = os.path.join(output_dir, "notes.md")
        self.deliverable_file = os.path.join(output_dir, "deliverable.md")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def create_plan(self, task: str, phases: list[str]) -> None:
        """
        Create the initial plan.md file.
        
        Args:
            task: The task description
            phases: List of phases to complete
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"""# Plan

**Task:** {task}

**Created:** {timestamp}
**Status:** In Progress

## Phases

"""
        for i, phase in enumerate(phases, 1):
            content += f"{i}. [ ] {phase}\n"
        
        content += f"""
## Progress Log

- {timestamp}: Plan created with {len(phases)} phases
"""
        
        with open(self.plan_file, 'w') as f:
            f.write(content)
    
    def update_plan(self, phase_index: int, status: str = "completed", notes: Optional[str] = None) -> None:
        """
        Update the plan.md file with phase progress.
        
        Args:
            phase_index: Index of the phase to update (0-based)
            status: Status of the phase (completed, in_progress, etc.)
            notes: Optional notes to add to the progress log
        """
        if not os.path.exists(self.plan_file):
            raise FileNotFoundError("plan.md does not exist. Create it first.")
        
        with open(self.plan_file, 'r') as f:
            content = f.read()
        
        # Update phase status
        lines = content.split('\n')
        for i, line in enumerate(lines):
            # Match lines that start with the phase number
            if line.strip().startswith(f"{phase_index + 1}. "):
                if status == "completed":
                    # Replace any checkbox status with [x]
                    if "[ ]" in line:
                        lines[i] = line.replace("[ ]", "[x]")
                    elif "[~]" in line:
                        lines[i] = line.replace("[~]", "[x]")
                elif status == "in_progress":
                    # Replace [ ] with [~]
                    if "[ ]" in line:
                        lines[i] = line.replace("[ ]", "[~]")
                break
        
        # Add to progress log
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        progress_entry = f"- {timestamp}: Phase {phase_index + 1} {status}"
        if notes:
            progress_entry += f" - {notes}"
        
        # Find the progress log section and add the entry
        for i, line in enumerate(lines):
            if line.strip() == "## Progress Log":
                lines.insert(i + 2, progress_entry)
                break
        
        with open(self.plan_file, 'w') as f:
            f.write('\n'.join(lines))
    
    def add_notes(self, section: str, content: str) -> None:
        """
        Add research notes to notes.md.
        
        Args:
            section: Section title for the notes
            content: Content to add
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Check if file exists
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as f:
                existing_content = f.read()
        else:
            existing_content = "# Research Notes\n\n"
        
        new_section = f"""
## {section}

**Timestamp:** {timestamp}

{content}

---

"""
        
        with open(self.notes_file, 'w') as f:
            f.write(existing_content + new_section)
    
    def create_deliverable(self, title: str, content: str) -> None:
        """
        Create or update the deliverable.md file.
        
        Args:
            title: Title of the deliverable
            content: Main content
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        deliverable_content = f"""# {title}

**Generated:** {timestamp}

{content}
"""
        
        with open(self.deliverable_file, 'w') as f:
            f.write(deliverable_content)
    
    def update_deliverable(self, section: str, content: str) -> None:
        """
        Update the deliverable.md file with new content.
        
        Args:
            section: Section to add or update
            content: Content to add
        """
        if not os.path.exists(self.deliverable_file):
            raise FileNotFoundError("deliverable.md does not exist. Create it first.")
        
        with open(self.deliverable_file, 'r') as f:
            existing_content = f.read()
        
        new_section = f"""
## {section}

{content}
"""
        
        with open(self.deliverable_file, 'a') as f:
            f.write(new_section)
    
    def read_file(self, file_type: str) -> str:
        """
        Read content from one of the managed files.
        
        Args:
            file_type: Type of file to read ('plan', 'notes', or 'deliverable')
        
        Returns:
            Content of the file
        """
        file_map = {
            'plan': self.plan_file,
            'notes': self.notes_file,
            'deliverable': self.deliverable_file
        }
        
        file_path = file_map.get(file_type)
        if not file_path:
            raise ValueError(f"Invalid file type: {file_type}")
        
        if not os.path.exists(file_path):
            return ""
        
        with open(file_path, 'r') as f:
            return f.read()
