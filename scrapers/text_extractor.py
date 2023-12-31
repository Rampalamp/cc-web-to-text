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
        # pattern to extract all html tags out of html
        cleaner_pattern = r"<[^>]*\/?>"

        cleaned_html = re.sub(cleaner_pattern, "", html)
        # lots of sites will return an abundance of extra white space.
        # its not really human friendly to read, but if fed to an AI for fine tuning, I don't think the machines would care?
        extra_white_removed_html = re.sub(r"\s+", " ", cleaned_html)

        cleanist_html = extra_white_removed_html
        # swap HTML entities out for actual character
        for entity, char in TextExtractor.HTML_ENTITIES.items():
            cleanist_html = cleanist_html.replace(entity, char)

        return cleanist_html
