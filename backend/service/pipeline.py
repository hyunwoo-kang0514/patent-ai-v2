from __future__ import annotations
from typing import Any
from fastapi import UploadFile
from dataclasses import dataclass
from config import Config
from openai import OpenAI


@dataclass
class PipelineResult:
    pass

def save_upload_to_temp(upload_file: Any, suffix: str):
    """
    Fast API 업러드 파일을 임시 파일로 저장후 Path 반환
    파이프라인에 전달하기 전에 호출

    Args:
        upload_file: FastAPI multipart/form-data에서 받은 UploadFile.
            .file.read()로 바이트를 읽을 수 있는 객체.
        suffix -> .pdf

    Returns:
        Path: 저장된 임시 파일이 절대 경로 (Path 객체).


    Raises:
        Exception: 파일 읽기/쓰기 실패시 만듬
    """
    fd, path = tempfile.mkstemp 



def run_pipeline(oa_file: UploadFile,  claims_file: UploadFile, spec_file: Any, examiner_override: str, app_override: str) -> PipelineResult:
    """
    This is a pipeline that create and implement OA first response + pattern report + stress test.
    """
    examiner_raw = ""
    examiner_canon = ""
    oa_app_no = ""
    oa_file_id = ""
    claims_file_id = ""
    spec_file_id = ""
    client = None

    """
    사용자가 OA 파일을 업로드 하면 
    -> 서버가 그 내용을 읽는다
    -> 서버의 임시 폴더에 PDF로 저장한다
    -> 그 임시 파일의 위치를 서버내의 Path 객체로 변환한다. 
    """

    try: 
        # get configurations
        cfg = Config.from_sources()
        # client
        client = OpenAI(api_key=cfg.openai_api_key)
        # get paht






