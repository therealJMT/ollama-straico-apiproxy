from fastapi.responses import JSONResponse

def assist_response(metadata, content=None):
    return JSONResponse(
        content={
            "model": metadata["model"],
            "created_at": "2023-12-12T14:13:43.416799Z",
            "message": {"role": "assistant", "content": content},
            "done": True,
            "total_duration": 5191566416,
            "load_duration": 2154458,
            "prompt_eval_count": metadata["prompt_tokens"],
            "prompt_eval_duration": 383809000,
            "eval_count": metadata["total_tokens"],
            "eval_duration": 4799921000,
        }
    )