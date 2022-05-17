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
from deutschland.studiensuche.model.response_facetten_inner import ResponseFacettenInner
from deutschland.studiensuche.model.response_facetten_inner_auswahl_inner import (
    ResponseFacettenInnerAuswahlInner,
)
from deutschland.studiensuche.model.response_items_inner import ResponseItemsInner
from deutschland.studiensuche.model.response_items_inner_studienangebot import (
    ResponseItemsInnerStudienangebot,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_abschlussgrad import (
    ResponseItemsInnerStudienangebotAbschlussgrad,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_hochschulart import (
    ResponseItemsInnerStudienangebotHochschulart,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_region import (
    ResponseItemsInnerStudienangebotRegion,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_studienanbieter import (
    ResponseItemsInnerStudienangebotStudienanbieter,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_studienanbieter_logo import (
    ResponseItemsInnerStudienangebotStudienanbieterLogo,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_studienform import (
    ResponseItemsInnerStudienangebotStudienform,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_studienmodelle_inner import (
    ResponseItemsInnerStudienangebotStudienmodelleInner,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_studienort import (
    ResponseItemsInnerStudienangebotStudienort,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_studienort_location import (
    ResponseItemsInnerStudienangebotStudienortLocation,
)
from deutschland.studiensuche.model.response_items_inner_studienangebot_studientyp import (
    ResponseItemsInnerStudienangebotStudientyp,
)
