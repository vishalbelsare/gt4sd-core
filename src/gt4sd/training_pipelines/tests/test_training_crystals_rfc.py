#
# MIT License
#
# Copyright (c) 2022 GT4SD team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""Crystals rfc trainer unit tests."""

import shutil
import tempfile
from typing import Any, Dict, cast

import importlib_resources

from gt4sd.training_pipelines import (
    TRAINING_PIPELINE_MAPPING,
    CrystalsRFCTrainingPipeline,
)

template_config = {
    "model_args": {"sym": "all"},
    "dataset_args": {"test_size": 0.2},
}


def test_train():

    pipeline = TRAINING_PIPELINE_MAPPING.get("crystals-rfc")

    assert pipeline is not None

    TEMPORARY_DIRECTORY = tempfile.mkdtemp()

    test_pipeline = cast(CrystalsRFCTrainingPipeline, pipeline())

    config: Dict[str, Any] = template_config.copy()
    config["training_args"] = {}
    config["training_args"]["output_path"] = TEMPORARY_DIRECTORY

    with importlib_resources.as_file(
        importlib_resources.files("gt4sd")
        / "training_pipelines/tests/crystals_rfc_sample.csv",
    ) as file_path:
        config["dataset_args"]["datapath"] = str(file_path)
        test_pipeline.train(**config)

    shutil.rmtree(TEMPORARY_DIRECTORY)
