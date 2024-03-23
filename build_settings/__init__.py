"""
Let's initialize some goodies.
"""
try:
    from settings import settings
except ImportError:
    from .settings import settings  # noqa
