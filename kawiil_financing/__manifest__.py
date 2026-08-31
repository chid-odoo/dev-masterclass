{
    "name": "Kawiil Financing",
    "summary": "Track loan applications for Kawiil Motors customers",
    "category": "Kawiil/Financing",
    "maintainer": "Odoo Developer",
    "website": "https://github.com/odoo-trainings/development-masterclass",
    "version": "1.0.0",
    "author": "ODOP Trainee",
    # TODO (3.05): add "contacts" to this list. Note what it does and does not buy
    # you: the partner form you inherit is base.view_partner_form, which lives in
    # base and is always installed, so the view would load either way. What contacts
    # adds is the Contacts app itself, and therefore somewhere to click to reach a
    # customer and see your smart button. Odoo installs everything named here before
    # your module, and refuses to install your module if one of them is missing.
    "depends": ["product"],
    "license": "OPL-1",
    "data": [
        "security/kawiil_financing_groups.xml",
        "security/ir.model.access.csv",
        "security/kawiil_financing_security.xml",
        "views/loan_application_views.xml",
        "views/loan_application_tag_views.xml",
        "views/loan_application_document_type_views.xml",
        # TODO (3.05): register "views/res_partner_views.xml" here. A data file that
        # is not listed is simply never read: no error, no view, and nothing to tell
        # you why your smart button did not appear.
        "views/kawiil_financing_menu.xml",
    ],
    "demo": [
        "demo/config_demo.xml",
        "demo/loan_demo.xml",
    ],
    "application": True,
}
