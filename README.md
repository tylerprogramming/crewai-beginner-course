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
