# coding=utf-8
import re
import clipboard
import argparse


def get_sentences():
    """Export sentences from a Kindle `My Clippings.txt` file."""
    
    # Pass Drive letter as argument
    parser = argparse.ArgumentParser(description="Kindle Drive Letter")
    parser.add_argument("drive", type=str)
    drive = parser.parse_args().drive
    path = f"{drive}:/documents/My Clippings.txt"
    
    # Read .txt file
    with open(f"{path}", encoding="utf-8") as notes:
        text_raw = notes.read()

    # Format the text
    text_formatted = re.sub("- Your Highlight on page .*\n\n", "", text_raw)
    text_formatted = re.sub("==========", "", text_formatted)

    # Pass to clipboard
    clipboard.copy(text_formatted)
    

if __name__ == "__main__":
    get_sentences()
