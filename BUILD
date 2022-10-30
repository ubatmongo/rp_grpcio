load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

py_binary(
    name = "rp_grpcio",
    srcs = ["rp_grpcio.py"],
    deps = [
        requirement("grpcio"),
    ],
)

# This rule adds a convenient way to update the requirements file.
compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)
