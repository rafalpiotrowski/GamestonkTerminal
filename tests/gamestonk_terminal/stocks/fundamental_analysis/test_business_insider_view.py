# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.fundamental_analysis import business_insider_view
from gamestonk_terminal import helper_funcs


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
    }


@pytest.mark.vcr
@pytest.mark.record_stdout
@pytest.mark.parametrize(
    "use_tab",
    [True, False],
)
def test_display_management(monkeypatch, use_tab):
    monkeypatch.setattr(helper_funcs.gtff, "USE_TABULATE_DF", use_tab)
    business_insider_view.display_management(ticker="TSLA", export="")
