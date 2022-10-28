load("@pypi//rp_grpcio:requirements.bzl", "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

#py_library(
#    name = "rp_grpcio",
#    srcs = ["runner.py"],
#    deps = [
#            requirement("grpcio"),
#        ]
#)

# This rule adds a convenient way to update the requirements file.
compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)
