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

# Browser setup for AWS Elastic Beanstalk server

In order to run the website hosted on AWS Elastic Beanstalk server, you need to enable the "Insecure origins treated as secure" flag on your browser. Follow the steps below to enable the flag on your browser:

1. In the address bar, type `[browser name]://flags` and press Enter. Replace `[browser name]` with the name of your browser (e.g., `chrome`, `firefox`, `edge`).
2. Search for "Insecure origins treated as secure" in the search bar.
3. Paste our website link http://vnonymous-env.eba-ai3bsdyf.us-west-2.elasticbeanstalk.com/ into the box area.
4. Click the dropdown menu and select "Enabled".
5. Click the "Relaunch" button at the bottom of the page to restart your browser.

# Project Setup and Testing Guide

This guide will walk you through the process of setting up your Python environment, installing necessary packages, configuring the database, and running the Django server. It also includes instructions for running Selenium and Pytest tests.
**Note:** The following guide uses `python` as the command to run Python. Depending on your system, you may need to use `python3` or `py` instead.

## Setup Guide

### Step 1: Install Python

If Python is not installed on your system, download it from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions. During the installation process, ensure to check the box that says "Add Python to PATH".

### Step 2: Set Up Virtual Environment

First, navigate to the `app` folder in your command line. Then, run the following command to install the required packages
Then, activate the virtual environment:

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

```console
pip install -r requirements.txt
```

### Step 4: FFmpeg Installation

FFmpeg is required to convert webm files to mp4 format. Follow the instructions below to install FFmpeg on your system:

- Windows 10/11:

  1. Go to the [official FFmpeg download website](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-github).
  2. Download "ffmpeg-XXXX-XX-XX-git-5d71f97e0e-full_build.zip" package (Date version might differ).
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
- MacOS:

  1. Make sure to have Home Brew installed:
     Go to [Home Brew Website](https://brew.sh/) to follow the instructions there if it is not installed.
  2. Run the following command to install ffmpeg:

     ```console
     brew install ffmpeg
     ```
  3. Check if ffmpeg installed properly by running this command:

     ```console
     ffmpeg
     ```

#### FFmpeg Code Configuration

- Using Local hosting:

  - Use this FFMpeg code to convert webm to mp4 in create_video function and record_filled_video on views.py file.
    ![FFmpeg successful](docs/weekly%20logs/images/Adrian_images/ReadMe_images/ffmpeg_local.png)
- Using AWS Elastic Beanstalk hosting:

  - Use this FFMpeg code for AWS Elastic Beanstalk server to convert webm to mp4 in create_video function and record_filled_video on views.py file.
    ![FFmpeg successful](docs/weekly%20logs/images/Adrian_images/ReadMe_images/ffmpeg_server.png)

### Step 5: Database Setup

- Using Local SQL Database:

  - Use this code to connect to local SQL database on settings.py file.
    ![Local SQL database connection code](docs/weekly%20logs/images/Adrian_images/ReadMe_images/local_sql.png)
- Using AWS RDS database:

  - Use this code to connect to AWS RDS database on settings.py file.
    ![AWS RDS SQL database connection code](docs/weekly%20logs/images/Adrian_images/ReadMe_images/rds.png)

Configure the database by applying migrations:

```console
python manage.py makemigrations
python manage.py migrate
```

### Step 6: AWS Access/Session Keys

- Using Local host AWS access:

  - To access AWS RDS and S3 buckets locally, you need to add your AWS account access and session keys.
  - Add your AWS Account Access and Session keys to use local host and access AWS RDS and S3 buckets on settings.py file.

    ![Local host code](docs/weekly%20logs/images/Adrian_images/ReadMe_images/aws_local.png)
- Using AWS Elastic Beanstalk hosting access:

  - Use this code for AWS Elastic Beanstalk server to connect to RDS database and S3 buckets on settings.py file.

    ![AWS Elastic Beanstalk server connection code](docs/weekly%20logs/images/Adrian_images/ReadMe_images/aws_server.png)

### Step 7: Start the Django Server

- Using Local host:

  - Use this code to host website locally on settings.py file.

    ![Local host code](docs/weekly%20logs/images/Adrian_images/ReadMe_images/local_host.png)
- Using AWS Elastic Beanstalk hosting:

  - Add your server url link for AWS Elastic Beanstalk server hosting on settings.py file.
    ![AWS Elastic Beanstalk server connection code](docs/weekly%20logs/images/Adrian_images/ReadMe_images/server_host.png)

Launch the Django development server:

```console
python manage.py runserver
```

### Step 8: Access the Website

Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the locally hosted website.

## Testing Guide

### Selenium Testing

#### **For the following section, make sure to configure the `views.py`, `database` and `AWS access/session keys` as mentioned in the previous sections.**

1. Check [Step 4](#step-4-ffmpeg-installation) to [Step 7](#step-7-start-the-django-server) for code changes to run local.
    - [FFmpeg local host code](#ffmpeg-code-configuration)
    - [Database local host code](#step-5-database-setup)
    - [AWS access local host code](#step-6-aws-accesssession-keys)
    - [Django Server local host code](#step-7-start-the-django-server)
2. Start the Django server.
3. In a different terminal window, activate the virtual environment. Navigate to the `Selenium_Tests` folder in your command line.
4. Run all Selenium tests:

   ```console
   python master_test.py
   ```
5. Run a specific test file (replace `[your_file_name_here]` with the specific test file name):

   ```console
   python [your_file_name_here].py
   ```

**Note:** Selenium Testing can be finicky depending on how fast your computer can run. If something fails, most of the time, if you run it again, the test will pass. Otherwise, add wait time to allow for the page to load.

6. Save Selenium test report into a txt file (replace `master_test.py` with any other test file name if needed):

   ```console
   python master_test.py > report.txt
   ```

### Pytest Testing

1. Check [Step 4](#step-4-ffmpeg-installation) to [Step 7](#step-7-start-the-django-server) for code changes to run local.
    - [FFmpeg local host code](#ffmpeg-code-configuration)
    - [Database local host code](#step-5-database-setup)
    - [AWS access local host code](#step-6-aws-accesssession-keys)
    - [Django Server local host code](#step-7-start-the-django-server)
2. For this section, the server is not required to be running.
3. Navigate into the `app` folder in your command line.
4. Run all Pytests:

   ```console
   python manage.py test pytests
   ```
5. Run a specific pytest (replace `[your_file_name_here]` with the specific test file name):

   ```console
   python manage.py test pytests.[your_file_name_here]
   ```

# Citations

- [Bootstrap studio](https://bootstrapstudio.io/)
- Our project structure was inspired by [this template](https://github.com/bunnythecompiler/video_app/tree/master)
- Login template was using [login template website](https://freefrontend.com/bootstrap-login-forms/)
- Register template was using [register template website](https://colorlib.com/wp/free-bootstrap-registration-forms/)
- Profile page template was using [profile template website](https://www.sliderrevolution.com/resources/bootstrap-profile/)
- AWS video face blurring was referenced by [AWS Rekognition Video](https://aws.amazon.com/blogs/machine-learning/blur-faces-in-videos-automatically-with-amazon-rekognition-video/)
