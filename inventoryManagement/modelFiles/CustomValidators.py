from django.core.validators import RegexValidator

validate_correct_text = RegexValidator(regex='^([a-zA-Z0-9]+\s)*[a-zA-Z0-9]+$',message='The text must start with, and end with, a alphanumeric character. There should NOT be any consecutive spaces too.',code='invalid_text')

validate_deviceTag = RegexValidator(regex='^([a-zA-z])(-)((?:[a-zA-Z][a-zA-Z]+))(-)((?:[a-zA-Z][a-zA-Z]+))(-)(\d+)$',message='The device tag MUST follow the pattern <location_firstLetter>-<department>-<deviceShortName>-<intergerNumber>',code='invalid_deviceTag')