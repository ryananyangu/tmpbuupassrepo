# Role Based Access Control

Provides restrictive access to the users in a system based on their role (User groups)
Above implies the entire format will be implemented with group and no granular permissions assigned to the user directly

## Features

- User is a member of one group or more groups
- Group contains many users and many permisions
- Each user created will have a group with their username
- Sub users will be registered on parent users group and they will be able to cascade the permisions downstream.

### Potential challenges

- How to handle deletion of parent sub. so that the other subs remain but permision related to the parent sub are removed.
NOTE: Group defines the role of the user in the system

#### APIS

1. Signup
2. Sign in
3. Invite user (Sub registration) to personal role
4. Invited user request accept request invited role
5. Add remove permisions from group
