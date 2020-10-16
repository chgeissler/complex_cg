import argparse

from adutils import Log

from .configs import load_config

conf = load_config()

fmt, datefmt = conf.logger_fmt
Log.set_format(fmt=fmt, datefmt=datefmt)


class Args:
    def __init__(self):
        # noinspection PyTypeChecker
        parser = argparse.ArgumentParser(
            description="complex",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )

        parser.add_argument(
            "--arg1",
            type=str,
            help="The first argument.",
            default="Hello World",
        )
        parser.add_argument(
            "--boolarg", action="store_true", help="A boolean arg.",
        )
        self.theargs = parser.parse_args()

    def run(self):

        pass


def main():
    args = Args()


if __name__ == "__main__":
    main()
