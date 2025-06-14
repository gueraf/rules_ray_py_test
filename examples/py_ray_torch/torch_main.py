import os

import ray
import torch
from absl import app, flags

from examples.py_ray_torch.torch_lib import sum_one_to_n

flags.DEFINE_integer("n", 10, "n, for sum from 1 to n.")

FLAGS = flags.FLAGS


@ray.remote
def sum_one_to_n_remote(n: int):
    return sum_one_to_n(n)


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

    print(f"PyTorch version: {torch.__version__}")

    sum = ray.get(sum_one_to_n_remote.remote(FLAGS.n))
    print(f"Sum from 1 to {FLAGS.n} is {sum}.")


if __name__ == "__main__":
    app.run(main)
