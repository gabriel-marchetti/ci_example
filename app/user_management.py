from typing import Dict, Optional, List
from app.db.data_access import DBInterface
from app.db.db_mock import MockDB
from app.user_model import User


_db: DBInterface = MockDB()


def set_db(db: DBInterface) -> None:
    """Replace the DB implementation used by user management."""
    global _db
    _db = db


def create_user(name: str, email: str, password: str,
                date_of_birth: str) -> Dict:
    """Create a user and return user data dict."""
    user = User(name=name, email=email, password=password,
                date_of_birth=date_of_birth)
    return _db.create(user.to_dict())


def get_user(user_id: int) -> Optional[Dict]:
    return _db.get(user_id)


def list_users() -> List[Dict]:
    return sorted(_db.list(), key=lambda user: user["email"].lower())


def delete_user(user_id: int) -> bool:
    return _db.delete(user_id)
