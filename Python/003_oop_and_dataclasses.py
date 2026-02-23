"""
Object-Oriented Programming in Python + dataclasses.

Educational goals of this file:
1) Understand how classes define behavior and state.
2) See how inheritance helps reuse code.
3) Review method overriding/extension patterns.
4) Learn why @dataclass is useful for data-centric models.
"""

from dataclasses import dataclass


class BankAccount:
    """
    A simple bank account model.

    Teaching note:
    - A class is a "blueprint".
    - An instance is a concrete object built from that blueprint.
    """

    def __init__(self, owner: str, balance: float = 0.0):
        # Instance attributes store per-object state.
        # Every account has its own owner and balance.
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Increase the account balance by a positive amount."""
        # Defensive programming: validate inputs early.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Decrease the account balance if funds are available."""
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        # Business rule: cannot withdraw more than current balance.
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def __str__(self) -> str:
        # __str__ customizes how the object looks when printed.
        # f"{value:.2f}" formats a float to exactly 2 decimals.
        return f"{self.owner}: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    """
    Specialized account that inherits from BankAccount.

    Teaching note:
    - Inheritance means "is-a" relationship.
    - SavingsAccount *is a* BankAccount with extra behavior.
    """

    def __init__(
        self,
        owner: str,
        balance: float = 0.0,
        interest_rate: float = 0.02,
    ):
        # super().__init__(...) calls parent constructor, avoiding duplication.
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        """Apply one interest step to the current balance."""
        # Equivalent to: balance = balance + balance * rate
        self.balance += self.balance * self.interest_rate


@dataclass
class Student:
    """
    Compact model class using @dataclass.

    Why dataclass is useful in teaching and real projects:
    - Automatically generates __init__, __repr__, and comparisons (depending on options).
    - Reduces boilerplate for classes that mostly hold data.
    - Keeps focus on domain logic instead of repetitive setup code.
    """

    name: str
    age: int
    grade: float

    def is_passing(self) -> bool:
        """Return True when grade reaches the passing threshold."""
        # This method adds behavior on top of plain data fields.
        return self.grade >= 60.0


if __name__ == "__main__":
    # ------------------------------------------------------------
    # Small runnable demo section.
    # In educational repositories, a __main__ demo helps students
    # execute the file directly and observe behavior immediately.
    # ------------------------------------------------------------

    # 1) Base class usage
    account = BankAccount("Ada", 100)
    account.deposit(50)
    account.withdraw(30)
    print(account)  # Expected: Ada: 120.00

    # 2) Inherited class usage + extra method
    savings = SavingsAccount("Linus", 500, 0.05)
    savings.apply_interest()
    print(savings)  # Expected: Linus: 525.00

    # 3) Dataclass usage
    student = Student("Grace", 20, 92.5)
    print(f"{student.name} passing: {student.is_passing()}")