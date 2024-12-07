Here's a simple **Prolog** program demonstrating its declarative nature and logical inference capabilities. This example defines a family tree and answers questions about relationships.

### **Prolog Family Tree Example**

```prolog
% Facts
parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).
parent(mary, alice).
parent(mary, bob).
parent(tom, james).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Gender facts
male(john).
male(tom).
male(bob).
male(james).
female(susan).
female(mary).
female(alice).

% Query examples
% ?- father(john, mary).     % Is John the father of Mary? (yes)
% ?- sibling(mary, tom).     % Are Mary and Tom siblings? (yes)
% ?- grandparent(john, alice). % Is John the grandparent of Alice? (yes)
% ?- grandparent(susan, james). % Is Susan the grandparent of James? (yes)
% ?- mother(mary, X).        % Who is the mother of X? (answers Alice, Bob)
```

---

### **How It Works**
1. **Facts** define the relationships (e.g., `parent(john, mary)` means John is a parent of Mary).
2. **Rules** infer new relationships (e.g., `father(X, Y)` checks if X is a parent and male).
3. **Queries** let you ask questions. For example:
   - `?- sibling(mary, tom).` Prolog will answer `true` if the relationship holds.

### Running Prolog
- Save the code in a file, e.g., `family.pl`.
- Run it using a Prolog interpreter like **SWI-Prolog**:
  ```bash
  swipl
  ?- [family].
  ?- father(john, mary).
  ```

Prolog will provide answers based on the facts and rules defined.
