load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_test")
load("@rules_ray_py//rules_ray_py:py_conda.bzl", "py_conda")

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    deps = [
        ":hello_world_lib",
        "@pip//absl_py",
        "@pip//pip_install_test",
    ],
)

py_library(
    name = "hello_world_lib",
    srcs = ["hello_world_lib.py"],
)

py_test(
    name = "hello_world_test",
    srcs = ["hello_world_test.py"],
    deps = [
        ":hello_world_lib",
        "@pip//absl_py",
    ],
)

py_conda(
    name = "hello_world_conda",
    wrapped_py_binary = ":hello_world",
)
