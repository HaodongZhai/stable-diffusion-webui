from modules import shared
from packaging import version
import re


v160 = version.parse("1.6.0")


def parse_version(text):
    if text is None:
        return None

    m = re.match(r'([^-]+-[^-]+)-.*', text)
    if m:
        text = m.group(1)

    try:
        return version.parse(text)
    except Exception as e:
        return None


def backcompat(d):
    """Checks infotext Version field, and enables backwards compatibility options according to it."""

    if not shared.opts.auto_backcompat:
        return

    ver = parse_version(d.get("Version"))
    if ver is None:
        return

    if ver < v160:
        d["Old prompt editing timelines"] = True
