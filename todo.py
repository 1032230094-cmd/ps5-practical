import sys
from rich.console import Console
from rich.table import Table

# Initialize the console for pretty printing
console = Console()

# A simple list to store tasks (in-memory storage)
# Each task is a dictionary: {'task': str, 'status': str}
tasks = []

def show_menu():
    """Displays the main menu options."""
    console.print("\n[bold cyan]--- TO-DO LIST MENU ---[/bold cyan]")
    console.print("[1] Add Task")
    console.print("[2] View Tasks")
    console.print("[3] Mark Task as Done")
    console.print("[4] Delete Task")
    console.print("[5] Exit")

def add_task():
    """Adds a new task to the list."""
    task_name = console.input("[bold yellow]Enter task name: [/bold yellow]")
    if task_name:
        tasks.append({"task": task_name, "status": "Pending"})
        console.print(f"[bold green]Task '{task_name}' added successfully![/bold green]")
    else:
        console.print("[bold red]Task name cannot be empty![/bold red]")

def view_tasks():
    """Displays all tasks in a nice table."""
    if not tasks:
        console.print("[italic red]No tasks found.[/italic red]")
        return

    table = Table(title="Your To-Do List")
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Task", style="magenta")
    table.add_column("Status", justify="center", style="green")

    for idx, t in enumerate(tasks):
        # Change status color based on state
        status_text = "[green]Done[/green]" if t["status"] == "Done" else "[red]Pending[/red]"
        table.add_row(str(idx + 1), t["task"], status_text)

    console.print(table)

def mark_done():
    """Marks a specific task as completed."""
    view_tasks()
    if not tasks: return

    try:
        idx = int(console.input("[bold yellow]Enter ID to mark as Done: [/bold yellow]")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["status"] = "Done"
            console.print(f"[bold green]Task '{tasks[idx]['task']}' marked as done![/bold green]")
        else:
            console.print("[bold red]Invalid ID.[/bold red]")
    except ValueError:
        console.print("[bold red]Please enter a valid number.[/bold red]")

def delete_task():
    """Removes a task from the list."""
    view_tasks()
    if not tasks: return

    try:
        idx = int(console.input("[bold yellow]Enter ID to delete: [/bold yellow]")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            console.print(f"[bold green]Task '{removed['task']}' deleted![/bold green]")
        else:
            console.print("[bold red]Invalid ID.[/bold red]")
    except ValueError:
        console.print("[bold red]Please enter a valid number.[/bold red]")

def main():
    """Main application loop."""
    console.print("[bold magenta]Welcome to your Python To-Do App![/bold magenta]")
    
    while True:
        show_menu()
        choice = console.input("[bold blue]Choose an option (1-5): [/bold blue]")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            console.print("[bold cyan]Goodbye![/bold cyan]")
            sys.exit()
        else:
            console.print("[bold red]Invalid choice, please try again.[/bold red]")

if __name__ == "__main__":
    main()