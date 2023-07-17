import re


class TextExtractor:
    # HTML_TAGS not used (yet?), but I suppose its a reference list...
    HTML_TAGS = [
        "div",
        "button",
        "section",
        "a",
        "p",
        "span",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "ul",
        "ol",
        "li",
        "img",
        "input",
        "form",
        "table",
        "tr",
        "th",
        "td",
        "header",
        "nav",
        "footer",
        "article",
        "aside",
        "main",
        "figure",
        "figcaption",
        "blockquote",
        "em",
        "strong",
        "code",
        "pre",
        "iframe",
        "audio",
        "video",
    ]

    HTML_ENTITIES = {
        "&nbsp;": " ",
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&quot;": '"',
        "&#39;": "'",
        "&#x27;": "'",
        # Add more HTML entities as needed
    }

    def extract_text(html):
        cleanish_text = re.compile("<.*?>")

        cleaner_html = re.sub(cleanish_text, "", html)

        cleanist_html = None
        for entity, char in TextExtractor.HTML_ENTITIES.items():
            cleanist_html = cleaner_html.replace(entity, char)

        return cleanist_html
