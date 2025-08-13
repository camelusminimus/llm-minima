# llm-minima


This is just my little repository to store my work while coding along Sebastian Raschka book ["Build a Large Language Model (from scratch)"](https://www.manning.com/books/build-a-large-language-model-from-scratch). I probably will not do a one-to-one version, and also...I have a nice AMD GPU I work on, so it will be tuned to work with [ROCm](https://rocm.docs.amd.com/)....hopefully work that is.


## Preliminary Setup

I found that under [Debian 13](https://www.debian.org/releases/trixie/) installing [ROCm](https://rocm.docs.amd.com/) worked [as described in the wiki](https://wiki.debian.org/ROCm). No proprietary AMD installs needed.

### Create venv and install dependencies

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```