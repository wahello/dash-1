from datetime import datetime
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def issue_token(user):
    payload = jwt_payload_handler(user)
    return {
        'token': jwt_encode_handler(payload),
        'user': user
    }


def validate_month(s):
    try:
        return datetime.strptime(s, '%Y-%m')
    except Exception:
        return None
