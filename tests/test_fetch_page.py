import pytest

import fetch_page


class TestFetchSearchPage:
    @pytest.mark.skip
    def test_load_start_page(self):
        start_page = fetch_page.load_start_page()
        assert "Select a location" in start_page.page_source
        start_page.close()

    @pytest.mark.skip
    def test_load_search_page(self):
        search_page = fetch_page.load_search_page()
        assert "Selector for the case search type" in search_page.page_source
        search_page.close()

    def test_query_case_id(self):
        result_page = fetch_page.query_case_id("J1-CV-20-001590")
        assert "04/27/2020" in result_page.page_source