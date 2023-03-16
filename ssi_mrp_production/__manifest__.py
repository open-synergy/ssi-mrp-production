# Copyright 2015-2016 Agile Business Group (<http://www.agilebg.com>)
# Copyright 2015 BREMSKERL-REIBBELAGWERKE EMMERLING GmbH & Co. KG
#    Author Marco Dieckhoff
# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "MRP Production",
    "version": "14.0.1.0.0",
    "category": "Manufacturing/Manufacturing",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://simetri-sinergi.id",
    "depends": [
        "mrp",
        "stock_move_backdating",
    ],
    "data": [
        "views/mrp_production_views.xml",
    ],
    "installable": True,
}
