workspace(name = "rp_grpcio")

# Inbuilt repos
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository", "new_git_repository")

# Python
http_archive(
    name = "rules_python",
    sha256 = "8c8fe44ef0a9afc256d1e75ad5f448bb59b81aba149b8958f02f7b3a98f5d9b4",
    strip_prefix = "rules_python-0.13.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.13.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python39",
    python_version = "3.9",
)

load("@python39//:defs.bzl", "interpreter")

# Override rules_python's version of installer to patch around https://github.com/pypa/installer/issues/134
http_archive(
    name = "pypi__installer",
    url = "https://files.pythonhosted.org/packages/1b/21/3e6ebd12d8dccc55bcb7338db462c75ac86dbd0ac7439ac114616b21667b/installer-0.5.1-py3-none-any.whl",
    sha256 = "1d6c8d916ed82771945b9c813699e6f57424ded970c9d8bf16bbc23e1e826ed3",
    type = "zip",
    build_file_content = """
package(default_visibility = ["//visibility:public"])

load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "lib",
    srcs = glob(["**/*.py"]),
    imports = ["."],
)
""",
    patches = ["//:installer_canonicalize_wheel_name.diff"],  # https://github.com/pypa/installer/pull/137
)

load("@rules_python//python/pip_install:repositories.bzl", "pip_install_dependencies")

pip_install_dependencies()

load("@rules_python//python/pip_install:pip_repository.bzl", "pip_repository")

pip_repository(
    name = "pypi",
    extra_pip_args = ["-v"],
    python_interpreter_target = interpreter,
    quiet = False,
    requirements_darwin = "//:requirements_darwin.txt",
    requirements_linux = "//:requirements_linux.txt",
)

load("@pypi//:requirements.bzl", "install_deps")

install_deps()

# protobuf
http_archive(
    name = "rules_proto_grpc",
    sha256 = "bbe4db93499f5c9414926e46f9e35016999a4e9f6e3522482d3760dc61011070",
    strip_prefix = "rules_proto_grpc-4.2.0",
    urls = ["https://github.com/rules-proto-grpc/rules_proto_grpc/archive/4.2.0.tar.gz"],
)

load("@rules_proto_grpc//:repositories.bzl", "rules_proto_grpc_repos", "rules_proto_grpc_toolchains")

rules_proto_grpc_toolchains()

rules_proto_grpc_repos()

load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")

rules_proto_dependencies()

rules_proto_toolchains()

load("@rules_proto_grpc//python:repositories.bzl", rules_proto_grpc_python_repos = "python_repos")

rules_proto_grpc_python_repos()

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")

grpc_extra_deps()

## pip_parse to load rules_proto_grpc_py3_deps isn't working
#pip_parse(
#    name = "rules_proto_grpc_py3_deps",
#    extra_pip_args = ["-v"],
#    quiet = False,
#    python_interpreter_target = interpreter,
#    requirements_lock = "@rules_proto_grpc//python:requirements.txt",
#)
#
#load("@rules_proto_grpc_py3_deps//:requirements.bzl", "install_deps")
#
#install_deps()
#load("@rules_python//python:pip.bzl", "pip_install")
#
#pip_install(
#    name = "rules_proto_grpc_py3_deps",
#    python_interpreter = "python3",
#    requirements = "@rules_proto_grpc//python:python_grpclib_library.txt",
#)

#load("@rules_proto_grpc//python:python_grpclib_library.bzl", "python_grpclib_library")
#python_grpclib_library()
