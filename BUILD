load("@io_bazel_rules_docker//container:container.bzl", "container_image", "container_layer")
load("@io_bazel_rules_docker//python:image.bzl", "py_layer")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

load("@rules_python//python:defs.bzl", "py_binary", "py_runtime", "py_runtime_pair")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

load("@pypi//:requirements.bzl", "requirement")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_darwin = "//:requirements_darwin.txt",
    requirements_linux = "//:requirements_linux.txt",
)

py_binary(
    name = "rp_grpcio",
    srcs = ["rp_grpcio.py"],
    deps = [
        requirement("google-cloud-storage"),

        # fake runtime deps
        requirement("aiodns"),
        requirement("cchardet"),

        # other deps
        requirement("aiobotocore"),
        requirement("aiohttp"),
        requirement("aiostream"),
        requirement("astunparse"),
        requirement("black"),
        requirement("boto3"),
        requirement("boto3-type-annotations"),
        requirement("botocore"),
        requirement("bugsnag"),
        requirement("colorama"),
        requirement("cryptography"),
        requirement("dataclasses-json"),
        requirement("dnspython"),
        requirement("docopt"),
        requirement("evergreen.py"),
        requirement("flask"),
        requirement("freezegun"),
        requirement("gitpython"),
        requirement("gnupg"),
        requirement("google-api-python-client"),
        requirement("google-auth-oauthlib"),
        requirement("google-cloud-iam"),
        requirement("graphviz"),
        requirement("hydra-core"),
        requirement("hypercorn"),
        requirement("inject"),
        requirement("javac-parser"),
        requirement("jinja2"),
        requirement("jira"),
        requirement("jproperties"),
        requirement("junit_xml"),
        requirement("keyring"),
        requirement("keyrings.alt"),
        requirement("libcst"),
        requirement("lxml"),
        requirement("matplotlib"),
        requirement("more_itertools"),
        requirement("motor"),
        requirement("mypy"),
        requirement("networkx"),
        requirement("omegaconf"),
        requirement("packaging"),
        requirement("pdpyras"),
        requirement("plotly"),
        requirement("prompt-toolkit"),
        requirement("pygithub"),
        requirement("pygments"),
        requirement("pylint"),
        requirement("pymongo"),
        requirement("pystache"),
        requirement("pytest"),
        requirement("pytest-mock"),
        requirement("python-box"),
        requirement("python-dateutil"),
        requirement("python-json-logger"),
        requirement("pytz"),
        requirement("pyyaml"),
        requirement("quart"),
        requirement("regex"),
        requirement("requests"),
        requirement("retry2"),
        requirement("rsa"),
        requirement("ruamel.yaml"),
        requirement("semver"),
        requirement("shrub.py"),
        requirement("slackclient"),
        requirement("structlog"),
        requirement("tenacity"),
        requirement("tinys3"),
        requirement("typed-json-dataclass"),
        requirement("urllib3"),
        requirement("yarl"),
    ],
)

py_runtime(
    name = "container_py3_runtime",
    interpreter_path = "/opt/python/bin/python3",
    python_version = "PY3",
)

py_runtime_pair(
    name = "container_py_runtime_pair",
    py3_runtime = ":container_py3_runtime",
)

toolchain(
    name = "container_py_toolchain",
    exec_compatible_with = [
        "@io_bazel_rules_docker//platforms:run_in_container",
    ],
    toolchain = "container_py_runtime_pair",
    toolchain_type = "@rules_python//python:toolchain_type",
)

container_layer(
    name = "python_layer",
    directory = "/opt",
    tars = ["@python3_interpreter//file"],
    operating_system = "linux",
)

container_image(
    name = "python_base",
    base = "@amazon2_linux//image",
    layers = [":python_layer"],
    symlinks = {
        "/usr/bin/python": "/opt/python/bin/python3"
    }
)

py_layer(
    name = "pip_tools_deps",
    deps = [
        "@pypi__pip_tools//:lib",
        "@pypi__build//:lib",
        "@pypi__pep517//:lib",
        "@pypi__tomli//:lib",
        "@pypi__importlib_metadata//:lib",
        "@pypi__colorama//:lib",
        "@pypi__click//:lib",
        "@pypi__pip//:lib",
        "@pypi__setuptools//:lib",
        "@pypi__wheel//:lib"
    ]
)

py3_image(
    name = "compile_linux_deps",
    srcs = ["compile_deps.py"],
    data = ["requirements.in"],
    deps = ["@rules_python//python/runfiles"],
    layers = [":pip_tools_deps"],
    main = "compile_deps.py",
    base = ":python_base",
)

sh_binary(
    name = "compile_all_deps",
    srcs = [":compile_all_deps.sh"],
    data = [
        ":requirements.update",
        ":compile_linux_deps"
    ],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)
