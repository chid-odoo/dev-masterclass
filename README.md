# 🚀 Odoo Developer Onboarding Program (ODOP)

Welcome to ODOP. This is the template for your assignment repository. It contains the base structure you need to start building your Odoo module, plus the automated tools that check your work.

You will not work in the template itself. Step 1 walks you through making your own copy.

---

## 📥 Step 1: Create Your Own Repository

Do not clone this template directly. Make your own copy first, so your work stays yours.

1. Open the template URL your instructor gave you.
2. Click **Use this template** > **Create a new repository**.
3. Name it however you like and set it to **Private**.
4. Clone your new repository to your machine and work there from now on.

Everything below refers to *your* repository, not the template.

---

## 🛠️ Step 2: Set Up Your Odoo.sh Environment

You will be doing all your testing and deployment on Odoo.sh.

1. Go to https://www.odoo.sh and log in with your GitHub account.
2. Click **Deploy your platform** and select the repository you created in Step 1.
3. When prompted for billing/subscription, enter the **Trial Code** provided by your instructor.
4. Odoo.sh will build your server. You are the administrator of this project!

---

## 🛑 Step 3: The Pull Request Workflow (MANDATORY) 🛑

To successfully complete your assignments and receive your certificate, **you must never push code directly to the main branch.** You must follow this Pull Request (PR) workflow for every task:

1. **Create a new branch** for your task:
    git checkout -b feature/task-1

2. **Write your Odoo code** inside the `kawiil_financing/` folder.

3. **Commit and push** your branch to GitHub:
    git add .
    git commit -m "Complete task 1 models and views"
    git push origin feature/task-1

4. **Open a Pull Request:** Go to GitHub, click the **Pull Requests** tab, and open a PR from your branch into the `main` branch.

---

## 🤖 Step 4: Automated Grading

When you open a Pull Request, an automated bot will immediately check your code. We use Pylint to ensure you are following standard Odoo framework rules (e.g., missing security files, SQL injection risks).

* **If the check fails (❌):** Check the logs in the "Details" section, fix the error locally, and push again. The bot will automatically re-run.
* **If the check passes (✅):** Great job! Your code meets the required baseline.

*Note: Your instructor will only review and merge your final PR for certification AFTER you have successfully passed the automated checks.*

---

## 🌟 Step 5: The "Level Up" (Week 2 Code Quality)

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
* `COMMANDS.md` - **Every command you will need**, for git, Odoo, the shell and the code checkers. Keep it open.
* `kawiil_financing/` - **This is where you will work.** The module folder is already created, with its `__manifest__.py`, `__init__.py` and `models/` package waiting for you to fill in. Your `views/` and `security/` folders go in here too, not in the repository root.

---

## 🧩 How to Read the Starter Code

The module ships with every assignment's scaffolding already in place, so the files you open will contain work you have not reached yet. Two markers tell you what to do with it:

* **`TODO`** - code you write yourself. The comment tells you the field, its type and anything non-obvious about it.
* **A commented-out worked example** - code that is written for you, but belongs to a later assignment. It is commented out so the module still installs at every step: uncommenting a link to a model that does not exist yet will crash the install.

Each worked example says which assignment it belongs to, in the form *"Uncomment it when you reach 2.03"*. Leave it alone until then, and when you get there remove the comment markers and nothing else.

The same rule governs `__manifest__.py`. The `data` and `demo` lists show every file you will eventually register, each tagged with the assignment that adds it. Add each line when you reach that assignment, not before, and insert it in the position shown rather than appending - Odoo resolves external ids in the order it reads the files.

Good luck, and happy coding!
