"""
003b — OOP and dataclasses (deeper dive).

This file builds on 003a and focuses on:
1) Composition ("has-a") vs Inheritance ("is-a")
2) Polymorphism: same interface, different behaviors
3) Contracts with ABCs and Protocols
4) Encapsulation with properties (enforcing invariants)
5) Dataclasses deeper: frozen/slots/default_factory/kw_only/order
6) Useful dataclasses helpers: asdict, replace, post_init

Run this file to see the demo output.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict, replace
from typing import Protocol, runtime_checkable, Iterable


# =============================================================================
# 1) Inheritance ("is-a") — when it fits well
# =============================================================================

class BankAccount:
    """
    Base account with an invariant: balance is never negative.
    Uses a property to keep the invariant safe.
    """

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = 0.0
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def __str__(self) -> str:
        return f"{self.owner}: {self.balance:.2f}"


class FeeAccount(BankAccount):
    """An account that charges a fixed fee on each withdrawal."""

    def __init__(self, owner: str, balance: float = 0.0, fee: float = 1.0):
        super().__init__(owner, balance)
        if fee < 0:
            raise ValueError("fee must be non-negative")
        self.fee = fee

    def withdraw(self, amount: float) -> None:
        # Polymorphism starts here: same method name, different behavior.
        super().withdraw(amount + self.fee)


class SavingsAccount(BankAccount):
    """An account that can apply interest."""

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        if interest_rate < 0:
            raise ValueError("interest_rate must be non-negative")
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        self._balance += self._balance * self.interest_rate


# =============================================================================
# 2) Composition ("has-a") — often better than inheritance
# =============================================================================
"""
Composition means: a class *has* another object and delegates work to it.

When it's useful:
- You want to add behavior without creating a deep inheritance tree.
- You want to combine behaviors dynamically (like LEGO bricks).
- You want a clear separation of responsibilities.

We'll model "policies" for withdrawals (fee, overdraft, etc.).
"""


class WithdrawalPolicy(ABC):
    """Contract for how withdrawals should be handled."""

    @abstractmethod
    def charge(self, account: "ComposedAccount", amount: float) -> float:
        """
        Return the total amount to subtract from the balance.
        (Could include fees, taxes, etc.)
        """
        raise NotImplementedError


class NoFeePolicy(WithdrawalPolicy):
    def charge(self, account: "ComposedAccount", amount: float) -> float:
        return amount


class FixedFeePolicy(WithdrawalPolicy):
    def __init__(self, fee: float):
        if fee < 0:
            raise ValueError("fee must be non-negative")
        self.fee = fee

    def charge(self, account: "ComposedAccount", amount: float) -> float:
        return amount + self.fee


class ComposedAccount:
    """
    A bank account that uses composition: it "has-a" policy object.

    Compared to inheritance:
    - Instead of subclassing for each variant, you swap the policy.
    """

    def __init__(self, owner: str, balance: float = 0.0, policy: WithdrawalPolicy | None = None):
        self.owner = owner
        self._balance = balance
        self.policy = policy or NoFeePolicy()

        if self._balance < 0:
            raise ValueError("Initial balance cannot be negative")

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        total = self.policy.charge(self, amount)
        if total > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= total

    def __str__(self) -> str:
        return f"{self.owner}: {self.balance:.2f} (policy={self.policy.__class__.__name__})"


# =============================================================================
# 3) Polymorphism: same interface, different behavior
# =============================================================================

def pay_bill(account: BankAccount, amount: float) -> None:
    """
    Works with any BankAccount subclass (BankAccount/FeeAccount/SavingsAccount...)
    Polymorphism: one function, many behaviors behind the same interface.
    """
    account.withdraw(amount)


def demo_polymorphism_inheritance() -> None:
    print("\n=== Polymorphism with inheritance ===")
    accounts: list[BankAccount] = [
        BankAccount("Ada", 100),
        FeeAccount("Ken", 100, fee=2),
        SavingsAccount("Grace", 100, interest_rate=0.10),
    ]

    for acc in accounts:
        pay_bill(acc, 10)
        print(acc)


# =============================================================================
# 4) Protocol: structural typing (duck typing with type checking)
# =============================================================================
"""
Protocol says: "I don't care about your class; I care about what you can do."
If you have a withdraw(amount) method, you can be used here.

This is very Pythonic: interfaces by behavior, not by explicit inheritance.
"""

@runtime_checkable
class Withdrawable(Protocol):
    def withdraw(self, amount: float) -> None: ...
    @property
    def balance(self) -> float: ...


def pay_many_bills(account: Withdrawable, bills: Iterable[float]) -> None:
    for b in bills:
        account.withdraw(b)


def demo_protocol() -> None:
    print("\n=== Protocol demo (works with different implementations) ===")
    a = BankAccount("Ada", 100)
    b = ComposedAccount("Linus", 100, policy=FixedFeePolicy(1))

    pay_many_bills(a, [5, 5])
    pay_many_bills(b, [5, 5])  # fee applies here

    print(a)
    print(b)

    # runtime_checkable lets you do isinstance checks (optional; mostly for demos)
    print("Is a Withdrawable?", isinstance(a, Withdrawable))
    print("Is b Withdrawable?", isinstance(b, Withdrawable))


# =============================================================================
# 5) Dataclasses deeper: defaults, factories, ordering, keyword-only, post_init
# =============================================================================

@dataclass(slots=True, order=True)
class Student:
    """
    order=True generates ordering methods based on field order.

    The first field(s) drive sorting. Here: grade first, so sorting groups by grade.
    Tip: You can change field order or use 'sort_index' to customize.
    """
    grade: float
    name: str
    age: int

    def __post_init__(self) -> None:
        # post_init runs after the generated __init__
        if not (0.0 <= self.grade <= 100.0):
            raise ValueError("grade must be between 0 and 100")
        if self.age < 0:
            raise ValueError("age must be non-negative")


@dataclass(slots=True, frozen=True, kw_only=True)
class Course:
    """
    frozen=True -> immutable
    kw_only=True -> forces keyword arguments for readability:
        Course(code="CS101", title="Intro", credits=6)
    """
    code: str
    title: str
    credits: int = 6


@dataclass(slots=True)
class Classroom:
    """
    default_factory avoids the classic mutable-default bug.
    """
    name: str
    course: Course
    students: list[Student] = field(default_factory=list)

    def add(self, s: Student) -> None:
        self.students.append(s)

    def average_grade(self) -> float:
        if not self.students:
            return 0.0
        return sum(s.grade for s in self.students) / len(self.students)


def demo_dataclasses_deeper() -> None:
    print("\n=== Dataclasses deeper ===")

    # order=True -> we can sort students
    students = [
        Student(grade=92.5, name="Grace", age=20),
        Student(grade=55.0, name="Ada", age=28),
        Student(grade=92.5, name="Linus", age=23),
    ]
    print("Unsorted:", students)
    print("Sorted:", sorted(students))  # by grade, then name, then age

    # frozen + kw_only
    course = Course(code="CS101", title="Intro to Python", credits=6)

    room = Classroom("Aula 1", course)
    for s in students:
        room.add(s)

    print("Avg grade:", f"{room.average_grade():.2f}")

    # asdict converts dataclass trees into dictionaries (useful for JSON)
    print("Course as dict:", asdict(course))

    # replace creates a modified copy (works best with frozen dataclasses)
    updated = replace(course, credits=9)
    print("Updated course:", updated)


# =============================================================================
# 6) One more practical example: composition to avoid subclass explosion
# =============================================================================

def demo_composition_policy_swap() -> None:
    print("\n=== Composition: swapping policies ===")
    acc = ComposedAccount("Marie", 50, policy=NoFeePolicy())
    print(acc)

    acc.withdraw(10)
    print("After withdraw with NoFeePolicy:", acc)

    # Swap behavior at runtime (no new subclass needed!)
    acc.policy = FixedFeePolicy(2)
    acc.withdraw(10)
    print("After withdraw with FixedFeePolicy:", acc)


# =============================================================================
# Main
# =============================================================================

def main() -> None:
    demo_polymorphism_inheritance()
    demo_protocol()
    demo_dataclasses_deeper()
    demo_composition_policy_swap()


if __name__ == "__main__":
    main()
