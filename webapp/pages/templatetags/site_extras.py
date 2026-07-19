from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Small hand-rolled line icons (24x24, stroke=currentColor) so the site has
# zero third-party font/icon dependency at runtime.
_ICONS = {
    "mail": """
        <path d="M3 5.5h18v13H3z"/>
        <path d="M3 5.5l9 7 9-7"/>
    """,
    "github": """
        <path d="M12 2a10 10 0 0 0-3.16 19.49c.5.1.68-.22.68-.48
            v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.46-1.16-1.11-1.47-1.11-1.47
            -.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.52 2.34 1.08
            2.91.83.09-.65.35-1.08.63-1.33-2.22-.25-4.56-1.11-4.56-4.93
            0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .84-.27
            2.75 1.02a9.6 9.6 0 0 1 5 0c1.91-1.3 2.75-1.02 2.75-1.02.55
            1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.83-2.34 4.68
            -4.57 4.93.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10
            0 0 0 12 2Z"/>
    """,
    "bluesky": """
        <path d="M12 8.5c-1-2.4-3.6-4.6-6-5.5-.6-.2-1 .3-.8.9
            1 3.1 1.9 8.4 2.9 10 .5.8 1.4 1.4 2.4 1.4h1
            c1 0 1.9-.6 2.4-1.4 1-1.6 1.9-6.9 2.9-10 .2-.6-.2-1.1-.8-.9
            -2.4.9-5 3.1-6 5.5Z"/>
    """,
    "linkedin": """
        <rect x="3" y="3" width="18" height="18" rx="2"/>
        <path d="M7.5 10v6.5M7.5 7.2v.1M11.5 16.5V13c0-1.4.9-2.2 2-2.2
            1.1 0 1.8.8 1.8 2.2v3.5"/>
        <path d="M11.5 10.3v.1"/>
    """,
    "scholar": """
        <path d="M2 9.5 12 4l10 5.5-10 5.5-10-5.5Z"/>
        <path d="M6 12v5c0 1.4 2.7 3 6 3s6-1.6 6-3v-5"/>
        <path d="M21 9.5v6"/>
    """,
    "osf": """
        <ellipse cx="12" cy="6" rx="8" ry="3"/>
        <path d="M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6"/>
        <path d="M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/>
    """,
    "arrow-left": """
        <path d="M19 12H5"/>
        <path d="M11 6l-6 6 6 6"/>
    """,
    "utensils": """
        <path d="M7 3v6M5 3v6c0 1.1.9 2 2 2s2-.9 2-2V3"/>
        <path d="M7 11v10"/>
        <path d="M17 3c-1.7 0-3 2-3 5s1.3 5 3 5v8"/>
    """,
    "book": """
        <path d="M4 5.5c2-1 5-1 8 .5 3-1.5 6-1.5 8-.5v13c-2-1-5-1-8 .5
            -3-1.5-6-1.5-8-.5Z"/>
        <path d="M12 6v13"/>
    """,
}


@register.simple_tag
def icon(name, css_class=""):
    body = _ICONS.get(name, "")
    return mark_safe(
        f'<svg class="icon {css_class}" viewBox="0 0 24 24" '
        f'fill="none" stroke="currentColor" stroke-width="1.6" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true">{body}</svg>'
    )
