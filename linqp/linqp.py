# -*- coding: utf-8 -*-

#    Copyright (c) 2018 Max Biloborodko.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

__author__ = 'f1ashhimself@gmail.com'

from functools import reduce


class Linqp:

    def __init__(self, elements: list):
        self._elements = elements
        self._query = lambda x: x

    def where(self, query) -> 'Linqp':
        """
        Filter records by given query.
        """
        previous_query = self._query
        self._query = lambda elements: [e for e in previous_query(
            elements) if query(e)]
        return self

    def _invoke(self) -> list:
        """
        Do query on elements.
        """
        return self._query(self._elements)

    def select_all(self) -> list:
        """
        Select all values that pass given criteria.
        """
        return self._invoke()

    def select(self, query) -> list:
        """
        Selects queried elements.
        """
        return [query(e) for e in self._invoke()]

    def select_first(self, query) -> object:
        """
        Selects first queried element.
        """
        return query(self._invoke()[0])

    def count(self) -> int:
        """
        Gets count of queried elements.
        """
        return len(self._invoke())

    def avg(self) -> int:
        """
        Selects average of queried elements.
        """
        result = self._invoke()
        return reduce(lambda x, y: x + y, result) / float(len(result))

    def min(self) -> int:
        """
        Gets minimum value of queried elements.
        """
        return min(self._invoke())

    def max(self) -> int:
        """
        Gets maximum value of queried elements.
        """
        return max(self._invoke())
