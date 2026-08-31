{
    "name": "Kawiil Library",
    "summary": "Track book checkouts and returns for your library",
    "category": "Services",
    "maintainer": "danny",
    "website": "https://github.com/odoo-trainings/development-masterclass",
    "version": "1.0.0",
    "author": "ODOP Trainee",
    "depends": ["base", "mail"],
    "license": "OPL-1",
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_views.xml",
        "views/library_checkout_views.xml",
        "views/kawiil_library_menu.xml",
    ],
    "demo": [
        "demo/library_demo.xml",
    ],
    "application": True,
}
