from domain.consolidation_engine import calculate_consolidation

def test_consolidation_with_five_equal_scores_returns_expected_value():
    # Arrange
    evidences = [
        0.80,
        0.80,
        0.80,
        0.80,
        0.80,
    ]

    weights = [3, 2, 2, 1, 1]

    # Act
    consolidation = calculate_consolidation(evidences, weights)

    # Assert
    assert abs(consolidation - 0.80) < 0.0001

def test_consolidation_with_three_scores_uses_first_three_weights():
    # Arrange
    evidences = [
        1.0,
        0.5,
        0.5,
    ]

    weights = [3, 2, 2, 1, 1]

    # Act
    consolidation = calculate_consolidation(evidences, weights)

    # Expected:
    # (1.0*3 + 0.5*2 + 0.5*2) / (3+2+2) = 5 / 7 ≈ 0.714285
    expected = 5 / 7

    # Assert
    assert abs(consolidation - expected) < 0.0001

def test_consolidation_ignores_evidences_after_five():
    # Arrange
    evidences = [
        1.0,  # peso 3
        1.0,  # peso 2
        1.0,  # peso 2
        1.0,  # peso 1
        1.0,  # peso 1
        0.0,  # debería ser ignorado
        0.0,  # debería ser ignorado
    ]

    weights = [3, 2, 2, 1, 1]

    # Act
    consolidation = calculate_consolidation(evidences, weights)

    # Expected:
    # Solo se usan los primeros 5 scores → resultado = 1.0
    expected = 1.0

    # Assert
    assert abs(consolidation - expected) < 0.0001
    
def test_consolidation_with_no_evidences_returns_zero():
    # Arrange
    evidences = []
    weights = [3, 2, 2, 1, 1]

    # Act
    consolidation = calculate_consolidation(evidences, weights)

    # Assert
    assert consolidation == 0.0
