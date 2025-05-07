load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library")
load("@rules_ray_py//rules_ray_py:ray_job.bzl", "ray_job")

py_library(
    name = "hello_world_lib",
    srcs = ["hello_world_lib.py"],
)

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    deps = [
        ":hello_world_lib",
        "@pip//absl_py",
        "@pip//ray",
    ],
)

ray_job(
    name = "hello_world_ray_job",
    wrapped_py_binary = ":hello_world",
)
