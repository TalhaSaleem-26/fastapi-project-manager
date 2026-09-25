from app.core.security import hash_password, verify_password


def test_password_hashing():
    password = "Test12345"

    hashed = hash_password(password)

    assert hashed != password 
    assert verify_password(password, hashed) is True
    
    

    
    