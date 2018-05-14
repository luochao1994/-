from datetime import datetime,timedelta

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from App.models import UserTicketModel


class MiddleWare(MiddlewareMixin):
    def process_request(self, request):
        ticket = request.COOKIES.get ('ticket')
        if not ticket:
            pass
        user_ticket = UserTicketModel.objects.filter(ticket=ticket)
        if user_ticket:
            if user_ticket[0].creat_time.replace (tzinfo=None) > datetime.utcnow ():
                request.user = user_ticket[0].u
            else:
                out_time=datetime.now()+timedelta(days=1)
                UserTicketModel.objects.filter(ticket=ticket,
                                               out_time=out_time).delete()