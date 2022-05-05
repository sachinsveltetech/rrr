from django.core.validators import RegexValidator

mobile_regex_validator=RegexValidator(regex=r"^[6-9]\d{9}$",message="Invalid phone number")

ip_regex_validator=RegexValidator(regex=r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b',message="Invalid ip address")