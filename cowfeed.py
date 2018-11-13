import feedparser
from subprocess import run
from time import sleep
from argparse import ArgumentParser
import os
import platform


def clear_screen():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def cowsay(text):
    result = run(["cowsay", text],
             capture_output=True,
             check=True)
    print(result.stdout.decode())


def main():
    parser = ArgumentParser()
    parser.add_argument("url", type=str)
    parser.add_argument("-p", "--persist", dest="persist",
                        action="store_true",
                        help="Keep previous feed items rather than overwriting")
    parser.add_argument("--delay", type=int, default=10,
                        help="Delay between printing items")
    args = parser.parse_args()

    while True:
        feed = feedparser.parse(args.url)

        for item in feed['items']:
            if not args.persist:
                clear_screen()
            cowsay(item["title"])
            sleep(args.delay)

            
if __name__ == "__main__":
    main()
