# coding: utf-8

# flake8: noqa

"""
    Kandji API

    <html><head></head><body><h1 id=&quot;welcome-to-the-kandji-api-documentation&quot;>Welcome to the Kandji API Documentation</h1> <p>You can find your API URL in Settings &gt; Access. The API URL will follow the below formats.</p> <ul> <li><p>US - <code>https://SubDomain.api.kandji.io</code></p> </li> <li><p>EU - <code>https://SubDomain.api.eu.kandji.io</code></p> </li> </ul> <p>For information on how to obtain an API token, please refer to the following support article.</p> <p><a href=&quot;https://support.kandji.io/api&quot;>https://support.kandji.io/api</a></p> <h4 id=&quot;rate-limit&quot;>Rate Limit</h4> <p>The Kandji API currently has an API rate limit of 10,000 requests per hour per customer.</p> <h4 id=&quot;request-methods&quot;>Request Methods</h4> <p>HTTP request methods supported by the Kandji API.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table> <thead> <tr> <th>Method</th> <th>Definition</th> </tr> </thead> <tbody> <tr> <td>GET</td> <td>The <code>GET</code> method requests a representation of the specified resource.</td> </tr> <tr> <td>POST</td> <td>The <code>POST</code> method submits an entity to the specified resource.</td> </tr> <tr> <td>PATCH</td> <td>The <code>PATCH</code> method applies partial modifications to a resource.</td> </tr> <tr> <td>DELETE</td> <td>The <code>DELETE</code> method deletes the specified resource.</td> </tr> </tbody> </table> </div><h4 id=&quot;response-codes&quot;>Response codes</h4> <p>Not all response codes apply to every endpoint.</p> <div class=&quot;click-to-expand-wrapper is-table-wrapper&quot;><table> <thead> <tr> <th>Code</th> <th>Response</th> </tr> </thead> <tbody> <tr> <td>200</td> <td>OK</td> </tr> <tr> <td>201</td> <td>Created</td> </tr> <tr> <td>204</td> <td>No content</td> </tr> <tr> <td></td> <td>Typical response when sending the DELETE method.</td> </tr> <tr> <td>400</td> <td>Bad Request</td> </tr> <tr> <td></td> <td>&quot;Command already running&quot; - The command may already be running in a <em>Pending</em> state waiting on the device.</td> </tr> <tr> <td></td> <td>&quot;Command is not allowed for current device&quot; - The command may not be compatible with the target device.</td> </tr> <tr> <td></td> <td>&quot;JSON parse error - Expecting ',' delimiter: line 3 column 2 (char 65)&quot;</td> </tr> <tr> <td>401</td> <td>Unauthorized</td> </tr> <tr> <td></td> <td>This error can occur if the token is incorrect, was revoked, or the token has expired.</td> </tr> <tr> <td>403</td> <td>Forbidden</td> </tr> <tr> <td></td> <td>The request was understood but cannot be authorized.</td> </tr> <tr> <td>404</td> <td>Not found</td> </tr> <tr> <td></td> <td>Unable to locate the resource in the Kandji tenant.</td> </tr> <tr> <td>415</td> <td>Unsupported Media Type</td> </tr> <tr> <td></td> <td>The request contains a media type which the server or resource does not support.</td> </tr> <tr> <td>500</td> <td>Internal server error</td> </tr> <tr> <td>503</td> <td>Service unavailable</td> </tr> <tr> <td></td> <td>This error can occur if a file upload is still being processed via the custom apps API.</td> </tr> </tbody> </table> </div><h4 id=&quot;data-structure&quot;>Data structure</h4> <p>The API returns all structured responses in JSON schema format.</p> <h4 id=&quot;examples&quot;>Examples</h4> <p>Code examples using the API can be found in the Kandji support <a href=&quot;https://github.com/kandji-inc/support/tree/main/api-tools&quot;>GitHub</a>.</p> </body></html>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from kandji_sdk.api.automated_device_enrollment_integrations_api import AutomatedDeviceEnrollmentIntegrationsApi
from kandji_sdk.api.blueprints_api import BlueprintsApi
from kandji_sdk.api.custom_apps_api import CustomAppsApi
from kandji_sdk.api.custom_profiles_api import CustomProfilesApi
from kandji_sdk.api.custom_scripts_api import CustomScriptsApi
from kandji_sdk.api.device_actions_api import DeviceActionsApi
from kandji_sdk.api.device_information_api import DeviceInformationApi
from kandji_sdk.api.device_secrets_api import DeviceSecretsApi
from kandji_sdk.api.in_house_apps_api import InHouseAppsApi
from kandji_sdk.api.library_items_api import LibraryItemsApi
from kandji_sdk.api.lost_mode_api import LostModeApi
from kandji_sdk.api.notes_api import NotesApi
from kandji_sdk.api.prism_api import PrismApi
from kandji_sdk.api.self_service_api import SelfServiceApi
from kandji_sdk.api.settings_api import SettingsApi
from kandji_sdk.api.tags_api import TagsApi
from kandji_sdk.api.threats_api import ThreatsApi
from kandji_sdk.api.users_api import UsersApi

# import ApiClient
from kandji_sdk.api_response import ApiResponse
from kandji_sdk.api_client import ApiClient
from kandji_sdk.configuration import Configuration
from kandji_sdk.exceptions import OpenApiException
from kandji_sdk.exceptions import ApiTypeError
from kandji_sdk.exceptions import ApiValueError
from kandji_sdk.exceptions import ApiKeyError
from kandji_sdk.exceptions import ApiAttributeError
from kandji_sdk.exceptions import ApiException

# import models into sdk package
