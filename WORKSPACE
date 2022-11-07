workspace(name = "rp_grpcio")

# Inbuilt repos
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

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
