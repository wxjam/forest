import pytest
import forest


@pytest.mark.parametrize("data,expected", [
        ({}, []),
        ({"datasets": []}, []),
        ({"datasets": [
            {
                "label": "Label",
                "driver": {
                    "name": "rdt",
                    "settings": {
                        "pattern": "/some/*.nc"
                    }
                }
            }
            ]}, [
                ("Label", ("rdt", {"pattern": "/some/*.nc"}))
        ]),
    ])
def test_specs(data, expected):
    actual = forest.config.specs(data)
    assert actual == expected


def test_dataset_spec():
    driver_spec = forest.config.DriverSpec("name")
    spec = forest.config.DatasetSpec("label", driver_spec)
    assert spec.label == "label"
    assert spec.driver.name == "name"
    assert spec.driver.settings == {}


def test_driver_spec():
    driver_name = "intake"
    spec = forest.config.DriverSpec(driver_name)
    assert spec.name == driver_name
    assert spec.settings == {}