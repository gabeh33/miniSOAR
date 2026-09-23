# File to get logs from Entra and feed them in a digestible way to the SOAR core
from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient
import logging
import configparser
import asyncio

# Setup logging for this program
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')
logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(logging.WARNING) # surpress non important azure logging output
logger = logging.getLogger(__name__)

# Setup config parser
config = configparser.ConfigParser()
config.read('config.cfg')

logger.info("App attempting to sign in")
cred = ClientSecretCredential(
    tenant_id = config["Azure"]["tenant_id"],
    client_secret = config["Azure"]["client_secret"],
    client_id = config["Azure"]["application_id"]
)

client = GraphServiceClient(credentials=cred, scopes=["https://graph.microsoft.com/.default"])

graph_url = "https://graph.microsoft.com/.default"


async def get_users() -> list[str]:
    """Gets a list of all users and returns that list of strings"""

    try:
        user_list = []
        users = await client.users.get()
        if users and users.value:
            for user in users.value:
                user_list.append(f"{user.display_name} ({user.mail or user.user_principal_name})")
        return user_list
    except Exception as e:
        logger.critical(f"Failed to fetch users with error{e}")
    

users = asyncio.run(get_users())
print(get_users.__doc__)
