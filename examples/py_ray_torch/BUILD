load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library", "py_test")
load("@rules_ray_py//rules_ray_py:ray_job.bzl", "ray_job")

py_library(
    name = "torch_lib",
    srcs = ["torch_lib.py"],
    deps = ["@pip//torch"],
)

py_test(
    name = "torch_lib_test",
    srcs = ["torch_lib_test.py"],
    deps = [
        ":torch_lib",
        "@pip//absl_py",
    ],
)

py_binary(
    name = "torch_main",
    srcs = ["torch_main.py"],
    deps = [
        ":torch_lib",
        "@pip//absl_py",
        "@pip//ray",
    ],
)

ray_job(
    name = "torch_main_ray_job",
    wrapped_py_binary = ":torch_main",
)
