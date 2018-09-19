# How to use GraphQL

GraphQL is a query language for your API, and a server-size runtime for executing queries by using a type system you define for you data.<br>

A GraphQL service is created by defining `types` and `fields` on those `types`, then providing functions for each field on each type. 

# [Introspection](https://graphql.org/learn/introspection/)

It's often useful to ask a GraphQL schema for information about what queries it supports. By querying the `__schema` filed, always available on the root type of a Query.

```js
{
  __schema {
    types {
      name
      kind
      description
    }
  }
}
```
then you will get a return like following
```js
{
  "data": {
    "__schema": {
      "types": [
        {
          "name": "Query",
          "kind": "OBJECT",
          "description": "The query type, represents all of the entry points into our object graph"
        },
        {
          "name": "Episode",
          "kind": "ENUM",
          "description": "The episodes in the Star Wars trilogy"
        },
        {
          "name": "Character",
          "kind": "INTERFACE",
          "description": "A character from the Star Wars universe"
        }
        ....
      ]
    }
  }
}
```
- `Query, Character, Human, Episode` These are the ones that we defined in our type system.

- Also there are build in scalars that the type system provide.

- `__Schema, __Type,` some preceded with a double underscore, indicating that they are part of the introspection system.

# Dynamic Variable

Variable(s) can be used to create dynamic queries when it comes to the implement in your code. Use the `GitHub` Graph API as a example. 
```js
query ($organization: String!) {
  organization(login: $organization) {
    name
    url
  }
}
```
then go to "Query Variables" panel to input:
```js
{ "organization": "facebook" }
```
the result is the same with query as 
```js
organization(log: "facebook") {
    name
    url
}
```
On a side note, you can also define a default variable in dynamic query. Like `query ($organization: String = "facebook") { ... }` it has to be a not required argument. By the way. `Sting!` means your must pass argument to your dynamic query.

# `query` statement

