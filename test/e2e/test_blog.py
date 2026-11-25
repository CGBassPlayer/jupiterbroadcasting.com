import re

from playwright.sync_api import APIRequestContext

HEADER = "/images/blog/texas-cyber-summit-2019/qb8egVZ1.jpg"


def test_blog_chips_differ_per_show(api_request_context: APIRequestContext):
    """
    Each show's chip on /blog/ has its own color class, so cards read apart at a glance
    """
    response = api_request_context.get("/blog/")
    assert response.ok, f"/blog/ returned {response.status}"
    chips = dict(re.findall(r'<span class="tag (is-[\w-]+) mb-2">([^<]+)</span>', response.text()))
    by_show = {show: cls for cls, show in chips.items()}
    assert {"LINUX Unplugged", "Jupiter EXTRAS"} <= by_show.keys(), by_show
    assert by_show["LINUX Unplugged"] != by_show["Jupiter EXTRAS"]


def test_header_image_not_repeated_in_body(api_request_context: APIRequestContext):
    """
    A header_image that the article body already shows isn't rendered a second time above it
    """
    response = api_request_context.get("/blog/texas-cyber-summit-2019/")
    assert response.ok, f"article returned {response.status}"
    assert response.text().count(f'src="{HEADER}"') == 1
