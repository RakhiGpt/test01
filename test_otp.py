from otp import generate_otp

def test_otp_length():
    otp = generate_otp()
    assert len(otp) ==6, "otp should be in 6 digits"

def test_otp_isdigit():
    otp = generate_otp()
    assert otp.isdigit(), "otp should contain only digits"