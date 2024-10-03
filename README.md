## Team Tasks Manager

Task Management for teams

#### License

mit# TeamTasksManager


#### Local Setup Instructions

Follow these steps to set up the Team Tasks Manager app locally:

1. Ensure you have Frappe and Bench installed on your system. If not, follow the [official Frappe installation guide](https://frappeframework.com/docs/user/en/installation).

2. Create a new bench:
   ```
   bench init frappe-bench
   cd frappe-bench
   ```

3. Create a new site:
   ```
   bench new-site [site name]
   ```
   Replace `[site name]` with your preferred site name.

4. Clone the Team Tasks Manager app from GitHub:
   ```
   bench get-app https://github.com/Thunder-BluePhoenix/TeamTasksManager
   ```

5. Install the app on your site:
   ```
   bench --site [site name] install-app team_tasks_manager
   ```

6. Migrate the database to create necessary tables:
   ```
   bench --site [site name] migrate
   ```

7. Build the assets:
   ```
   bench build
   ```

8. Start the Frappe development server:
   ```
   bench start
   ```

9. Access your site by navigating to `http://[site name]:8000` in your web browser. If you're using a virtual machine, make sure to set up port forwarding.

10. Log in with the administrator account and start using the Team Tasks Manager!

## Troubleshooting

If you encounter any issues during setup:

1. Ensure all dependencies are installed:
   ```
   bench setup requirements
   ```

2. Clear cache and rebuild assets:
   ```
   bench clear-cache
   bench build
   ```

3. Restart the Frappe server:
   ```
   bench restart
   ```

If problems persist, please open an issue on the GitHub repository with details about the error you're encountering.
