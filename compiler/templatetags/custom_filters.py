from django import template
import markdown2

register = template.Library()

@register.filter
def render_markdown(text):
    """Converts Markdown text to HTML with syntax highlighting."""
    if not text:
        return ""
    return markdown2.markdown(
        text,
        extras=["fenced-code-blocks", "tables", "strike", "code-friendly"]
    )
