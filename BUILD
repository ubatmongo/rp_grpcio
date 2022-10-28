load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_test")

py_binary(
    name = "rp_grpcio",
    srcs = ["main.py"],
    deps = [
        requirement("grpcio"),
    ],
)
