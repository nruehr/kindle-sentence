# coding=utf-8
import re
import clipboard

def get_sentences():
    """Export sentences from a kinde clippings text file."""
    # Read .txt file
    with open('H:/documents/My Clippings.txt', encoding='utf-8') as notes:
        text_raw = notes.read()

    # Format the text
    text_formatted = re.sub("- Your Highlight on page .*\n\n", "", text_raw)
    text_formatted = re.sub("==========", "", text_formatted)

    # Pass to clipboard
    clipboard.copy(text_formatted)

if __name__ == "__main__":
    get_sentences()
