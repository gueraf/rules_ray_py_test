import os

import ray
from absl import app, flags

from examples.py_ray_hello_world.hello_world_lib import make_hello_message

flags.DEFINE_string("name", "Fabian", "Name to greet.")

FLAGS = flags.FLAGS


def say_hello(name: str):
    msg = make_hello_message(name)
    print(f"{msg} from PID {os.getpid()}!")


@ray.remote
def say_hello_remote(name: str):
    say_hello(name)


def main(argv):
    del argv  # Unused.

    ray.init(
        runtime_env={
            "env_vars": {
                "PYTHONPATH": os.path.dirname(os.path.realpath(__file__)).split(
                    "/site-packages/", 1
                )[0]
                + "/site-packages/site-packages/"
            },
        }
    )

    say_hello(FLAGS.name)
    ray.get(say_hello_remote.remote(FLAGS.name))


if __name__ == "__main__":
    app.run(main)
