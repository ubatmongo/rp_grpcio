load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@rules_python//python:pip.bzl", "compile_pip_requirements", "pip_parse")
load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_github_grpc_grpc//bazel:python_rules.bzl", "py_grpc_library", "py_proto_library")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)

py_binary(
    name = "rp_grpcio",
    srcs = ["rp_grpcio.py"],
    deps = [
        requirement("grpcio"),
    ],
)

#proto_library(
#    name = "helloworld_proto",
#    srcs = ["proto/greeting.proto"],
#)
#
#py_proto_library(
#    name = "helloworld_py_proto",
#    deps = [":helloworld_proto"],
#)
#
#py_grpc_library(
#    name = "helloworld_py_grpc",
#    srcs = [":helloworld_proto"],
#    deps = [":helloworld_py_proto"],
#)
#
#py_binary(
#    name = "greeter_server",
#    srcs = ["greeter_server.py"],
#    deps = [":helloworld_py_grpc"],
#)
#
#py_binary(
#    name = "greeter_client",
#    srcs = ["greeter_client.py"],
#    deps = [":helloworld_py_grpc"],
#)
