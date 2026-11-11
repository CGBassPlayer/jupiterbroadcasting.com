import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parents[2] / "scripts"))
import generate_pick  # noqa: E402


def form(name="Telescope", url="https://github.com/LunarKittyy/Telescope", description="Use your phone as a webcam",
         license="GPL-3.0", show="LINUX Unplugged", episode="690") -> str:
    return (
        f"### Name\n\n{name}\n\n### Pick URL\n\n{url}\n\n### Description\n\n{description}\n\n"
        f"### License\n\n{license}\n\n### Show\n\n{show}\n\n### Episode Number\n\n{episode}"
    )


def generate(tmp_path, body, number=1234):
    return generate_pick.generate(body, number, tmp_path)


def load(result):
    return yaml.safe_load(Path(result["file"]).read_text(encoding="utf-8"))


def test_writes_pick_file_matching_existing_data_format(tmp_path):
    result = generate(tmp_path, form())
    assert result["branch"] == "1234-telescope"
    assert result["title"] == "Telescope"
    assert Path(result["file"]) == tmp_path / "telescope.yaml"
    assert Path(result["file"]).read_text(encoding="utf-8").startswith("---\n")
    assert load(result) == {
        "title": "Telescope",
        "url": "https://github.com/LunarKittyy/Telescope",
        "description": "Use your phone as a webcam",
        "license": "GPL-3.0",
        "shows": [{"episode": 690, "show": "LINUX Unplugged", "slug": "linux-unplugged"}],
    }


def test_multiple_shows_get_the_same_episode(tmp_path):
    pick = load(generate(tmp_path, form(show="LINUX Unplugged, Self-Hosted", episode="12")))
    assert [(s["slug"], s["episode"]) for s in pick["shows"]] == [("linux-unplugged", 12), ("self-hosted", 12)]


def test_empty_license_is_null(tmp_path):
    assert load(generate(tmp_path, form(license="_No response_")))["license"] is None


def test_crlf_body_from_the_web_form(tmp_path):
    pick = load(generate(tmp_path, form().replace("\n", "\r\n")))
    assert pick["title"] == "Telescope"
    assert pick["shows"][0]["episode"] == 690


def test_multiline_description_is_collapsed(tmp_path):
    pick = load(generate(tmp_path, form(description="line one\n\nline two")))
    assert pick["description"] == "line one line two"


@pytest.mark.parametrize("description", [
    "key: value",
    "has 'quotes' and \"double quotes\"",
    "# not a comment",
    "- not a list",
    "--- document end",
    "{{ 7 * 7 }} ${{ secrets.GITHUB_TOKEN }} $(rm -rf /) `id`",
    "ends with colon:",
    "yes",
])
def test_hostile_description_round_trips_as_a_plain_string(tmp_path, description):
    result = generate(tmp_path, form(description=description))
    assert load(result)["description"] == description
    assert set(load(result)) == {"title", "url", "description", "license", "shows"}


@pytest.mark.parametrize("title,expected", [
    ("Shotcut - New version 24.08", "shotcut-new-version-24.08"),
    ("n.eko", "n.eko"),
    ("../../etc/passwd", "etc-passwd"),
    ("a/b\\c", "a-b-c"),
    ("savr..", "savr"),
    ("foo.lock", "foo"),
    ("Hexecute 🪄", "hexecute"),
])
def test_slug_is_a_safe_file_and_branch_name(title, expected):
    assert generate_pick.slugify(title) == expected


def test_path_traversal_title_stays_inside_picks_dir(tmp_path):
    picks = tmp_path / "picks"
    picks.mkdir()
    result = generate(picks, form(name="../../evil"))
    assert Path(result["file"]).parent == picks
    assert not (tmp_path / "evil.yaml").exists()


def test_existing_pick_gets_new_episode_without_touching_its_details(tmp_path):
    generate(tmp_path, form(name="Bore", description="original", episode="10"))
    result = generate(tmp_path, form(name="Bore", description="changed", episode="20"))
    pick = load(result)
    assert pick["description"] == "original"
    assert [s["episode"] for s in pick["shows"]] == [10, 20]


def test_existing_pick_with_string_episode_is_not_duplicated(tmp_path):
    (tmp_path / "planify.yaml").write_text(
        "---\ndescription: d\nlicense: GPL-3.0\nshows:\n- episode: '598'\n  show: LINUX Unplugged\n"
        "  slug: linux-unplugged\ntitle: planify\nurl: https://example.com\n",
        encoding="utf-8",
    )
    pick = load(generate(tmp_path, form(name="planify", episode="598")))
    assert len(pick["shows"]) == 1


@pytest.mark.parametrize("override", [
    {"name": ""},
    {"name": "!!!"},
    {"url": ""},
    {"url": "javascript:alert(1)"},
    {"url": "ftp://example.com/x"},
    {"url": "https://example.com/a b"},
    {"description": "_No response_"},
    {"show": "Not A Show"},
    {"show": "LINUX Unplugged, Not A Show"},
    {"episode": "abc"},
    {"episode": "0"},
    {"episode": "-5"},
    {"episode": "6.5"},
    {"episode": ""},
])
def test_invalid_input_is_rejected_and_writes_nothing(tmp_path, override):
    with pytest.raises(ValueError):
        generate(tmp_path, form(**override))
    assert list(tmp_path.iterdir()) == []


def test_missing_sections_are_rejected(tmp_path):
    with pytest.raises(ValueError):
        generate(tmp_path, "### Name\n\nOnly a name")


def test_main_writes_step_outputs_and_reports_errors(tmp_path, monkeypatch, capsys):
    out = tmp_path / "github_output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(out))
    monkeypatch.setenv("PICKS_DIR", str(tmp_path))
    monkeypatch.setenv("ISSUE_NUMBER", "77")
    monkeypatch.setenv("ISSUE_BODY", form())
    assert generate_pick.main() == 0
    assert out.read_text(encoding="utf-8").splitlines() == [
        f"file={tmp_path / 'telescope.yaml'}",
        "title=Telescope",
        "branch=77-telescope",
    ]

    monkeypatch.setenv("ISSUE_BODY", form(episode="nope"))
    assert generate_pick.main() == 1
    assert capsys.readouterr().out.startswith("::error::Episode Number")
