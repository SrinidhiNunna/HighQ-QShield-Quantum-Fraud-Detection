from qiskit.circuit.library import ZZFeatureMap

def build_feature_map(num_features=4):

    feature_map = ZZFeatureMap(
        feature_dimension=num_features,
        reps=2
    )

    return feature_map