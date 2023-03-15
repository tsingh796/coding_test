
from rest_framework.response import Response
from rest_framework.views import APIView
from .commons.import_data import ImportData

class ListUsers(APIView):
    # def __init__(self):
    #     self.import_data = import_data()
    #     super().__init__()

    def get(self, req):
        import_data = ImportData()
        import_data.handle(weather="weather")
        return Response({"Message": "Migration Successfull"})