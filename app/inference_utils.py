def label_from_prob(prob_dog: float, threshold: float = 0.5) -> str:
    return "dog" if prob_dog > threshold else "cat"
