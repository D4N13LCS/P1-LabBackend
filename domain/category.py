import uuid
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime

from events.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated,
)

MAX_NAME = 255


@dataclass
class Category:
    """
    Entidade Category (sem Framework)
    - name (obrigatório) <= 255
    - id, description, is_active (opcionais)
    - is_active default = True
    - gera o id automaticamente (uuid4) se não for informado
    - permite update(name/description) e ativar/desativar
    - registra eventos de domínio
    """
    name: str
    description: str = ""
    is_active: bool = True
    id: Optional[str] = field(default=None)
    events: List[object] = field(default_factory=list, init=False, repr=False)

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())

        self.name = self._validate_name(self.name)
        self.description = self.description or ""
        self.is_active = bool(self.is_active)

        # Evento de criação
        self.events.append(CategoryCreated(self.id, self.name, self.description, self.is_active))

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise ValueError("name deve ser string")
        n = name.strip()
        if not n:
            raise ValueError("name é obrigatório")
        if len(n) > MAX_NAME:
            raise ValueError(f"name deve ter no máximo {MAX_NAME} caracteres")
        return n

    # Serialização
    def to_dict(self) -> dict:
        return {
            "class_name": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Category":
        return cls(
            id=data.get("id"),
            name=data["name"],
            description=data.get("description", ""),
            is_active=data.get("is_active", True),
        )

    
    # Comportamentos
    def update(self, *, name: Optional[str] = None, description: Optional[str] = None) -> None:
        updated_fields = {}
        if name is not None:
            self.name = self._validate_name(name)
            updated_fields["name"] = self.name
        if description is not None:
            self.description = description
            updated_fields["description"] = self.description

        if updated_fields:
            self.events.append(CategoryUpdated(self.id, updated_fields))

    def activate(self) -> None:
        self.is_active = True
        self.events.append(CategoryActivated(self.id))

    def deactivate(self) -> None:
        self.is_active = False
        self.events.append(CategoryDeactivated(self.id))

    
    # Logs e Depuração
    def __str__(self) -> str:
        return f"{self.name} | {self.description} ({self.is_active})"

    def __repr__(self) -> str:
        return f"<Category {self.name} ({self.id})>"
