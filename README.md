# Employee Productivity and Task Management System
## Features

- **Task Management**: Add, update, and manage tasks with parameters like priority, deadlines, and recurrence.
- **Deadline Notifications**: Alerts for upcoming and missed deadlines.
- **Recurring Tasks**: Automatically regenerates daily, weekly, or monthly tasks.
- **Insights and Reporting**: Provides detailed analysis of employee efficiency and task completion.
- **Data Export**: Export tasks and reports to CSV for offline analysis.
- **Visualization**: Visual dashboards for task status and team performance.
- **Search Functionality**: Quickly locate tasks by employee name, task name, or status.

## Technologies Used

- **Programming Language**: Python
- **Database**: SQLite
- **Visualization Libraries**: Matplotlib, Seaborn
- **Data Handling**: Pandas

## How to Install and Run
1. Prerequisites

- Python 3.8 or higher installed on your system.
- Required libraries: Install them using pip:
  ```bash
  pip install pandas matplotlib seaborn
  ```

2. Clone the Repository

Clone the GitHub repository to your local machine:
```bash
git clone https://github.com/yourusername/employee-productivity-system.git
cd employee-productivity-system
```

3. Run the Project

Execute the Python script to start the program:
```bash
python productivity_system.py
```

## Usage Instructions
1. Task Management

- **Add Task**:
  - Enter task details like employee name, task name, priority, estimated time, actual time, status, deadline, and recurrence type.
- **View Tasks**:
  - Displays all tasks in the database with relevant details.
- **Update Task Status**:
  - Change task status to "Pending", "In Progress", or "Completed".

2. Generate Insights

- Select the "Generate Insights" option to:
  - Analyze employee efficiency.
  - View a breakdown of task statuses (Completed, Pending, In Progress).
  - Identify missed deadlines.

3. Visualizations

- Visualize team performance through bar charts and graphs, showing:
  - Task status distribution by employee.
  - Efficiency trends over time.

4. Export Data

- Export all tasks and insights to a CSV file:
  ```bash
  Enter filename: tasks.csv
  ```


## Team Members and Contribution

| Member Name         | Contribution Description                                                                                   |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| **Mrigankar Sonowal** | Database design and task management modules. Recurring task logic implementation.                       |
| **Nilesh Vasava**   | Deadline notifications, insights generation, and data validation.                                         |
| **Prakhya Singh**   | Visualization components using Matplotlib and Seaborn. Data export functionality.                        |
| **Prateek Guha**    | CLI interaction, advanced search functionality, and documentation.                                       |

## Future Enhancements

- Integration with external tools like Slack or Trello for task notifications.
- A web-based interface for better accessibility.
- Machine learning-based predictive analytics for task completion times.

License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Submit a pull request.

## Contact

For questions or suggestions, contact:
- **Mrigankar Sonowal**: [mrigankars.mbaba04@iimamritsar.ac.in](mailto:mrigankars.mbaba04@iimamritsar.ac.in)
- **Nilesh Vasava**: [nileshv.mbaba04@iimamritsar.ac.in](mailto:nileshv.mbaba04@iimamritsar.ac.in)
- **Prakhya Singh**: [prakhyas.mbaba04@iimamritsar.ac.in](mailto:prakhyas.mbaba04@iimamritsar.ac.in)
- **Prateek Guha**: [prateekg.mbaba04@iimamritsar.ac.in](mailto:prateekg.mbaba04@iimamritsar.ac.in)

