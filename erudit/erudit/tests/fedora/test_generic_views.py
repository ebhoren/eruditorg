# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.test import RequestFactory

from erudit.fedora.objects import JournalDigitalObject
from erudit.fedora.views.generic import FedoraFileDatastreamView
from erudit.models import Journal
from erudit.tests import BaseEruditTestCase


class TestFedoraFileDatastreamView(BaseEruditTestCase):
    def setUp(self):
        super(TestFedoraFileDatastreamView, self).setUp()
        self.factory = RequestFactory()

    def test_raises_if_the_fedora_object_class_is_not_defined(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            pass

        request = self.factory.get('/')

        # Run & check
        with self.assertRaises(ImproperlyConfigured):
            MyView.as_view()(request)

    def test_raises_if_the_django_object_can_not_be_retrieved(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            fedora_object_class = JournalDigitalObject

        request = self.factory.get('/')

        # Run & check
        with self.assertRaises(ImproperlyConfigured):
            MyView.as_view()(request)

    def test_raises_if_the_content_type_is_not_defined(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            fedora_object_class = JournalDigitalObject
            model = Journal

        request = self.factory.get('/')

        # Run & check
        with self.assertRaises(ImproperlyConfigured):
            MyView.as_view()(request, pk=self.journal.pk)

    def test_raises_if_the_datastream_name_is_not_defined(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            content_type = 'image/jpeg'
            fedora_object_class = JournalDigitalObject
            model = Journal

        request = self.factory.get('/')

        # Run & check
        with self.assertRaises(ImproperlyConfigured):
            MyView.as_view()(request, pk=self.journal.pk)

    def test_raises_if_the_datastream_is_not_defined_on_the_digital_object(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            content_type = 'image/jpeg'
            datastream_name = 'dummy'
            fedora_object_class = JournalDigitalObject
            model = Journal

        request = self.factory.get('/')

        # Run & check
        with self.assertRaises(ImproperlyConfigured):
            MyView.as_view()(request, pk=self.journal.pk)

    def test_raises_if_the_datastream_does_not_have_content(self):
        # Setup
        class Dummy(object):
            logo = 'dummy'

        class MyView(FedoraFileDatastreamView):
            content_type = 'image/jpeg'
            datastream_name = 'logo'
            fedora_object_class = JournalDigitalObject
            model = Journal

            def get_fedora_object(self):
                return Dummy()

        request = self.factory.get('/')

        # Run & check
        with self.assertRaises(ImproperlyConfigured):
            MyView.as_view()(request, pk=self.journal.pk)

    def test_can_return_the_fedora_pid(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            fedora_object_class = JournalDigitalObject
            model = Journal

        view = MyView()
        view.kwargs = {'pk': self.journal.pk}

        # Run & check
        pid = view.get_fedora_object_pid()
        self.assertEqual(pid, self.journal.pid)

    def test_raises_http_404_if_the_datastream_cannot_be_retrieved(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            content_type = 'image/jpeg'
            datastream_name = 'logo'
            fedora_object_class = JournalDigitalObject
            model = Journal

        request = self.factory.get('/')

        # Run & check
        with self.assertRaises(Http404):
            MyView.as_view()(request, pk=self.journal.pk)

    def test_generates_a_response_with_the_appropriate_content_type(self):
        # Setup
        class MyView(FedoraFileDatastreamView):
            content_type = 'image/jpeg'
            datastream_name = 'logo'
            fedora_object_class = JournalDigitalObject
            model = Journal

            def get_datastream_content(self, fedora_object):
                return 'dummy'

        request = self.factory.get('/')

        # Run & check
        response = MyView.as_view()(request, pk=self.journal.pk)
        self.assertEqual(response['Content-Type'], 'image/jpeg')
