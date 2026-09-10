from src.loader import DataLoader


def test_load_json():
    """Test loading a JSON file."""

    loader = DataLoader()
    data = loader.load("data/sample.json")

    assert isinstance(data, list)
    assert len(data) > 0