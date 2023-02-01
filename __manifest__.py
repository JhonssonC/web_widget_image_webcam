# Copyright 2016 Siddharth Bhalgami <siddharth.bhalgami@gmail.com>
# Copyright (C) 2019-Today: Druidoo (<https://www.druidoo.io>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Web Widget - Image WebCam",
    "summary": "Allows to take image with WebCam",
    "version": "15.0.1.0.1",
    "category": "web",
    "website": "https://github.com/OCA/web",
    "author": "Tech Receptives, "
    "Kaushal Prajapati, "
    "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    'sequence': -98,
    "data": [
        #"views/assets.xml"
    ],
'assets': {
        # -----------------------------
        # MAIN BUNDLES
        # -----------------------------
        'web.assets_qweb': [
            # EXAMPLE: Add everyithing in the folder
            #'web/static/src/**/*.xml',
            # EXAMPLE: Remove every .xml file
            #('remove', 'web/static/src/legacy/**/*.xml'),
            'web_widget_image_webcam/static/src/xml/web_widget_image_webcam.xml'
        ],
        'web.assets_common_minimal': [
            'web_widget_image_webcam/static/src/lib/webcam.js',
            # EXAMPLE lib
            #'web/static/lib/es6-promise/es6-promise-polyfill.js',

            #'balancesEnergeticos/static/lib/leaflet/leaflet.js',

        ],
        'web.assets_common': [
            # EXAMPLE Can include sub assets bundle
            #('include', 'web._assets_helpers'),
            #'web/static/lib/bootstrap/scss/_variables.scss',
            #'balancesEnergeticos/static/src/css/leaflet.css',
        ],
        'web.assets_common_lazy': [
            # ...
        ],
        'web.assets_backend': [
            # EXAMPLE Any files
            #'balancesEnergeticos/static/src/js/utmLatLng.js',
            #'balancesEnergeticos/static/src/js/map.js',
            #'balancesEnergeticos/static/src/js/*',

            'web_widget_image_webcam/static/src/js/webcam_widget.js',
        ],
        "web.assets_backend_legacy_lazy": [
            # ...
        ],
        'web.assets_frontend_minimal': [
            # ...
        ],
        'web.assets_frontend': [
            # ...
            'web_widget_image_webcam/static/src/css/web_widget_image_webcam.css',
        ],
        'web.assets_frontend_lazy': [
            # ...
        ],
        'web.assets_backend_prod_only': [
            # ...
        ],
        'web.report_assets_common': [
            # ...
        ],
        'web.report_assets_pdf': [
            # ...
        ],

        # --------------------------------
        # SUB BUNDLES
        # --------------------------------
        # These bundles can be used by main bundles but are not supposed to be
        # called directly from XML templates.
        #
        # Their naming conventions are similar to those of the main bundles,
        # with the addition of a prefixed underscore to reflect the "private"
        # aspect.
        #
        # Exemples:
        #   > web._assets_helpers = define assets needed in most main bundles

        'web._assets_primary_variables': [
            # ...
        ],
        'web._assets_secondary_variables': [
            # ...
        ],
        'web._assets_helpers': [
            # ...
        ],
        'web._assets_bootstrap': [
            # ...
        ],
        'web._assets_backend_helpers': [
            # ...
        ],
        'web._assets_frontend_helpers': [
            # ...
        ],
        'web._assets_common_styles': [
            # ...
        ],
        'web._assets_common_scripts': [
            # ...
        ],

        # Used during the transition of the web architecture
        'web.frontend_legacy': [
            # ...
        ],

        # -----------------------------------
        # TESTS BUNDLES
        # -----------------------------------

        'web.assets_tests': [
            # ...
        ],
        'web.tests_assets': [
            # ...
        ],
        'web.qunit_suite_tests': [
            # ...
        ],
        'web.qunit_mobile_suite_tests': [
            # ...
        ],
        # Used during the transition of the web architecture
        'web.frontend_legacy_tests': [
            # ...
        ],
    },
    "depends": ["web"],
    "qweb": ["static/src/xml/web_widget_image_webcam.xml"],
    'application': True,
    "auto_install": False,
    'installable': True,
}
