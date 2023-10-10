[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12113061&assignment_repo_type=AssignmentRepo)

# Project-Starter

Please use the provided folder structure for your docs (project plan, design documentation, communications log, weekly logs, and final documentation), source code, testing, etc.    You are free to organize any additional internal folder structure as required by the project.  Please use a branching workflow and once an item is ready, do remember to issue a PR, code review, and merge it into the develop branch and then the master branch.

```
.
├── docs                    # Documentation files (alternatively `doc`)
│   ├── project plan        # Project plan document
│   ├── design              # Getting started guide
│   ├── final               # Getting started guide
│   ├── logs                # Team Logs
│   └── ...
├── app                     # Source files
├── tests                   # Automated tests
├── utils                   # Tools and utilities
└── README.md
```

Also, update your README.md file with the team and client/project information.  You can find details on writing GitHub Markdown [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) as well as a [handy cheatsheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf).

## Install Guide


1. **Create a Python Virtual Environment (Optional, but Recommended):** Before installing the required packages, it's a good practice to create a Python virtual environment. This isolates your project dependencies from the system-wide Python environment. Use the following commands to create a virtual environment:

   * **Windows** (Command Prompt):

     ```console
     python -m venv myenv
     ```

     To activate the virtual environment:

     ```console
     myenv\Scripts\activate
     ```

   * **Windows** (PowerShell):

     ```console
     python -m venv myenv
     ```

     To activate the virtual environment:

     ```console
     .\myenv\Scripts\Activate.ps1
     ```

   * **Bash (Linux/macOS)** :

     ```console
     python3 -m venv myenv
     ```

     To activate the virtual environment:

     ```console
     source myenv/bin/activate
     ```

2. **Install Required Packages:** With the virtual environment activated (if you created one), proceed to install the necessary packages by running the following command in your terminal:

   ```console
   pip install -r requirements.txt
   ```

3. **Database Setup:** Configure the database by applying migrations with these commands:

   ```console
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. **Start the Django Server:** Launch the Django development server with this command:

   ```console
   python3 manage.py runserver
   ```

5. **Access the Website:** Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the locally hosted website.

By following these steps, you'll have a Python virtual environment set up and activated, ensuring a clean and isolated environment for your Django project.
