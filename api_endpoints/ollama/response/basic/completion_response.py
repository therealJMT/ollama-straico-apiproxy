from fastapi.responses import JSONResponse


def generate_response(metadata, content=""):
    return JSONResponse(
        content={
            "model": metadata["model"],
            "created_at": "2023-08-04T19:22:45.499127Z",
            "response": content,
            "done": True,
            "total_duration": 10706818083,
            "load_duration": 6338219291,
            "prompt_eval_count": metadata["prompt_tokens"],
            "prompt_eval_duration": 130079000,
            "eval_count": metadata["total_tokens"],
            "eval_duration": 4232710000,
        }
    )


def assist_response(metadata, content="", tool_calls=None):
    message = {
        "role": "assistant",
        "content": content,
    }

    if tool_calls is not None:
        message["tool_calls"] = tool_calls

    return JSONResponse(
        content={
            "model": metadata["model"],
            "created_at": "2023-12-12T14:13:43.416799Z",
            "message": message,
            "done": True,
            "total_duration": 5191566416,
            "load_duration": 2154458,
            "prompt_eval_count": metadata["prompt_tokens"],
            "prompt_eval_duration": 383809000,
            "eval_count": metadata["total_tokens"],
            "eval_duration": 4799921000,
        }
    )
