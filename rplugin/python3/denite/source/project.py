# -*- coding: utf-8 -*-

from .base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'toggl/project'
        self.kind = 'toggl/project'

    def gather_candidates(self, context):
        projects = self.vim.call('toggl#projects')
        return [self._convert(project) for project in projects]

    def _convert(self, info):
        abbr = '[%d] %s' % (info['id'], info['name'])
        return {
                'word': info['name'],
                'abbr': abbr,
                'action__path': info
                }
