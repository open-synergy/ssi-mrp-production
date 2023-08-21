import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-mrp-production",
    description="Meta package for open-synergy-ssi-mrp-production Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_mrp_production',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
