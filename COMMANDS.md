# Command Reference

Every command you need during the course, in one place. Replace anything in
`<angle brackets>` with your own value.

---

## Git workflow

You never commit to `main` directly. One branch per task, then a pull request.

Allow Odoo.sh to push code to the repository using a writable deploy key on the Settings Page.

```bash
# Configure Identity (Every time you have a new container): Ensure your commits are attributed to you.
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"


# Commit and push
git add .
git commit -m "[ADD]: [2.01] initialize kawiil_financing manifest."
odoosh-push
```

Then open the pull request on GitHub, from your branch into `main`.

Commit messages follow `[TAG]: [chapter] what you did.` The tag says what kind
of change it is: `ADD` for new features, `FIX` for bug fixes, `IMP` for
improvements to something that already works, `REF` for refactoring, `REM` for
removals. Each assignment tells you the exact message to use.

```bash
# Fix the last commit message if you got it wrong (before pushing)
git commit --amend -m "[ADD]: [2.01] initialize kawiil_financing manifest."

# Push more work to a branch you already pushed
git add .
git commit -m "[FIX]: [2.01] correct manifest category."
git push
```

---

## Running Odoo locally

Skip this section if you are working entirely on Odoo.sh.

```bash
# Install the module into a fresh database
odoo-bin -c <config-file> -d <database> -i kawiil_financing --stop-after-init

# Upgrade it after you change Python or XML
odoo-bin -c <config-file> -d <database> -u kawiil_financing --stop-after-init

# Start the server and leave it running
odoo-bin -c <config-file> -d <database>
```

`-i` installs, `-u` upgrades. You need `-u` after touching `__manifest__.py`,
adding a data file, or changing anything in `models/` — a restart alone is not
enough. `--stop-after-init` exits once the work is done instead of serving.

Demo data only loads into a database that was created with it enabled. If you
created yours with `--without-demo=all`, the records in `demo/` will never
appear and neither will `base.res_partner_1`.

---

## The Odoo shell

A Python prompt with your database attached. This is how you inspect your work
before there is any user interface to click on.

```bash
odoo-bin shell -c <config-file> -d <database>
```

On Odoo.sh: open the branch Editor and start a new Shell from the launcher.

**Nothing you change here is saved.** The shell rolls the transaction back when
you exit. Run `env.cr.commit()` before leaving if you want a change to stick.
Reading and searching need no commit.

The shell runs as superuser, which is why you can read your model before it has
any access rules. A normal user cannot.

---

## ORM commands

`env` is your way into every model. `env['loan.application']` is an empty
recordset you can search from.

```python
# Count and fetch
env['loan.application'].search_count([])
loans = env['loan.application'].search([])

# One field across every record in the set
loans.mapped('name')

# Follow a Many2one and read through it
loans.mapped('partner_id.name')

# Look a record up by the external id you gave it in XML
loan = env.ref('kawiil_financing.loan_application_demo_2')
loan.date_applied

# Filter in the database, with a domain
env['loan.application'].search([('state', '=', 'sent')])
env['loan.application'].search([('loan_amount', '>', 10000)])

# Filter in Python, on records you already hold
loans.filtered(lambda loan: loan.loan_amount > 10000)
loans.sorted('date_applied')

# Read fields as dictionaries
loans.read(['name', 'partner_id', 'date_applied'])

# Modify
loan.write({'state': 'approved'})
loan.state

# Create
new_loan = env['loan.application'].create({
    'name': 'LOAN/SHELL/001',
    'partner_id': env.ref('base.res_partner_4').id,
    'interest_rate': 7.5,
    'loan_amount': 9500,
})

# Delete
new_loan.unlink()

# Keep your changes
env.cr.commit()
```

A domain is a list of `(field, operator, value)` tuples. An empty domain `[]`
matches everything. `search` filters in SQL and is what you want for anything
large; `filtered` filters records already in memory.

---

## Code quality checks

These are the same three commands the Quality Gate runs on your pull request,
so run them before you push and you will not be surprised.

```bash
pip install -r requirements.txt

ruff check .            # lint
ruff format --check .   # formatting, without changing anything
pylint --rcfile=.pylintrc .
```

To fix problems instead of just reporting them:

```bash
ruff check . --fix
ruff format .
```

From week 2, once your instructor tells you to level up:

```bash
pre-commit run --all-files   # format everything now
pre-commit install           # and on every commit from here on
```
