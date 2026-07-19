"""
패키지의 인터페이스를 정의한다. init 파일이 있으면 외부에서 어떤 메서드가 어떤 파일에 정의되어 있는지 알 필요 없이
바로 from oa_service import run_pipeline 등을 import 해서 사용할 수 있다.

만약에 이게 없으면 어떤 메서드가 어떤 파일에 정의되어 있는지 알아야 하며 예를들어

from oa_service.pipeline import run_pipeline등을 진행해야한다.
"""
from .pipeline import (
    PipelineResult,
    get_file_path,
    run_pipeline,
    run_pipeline_to_result,
)

# 외부에서 사용해도 되는 것들을 정의한다. 나머지는 내부 구현이다.
__all__ = [
    "PipelineResult",
    "get_file_path",
    "run_pipeline",
    "run_pipeline_to_result"
]