# ODOP assignment 2.01 — initialize the kawiil_financing manifest.
#
# Fill in every value marked TODO below, then add the one file this module is
# still missing:
#
#   kawiil_financing/static/description/icon.png  your app icon. Both the file
#                                                 name and the folder path have
#                                                 to match exactly.
#
# Odoo reads this file to build the Apps list. Spelling matters throughout the
# module: two underscores on each side of __manifest__ and __init__. Get one
# wrong and Odoo skips the whole directory without saying why.
#
# Do not delete any key below. The Quality Gate in
# .github/workflows/odoo-lint.yml requires name, version, author, license and
# maintainer to be present, and it runs on every pull request into main.
{
    # The app title in the Apps list. This is the text you search for when you
    # install the module.
    "name": "TODO",
    # One line saying what the module does, shown under the title.
    "summary": "TODO",
    # Where the app is filed in the Apps list. Odoo splits this on "/", so
    # "Parent/Child" files it under a Child group inside Parent.
    "category": "TODO",
    # Your full name.
    "maintainer": "TODO",
    # Where to find this module's source. Leave as is.
    "website": "https://github.com/odoo-trainings/development-masterclass",
    # This module's own version number. Leave as is.
    "version": "1.0.0",
    # Checked byte-for-byte by the linter. Leave as is.
    "author": "ODOP Trainee",
    # The modules Odoo must install before this one. "base" is the framework
    # itself, so every module depends on it.
    # TODO (assignment 2.03): this module starts linking to products, so swap
    # this for the "product" module. Drop "base" when you do — product already
    # depends on it, and Odoo installs the whole chain for you.
    "depends": ["base"],
    # Odoo Proprietary License, the default for custom customer work.
    "license": "OPL-1",
    # XML and CSV files Odoo loads on install, in the order you list them.
    #
    # TODO: register each file in the assignment that creates it, and only
    # then. Listing a file before its models exist crashes the install, so add
    # the lines marked 2.06 when you get to 2.06, not now.
    #
    # Order is not cosmetic — Odoo resolves external ids as it reads, so a file
    # can only refer to something a file above it already created. Security,
    # then views, then the menu that points at them. That means the list grows
    # by insertion, not by appending: at 2.06 the security files go in above
    # the views you added at 2.05.
    #
    # The finished list, with the assignment that adds each line:
    #     "security/kawiil_financing_groups.xml",             2.06
    #     "security/ir.model.access.csv",                     2.06
    #     "security/kawiil_financing_security.xml",           2.06
    #     "views/loan_application_views.xml",                 2.05
    #     "views/loan_application_tag_views.xml",             2.08
    #     "views/loan_application_document_type_views.xml",   2.08
    #     "views/kawiil_financing_menu.xml",                  2.05
    "data": [],
    # Sample records, loaded only when a database is created with demo data.
    #
    # TODO: same rule as above — one line per assignment, inserted in order.
    # Configuration data before transactional data, so the loans can refer to
    # tags that already exist:
    #     "demo/config_demo.xml",   2.08
    #     "demo/loan_demo.xml",     2.04
    "demo": [],
    # True gives the module its own top-level menu and makes it show up as an
    # app. False would make it a technical module that only extends others.
    "application": True,
}
