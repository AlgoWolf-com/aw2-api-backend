import logging
from apigw import Router, Response
from util import validate_json_schema
from datatypes.constants import HttpMethod

logger = logging.getLogger(__name__)
logger.critical("Function startup")

router = Router()


@validate_json_schema(__file__)
def handler(event, ctx):
    return router.handle(event, ctx)


@router.route("/message", methods=(HttpMethod.GET,))
def get_message(*_):
    return Response.ok({"message": "Hello World!"})
