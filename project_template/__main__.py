import argparse

from adutils import Log

from .configs import load_config
from .subdir_1.subpythonfile_1 import func1

conf = load_config()

fmt, datefmt = conf.logger_fmt
Log.set_format(fmt=fmt, datefmt=datefmt)


class Args:
    def __init__(self):
        # noinspection PyTypeChecker
        parser = argparse.ArgumentParser(
            description="project_template",
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

        func1(self.theargs.arg1)


def main():
    args = Args()
    args.run()


if __name__ == "__main__":
    main()
