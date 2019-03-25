# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import pytest

from datetime import datetime, timedelta

import llnl.util.lang
from llnl.util.lang import pretty_date, match_predicate


@pytest.fixture()
def now():
    return datetime.now()


def test_pretty_date():
    """Make sure pretty_date prints the right dates."""
    now = datetime.now()

    just_now = now - timedelta(seconds=5)
    assert pretty_date(just_now, now) == "just now"

    seconds = now - timedelta(seconds=30)
    assert pretty_date(seconds, now) == "30 seconds ago"

    a_minute = now - timedelta(seconds=60)
    assert pretty_date(a_minute, now) == "a minute ago"

    minutes = now - timedelta(seconds=1800)
    assert pretty_date(minutes, now) == "30 minutes ago"

    an_hour = now - timedelta(hours=1)
    assert pretty_date(an_hour, now) == "an hour ago"

    hours = now - timedelta(hours=2)
    assert pretty_date(hours, now) == "2 hours ago"

    yesterday = now - timedelta(days=1)
    assert pretty_date(yesterday, now) == "yesterday"

    days = now - timedelta(days=3)
    assert pretty_date(days, now) == "3 days ago"

    a_week = now - timedelta(weeks=1)
    assert pretty_date(a_week, now) == "a week ago"

    weeks = now - timedelta(weeks=2)
    assert pretty_date(weeks, now) == "2 weeks ago"

    a_month = now - timedelta(days=30)
    assert pretty_date(a_month, now) == "a month ago"

    months = now - timedelta(days=60)
    assert pretty_date(months, now) == "2 months ago"

    a_year = now - timedelta(days=365)
    assert pretty_date(a_year, now) == "a year ago"

    years = now - timedelta(days=365 * 2)
    assert pretty_date(years, now) == "2 years ago"


@pytest.mark.parametrize('delta,pretty_string', [
    (timedelta(days=1), 'a day ago'),
    (timedelta(days=1), 'yesterday'),
    (timedelta(days=1), '1 day ago'),
    (timedelta(weeks=1), '1 week ago'),
    (timedelta(weeks=3), '3 weeks ago'),
    (timedelta(days=30), '1 month ago'),
    (timedelta(days=730), '2 years  ago'),
])
def test_pretty_string_to_date_delta(now, delta, pretty_string):
    t1 = now - delta
    t2 = llnl.util.lang.pretty_string_to_date(pretty_string, now)
    assert t1 == t2


@pytest.mark.parametrize('format,pretty_string', [
    ('%Y', '2018'),
    ('%Y-%m', '2015-03'),
    ('%Y-%m-%d', '2015-03-28'),
])
def test_pretty_string_to_date(format, pretty_string):
    t1 = datetime.strptime(pretty_string, format)
    t2 = llnl.util.lang.pretty_string_to_date(pretty_string, now)
    assert t1 == t2


def test_match_predicate():
    matcher = match_predicate(lambda x: True)
    assert matcher('foo')
    assert matcher('bar')
    assert matcher('baz')

    matcher = match_predicate(['foo', 'bar'])
    assert matcher('foo')
    assert matcher('bar')
    assert not matcher('baz')

    matcher = match_predicate(r'^(foo|bar)$')
    assert matcher('foo')
    assert matcher('bar')
    assert not matcher('baz')

    with pytest.raises(ValueError):
        matcher = match_predicate(object())
        matcher('foo')