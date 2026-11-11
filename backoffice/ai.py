"""The one place the back office talks to an AI model.

Always call it as:

    from backoffice import ai
    reply = ai.ask_llm(prompt)

No real model is set up yet, so on your machine ask_llm returns a demo reply. Set the
environment variable BACKOFFICE_AI=fail to make it raise RuntimeError instead, like a real model
that is down: every feature that uses AI needs a fixed fallback text for that.
Darbni's tests replace ask_llm with a fake model.
"""

import os


def ask_llm(prompt: str) -> str:
    if os.environ.get("BACKOFFICE_AI") == "fail":
        raise RuntimeError("The AI is down (BACKOFFICE_AI=fail)")
    return "[Demo AI reply] Dear customer, we are sorry. We will look into it today."
