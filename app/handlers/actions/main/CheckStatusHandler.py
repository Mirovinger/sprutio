from tornado import web
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch

from core import FM


class CheckStatusHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        status = self.get_post('status')
        session = self.get_post('session')

        if status is None:
            self.json({
                'error': True,
                'message': 'no status provided'
            })
            self.finish()
            return

        if session is None:
            self.json({
                'error': True,
                'message': 'no session provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.CHECK_STATUS, module=session['type'],
                                 status=status, session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
