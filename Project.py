import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Database Setup
def setup_database():
    conn = sqlite3.connect('productivity.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        employee_name TEXT,
                        task_name TEXT,
                        priority TEXT,
                        estimated_time INTEGER,
                        actual_time INTEGER,
                        status TEXT,
                        deadline TEXT,
                        recurring TEXT,
                        date TEXT
                     )''')
    conn.commit()
    conn.close()

# Add Task
def add_task(employee_name, task_name, priority, estimated_time, actual_time, status, deadline, recurring):
    conn = sqlite3.connect('productivity.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO tasks (employee_name, task_name, priority, estimated_time, actual_time, status, deadline, recurring, date) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (employee_name, task_name, priority, estimated_time, actual_time, status, deadline, recurring,
                    datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

# Update Task Status
def update_task_status(task_id, status):
    conn = sqlite3.connect('productivity.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
    conn.commit()
    conn.close()

# View Tasks
def view_tasks():
    conn = sqlite3.connect('productivity.db')
    tasks = pd.read_sql_query('SELECT * FROM tasks', conn)
    conn.close()
    return tasks

# Prioritize Tasks
def prioritize_tasks():
    tasks = view_tasks()
    tasks['deadline'] = pd.to_datetime(tasks['deadline'])
    prioritized_tasks = tasks.sort_values(by=['priority', 'deadline'], ascending=[True, True])
    print("\nPrioritized Tasks (Sorted by Priority and Deadline):")
    print(prioritized_tasks[['id', 'employee_name', 'task_name', 'priority', 'deadline', 'status']])
    return prioritized_tasks

# Notify Deadlines
def notify_deadlines():
    tasks = view_tasks()
    tasks['deadline'] = pd.to_datetime(tasks['deadline'])
    current_date = datetime.now()

    upcoming = tasks[(tasks['deadline'] >= current_date) & (tasks['deadline'] <= current_date + timedelta(days=3))]
    missed = tasks[tasks['deadline'] < current_date]

    if not upcoming.empty:
        print("\n[Upcoming Deadlines]")
        print(upcoming[['id', 'employee_name', 'task_name', 'priority', 'deadline']])
    else:
        print("\nNo upcoming deadlines in the next 3 days.")

    if not missed.empty:
        print("\n[Missed Deadlines]")
        print(missed[['id', 'employee_name', 'task_name', 'priority', 'deadline']])
    else:
        print("\nNo missed deadlines!")

# Generate Insights
def generate_detailed_insights():
    tasks = view_tasks()
    total_tasks = len(tasks)
    completed_tasks = len(tasks[tasks['status'] == 'Completed'])
    pending_tasks = len(tasks[tasks['status'] == 'Pending'])
    missed_deadlines = len(tasks[pd.to_datetime(tasks['deadline']) < datetime.now()])

    print(f"\nTotal Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Missed Deadlines: {missed_deadlines}")

# Visualization
def visualize_team_performance():
    tasks = view_tasks()
    sns.set(style="whitegrid")

    # Task Completion by Status
    plt.figure(figsize=(10, 6))
    sns.countplot(x='employee_name', hue='status', data=tasks)
    plt.title('Team Performance: Task Completion Status')
    plt.xlabel('Employee Name')
    plt.ylabel('Task Count')
    plt.legend(title='Status')
    plt.show()

    # Efficiency by Employee
    tasks['Efficiency'] = tasks['estimated_time'] / tasks['actual_time']
    plt.figure(figsize=(10, 6))
    sns.barplot(x='employee_name', y='Efficiency', data=tasks)
    plt.title('Efficiency by Employee')
    plt.xlabel('Employee Name')
    plt.ylabel('Efficiency')
    plt.show()

# Search Tasks
def search_tasks():
    tasks = view_tasks()
    search_criteria = input("Search by (employee_name/task_name/status): ").strip().lower()
    query = input(f"Enter the value for {search_criteria}: ").strip()

    if search_criteria in tasks.columns:
        results = tasks[tasks[search_criteria].str.contains(query, case=False)]
        print(f"\nSearch Results for '{query}':")
        print(results)
    else:
        print("Invalid search criteria!")

# Export Data
def export_to_file(filename):
    tasks = view_tasks()
    tasks.to_csv(filename, index=False)
    print(f"Tasks exported to {filename}")

# Recurring Task Scheduler
def handle_recurring_tasks():
    tasks = view_tasks()
    conn = sqlite3.connect('productivity.db')
    cursor = conn.cursor()

    for _, task in tasks.iterrows():
        if task['recurring'] != 'None':
            deadline = pd.to_datetime(task['deadline'])
            if datetime.now().date() > deadline.date():
                recurring = task['recurring']
                if recurring == 'Daily':
                    new_deadline = (deadline + timedelta(days=1)).strftime('%Y-%m-%d')
                elif recurring == 'Weekly':
                    new_deadline = (deadline + timedelta(weeks=1)).strftime('%Y-%m-%d')
                elif recurring == 'Monthly':
                    new_deadline = (deadline + timedelta(days=30)).strftime('%Y-%m-%d')
                else:
                    continue
                cursor.execute('''INSERT INTO tasks (employee_name, task_name, priority, estimated_time, actual_time, status, deadline, recurring, date) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                               (task['employee_name'], task['task_name'], task['priority'], task['estimated_time'],
                                task['actual_time'], 'Pending', new_deadline, recurring,
                                datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

# Main Menu
def main():
    setup_database()
    handle_recurring_tasks()

    while True:
        print("\nEmployee Productivity Tracker")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Generate Detailed Insights")
        print("5. Visualize Team Performance")
        print("6. Export Tasks to CSV")
        print("7. Prioritize Tasks")
        print("8. Notify Deadlines")
        print("9. Search Tasks")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            employee_name = input("Enter employee name: ")
            task_name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ")
            estimated_time = int(input("Enter estimated time (hours): "))
            actual_time = int(input("Enter actual time (hours): "))
            status = input("Enter status (Pending/In Progress/Completed): ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            recurring = input("Is this a recurring task? (None/Daily/Weekly/Monthly): ")
            add_task(employee_name, task_name, priority, estimated_time, actual_time, status, deadline, recurring)
            print("Task added successfully!")
        elif choice == '2':
            print(view_tasks())
        elif choice == '3':
            task_id = int(input("Enter task ID: "))
            status = input("Enter new status (Pending/In Progress/Completed): ")
            update_task_status(task_id, status)
            print("Task status updated successfully!")
        elif choice == '4':
            generate_detailed_insights()
        elif choice == '5':
            visualize_team_performance()
        elif choice == '6':
            filename = input("Enter filename (e.g., tasks.csv): ")
            export_to_file(filename)
        elif choice == '7':
            prioritize_tasks()
        elif choice == '8':
            notify_deadlines()
        elif choice == '9':
            search_tasks()
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

