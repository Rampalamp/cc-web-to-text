import argparse
import os
import time
from scrapers import SingleScrape


def main(url):
    # get working dir, adjust string to save into /fetched_data/ dir
    WORKING_DIR = os.getcwd() + "/fetched_data/"

    if not os.path.exists(WORKING_DIR):
        os.makedirs(WORKING_DIR)

    # Strip URL of odd characters, timestamp for uniqueness and append to end of WORKING_DIR
    SAVE_PATH = (
        WORKING_DIR + "".join(filter(str.isalnum, url)) + str(time.time()) + ".txt"
    )

    text = SingleScrape.get_text(url)

    if text is not None:
        with open(SAVE_PATH, "w") as file:
            file.write(text)

        print(f"Finished writing to file : {SAVE_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch text from a website.")
    parser.add_argument(
        "-u", "--url", type=str, required=True, help="URL of the website"
    )

    args = parser.parse_args()

    main(args.url)
