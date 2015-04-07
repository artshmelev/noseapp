# -*- coding: utf-8 -*-

import logging

from noseapp.suite.mediator import TestCaseMediator


logger = logging.getLogger(__name__)


class Suite(object):
    """
    Base Suite class for group or one TestCase.

    Usage DEFAULT_REQUIRE property for default extensions require.
    """

    mediator_class = TestCaseMediator

    def __init__(self, name, require=None):
        """
        :param name: suite name
        :type name: str
        :param require: extension names list
        :type require: list
        """
        self._name = name

        if hasattr(self, 'DEFAULT_REQUIRE'):
            self._require = self.DEFAULT_REQUIRE + (require or [])
        else:
            self._require = require

        self._mediator = self.mediator_class(require=self._require)

    @property
    def name(self):
        return self._name

    @property
    def require(self):
        return self._require

    def register(self, cls):
        """
        Add test case class

        :type cls: noseapp.case.TestCase
        """
        logger.debug('Registering test case "{}" in {} '.format(cls.__name__, repr(self)))

        self._mediator.add_test_case(cls)
        return cls

    def get_map(self):
        return self._mediator.create_map()

    def init_extensions(self):
        """
        Init extensions for test cases. Without building suite.
        """
        for case in self._mediator.test_cases:
            case.with_require(self._require)

    def __call__(self, nose_config, test_loader, class_factory):
        """
        Build suite
        """
        logging.debug('Building {}'.format(repr(self)))

        return self._mediator.create_suite(
            nose_config, test_loader, class_factory,
        )

    def __repr__(self):
        return '<Suite {}>'.format(self._name)
