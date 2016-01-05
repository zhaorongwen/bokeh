"""Pre-configured tile sources with urls and attribution for common 3rd-party tile services.
"""
from .models.tiles import WMTSTileSource

STAMEN_TONER = WMTSTileSource(
    url='https://stamen-tiles.a.ssl.fastly.net/toner/{Z}/{X}/{Y}.png',
    attribution=(
        'Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
        'under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>.'
        'Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, '
        'under <a href="http://www.openstreetmap.org/copyright">ODbL</a>'
    )
)


STAMEN_TONER_LABELS = WMTSTileSource(
    url='https://stamen-tiles.a.ssl.fastly.net/toner-labels/{Z}/{X}/{Y}.png',
    attribution=(
        'Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
        'under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>.'
        'Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, '
        'under <a href="http://www.openstreetmap.org/copyright">ODbL</a>'
    )
)

STAMEN_TERRAIN = WMTSTileSource(
    url='https://stamen-tiles.a.ssl.fastly.net/terrain/{Z}/{X}/{Y}.png',
    attribution=(
        'Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
        'under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. '
        'Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under '
        '<a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.'
    )
)
