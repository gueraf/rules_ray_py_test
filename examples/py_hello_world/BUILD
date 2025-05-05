load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_test")
load("//:rules_ray_py/rules_ray_py/py_tar_zst.bzl", "py_tar_zst")

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

py_tar_zst(
    name = "hello_world_tar_zst",
    wrapped_py_package = ":hello_world",
)
