import os
from dotenv import load_dotenv

from adutils import read_file, Log, log_me
from adutils import TransparentPath as Path

load_dotenv()


def get_environ(s: str):
    if "$" not in s:
        return s
    if s == "$":
        return ""

    split_s = s.split("$")
    new_s = split_s[0]
    for subs in split_s[1:]:
        if subs == "":
            continue
        if os.sep not in subs:
            new_s = "".join([new_s, os.environ[subs]])
        elif subs == os.sep:
            continue
        else:
            env = os.environ[subs.split(os.sep)[0]]
            newnew_s = os.sep.join([env] + subs.split(os.sep)[1:])
            new_s = "".join([new_s, newnew_s])
    return new_s


class Configs:

    instance = None

    def __init__(self):

        path = Path(__file__).parent / "configs.json"
        if "configpath" in os.environ:
            Log.debug("Found configpath in .env")
            spath = os.environ["configpath"]
            if spath != "" and spath is not None and Path(spath).is_file():
                Log.debug("configpath points to a valid file. Using it")
                path = Path(spath)
            else:
                Log.debug("configpath points to a non-valid file. Using "
                          "default configs")
        else:
            Log.debug("configpath not found in .env")

        self.data = read_file(path)
        Log.debug(f"Configs loaded:\n{self.data}")
        Configs.instance = self

    def __getattr__(self, item):
        new = Path(get_environ(self.data["paths"][item]))
        setattr(self, item, new)
        return new

    @property
    def logger_fmt(self):
        return (
            self.data["logger_fmt"]["fmt"],
            self.data["logger_fmt"]["datefmt"],
        )


@log_me(level=5)
def load_config():

    if Configs.instance is None:
        Configs()

    return Configs.instance
