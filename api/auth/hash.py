from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    """ハッシュ値生成"""
    def get_password_hash(password: str):
        """ハッシュ値生成"""
        return pwd_cxt.hash(password)

    def verify_password(hashed_password, plain_password):
        """ハッシュ値検証"""
        return pwd_cxt.verify(plain_password, hashed_password)
