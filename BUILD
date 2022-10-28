load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_test")

py_library(
    name = "rp_grpcio",
    srcs = ["runner.py"],
    deps = [
        requirement("grpcio"),
    ],
)
