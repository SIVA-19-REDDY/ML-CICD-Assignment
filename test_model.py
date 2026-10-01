from model import train_model


def test_model_accuracy():
    model, accuracy = train_model()

    assert model is not None
    assert accuracy >= 0.70


def test_model_exists():
    model, accuracy = train_model()

    assert model is not None
