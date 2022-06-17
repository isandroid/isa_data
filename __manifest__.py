# -*- coding: utf-8 -*-
{
    'name': "Data Isa",

    'summary': """Aplikasi Menejemen Data Isa""",

    'description': """Aplikasi Menejemen Data Isa""",

    'author': "Isa Mujahid Islam",
    'website': "http://www.isa.web.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/isa_data.jemaat.csv',
        'views/views.xml',
        'views/jemaat.xml',
        'views/jemaat_kelompok.xml',
        'views/kegiatan_jenis.xml',
        'views/alquran_surah.xml',
        'views/kegiatan.xml',
        'views/keuangan_akun.xml',
        'views/keuangan_dkm.xml',
        'views/keuangan_bensin.xml',
        'views/madrasah_pelajaran.xml',
        'views/madrasah_murid.xml',
        'views/madrasah_absensi.xml',
        'views/madrasah_kurikulum.xml',
        'views/madrasah_kbm.xml',
        'views/madrasah_nilai.xml',
        'views/homeopati_remedi.xml',
        'views/homeopati_resep.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    'license': 'OPL-1',
}
