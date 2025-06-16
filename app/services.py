from app.config.redis import redis_obj


class Login:
    @staticmethod
    def get_otp_of_user(phone):
       user_otp =  redis_obj.hget(f"USER:{phone}", "otp")
       return int(user_otp)

class OTP:
    @staticmethod
    def send_otp(phone):
        pass

    @staticmethod
    def set_otp(phone, otp):
        redis_obj.hset(f"USER:{phone}", "otp", otp)

