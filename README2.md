# Project Setup and Testing Guide

This guide will walk you through the process of setting up your Python environment, installing necessary packages, configuring the database, and running the Django server. It also includes instructions for running Selenium and Pytest tests.

## Setup Guide

### Step 1: Install Python

If Python is not installed on your system, download it from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions. During the installation process, ensure to check the box that says "Add Python to PATH".

### Step 2: Set Up Virtual Environment

First, install the `virtualenv` package using pip:

```console
pip install virtualenv
```

Next, create a virtual environment:

```console
python -m venv myenv
```

Activate the virtual environment:

- MacOS/Linux:

    ```console
    source myenv/bin/activate
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

### Step 4: Database Setup

Configure the database by applying migrations:

```console
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Start the Django Server

Launch the Django development server:

```console
python manage.py runserver
```

### Step 6: Access the Website

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

