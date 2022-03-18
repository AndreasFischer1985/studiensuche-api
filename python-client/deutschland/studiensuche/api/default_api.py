"""
    Arbeitsagentur Studiensuche API

    Eine der größten Datenbanken für Studienangebote in Deutschland durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 5aee2cfe-1709-48a9-951d-eb48f8f73a74  **ClientSecret:** 3309a57a-9214-40db-9abe-28b1bb30c08c  **Achtung**: der generierte Token muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.studiensuche.api_client import ApiClient
from deutschland.studiensuche.api_client import Endpoint as _Endpoint
from deutschland.studiensuche.model.response import Response
from deutschland.studiensuche.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.studiensuche_endpoint = _Endpoint(
            settings={
                "response_type": (Response,),
                "auth": ["clientCredAuth"],
                "endpoint_path": "/pc/v1/studienangebote",
                "operation_id": "studiensuche",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "sw",
                    "sfa",
                    "sfe",
                    "orte",
                    "pg",
                    "uk",
                    "re",
                    "sfo",
                    "st",
                    "smo",
                    "abg",
                    "hsa",
                    "san",
                    "ffst",
                ],
                "required": [],
                "nullable": [],
                "enum": [
                    "uk",
                    "re",
                    "sfo",
                    "st",
                    "smo",
                    "abg",
                    "hsa",
                    "ffst",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("uk",): {
                        "BUNDESWEIT": "Bundesweit",
                        "25": "25",
                        "50": "50",
                        "100": "100",
                        "150": "150",
                        "200": "200",
                    },
                    ("re",): {
                        "BW": "BW",
                        "BY": "BY",
                        "BE": "BE",
                        "BB": "BB",
                        "HB": "HB",
                        "HH": "HH",
                        "HE": "HE",
                        "MV": "MV",
                        "NI": "NI",
                        "NW": "NW",
                        "RP": "RP",
                        "SL": "SL",
                        "SN": "SN",
                        "ST": "ST",
                        "SH": "SH",
                        "TH": "TH",
                    },
                    ("sfo",): {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5},
                    ("st",): {"0": 0, "1": 1},
                    ("smo",): {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5},
                    ("abg",): {
                        "0": 0,
                        "1": 1,
                        "2": 2,
                        "3": 3,
                        "4": 4,
                        "10": 10,
                        "12": 12,
                    },
                    ("hsa",): {
                        "101": 101,
                        "106": 106,
                        "107": 107,
                        "108": 108,
                        "113": 113,
                        "114": 114,
                    },
                    ("ffst",): {"1": 1, "2": 2},
                },
                "openapi_types": {
                    "sw": (str,),
                    "sfa": (int,),
                    "sfe": (str,),
                    "orte": (str,),
                    "pg": (int,),
                    "uk": (str,),
                    "re": (str,),
                    "sfo": (int,),
                    "st": (int,),
                    "smo": (int,),
                    "abg": (int,),
                    "hsa": (int,),
                    "san": (int,),
                    "ffst": (int,),
                },
                "attribute_map": {
                    "sw": "sw",
                    "sfa": "sfa",
                    "sfe": "sfe",
                    "orte": "orte",
                    "pg": "pg",
                    "uk": "uk",
                    "re": "re",
                    "sfo": "sfo",
                    "st": "st",
                    "smo": "smo",
                    "abg": "abg",
                    "hsa": "hsa",
                    "san": "san",
                    "ffst": "ffst",
                },
                "location_map": {
                    "sw": "query",
                    "sfa": "query",
                    "sfe": "query",
                    "orte": "query",
                    "pg": "query",
                    "uk": "query",
                    "re": "query",
                    "sfo": "query",
                    "st": "query",
                    "smo": "query",
                    "abg": "query",
                    "hsa": "query",
                    "san": "query",
                    "ffst": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def studiensuche(self, **kwargs):
        """Studiensuche  # noqa: E501

        Die Studiensuche ermöglicht, verfügbare Studienangebote mit verschiedenen GET-Parametern zu filtern. In der Regel ist dabei die Angabe mindestens eines Suchwortes (sw), Studienfeldes (sfe) oder eines Studienfachs (sfa) erforderlich. Eine Ausnahme von dieser Regel besteht beispielsweise darin, den Filter zum Studienmodell (smo) auf 5 (für Duales Studium) zu setzen.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.studiensuche(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            sw (str): Suchwort. [optional]
            sfa (int): Studienfach-ID. [optional]
            sfe (str): dkzIds einer Studienfeld(gruppe), idR. zwei Semikolon-getrennte Werte je Studienfeld(gruppe). [optional]
            orte (str): Ortsangabe nebst Postleitzahl und Koordinaten. [optional]
            pg (int): Ergebnissseite. [optional]
            uk (str): Umkreis - Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km.. [optional]
            re (str): Region/Bundesland - BW=Baden-Württemberg, BY=Bayern, BE=Berlin, BB=Brandenburg, HB=Bremen, HH=Hamburg, HE=Hessen, MV=Mecklenburg-Vorpommern, NI=Niedersachsen, NW=Nordrhei-Westfalen, RP=Rheinland-Pfalz, SL=Saarland, SN=Sachsen, ST=Sachsen-Anhalt, SH=Schleswig-Holstein, TH=Thüringen. Mehrere Komma-getrennte Angaben möglich.. [optional]
            sfo (int): Studienform - 1=Vollzeitstudium, 2=Teilzeitstudium, 3=Wochenendveranstaltung, 4=Fernstudium, 5=Selbststudium. Mehrere Semikolon-getrennte Angaben möglich.. [optional]
            st (int): Studientyp - 0=Studiengang grundständig, 1=Studiengang weiterführend.. [optional]
            smo (int): Studiengangmodell - 1=ausbildungsintegrierend, 2=berufsintegrierend, 3=berufsbegleitend, 4=praxisintegrierend, 5=Duales Studium allgemein. Mehrere Semikolon-getrennte Angaben möglich.. [optional]
            abg (int): Studiengangsabschlussgrad - 0=ohne Angabe, 1=Abschlussprüfung, 2=Bachelor, 3=Diplom, 4=Diplom(FH), 10=Master, 12=Staatsexamen. [optional]
            hsa (int): Hochschulart - 101=Berufsakademie/Duale Hochschule, 106=FH/FAW, 107=Kunst- und Musikhochschule, 108=Universität, 111=Verwaltungshochschule, 113=Private Hochschule. 114=Hochschule eigenen Typs. Mehrere Semikolon-getrennte Angaben möglich.. [optional]
            san (int): Studienanbieter-ID. [optional]
            ffst (int): Eignungstest - 1=Studiencheck, 2=OSA. Mehrere Semikolon-getrennte Angaben möglich.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.studiensuche_endpoint.call_with_http_info(**kwargs)