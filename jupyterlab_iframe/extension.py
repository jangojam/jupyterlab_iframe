from notebook.base.handlers import IPythonHandler


class IFrameHandler(IPythonHandler):
    def initialize(self, iframes=None):
        self.iframes = iframes

    def get(self):
        self.finish(self.iframes)


def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    iframes = nb_server_app.config.get('JupyterLabIFrame', {}).get('iframes', [])
    host_pattern = '.*$'
    print('Installing jupyterlab_iframe handler on path %s' % '/iframes')
    print('Handinling iframes: %s' % iframes)
    web_app.add_handlers(host_pattern, [('/iframes', IFrameHandler, {'iframes': iframes})])
