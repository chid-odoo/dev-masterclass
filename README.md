# 🚀 Odoo Developer Onboarding Program (ODOP)

Welcome to your official ODOP assignment repository! GitHub Classroom has generated this private workspace specifically for you. This repository contains the base structure you need to start building your Odoo module, as well as the automated tools that will evaluate your progress.

---

## 🛠️ Step 1: Set Up Your Odoo.sh Environment

You will be doing all your testing and deployment on Odoo.sh.

1. Go to https://www.odoo.sh and log in with your GitHub account.
2. Click **Deploy your platform** and select this exact GitHub repository.
3. When prompted for billing/subscription, enter the **Trial Code** provided by your instructor.
4. Odoo.sh will build your server. You are the administrator of this project!

---

## 🛑 Step 2: The Pull Request Workflow (MANDATORY) 🛑

To successfully complete your assignments and receive your certificate, **you must never push code directly to the main branch.** You must follow this Pull Request (PR) workflow for every task:

1. **Create a new branch** for your task:
    git checkout -b feature/task-1

2. **Write your Odoo code** directly in the root directory of this repository.

3. **Commit and push** your branch to GitHub:
    git add .
    git commit -m "Complete task 1 models and views"
    git push origin feature/task-1

4. **Open a Pull Request:** Go to GitHub, click the **Pull Requests** tab, and open a PR from your branch into the `main` branch.

---

## 🤖 Step 3: Automated Grading

When you open a Pull Request, an automated bot will immediately check your code. We use Pylint to ensure you are following standard Odoo framework rules (e.g., missing security files, SQL injection risks).

* **If the check fails (❌):** Check the logs in the "Details" section, fix the error locally, and push again. The bot will automatically re-run.
* **If the check passes (✅):** Great job! Your code meets the required baseline.

*Note: Your instructor will only review and merge your final PR for certification AFTER you have successfully passed the automated checks.*

---

## 🌟 Step 4: The "Level Up" (Week 2 Code Quality)

Later in the course, your instructor will ask you to activate our modern Odoo code formatting tools (Ruff & Pre-commit). Do not run these until instructed.

When you are told to "Level Up" your environment, open your terminal and run:

1. **Format all your existing code instantly:**
    pre-commit run --all-files

2. **Activate the automatic checker for future commits:**
    pre-commit install

From this moment on, your code will be automatically formatted and cleaned every time you type `git commit`.

---

## 📂 Repository Structure

Your repository is pre-configured with the following structure:

* `.github/workflows/` - Contains the automated grading scripts (Do not edit).
* `.pylintrc`, `ruff.toml`, `.pre-commit-config.yaml` - The rules engines for the code checkers (Do not edit).
* `requirements.txt` - Automatically installs required tools in the background.
* **Root Directory** - **This is where you will work.** Create your Odoo module (e.g., your `__manifest__.py`, `models/`, `views/`) directly in the base folder of this repository.

Good luck, and happy coding!
