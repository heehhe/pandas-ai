from typing import Optional, Union

from pandasai.agent.base_security import BaseSecurity
from pandasai.config import load_config_from_json
from pandasai.ee.agents.security_agent.pipeline.security_pipeline import (
    SecurityPipeline,
)
from pandasai.pipelines.abstract_pipeline import AbstractPipeline
from pandasai.pipelines.pipeline_context import PipelineContext
from pandasai.schemas.df_config import Config


class SecurityAgent(BaseSecurity):
    def __init__(
        self,
        config: Optional[Union[Config, dict]] = None,
        pipeline: AbstractPipeline = None,
    ) -> None:
        context = None

        if isinstance(config, dict):
            config = Config(**load_config_from_json(config))
        elif config is None:
            config = Config()

        context = PipelineContext(None, config)

        pipeline = pipeline or SecurityPipeline(context=context)
        super().__init__(pipeline)

    def evaluate(self, query: str) -> bool:
        return self.pipeline.run(query)
