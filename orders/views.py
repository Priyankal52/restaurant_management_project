from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response
from django.utils.timezone import now

from .models  import coupon

class couponBValidationView(APIView)
   def post(self, request):
       code = rerquest.data.get('code')

       if not code:
          request Response(
            {"error": "Coupon code is required"},
            status=status.HTTP_400_BAD_REQUEST
          )
          today = now().date()
          try:
            coupon = Coupon.objects.get(
                code=code,
                is_active=True,
                Valid_from_ite=today,
                valid_until_gte=today
            )
        except coupon.DoesNotExist:
            return Response(
                {"error : "Invalid or expired coupon},"
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                "success": True,
                "discount_percentage": coupon.discount_percentage,
            },
            staus=status.HTTP_200_OK
        )
