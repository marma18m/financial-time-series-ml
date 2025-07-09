# financial-time-series-ml

TODO: redactar readme

### Starting Jupyter Lab

_TL;DR Run `make up` and navigate to the URL displayed in the logs._

We recommend to use [pyenv](https://github.com/pyenv/pyenv) along with [direnv](https://github.com/direnv/direnv/wiki/Python#pyenv) to manage different versions of Python. There's a `.python-version` file indicating the version we have tested the notebooks with. Also, all required packages are defined in `requirements.txt`, you may want to run the usual `pip install -r requirements.txt` to install them.

In case you want to [run Jupyter Lab using Docker](https://jupyter-docker-stacks.readthedocs.io/en/latest), this is a good starting point:

```bash
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter/scipy-notebook
```

There is more information about the different Jupyter stacks [here](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html). If you want to install packages inside, you could either access to the container and run `pip install` or [use a custom `Dockerfile` for this](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#using-mamba-install-or-pip-install-in-a-child-docker-image). We have done some work for you, running `make up` in this repository will bring JupyterLab up.
