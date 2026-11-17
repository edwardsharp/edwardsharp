from html import escape, unescape
from pathlib import Path
import re

START, END = "<!-- featured-index:start -->", "<!-- featured-index:end -->"


def update_index(text):
    prefix, rest = text.split(START)
    _, body = rest.split(END)
    rows = []
    pattern = r'(?:^<a (?:name|id)="([^"]+)"></a>\n\n)?^### ([^\n]+)\n\n`(S|MD|M|L|XL)`([^\n]*)'
    for year, section in re.findall(r"^## (\d{4})\n(.*?)(?=^## |\Z)", body, re.M | re.S):
        projects = re.findall(pattern, section, re.M)
        for i, (anchor, title, size, tags) in enumerate(projects):
            images = "".join(" " + image for image in re.findall(r"<img\b[^>]*>", title, re.I))
            title = unescape(re.sub(r"<[^>]*>", "", title)).strip()
            anchor = anchor or re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")
            cell = "" if i else f'<td rowspan="{len(projects)}" valign="top">{year}</td>'
            tags = " ".join(f"<code>{escape(tag)}</code>" for tag in re.findall(r"`([^`]+)`", tags))
            rows.append(f'<tr>{cell}<td><a href="#{escape(anchor)}">{escape(title)}{images}</a></td><td><code>{size}</code></td><td>{tags}</td></tr>')
    if not rows:
        raise ValueError("no featured sections found")
    return prefix + START + "\n<table>\n" + "\n".join(rows) + "\n</table>\n" + END + body


if __name__ == "__main__":
    readme = Path(__file__).with_name("README.md")
    readme.write_text(update_index(readme.read_text(encoding="utf-8")), encoding="utf-8")
