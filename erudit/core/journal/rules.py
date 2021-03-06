# -*- coding: utf-8 -*-

import rules
from rules.predicates import is_authenticated
from rules.predicates import is_staff
from rules.predicates import is_superuser

from .rules_helpers import get_editable_journals


@rules.predicate
def can_edit_journal(user, journal=None):
    # TODO: add proper permissions checks
    if journal is None:
        return bool(get_editable_journals(user).count())
    else:
        return bool(journal.members.filter(id=user.id).count())


rules.add_perm('journal.edit_journal',
               is_authenticated & (is_superuser | is_staff | can_edit_journal))
