import feedparser
from subprocess import run
from time import sleep#
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import os
import platform


DEFAULT_FORMAT_STR = "{title}:\n{content}"


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
    parser.add_argument("-f", "--format", type=str, default=DEFAULT_FORMAT_STR,
                        help="Item format string (Python format style, {})")
    args = parser.parse_args()

    from bs4 import BeautifulSoup as soup

    while True:
        feed = feedparser.parse(args.url)
        if feed.bozo:
            raise feed.bozo_exception

        for item in feed['entries']:
            if item.content:
                content_html = item.content[0]['value']
                content = BeautifulSoup(content_html,
                features="html.parser").get_text()
            else:
                content = ''

            if not args.persist:
                clear_screen()

            cowsay(args.format.format(title=item.title, content=content))
            sleep(args.delay)


if __name__ == "__main__":
    main()
