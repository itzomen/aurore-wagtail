from rest_framework.response import Response
from rest_framework.views import APIView

from aurore.apps.api.exception_handlers import (
    drf_default_with_modifications_exception_handler,
    hacksoft_proposed_exception_handler,
)
from aurore.apps.errors.services import trigger_errors
from aurore.apps.users.services import user_create


class TriggerErrorApi(APIView):
    def get(self, request):
        data = {
            "drf_default_with_modifications": trigger_errors(
                drf_default_with_modifications_exception_handler
            ),
            "hacksoft_proposed": trigger_errors(hacksoft_proposed_exception_handler),
        }

        return Response(data)


class TriggerValidateUniqueErrorApi(APIView):
    def get(self, request):
        # Due to the fiddling with transactions, this example a different API
        user_create(email="unique@domain.io", password="user")
        user_create(email="unique@domain.io", password="user")

        return Response()


class TriggerUnhandledExceptionApi(APIView):
    def get(self, request):
        raise Exception("Oops")

        return Response()
