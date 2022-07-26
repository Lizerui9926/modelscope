from typing import Any, Dict

import torch

from modelscope.metainfo import Pipelines
from modelscope.pipelines.base import Input
from modelscope.utils.constant import Tasks
from modelscope.utils.logger import get_logger
from ..base import Model, Pipeline
from ..builder import PIPELINES

logger = get_logger()


@PIPELINES.register_module(
    Tasks.video_multi_modal_embedding,
    module_name=Pipelines.video_multi_modal_embedding)
class VideoMultiModalEmbeddingPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a video_multi_modal_embedding pipeline for prediction
        Args:
            model: model id on modelscope hub.
        """
        super().__init__(model=model)

    def preprocess(self, input: Input) -> Dict[str, Any]:
        return input

    def _process_single(self, input: Input, *args, **kwargs) -> Dict[str, Any]:
        with self.place_device():
            out = self.forward(input)

        self._check_output(out)
        return out

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        return self.model(input)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
