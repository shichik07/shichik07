from . import content


def site_globals(request):
    return {
        "nav_links": content.NAV_LINKS,
        "social_links": content.SOCIAL_LINKS,
        "site_name": content.SITE_NAME,
    }
