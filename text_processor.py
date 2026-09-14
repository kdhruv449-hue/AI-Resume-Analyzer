import re


def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Preserve important technical skills
    text = text.replace("c++", "cplusplus")
    text = text.replace("c#", "csharp")
    text = text.replace(".net", "dotnet")
    text = text.replace("node.js", "nodejs")

    # Remove other special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove spaces from beginning and end
    text = text.strip()

    return text