load("@bazel_skylib//rules:diff_test.bzl", "diff_test")
load("@bazel_skylib//rules:write_file.bzl", "write_file")

load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@pypi//:requirements.bzl", "requirement")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_darwin = "//:requirements_darwin.txt",
    requirements_linux = "//:requirements_linux.txt",
)

# The requirements.bzl file is generated with a reference to the interpreter for the host platform.
# In order to check in a platform-agnostic file, we have to replace that reference with the symbol
# loaded from our python toolchain.
genrule(
    name = "make_platform_agnostic",
    srcs = ["@pypi//:requirements.bzl"],
    outs = ["requirements.clean.bzl"],
    cmd = " | ".join([
        "cat $<",
        # Insert our load statement after the existing one so we don't produce a file with buildifier warnings
        """sed -e '/^load.*/i\\'$$'\\n''load("@python39//:defs.bzl", "interpreter")'""",
        """tr "'" '"' """,
        """sed 's#"@python39_.*//:bin/python3"#interpreter#' >$@""",
    ]),
)

write_file(
    name = "gen_update",
    out = "update.sh",
    content = [
        # This depends on bash, would need tweaks for Windows
        "#!/usr/bin/env bash",
        # Bazel gives us a way to access the source folder!
        "cd $BUILD_WORKSPACE_DIRECTORY",
        "cp -fv bazel-bin/requirements.clean.bzl requirements.bzl",
    ],
)

sh_binary(
    name = "vendor_requirements",
    srcs = ["update.sh"],
    data = [":make_platform_agnostic"],
)

# Similarly ensures that the requirements.bzl file is updated
# based on the requirements.txt lockfile.
diff_test(
    name = "test_vendored",
    failure_message = "Please run:  bazel run //:vendor_requirements",
    file1 = "requirements.bzl",
    file2 = ":make_platform_agnostic",
)

load("@pypi//:requirements.bzl", "requirement")

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
