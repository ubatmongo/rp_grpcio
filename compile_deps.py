#!/usr/bin/env python3

import os
import sys

from piptools.scripts.compile import cli

from rules_python.python.runfiles import runfiles

rf = runfiles.Create()

os.environ["CUSTOM_COMPILE_COMMAND"] = "bazel run //:requirements.update"

sys.argv.append("--allow-unsafe")
sys.argv.append("--generate-hashes")
sys.argv.append("--output-file")
sys.argv.append("-")
sys.argv.append("./requirements.in")

cli()
