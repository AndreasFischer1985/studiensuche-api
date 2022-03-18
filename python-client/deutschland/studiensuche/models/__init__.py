# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.studiensuche.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.studiensuche.model.response import Response
from deutschland.studiensuche.model.response_auswahl import ResponseAuswahl
from deutschland.studiensuche.model.response_facetten import ResponseFacetten
from deutschland.studiensuche.model.response_items import ResponseItems
from deutschland.studiensuche.model.response_studienangebot import (
    ResponseStudienangebot,
)
from deutschland.studiensuche.model.response_studienangebot_abschlussgrad import (
    ResponseStudienangebotAbschlussgrad,
)
from deutschland.studiensuche.model.response_studienangebot_hochschulart import (
    ResponseStudienangebotHochschulart,
)
from deutschland.studiensuche.model.response_studienangebot_region import (
    ResponseStudienangebotRegion,
)
from deutschland.studiensuche.model.response_studienangebot_studienanbieter import (
    ResponseStudienangebotStudienanbieter,
)
from deutschland.studiensuche.model.response_studienangebot_studienanbieter_logo import (
    ResponseStudienangebotStudienanbieterLogo,
)
from deutschland.studiensuche.model.response_studienangebot_studienform import (
    ResponseStudienangebotStudienform,
)
from deutschland.studiensuche.model.response_studienangebot_studienmodelle import (
    ResponseStudienangebotStudienmodelle,
)
from deutschland.studiensuche.model.response_studienangebot_studienort import (
    ResponseStudienangebotStudienort,
)
from deutschland.studiensuche.model.response_studienangebot_studienort_location import (
    ResponseStudienangebotStudienortLocation,
)
from deutschland.studiensuche.model.response_studienangebot_studientyp import (
    ResponseStudienangebotStudientyp,
)
