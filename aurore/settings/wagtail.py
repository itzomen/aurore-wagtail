# Read more
# https://docs.wagtail.org/en/stable/reference/settings.html
from aurore.env import env

WAGTAIL_SITE_NAME = "Aurore Store"

WAGTAILADMIN_BASE_URL = env("WAGTAILADMIN_BASE_URL", default="http://app.example.com/")

WAGTAILAPI_BASE_URL = env("WAGTAILAPI_BASE_URL", default="http://api.example.com/")

# Search
# https://docs.wagtail.io/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Wagtail email notifications from address
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = "hello@aurorestore.com"

# Wagtail email notification format
WAGTAILADMIN_NOTIFICATION_USE_HTML = True

# Reverse the default case-sensitive handling of tags
TAGGIT_CASE_INSENSITIVE = True

WAGTAIL_GRAVATAR_PROVIDER_URL = "//www.gravatar.com/avatar"

WAGTAIL_MODERATION_ENABLED = True

WAGTAILIMAGES_MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # i.e. 20MB

# https://docs.wagtail.org/en/stable/advanced_topics/images/feature_detection.html#image-feature-detection
# WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = True


"""
For admins only, Wagtail performs a check on the dashboard to see if newer
releases are available. This also provides the Wagtail team with the hostname
of your Wagtail site. If you'd rather not receive update notifications, or if
you'd like your site to remain unknown, you can disable it with this setting.
"""
WAGTAIL_ENABLE_UPDATE_CHECK = True

# WAGTAIL_FRONTEND_LOGIN_URL = "cms/dashboard/"

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DATE_INPUT_FORMATS
WAGTAIL_DATE_FORMAT = "%d.%m.%Y."
WAGTAIL_DATETIME_FORMAT = "%d.%m.%Y. %H:%M"
WAGTAIL_TIME_FORMAT = "%H:%M"

WAGTAIL_WORKFLOW_ENABLED = False
