# -*- coding: utf-8 -*-

from .base import Base

BUFFER_HIGHLIGHT_SYNTAX = [
    {'name': 'Client', 'link': 'Comment', 're': r'(.\+)'}
]

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

    def highlight(self) -> None:
        for syn in BUFFER_HIGHLIGHT_SYNTAX:
            self.vim.command(
                'syntax match {0}_{1} /{2}/ contained containedin={0}'.format(
                    self.syntax_name, syn['name'], syn['re']))
            self.vim.command(
                'highlight default link {}_{} {}'.format(
                    self.syntax_name, syn['name'], syn['link']))

    def gather_candidates(self, context):
        projects = self.vim.call('toggl#projects')
        return [self._convert(project, context) for project in projects]

    def _convert(self, info, context):
        client_name = '({})'.format(context['__clients'][info.get('cid')]) if info.get('cid') else ''
        abbr = '{} {}'.format(info['name'], client_name)
        return {
                'word': info['name'],
                'abbr': abbr,
                'action__project': info
                }
