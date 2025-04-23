from fastapi import FastAPI
from pydantic import BaseModel
import logging
from app.llm_wrapper import LocalLLMService

app = FastAPI()
logging.basicConfig(level=logging.INFO)

model_path = "app/model/Meta-Llama-3-8B-Instruct.Q4_0.gguf"
llm_service = LocalLLMService(model_path=model_path)

class CleanRequest(BaseModel):
    text: str

class CleanResponse(BaseModel):
    cleaned_text: str

@app.post("/clean", response_model=CleanResponse)
def clean_text(request: CleanRequest):
    logging.info(f"Received /clean request: {request.text}")
    cleaned_text = llm_service.clean_text(request.text)
    logging.info(f"Returning cleaned text: {cleaned_text}")
    return {"cleaned_text": cleaned_text}
