"""
All views related to drf_instamojo

Author: Himanshu Shankar (https://himanshus.com)
"""
from drfaddons.generics import OwnerListCreateAPIView
from rest_framework.generics import ListCreateAPIView


class ListAddPaymentRequestView(OwnerListCreateAPIView):
    """
    Creates and Lists all payment requests by current user.

    Author: Himanshu Shankar (https://himanshus.com)
    """

    from .models import PaymentRequest
    from .serializers import PaymentRequestSerializer

    serializer_class = PaymentRequestSerializer
    queryset = PaymentRequest.objects.all()


class ListAddPaymentView(ListCreateAPIView):
    """
    Creates and Lists all Payments made by current user.

    Author: Himanshu Shankar (https://himanshus.com)
    """

    from .models import Payment
    from .serializers import PaymentSerializer

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
