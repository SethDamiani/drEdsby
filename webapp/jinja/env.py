from jinja2.environment import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from webapp.jinja.filters import test


class JinjaEnvironment(Environment):
    def _init_(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['static'] = staticfiles_storage.url
        self.globals['reverse'] = reverse
        self.filters['test'] = test
