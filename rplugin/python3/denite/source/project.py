# -*- coding: utf-8 -*-

from .base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'toggl/project'
        self.kind = 'toggl/project'

    def on_init(self, context):
        clients = self.vim.call('toggl#clients')
        client_ids = map(lambda c: c['id'], clients)
        client_names = map(lambda c: c['name'], clients)
        context['__clients'] = dict(zip(client_ids, client_names))

    def gather_candidates(self, context):
        projects = self.vim.call('toggl#projects')
        return [self._convert(project, context) for project in projects]

    def _convert(self, info, context):
        client_name = context['__clients'][info.get('cid')] if info.get('cid') else ''
        abbr = '%s %s' % (info['name'], client_name)
        return {
                'word': info['name'],
                'abbr': abbr,
                'action__project': info
                }
