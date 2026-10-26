## CrewAI Beginner Course

- install pycharm community edition ide (if you don't have one)
- install anaconda (if you don't want to use venv)

Join my [Discord](https://discord.gg/Db6e8KkHww) community for any questions!

Use Python 3.10, 3.11 or 3.12. The course was recorded on `crewai==0.35.8` (July 2024), and `requirements.txt` pins `numpy==1.26.4`, which publishes wheels only up to Python 3.12.

To install for the beginning of the tutorial, type this in your terminal: <br>
<code>pip install crewai==0.35.8</code>

The package is `crewai`. `pip install crew` installs an unrelated AMQP library. Keep the `==0.35.8` pin: current CrewAI (1.x) is a different API, and for example rejects the `verbose=2` passed to `Crew` in `main.py` (it now takes `True`/`False`).

`pip install -r requirements.txt` and `pip install 'crewai[tools]==0.35.8'` no longer install. Both need `lancedb` 0.5.x (pinned directly in `requirements.txt`, and required as `lancedb>=0.5.4,<0.6` by every `crewai-tools` 0.4.x release), and those `lancedb` releases are no longer on PyPI; the oldest one left is 0.14.0. That affects `rag_pdf/`, which imports `crewai_tools` (it also imports `decouple`, from `pip install python-decouple`, which is not in `requirements.txt`). `main.py` and `tools-example.py` only need `crewai==0.35.8` (its dependencies include `langchain-community` and `python-dotenv`).

For current CrewAI code (CrewAI 1.15), see [tylerprogramming/ai](https://github.com/tylerprogramming/ai/tree/main/frameworks/crewai).

### I explain where to use these in the video

## Models used in this course were retired

`gpt-4` and `gpt-3.5-turbo` were shut down on 2026-10-23 ([OpenAI deprecations page](https://developers.openai.com/api/docs/deprecations)), so these files fail with `model_not_found` until you change the model name:

| File | Model in the code |
| --- | --- |
| `main.py` | `OPENAI_MODEL_NAME = "gpt-4"` |
| `.env.example` (used by `tools-example.py`) | `OPENAI_MODEL_NAME=gpt-4` |
| `rag_pdf/agents.py` | `ChatOpenAI(model_name="gpt-4", ...)` and `ChatOpenAI(model_name="gpt-3.5-turbo", ...)` |

`main - ollama - localai.py` runs `phi3:3.8b` on a local Ollama server and is not affected.

Use `gpt-5.4-mini` as the replacement in all three places. CrewAI 0.35.8 calls OpenAI through `langchain-openai` 0.1.7, which always sends `temperature` (0.7 unless you set it). `gpt-5.4-mini` defaults to reasoning effort `none`, so it accepts that. OpenAI's listed substitutes, `gpt-5.6-sol` (for `gpt-4`) and `gpt-5.6-terra` (for `gpt-3.5-turbo`), default to reasoning effort `medium`, and OpenAI's docs say to remove `temperature` whenever reasoning effort is not `none`. Those need code changes this old LangChain version does not make easy.

Price per 1M input/output tokens: `gpt-5.4-mini` $0.75 / $4.50, `gpt-5.6-terra` $2 / $12, `gpt-5.6-sol` $4 / $20.
