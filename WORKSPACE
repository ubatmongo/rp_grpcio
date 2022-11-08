workspace(name = "rp_grpcio")

# Inbuilt repos
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")

# Override rules_go https://github.com/bazelbuild/rules_docker/issues/2036
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "099a9fb96a376ccbbb7d291ed4ecbdfd42f6bc822ab77ae6f1b5cb9e914e94fa",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.35.0/rules_go-v0.35.0.zip",
    ],
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.19.1")

# rules_pkg
http_archive(
    name = "rules_pkg",
    sha256 = "451e08a4d78988c06fa3f9306ec813b836b1d076d0f055595444ba4ff22b867f",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/0.7.1/rules_pkg-0.7.1.tar.gz",
        "https://github.com/bazelbuild/rules_pkg/releases/download/0.7.1/rules_pkg-0.7.1.tar.gz",
    ],
)

load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")

rules_pkg_dependencies()

# Python
http_archive(
    name = "rules_python",
    sha256 = "8c8fe44ef0a9afc256d1e75ad5f448bb59b81aba149b8958f02f7b3a98f5d9b4",
    strip_prefix = "rules_python-0.13.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.13.0.tar.gz",
)

# Docker
http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "b1e80761a8a8243d03ebca8845e9cc1ba6c82ce7c5179ce2b295cd36f7e394bf",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.25.0/rules_docker-v0.25.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

register_toolchains("//:container_py_toolchain")

load("@io_bazel_rules_docker//python:image.bzl", _py_image_repos = "repositories")

_py_image_repos()

# Defer python toolchains til after we've registered our internal ones
load("@rules_python//python:repositories.bzl", "python_register_toolchains")
PYTHON_VERSION = "3.9.13"

python_register_toolchains(
    name = "python39",
    python_version = PYTHON_VERSION,
)

# Override rules_python's version of installer to patch around https://github.com/pypa/installer/issues/134
http_archive(
    name = "pypi__installer",
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
    sha256 = "1d6c8d916ed82771945b9c813699e6f57424ded970c9d8bf16bbc23e1e826ed3",
    type = "zip",
    url = "https://files.pythonhosted.org/packages/1b/21/3e6ebd12d8dccc55bcb7338db462c75ac86dbd0ac7439ac114616b21667b/installer-0.5.1-py3-none-any.whl",
)

load("@rules_python//python/pip_install:repositories.bzl", "pip_install_dependencies")

pip_install_dependencies()

load("@rules_python//python/pip_install:pip_repository.bzl", "pip_repository")
load("@python39//:defs.bzl", "interpreter")

# deps
pip_repository(
    name = "pypi",
    python_interpreter_target = interpreter,
    requirements_darwin = "//:requirements_darwin.txt",
    requirements_linux = "//:requirements_linux.txt",
)

load("@pypi//:requirements.bzl", "install_deps")

install_deps()

load("@rules_python//python:versions.bzl", get_python_release_url = "get_release_url")

(_, python_url, _) = get_python_release_url("x86_64-unknown-linux-gnu", PYTHON_VERSION)

http_file(
    name = "python3_interpreter",
    url = python_url,
    downloaded_file_path = "python.tar.gz",
)

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)

container_pull(
    name = "amazon2_linux",
    architecture = "amd64",
    registry = "index.docker.io",
    repository = "amazonlinux",
    tag = "2",
)
