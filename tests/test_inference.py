from app.inference_utils import label_from_prob

def test_label_from_prob():
    assert label_from_prob(0.9) == "dog"
    assert label_from_prob(0.1) == "cat"
    assert label_from_prob(0.5) == "cat"
