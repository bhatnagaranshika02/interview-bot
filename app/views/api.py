from ..services import Login, OTP
from flask import jsonify
from flask_restful import Resource, request


class OTPView(Resource):
    def get(self):
        payload = request.json

        phone = payload.get("phone")
        if not phone:
            return jsonify(
                {
                    "error": "phone number is required"
                }
            ), 400

        OTP.send_otp(phone)
        OTP.set_otp(phone, 12345)
        return {
            "success": "otp sent successfully",
            "otp": 12345
        }, 200


class LoginView(Resource):
    def post(self):
        payload = request.get_json()

        phone = int(payload["phone"])
        otp = int(payload["otp"])

        user_otp = Login.get_otp_of_user(phone)
  
        if otp == user_otp:
            return {
                "success": "Login Successful"
            }, 200

        else:
            return{
               "error": "incorrect otp, please try again"
            }, 400




