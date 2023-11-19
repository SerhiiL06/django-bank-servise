from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class CardNumberValidator(RegexValidator):
    message = "the card number must be have a 16 digit's"
    regex = "^[\d{4}-/d{4}-/d{4}-/d{4}$]"


@deconstructible
class DateValidator(RegexValidator):
    regex = r"^(0[1-9]|1[0-2])/(2[2-3]|[3-9][0-9])$"
