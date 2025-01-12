import graphene
from graphene_django.types import DjangoObjectType
from simulator.models import Simulator  # Import your Simulator model

# Define a GraphQL type for the Simulator model
class SimulatorType(DjangoObjectType):
    class Meta:
        model = Simulator

# Query to list all simulators
class Query(graphene.ObjectType):
    all_simulators = graphene.List(SimulatorType)

    def resolve_all_simulators(self, info, **kwargs):
        return Simulator.objects.all()

# Mutation to create a new simulator
class CreateSimulator(graphene.Mutation):
    class Arguments:
        kpi_id = graphene.Int(required=True)
        start_date = graphene.DateTime(required=True)
        interval = graphene.String(required=True)

    simulator = graphene.Field(SimulatorType)

    def mutate(self, info, kpi_id, start_date, interval):
        simulator = Simulator(kpi_id=kpi_id, start_date=start_date, interval=interval)
        simulator.save()
        return CreateSimulator(simulator=simulator)

# Mutation to update a simulator
class UpdateSimulator(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        kpi_id = graphene.Int()
        start_date = graphene.DateTime()
        interval = graphene.String()

    simulator = graphene.Field(SimulatorType)

    def mutate(self, info, id, kpi_id=None, start_date=None, interval=None):
        simulator = Simulator.objects.get(pk=id)
        if kpi_id is not None:
            simulator.kpi_id = kpi_id
        if start_date is not None:
            simulator.start_date = start_date
        if interval is not None:
            simulator.interval = interval
        simulator.save()
        return UpdateSimulator(simulator=simulator)

# Mutation to delete a simulator
class DeleteSimulator(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()  
    message = graphene.String()   

    def mutate(self, info, id):
        try:
            simulator = Simulator.objects.get(pk=id)
            simulator.delete()
            return DeleteSimulator(success=True, message="Simulator deleted successfully")
        except Simulator.DoesNotExist:
            return DeleteSimulator(success=False, message="Simulator not found")
        
# Define all mutations
class Mutation(graphene.ObjectType):
    create_simulator = CreateSimulator.Field()
    update_simulator = UpdateSimulator.Field()
    delete_simulator = DeleteSimulator.Field()

# Create the schema
schema = graphene.Schema(query=Query, mutation=Mutation)