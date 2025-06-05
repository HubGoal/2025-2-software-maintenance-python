import os
import json
import uuid
from datetime import datetime
 
#Comentario para probar commits con fines demostrativos
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_name = "tasks.json"
        self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    self.tasks = json.load(file)
            except Exception as e:
                print(f"Error loading task data: {e}. Starting with empty task list.")
                self.tasks = []
    
    def save_tasks(self):
        try:
            with open(self.file_name, "w") as file:
                json.dump(self.tasks, file, indent=4)
        except Exception as e:
            print(f"Error saving task data: {e}")
    
    def add_task(self, title, description):
        if not title.strip():
            print("Title cannot be empty.")
            return
        if not description.strip():
            print("Description cannot be empty.")
            return
        
        task = {
            "id": str(uuid.uuid4()),
            "title": title.strip(),
            "description": description.strip(),
            "status": "Pending",
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\n" + "=" * 100)
        print(f"{'ID':<10} {'TITLE':<20} {'STATUS':<10} {'CREATED DATE':<20} {'DESCRIPTION':<30}")
        print("-" * 100)
        
        for task in self.tasks:
            short_id = task['id'][:8]
            print(f"{short_id:<10} {task['title'][:18]:<20} {task['status']:<10} {task['created_date']:<20} {task['description'][:28]:<30}")
        
        print("=" * 100 + "\n")
    
    def mark_complete(self, task_id):
        if not task_id.strip():
            print("Task ID cannot be empty.")
            return

        for task in self.tasks:
            if task["id"].startswith(task_id.strip()):
                if task["status"] == "Completed":
                    print(f"Task '{task['title']}' is already completed.")
                else:
                    task["status"] = "Completed"
                    self.save_tasks()
                    print(f"Task '{task['title']}' marked as completed!")
                return
        print(f"Task with ID starting with '{task_id}' not found.")
    
    def delete_task(self, task_id):
        if not task_id.strip():
            print("Task ID cannot be empty.")
            return

        for i, task in enumerate(self.tasks):
            if task["id"].startswith(task_id.strip()):
                removed = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task '{removed['title']}' deleted successfully!")
                return
        print(f"Task with ID starting with '{task_id}' not found.")


def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        
        elif choice == "2":
            task_manager.list_tasks()
        
        elif choice == "3":
            task_id = input("Enter beginning of task ID to mark as complete: ")
            task_manager.mark_complete(task_id)
        
        elif choice == "4":
            task_id = input("Enter beginning of task ID to delete: ")
            task_manager.delete_task(task_id)
        
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break


if __name__ == "__main__":
    main()
