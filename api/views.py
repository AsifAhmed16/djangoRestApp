import re
import base64
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


class RequestController(APIView):

    @csrf_exempt
    def post(self, request):
        res = {}
        try:
            request_id = self.request.data.get('requestId')
            name_encode = self.request.data.get('accountName')
            amount_encode = self.request.data.get('amount')

            # Step 1: Decode name
            name_decode = base64.b64decode(name_encode).decode("utf-8")
            print(name_decode)

            # Step 2: Decode amount
            amount = base64.b64decode(amount_encode).decode("utf-8")
            print(amount)

            # Step 3: Removing special characters from amount
            amount_with_no_special_chars = re.sub(r"[^a-zA-Z0-9]", "", amount)
            print(amount_with_no_special_chars)

            # Step 4: Capitalizing chars of the amount
            amount_capitalize = amount_with_no_special_chars.upper()
            print(amount_capitalize)

            # Step 5: Convert Romanian number to decimal
            sym_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
            amount_decode = 0
            for each in amount_capitalize:
                if each in sym_dict.keys():
                    amount_decode += sym_dict[each]
            print(amount_decode)

            res = {
                "requestId": request_id,
                "accountName": name_decode,
                "amount": amount_decode
            }
        except Exception as exc:
            print(exc)
        return Response(res, status=status.HTTP_200_OK)
