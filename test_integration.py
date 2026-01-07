"""
Integration test for the Manus Agent.
Tests all core functionality.
"""
import os
import shutil
from manus_agent import ManusAgent
from file_manager import FileManager


def test_file_manager():
    """Test FileManager basic operations."""
    print("Testing FileManager...")
    
    # Create a test directory
    test_dir = "test_output"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    fm = FileManager(test_dir)
    
    # Test plan creation
    fm.create_plan("Test Task", ["Phase 1", "Phase 2", "Phase 3"])
    assert os.path.exists(fm.plan_file), "Plan file should exist"
    
    # Test plan updates
    fm.update_plan(0, "completed", "Test note")
    content = fm.read_file('plan')
    assert "[x]" in content, "Phase should be marked as completed"
    assert "Test note" in content, "Note should be in progress log"
    
    # Test notes
    fm.add_notes("Test Section", "Test content here")
    assert os.path.exists(fm.notes_file), "Notes file should exist"
    notes = fm.read_file('notes')
    assert "Test Section" in notes, "Section should be in notes"
    
    # Test deliverable
    fm.create_deliverable("Test Deliverable", "Main content")
    assert os.path.exists(fm.deliverable_file), "Deliverable file should exist"
    deliverable = fm.read_file('deliverable')
    assert "Test Deliverable" in deliverable, "Title should be in deliverable"
    
    # Cleanup
    shutil.rmtree(test_dir)
    print("✓ FileManager tests passed")


def test_manus_agent():
    """Test ManusAgent basic operations."""
    print("Testing ManusAgent...")
    
    test_dir = "test_output"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    agent = ManusAgent(test_dir)
    
    # Test task start
    agent.start_task("Test Task", ["Phase 1", "Phase 2"])
    assert agent.task == "Test Task", "Task should be set"
    assert len(agent.phases) == 2, "Should have 2 phases"
    assert agent.current_phase == 0, "Should start at phase 0"
    
    # Test phase execution
    def test_research(phase_name):
        return f"Research for {phase_name}"
    
    def test_work(phase_name):
        return f"Work for {phase_name}"
    
    agent.execute_phase(0, research_callback=test_research)
    assert agent.current_phase == 1, "Should advance to phase 1"
    
    agent.execute_phase(1, work_callback=test_work)
    assert agent.current_phase == 2, "Should advance to phase 2"
    
    # Test status
    status = agent.get_status()
    assert status['completed_phases'] == 2, "Should have 2 completed phases"
    assert status['progress_percentage'] == 100.0, "Should be 100% complete"
    
    # Test deliverable generation
    agent.generate_deliverable()
    assert os.path.exists(agent.file_manager.deliverable_file), "Deliverable should exist"
    
    # Cleanup
    shutil.rmtree(test_dir)
    print("✓ ManusAgent tests passed")


def test_iteration():
    """Test automatic iteration."""
    print("Testing iteration...")
    
    test_dir = "test_output"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    agent = ManusAgent(test_dir)
    agent.start_task("Test Iteration", ["Phase 1", "Phase 2", "Phase 3"])
    
    def research(phase_name):
        return f"Research: {phase_name}"
    
    def work(phase_name):
        return f"Work: {phase_name}"
    
    # Iterate with callbacks
    agent.iterate(
        research_callbacks=[research, None, None],
        work_callbacks=[None, work, work]
    )
    
    assert agent.current_phase == 3, "All phases should be complete"
    
    status = agent.get_status()
    assert status['progress_percentage'] == 100.0, "Should be 100% complete"
    
    # Verify files exist
    assert os.path.exists(agent.file_manager.plan_file), "Plan should exist"
    assert os.path.exists(agent.file_manager.notes_file), "Notes should exist"
    
    # Verify content
    plan = agent.file_manager.read_file('plan')
    assert plan.count('[x]') == 3, "All phases should be marked complete"
    
    # Cleanup
    shutil.rmtree(test_dir)
    print("✓ Iteration tests passed")


def test_file_content():
    """Test that generated files have proper content."""
    print("Testing file content...")
    
    test_dir = "test_output"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    agent = ManusAgent(test_dir)
    agent.start_task("Content Test", ["Phase 1", "Phase 2"])
    
    agent.execute_phase(0, research_callback=lambda p: "Research content")
    agent.execute_phase(1, work_callback=lambda p: "Work content")
    agent.generate_deliverable(content_generator=lambda: "Custom deliverable")
    
    # Check plan content
    plan = agent.file_manager.read_file('plan')
    assert "Content Test" in plan, "Task name should be in plan"
    assert "Phase 1" in plan, "Phase 1 should be in plan"
    assert "Phase 2" in plan, "Phase 2 should be in plan"
    assert "## Progress Log" in plan, "Should have progress log"
    
    # Check notes content
    notes = agent.file_manager.read_file('notes')
    assert "Research content" in notes, "Research should be in notes"
    assert "Work content" in notes, "Work should be in notes"
    assert "Timestamp:" in notes, "Should have timestamps"
    
    # Check deliverable content
    deliverable = agent.file_manager.read_file('deliverable')
    assert "Custom deliverable" in deliverable, "Custom content should be in deliverable"
    assert "Generated:" in deliverable, "Should have generation timestamp"
    
    # Cleanup
    shutil.rmtree(test_dir)
    print("✓ File content tests passed")


def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("Running Integration Tests")
    print("="*60 + "\n")
    
    try:
        test_file_manager()
        test_manus_agent()
        test_iteration()
        test_file_content()
        
        print("\n" + "="*60)
        print("All tests passed! ✓")
        print("="*60 + "\n")
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}\n")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}\n")
        return 1


if __name__ == "__main__":
    exit(main())
