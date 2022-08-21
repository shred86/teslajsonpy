#  SPDX-License-Identifier: Apache-2.0
"""
Python Package for controlling Tesla API.

For more details about this api, please refer to the documentation at
https://github.com/zabuldon/teslajsonpy
"""
IDLE_INTERVAL = 600  # interval after parking to check at regular update_interval
ONLINE_INTERVAL = 60  # interval for checking online state; does not hit individual cars
SLEEP_INTERVAL = 660  # interval required to let vehicle sleep; based on testing
DRIVING_INTERVAL = 60  # interval when driving detected
UPDATE_INTERVAL = 300  # Default polling interval for vehicle
WEBSOCKET_TIMEOUT = 11  # time for websocket to timeout
RELEASE_NOTES_URL = "https://teslascope.com/teslapedia/software/"
AUTH_DOMAIN = "https://auth.tesla.com"
API_URL = "https://owner-api.teslamotors.com"
WS_URL = "wss://streaming.vn.teslamotors.com/streaming"

TESLA_PRODUCT_TYPE_VEHICLES = "vehicles"

CHARGE_CURRENT_MIN = 5

PRODUCT_TYPE_ENERGY_SITES = "energy_sites"
PRODUCT_TYPE_POWERWALLS = "powerwalls"
DEFAULT_ENERGYSITE_NAME = "My Home"
RESOURCE_TYPE = "resource_type"
RESOURCE_TYPE_SOLAR = "solar"
RESOURCE_TYPE_BATTERY = "battery"
