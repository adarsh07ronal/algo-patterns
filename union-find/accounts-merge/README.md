# Accounts Merge (Medium)

## Problem

Given a list of `accounts`, where `accounts[i] = [name, email1, email2, ...]`, merge accounts
that belong to the same person. Two accounts belong to the same person if they share at least
one email (accounts can be transitively linked through a chain of shared emails, even if the
`name` differs is irrelevant — emails are the source of truth, and all accounts belonging to one
person share the same name). Return the merged accounts as `[name, sorted email list...]` in any
order.

**Example**

```
Input: accounts = [
  ["John","johnsmith@mail.com","john_newyork@mail.com"],
  ["John","johnsmith@mail.com","john00@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnnybravo@mail.com"]
]
Output: [
  ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnnybravo@mail.com"]
]
```
The first two "John" accounts share `johnsmith@mail.com` and merge; the third "John" (with
`johnnybravo@mail.com`) shares no email with anyone, so it stays separate.

**Constraints**

- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- Emails consist of lowercase letters and `@`/`.`; each email belongs to exactly one account
  index the first time it's seen, but can be repeated across accounts to signal a merge.

## Approach

Treat each **account index** (not each email) as a DSU element. Keep a dictionary
`email_to_owner` mapping an email to the first account index that introduced it. Walk every
account's emails: if an email was already seen under a different account index, `union` the
current account index with that earlier owner — this is the moment two accounts are declared
"the same person." If the email is new, just record its owner.

After processing everything, group all emails by the **root** account index of their original
owner (`find(email_to_owner[email])`). Each group of emails belongs to one merged account; the
`name` for that group is `accounts[root][0]` (all accounts merged together are guaranteed the
same person, hence same name). Sort each group's emails for the required output format.

Union-find is the natural fit because "belongs to the same person" is a transitive equivalence
relation discovered incrementally as we scan emails — exactly what union-find is built to
maintain. A DFS/BFS alternative would require building an explicit graph (accounts as nodes,
edges wherever emails overlap) first, which is extra bookkeeping; union-find lets us discover
and merge on the fly in a single pass over the input.

## Edge Cases

- **Account with no shared emails**: never unioned with anything, remains its own singleton
  group in the output.
- **Chain of shared emails across 3+ accounts** (A-B share one email, B-C share a different
  email): handled correctly because union-find merges are transitive — A, B, C end up under the
  same root even though A and C share no email directly.
- **Single account**: output is just that one account, emails sorted.
- **Duplicate emails within the same account**: harmless; unioning an index with itself is a
  no-op.

## Complexity

- **Time**: O(K log K * α(N)) where `K` is the total number of email entries across all
  accounts and `N` is the number of accounts — building the DSU and email map is O(K) with
  near-O(1) unions/finds, and sorting emails within each merged group contributes the log
  factor.
- **Space**: O(K) for the email-to-owner map and O(N) for the DSU arrays.

[<- Previous](../redundant-connection/README.md) | [Category Index](../README.md) | [Next ->](../graph-valid-tree/README.md)
