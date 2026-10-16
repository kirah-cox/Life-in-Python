from life_python import glider, neighbors, determineCellSurvival, determineNextGeneration, simulateFutureGeneration


def test_neighbors_returns_eight_cells_without_itself():
    result = neighbors(0, 0)
    assert len(result) == 8
    assert (0, 0) not in result


def test_lone_cell_dies():
    assert determineNextGeneration([(0, 0)]) == []


def test_live_cell_survives_with_two_or_three_neighbors():
    two = [(0, 0), (1, 0), (-1, 0)]
    three = [(0, 0), (1, 0), (-1, 0), (0, 1)]
    assert determineCellSurvival(0, 0, two) is True
    assert determineCellSurvival(0, 0, three) is True


def test_live_cell_dies_from_wrong_amount_of_neighbors():
    one = [(0, 0), (1, 0)]
    four = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    assert determineCellSurvival(0, 0, one) is False
    assert determineCellSurvival(0, 0, four) is False


def test_dead_cell_survival():
    three = [(1, 0), (-1, 0), (0, 1)]
    two = [(1, 0), (-1, 0)]
    assert determineCellSurvival(0, 0, three) is True
    assert determineCellSurvival(0, 0, two) is False