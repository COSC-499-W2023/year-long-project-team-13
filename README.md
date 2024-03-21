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

1. **Activate the virtual environment:** If you created a virtual environment, activate it by running the following command in your terminal:

   If you have never created a virtual environment, you need to install Python first.

   Then, install the virtualenv package first:

   ```console
   pip install virtualenv
   ```

   Once you install the virtualenv package, you can create a virtual environment by running the following command:

   MacOS/Linux:

   ```console
   source myenv/bin/activate
   ```

   Cmd.exe:

   ```console
   myenv\Scripts\activate.bat
   ```

   Powershell:

   ```console
   myenv\Scripts\Activate.ps1
   ```

   Git bash:

   ```console
   . myenv/Scripts/activate
   ```
2. **Install Required Packages:** With the virtual environment activated (if you created one), proceed to install the necessary packages by running the following command in your terminal:

   Macos:

   ```console
   python -m pip install -r requirements.txt
   ```

   Windows/git bash:

   ```console
   py -m pip install -r requirements.txt
   ```

   Depending on the system an environment already created, it is possible that the command above will not work. If that is the case, change the py in front to **python** and try again:

   ```console
   python -m pip install -r requirements.txt
   ```
3. **Database Setup:** Configure the database by applying migrations with these commands:

   ```console
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Start the Django Server:** Launch the Django development server with this command:

   ```console
   python manage.py runserver
   ```
5. **Access the Website:** Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the locally hosted website.

By following these steps, you'll have a Python virtual environment set up and activated, ensuring a clean and isolated environment for your Django project.

## Testing Guide
### Selenium Testing
1. Start the django server
2. Navigate to the folder Selenium_Tests in your command line
3. To run all selenium tests, use the command:
   ```console
   python master_test.py
   ```
   or
   ```console
   py master_test.py
   ```

4. To run a specific test file, use the command:
   ```console
   # Replace with the specific test file name
   python [your_file_name_here].py
   ```
   or
   ```console
   # Replace with the specific test file name
   py [your_file_name_here].py
   ```
   Note: Selenium Testing can be finicky depending on how fast your computer can run. If something fails, most of the time if you run it again. The test will pass. Otherwise, add wait time to allow for the page to load.
### Pytest Testing

