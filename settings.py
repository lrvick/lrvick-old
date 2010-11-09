import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Lance Vick', 'lance@lrvick.net'),
)

MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE':'mysql',
    'NAME':'lrvick',
    'USER':'lrvick',
  }
}
APPEND_SLASH = False

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')

MEDIA_URL = '/media/'

STATIC_DOC_ROOT = os.path.join(PROJECT_PATH,'static')

ADMIN_MEDIA_PREFIX = '/media/admin/'

TWITTER_USER = 'lrvick'

TWITTER_TIMEOUT = '3600'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
	  'django.template.loaders.app_directories.Loader', 
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
		'pagination.middleware.PaginationMiddleware',
		'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
		os.path.join(PROJECT_PATH,'templates'),
		os.path.join(PROJECT_PATH,'blog/templates'),
		os.path.join(PROJECT_PATH,'projects/templates'),
		os.path.join(PROJECT_PATH,'code_samples/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
		'django.contrib.comments',
		'django.contrib.admin',
		'django.contrib.markup',
		'django.contrib.sitemaps',
		'django.contrib.sites',
		'django.contrib.flatpages',
		'markitup',
		'adminfiles',
		'tagging',
	  'sorl.thumbnail',
		'django_extensions',
		'blog',
		'projects',
		'code_samples',
		'pagination',
)
MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})
MARKITUP_SET = 'markitup/sets/textile'

#Load installation specific settings/passwords from external file with restrictive permissions
execfile(os.path.join(PROJECT_PATH,'.private-settings'))

# vim: ai ts=4 sts=4 et sw=4
