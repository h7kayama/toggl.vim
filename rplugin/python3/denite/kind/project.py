# -*- coding: utf-8 -*-

from .base import Base

class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'toggl/project'
        self.default_action = 'set_current'

    def action_set_current(self, context):
        for target in context['targets']:
            project = target['action__project']
            self.vim.call('toggl#update_current', {'pid': project['id']})
