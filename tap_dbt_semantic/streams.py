"""Stream type classes for tap-dbt-semantic."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_dbt_semantic.client import dbt-semanticStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class UsersStream(dbt-semanticStream):
    """Define custom stream."""

    name = "users"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID",
        ),
        th.Property(
            "age",
            th.IntegerType,
            description="The user's age in years",
        ),
        th.Property(
            "email",
            th.StringType,
            description="The user's email address",
        ),
        th.Property(
            "address",
            th.ObjectType(
                th.Property("street", th.StringType),
                th.Property("city", th.StringType),
                th.Property(
                    "state",
                    th.StringType,
                    description="State name in ISO 3166-2 format",
                ),
                th.Property("zip", th.StringType),
            ),
        ),
    ).to_dict()
    primary_keys = ["id"]
    replication_key = None
    graphql_query = """
        users {
            name
            id
            age
            email
            address {
                street
                city
                state
                zip
            }
        }
        """


class GroupsStream(dbt-semanticStream):
    """Define custom stream."""

    name = "groups"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()
    primary_keys = ["id"]
    replication_key = "modified"
    graphql_query = """
        groups {
            name
            id
            modified
        }
        """
