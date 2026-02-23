"""
OOP in Python + dataclasses — a practical, readable summary.

Educational goals:
1) Understand how classes define state (attributes) and behavior (methods).
2) Use encapsulation: keep invariants true (e.g., balance >= 0).
3) See inheritance and method overriding with super().
4) Learn common OOP tools: classmethod, staticmethod, properties.
5) Use @dataclass for data-centric models (less boilerplate, more clarity).

Tip:
- This file is runnable: execute it to see the demo outputs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar


# =============================================================================
# 1) A basic class: state + behavior + invariants
# =============================================================================

class BankAccount:
    """
    A simple bank account model.

    Key ideas:
    - Instances hold per-object state (owner, balance).
    - Methods operate on that state.
    - Invariants: rules that should always hold true (e.g., balance >= 0).

    Note on "encapsulation":
    - Python doesn't enforce private fields strongly, but conventions matter.
    - A leading underscore (e.g., _balance) means "internal use".
    """

    # Class attribute (shared by all instances)
    bank_name: ClassVar[str] = "Example Bank"

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = 0.0  # internal storage
        self.deposit(balance) if balance > 0 else None  # reuse validation logic

    @property
    def balance(self) -> float:
        """Read-only public view of the balance (use deposit/withdraw to change it)."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Increase balance by a positive amount."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Decrease balance by a positive amount if funds are available."""
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __str__(self) -> str:
        return f"{self.owner}: {self._balance:.2f}"

    def __repr__(self) -> str:
        # repr is meant for developers/debugging
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"

    @classmethod
    def with_bonus(cls, owner: str, initial: float, bonus: float) -> "BankAccount":
        """
        Alternative constructor.

        Why classmethod:
        - It receives the class (cls), so it works well with inheritance.
        - Subclasses calling it will build the subclass type.
        """
        account = cls(owner, initial)
        account.deposit(bonus)
        return account

    @staticmethod
    def is_valid_owner(name: str) -> bool:
        """
        Static utility: logically related to BankAccount but doesn't need self/cls.
        """
        return bool(name.strip())


# =============================================================================
# 2) Inheritance: "is-a" relationship + extension
# =============================================================================

class SavingsAccount(BankAccount):
    """
    SavingsAccount is-a BankAccount with interest.

    - Inherits: owner, balance, deposit, withdraw, etc.
    - Adds: interest_rate + apply_interest().
    """

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        if interest_rate < 0:
            raise ValueError("interest_rate must be non-negative")
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        """Apply one interest step to current balance."""
        self._balance += self._balance * self.interest_rate

    def __str__(self) -> str:
        # Overriding: customize string representation, but reuse base formatting
        base = super().__str__()
        return f"{base} (savings @ {self.interest_rate:.2%})"


# =============================================================================
# 3) Overriding patterns: extend behavior with super()
# =============================================================================

class FeeAccount(BankAccount):
    """
    Example of overriding a method to extend behavior.
    Each withdraw has a fixed fee.
    """

    def __init__(self, owner: str, balance: float = 0.0, fee: float = 1.0):
        super().__init__(owner, balance)
        if fee < 0:
            raise ValueError("fee must be non-negative")
        self.fee = fee

    def withdraw(self, amount: float) -> None:
        """
        Override: total cost is amount + fee.
        We still reuse parent's validation and logic via super().
        """
        super().withdraw(amount + self.fee)


# =============================================================================
# 4) Dataclasses: best for data-centric models
# =============================================================================

@dataclass(slots=True)
class Student:
    """
    A compact model class using @dataclass.

    Why dataclass:
    - Auto-generates __init__, __repr__, __eq__ (and more options).
    - Makes it obvious the class is mainly "data + small behavior".
    - Great for DTOs, domain models, configuration objects, etc.

    slots=True:
    - Memory-friendly and prevents adding new attributes at runtime.
      (good for teaching "this is the schema")
    """

    name: str
    age: int
    grade: float

    def is_passing(self, threshold: float = 60.0) -> bool:
        return self.grade >= threshold


@dataclass(frozen=True, slots=True)
class Course:
    """
    frozen=True makes instances immutable (like a tuple with names).
    Useful when you want objects you can safely share without accidental changes.
    """
    code: str
    title: str


@dataclass(slots=True)
class Classroom:
    """
    Example of default_factory for mutable defaults.
    DO NOT use students: list[Student] = []  (shared list bug!)
    """
    name: str
    course: Course
    students: list[Student] = field(default_factory=list)

    def add_student(self, s: Student) -> None:
        self.students.append(s)

    def average_grade(self) -> float:
        if not self.students:
            return 0.0
        return sum(s.grade for s in self.students) / len(self.students)


# =============================================================================
# 5) Common gotchas (quick notes)
# =============================================================================
"""
Gotchas:
- Avoid mutable default arguments in normal functions and dataclasses:
    def f(x=[]): ...  # BAD
  Use None + create a new list, or dataclasses.field(default_factory=list).

- Inheritance is not always the best tool:
  sometimes composition ("has-a") is better than inheritance ("is-a").

- Prefer calling super() in overridden methods when you want to extend
  parent behavior rather than rewrite it entirely.
"""


# =============================================================================
# Demo
# =============================================================================

def main() -> None:
    print("=== BankAccount ===")
    account = BankAccount("Ada", 100)
    account.deposit(50)
    account.withdraw(30)
    print(account)          # Ada: 120.00
    print(repr(account))    # debug-friendly

    print("\n=== Alternative constructor + staticmethod ===")
    if BankAccount.is_valid_owner("  Linus  "):
        promo = BankAccount.with_bonus("Linus", initial=200, bonus=25)
        print(promo)        # Linus: 225.00

    print("\n=== SavingsAccount (inheritance) ===")
    savings = SavingsAccount("Grace", 500, interest_rate=0.05)
    savings.apply_interest()
    print(savings)          # Grace: 525.00 (savings @ 5.00%)

    print("\n=== FeeAccount (overriding + super) ===")
    fee_acc = FeeAccount("Ken", 100, fee=2)
    fee_acc.withdraw(10)    # withdraw 12 total
    print(fee_acc)          # Ken: 88.00

    print("\n=== Dataclasses ===")
    student = Student("Grace", 20, 92.5)
    print(student)          # Student(name='Grace', age=20, grade=92.5)
    print(f"{student.name} passing: {student.is_passing()}")

    course = Course("CS101", "Intro to Python")   # immutable (frozen=True)
    room = Classroom("Aula 1", course)
    room.add_student(student)
    room.add_student(Student("Ada", 28, 55.0))
    print(f"Class avg: {room.average_grade():.2f}")


if __name__ == "__main__":
    main()
