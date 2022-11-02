load("@bazel_skylib//rules:diff_test.bzl", "diff_test")
load("@bazel_skylib//rules:write_file.bzl", "write_file")

#load("@pypi//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@rules_python//python:pip.bzl", "compile_pip_requirements", "pip_parse")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.in",
    requirements_txt = "requirements_lock.txt",
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
    ],
)
