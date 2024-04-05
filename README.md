[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12113061&assignment_repo_type=AssignmentRepo)

# Project-Starter

Please use the provided folder structure for your docs (project plan, design documentation, communications log, weekly logs, and final documentation), source code, testing, etc. You are free to organize any additional internal folder structure as required by the project. Please use a branching workflow and once an item is ready, do remember to issue a PR, code review, and merge it into the develop branch and then the master branch.

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

Also, update your README.md file with the team and client/project information. You can find details on writing GitHub Markdown [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) as well as a [handy cheatsheet](https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf).

# Project Setup and Testing Guide

This guide will walk you through the process of setting up your Python environment, installing necessary packages, configuring the database, and running the Django server. It also includes instructions for running Selenium and Pytest tests.
**Note:** The following guide uses `python` as the command to run Python. Depending on your system, you may need to use `python3` or `py` instead.

## Setup Guide

### Step 1: Install Python

If Python is not installed on your system, download it from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions. During the installation process, ensure to check the box that says "Add Python to PATH".

### Step 2: Set Up Virtual Environment

Activate the virtual environment:

- MacOS/Linux:

  ```console
  source myenv/Scripts/activate
  ```
- Cmd.exe:

  ```console
  myenv\Scripts\activate.bat
  ```
- Powershell:

  ```console
  myenv\Scripts\Activate.ps1
  ```
- Git bash:

  ```console
  . myenv/Scripts/activate
  ```

### Step 3: Install Required Packages

With the virtual environment activated, install the necessary packages.
First, navigate to the `app` folder in your command line. Then, run the following command to install the required packages

```console
pip install -r requirements.txt
```

### Step 4: FFmpeg Installation

If FFmpeg is not installed on your system, follow the instructions:
   - Windows 10/11

   1. Go to the [official FFmpeg download website](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-github).
   2. Download "ffmpeg-XXXX-XX-XX-git-5d71f97e0e-full_build.zip" package (Date version might different).
   3. Extract the ffmpeg zip file into your C drive ("C:\").
   4. Rename your extracted ffmpeg folder to "ffmpeg".
   5. Navigate to the bin folder and copy the bin navigation path ("C:\ffmpeg\bin").
   6. Type “Edit the system environment variables” on the search tab and open it.
   7. Click the "Environment Variables" button.
   8. Click and edit the "Path" inside the "System variables" table.
   9. Add a new path with your copied bin navigation path ("C:\ffmpeg\bin").
   10. Click "OK" to save.
   11. Type this command in Command Prompt to check if FFmpeg is working:
   ```console
   ffmpeg
   ```
   If successfully installed, FFmpeg displays configuration options.
   ![FFmpeg successful](docs/weekly%20logs/images/Adrian_images/ReadMe_images/ffmpeg.png)

   - MacOS

   1. Go to the [official FFmpeg download website](https://www.ffmpeg.org/download.html).
   2. In the **Get packages & executable files** section, hover over the Apple logo and select the **Static builds for macOS 64-bit** link.
   ![ffmpeg download](docs/weekly%20logs/images/Adrian_images/ReadMe_images/ffmpeg_mac_link.png)
   3. In the FFmpeg section, download the latest FFmpeg zip file.
   ![ffmpeg download](docs/weekly%20logs/images/Adrian_images/ReadMe_images/ffmpeg_mac_zip.png)
   4. Extract the ffmpeg zip file into a directory path of your choice.
   5. In the terminal, navigate to the directory path of your FFmpeg file location. If your FFmpeg is located at "/Users/test/local" type:
   ```console
   export PATH=$PATH:/Users/test/Local
   ```
   6. Type this command in the terminal to check if FFmpeg is working:
   ```console
   ffmpeg
   ```

### Step 5: Database Setup

Configure the database by applying migrations:

```console
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Start the Django Server

Launch the Django development server:

```console
python manage.py runserver
```

### Step 7: Access the Website

Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the locally hosted website.

## Testing Guide

### Selenium Testing

1. Start the Django server.
2. Navigate to the `Selenium_Tests` folder in your command line.
3. Run all Selenium tests:

   ```console
   python master_test.py
   ```
4. Run a specific test file (replace `[your_file_name_here]` with the specific test file name):

   ```console
   python [your_file_name_here].py
   ```

**Note:** Selenium Testing can be finicky depending on how fast your computer can run. If something fails, most of the time, if you run it again, the test will pass. Otherwise, add wait time to allow for the page to load.

5. Save Selenium test report into a txt file (replace `master_test.py` with any other test file name if needed):

   ```console
   python master_test.py > report.txt
   ```

### Pytest Testing

1. Navigate into the `app` folder in your command line.
2. Run all Pytests:

   ```console
   python manage.py test pytests
   ```
3. Run a specific pytest (replace `[your_file_name_here]` with the specific test file name):

   ```console
   python manage.py test pytests.[your_file_name_here]
   ```
