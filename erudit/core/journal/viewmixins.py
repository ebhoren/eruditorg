# -*- coding: utf-8 -*-

from django.db.models import Q
from django.http import Http404
from django.utils.functional import cached_property

from ipware.ip import get_ip

from core.subscription.models import InstitutionIPAddressRange
from core.subscription.models import JournalAccessSubscription
from erudit.models import Journal


class JournalCodeDetailMixin(object):
    """
    Simply allows retrieving a Journal instance using its code.
    """
    def get_journal(self):
        try:
            return Journal.objects.get(code=self.kwargs['code'])
        except Journal.DoesNotExist:
            raise Http404

    def get_object(self, queryset=None):
        return self.get_journal()

    @cached_property
    def journal(self):
        return self.get_journal()


class ArticleAccessCheckMixin(object):
    """
    Defines a way to check whether the current user can browse a
    given Érudit article.
    """
    def get_article(self):
        """ Returns the considered article.

        By default the method will try to fetch the article using the
        :meth:`get_object<django:django.views.generic.detail.SingleObjectMixin.get_object>` method.
        But subclasses can override this to control the way the article is retrieved.
        """
        return self.get_object()

    def get_context_data(self, **kwargs):
        """ Inserts a flag indicating if the article can be accessed in the context. """
        context = super(ArticleAccessCheckMixin, self).get_context_data(**kwargs)
        context['article_access_granted'] = self.has_access()
        return context

    def has_access(self):
        """ Returns a boolean indicating if the article can be accessed.

        The following verifications are performed in order to determine if an article
        can be browsed:

            1- it is in open access
            2- the current user has access to it with its individual account
            3- the current IP address is inside on of the IP address ranges allowed
               to access to it
        """
        article = self.get_article()

        # 1- Is the article in open access?
        if article.open_access:
            return True

        # 2- Is the current user allowed to access the article?
        if not self.request.user.is_anonymous():
            individual_subscriptions = JournalAccessSubscription.objects.filter(
                Q(full_access=True) |
                Q(journal=article.issue.journal) |
                Q(journals__id=article.issue.journal_id),
                user=self.request.user,
            )
            if individual_subscriptions.exists():
                return True

        # 3- Is the current IP address allowed to access the article as an institution?
        ip = get_ip(self.request)
        institutional_subscriptions = JournalAccessSubscription.objects.filter(
            Q(full_access=True) |
            Q(journal=article.issue.journal) |
            Q(journals__id=article.issue.journal_id),
            organisation__isnull=False)
        institutional_access = institutional_subscriptions.exists() and \
            InstitutionIPAddressRange.objects.filter(
                subscription__in=institutional_subscriptions,
                ip_start__lte=ip, ip_end__gte=ip).exists()
        if institutional_access:
            return True

        return False
