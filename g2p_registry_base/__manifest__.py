# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Registry: Base",
    "category": "G2P",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": ["base", "mail", "contacts", "web"],
    "data": [
        "security/g2p_security.xml",
        "security/ir.model.access.csv",
        "wizard/disable_registrant_view.xml",
        "views/main_view.xml",
        "views/reg_relationship_view.xml",
        "views/relationships_view.xml",
        "views/reg_id_view.xml",
        "views/id_types_view.xml",
        "views/phone_number_view.xml",
        "views/tags_view.xml",
    ],
    "assets": {
        "web.assets_qweb": [
            "g2p_registry_base/static/src/xml/custom_web.xml",
        ],
    },
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
}
