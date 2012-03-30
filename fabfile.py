from armstrong.dev.tasks import *


settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.arm_access',
        'armstrong.core.arm_content',
        'armstrong.core.arm_sections',
        'armstrong.apps.content',
        'south',
        'taggit',
    ),
    'SITE_ID': 1,
}

main_app = "content"
tested_apps = (main_app, )
