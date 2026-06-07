# Environment Setup Guide

## Purpose

This guide helps students prepare their computer for the course. By the end, each student should have:

- Python installed
- A GitHub account
- draw.io available for flowcharts and diagrams
- Windsurf installed as the programming IDE
- A simple way to confirm that everything works

## Free Software Requirement

All required tools for this course should be free to use for students.

Students should not purchase paid plans, subscriptions, add-ons, or upgrades for this course. If any website asks for payment, a credit card, or a paid upgrade, stop and ask the instructor before continuing.

| Tool | Free Option to Use | Payment Needed? |
| --- | --- | --- |
| Python | Official Python download | No |
| GitHub | GitHub Free personal account | No |
| draw.io | Online app or desktop app | No |
| Windsurf | Free plan | No |
| Git | Official Git installer | No |

Important notes:

- Python is free and open source.
- GitHub has paid plans, but this course only needs a free personal account.
- draw.io is free to use and does not require a paid account.
- Windsurf has paid plans, but this course only requires the Free plan.
- Git is free and open source.

## 1. Install Python

Python is free and open source. Download it only from the official Python website.

### Windows

1. Go to <https://www.python.org/downloads/>.
2. Download the latest Python 3 version.
3. Run the installer.
4. Important: check **Add Python to PATH** before clicking Install.
5. Finish the installation.

### macOS

1. Go to <https://www.python.org/downloads/>.
2. Download the latest Python 3 version for macOS.
3. Run the installer.
4. Finish the installation.

### Cross-Validate Python Installation

Open Terminal, Command Prompt, or PowerShell and run:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

You should see a Python 3 version, such as:

```text
Python 3.12.x
```

Then test a simple Python command:

```bash
python -c "print('Python is working')"
```

If your computer uses `python3`, run:

```bash
python3 -c "print('Python is working')"
```

Expected output:

```text
Python is working
```

## 2. Create a GitHub Account

GitHub offers free and paid plans. For this course, students should use a free personal account.

1. Go to <https://github.com/>.
2. Click **Sign up**.
3. Use an email address you can access.
4. Create a username and password.
5. Verify your email address.
6. Sign in to GitHub.
7. Do not upgrade to GitHub Pro, Team, or Enterprise for this course.

### Cross-Validate GitHub Account

Confirm that:

- You can sign in at <https://github.com/>.
- You can see your GitHub username in the top-right menu.
- You can open this page: <https://github.com/new>.

Optional first check:

1. Create a new repository named `first-python-project`.
2. Add a short description.
3. Select **Public** or **Private**, based on class instructions.
4. Check **Add a README file**.
5. Click **Create repository**.

If the repository page opens, your GitHub account is ready.

## 3. Install draw.io

Students will use draw.io to create flowcharts and architecture diagrams. draw.io is free to use.

### Option A: Use Online Version

1. Go to <https://app.diagrams.net/>.
2. Choose a storage option, such as Device.
3. Create a new diagram.
4. Select **Flowchart** or **Blank Diagram**.

### Option B: Install Desktop Version

1. Go to <https://github.com/jgraph/drawio-desktop/releases>.
2. Download the installer for your operating system.
3. Run the installer.
4. Open draw.io after installation.

### Cross-Validate draw.io

Create a small flowchart with:

- Start shape
- Process shape
- Decision shape
- End shape

Save the file as:

```text
first-flowchart.drawio
```

If you can reopen the file and see your diagram, draw.io is ready.

## 4. Install Windsurf IDE

Students will use Windsurf as the IDE for writing and running code. Windsurf has free and paid plans. For this course, students should use the Free plan only.

1. Go to <https://windsurf.com/>.
2. Download Windsurf for your operating system.
3. Run the installer.
4. Open Windsurf.
5. Sign in if prompted.
6. Choose the Free plan if plan selection is shown.
7. Do not enter payment information or upgrade to a paid plan for this course.

### Cross-Validate Windsurf Installation

1. Open Windsurf.
2. Create or open a folder named:

```text
first-python-project
```

3. Create a new file named:

```text
hello.py
```

4. Add this code:

```python
print("Hello, world!")
```

5. Run the file from Windsurf's terminal or run option.

Expected output:

```text
Hello, world!
```

If you see this output, Windsurf is ready for Python programming.

## 5. Optional: Install Git

Git helps students connect their local code to GitHub. Some IDEs include Git support, but installing Git directly is useful. Git is free and open source.

### Windows

1. Go to <https://git-scm.com/downloads>.
2. Download Git for Windows.
3. Run the installer using the default options.

### macOS

Open Terminal and run:

```bash
git --version
```

If Git is not installed, macOS usually prompts you to install command line tools. Follow the prompt.

You can also download Git from:

<https://git-scm.com/downloads>

### Cross-Validate Git Installation

Run:

```bash
git --version
```

Expected output should look like:

```text
git version 2.x.x
```

Then configure your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Check the configuration:

```bash
git config --global --list
```

You should see your name and email listed.

## 6. Final Setup Checklist

Before the first programming lab, confirm:

- None of the required tools asked you to pay.
- You did not enter credit card or payment information.
- Python version command works.
- A simple Python print command works.
- You can sign in to GitHub.
- You can create or open a GitHub repository.
- draw.io can create and save a flowchart.
- Windsurf opens successfully.
- Windsurf can run `hello.py`.
- Optional but recommended: Git version command works.

## 7. Troubleshooting

### Python command not found

Try `python3 --version` instead of `python --version`.

On Windows, reinstall Python and make sure **Add Python to PATH** is checked.

### Windsurf cannot run Python

Check that Python is installed first. Then open Windsurf again and try running the file from the terminal.

### GitHub login issue

Confirm that your email was verified. If needed, reset your password from GitHub's login page.

### draw.io file will not save

Try saving to your local device instead of cloud storage.

## 8. First Practice Task

After setup, create a file named `student_intro.py` and write a program that prints:

- Your name
- Your grade
- One app or game you like
- One thing you want to build in this course

Example:

```python
print("Name: Alex")
print("Grade: 10")
print("Favorite app: YouTube")
print("I want to build: A quiz game")
```
