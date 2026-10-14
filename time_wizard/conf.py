from django.conf import settings


def get_time_wizard_countries():
    from holidays.utils import list_supported_countries

    country_provinces = list_supported_countries(include_aliases=False)
    countries = sorted(country_provinces.keys())
    return getattr(settings, 'TIME_WIZARD_COUNTRIES', countries)


def get_time_wizard_country_provinces():
    from holidays.utils import list_supported_countries

    country_provinces = list_supported_countries(include_aliases=False)
    return getattr(settings, 'TIME_WIZARD_COUNTRY_PROVINCES', country_provinces)
