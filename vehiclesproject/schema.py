from graphene_federation import build_schema

from vehiclesapp.graphql.schema import VehicleQueries
from vehiclesapp.graphql.mutations import VehicleMutations

class Query(
    VehicleQueries,
):
    pass

class Mutation(
    VehicleMutations
):
    pass

schema = build_schema(query=Query, mutation=Mutation, enable_federation_2=True)