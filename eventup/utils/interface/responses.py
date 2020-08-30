""""Utils Response"""

# Rest Library
from rest_framework.response import Response


class CustomActions():
    def custom_response(self, response):
        status_data = response['status_code']
        response.pop('status_code')
        return Response(response, status=status_data)

    def set_response(self, status_code, message=None, data=None, status=None):
        response = {
            "status_code": status_code,
            # Fix Condition
            "status": status_code < 300,
            "message": message
        }
        if data:
            response.update({'data': data})
        if message:
            response.update({'message': message})
        return response
