from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: Hard difficulty range was smaller than Normal (1-50 vs 1-100) ---

def test_hard_range_wider_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, "Hard difficulty should have a wider range than Normal"

def test_hard_range_value():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 500


# --- Bug 3: Hint messages were flipped (too high said "Go HIGHER", too low said "Go LOWER") ---

def test_too_high_hint_says_go_lower():
    outcome, message = check_guess(90, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'Go LOWER' hint when guess is too high, got: {message}"

def test_too_low_hint_says_go_higher():
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'Go HIGHER' hint when guess is too low, got: {message}"
