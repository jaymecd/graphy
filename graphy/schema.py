import graphene

from graphy.leads import gql_actions as lead_actions
from graphy.location import gql_actions as location_actions


class Query(
    graphene.ObjectType,
    location_actions.AddressQuery,
    location_actions.CountyQuery,
    lead_actions.LeadQuery,
):
    pass


schema = graphene.Schema(query=Query)