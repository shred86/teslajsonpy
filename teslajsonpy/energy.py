"""Tesla Energy energy site."""
from teslajsonpy.const import (
    RESOURCE_TYPE,
    DEFAULT_ENERGYSITE_NAME,
)


class EnergySite:
    """Base class to represents a Tesla Energy site."""

    def __init__(self, api, energysite, data) -> None:
        """Initialize EnergySite."""
        self._api = api
        self._energysite = energysite
        self._data = data

    @property
    def energysite_id(self) -> int:
        """Return energy site id (aka site_id)."""
        return self._energysite.get("energy_site_id")

    @property
    def has_load_meter(self) -> bool:
        """Return True if energy site has a load meter."""
        return self._energysite.get("components").get("load_meter")

    @property
    def id(self) -> int:
        """Return id (aka battery_id)."""
        return self._energysite.get("id")

    @property
    def resource_type(self) -> str:
        """Return energy site type."""
        return self._energysite[RESOURCE_TYPE]

    @property
    def site_name(self) -> str:
        """Return energy site name."""
        # "site_name" not a valid key if name never set in Tesla app
        return self._energysite.get("site_name", DEFAULT_ENERGYSITE_NAME)


class SolarSite(EnergySite):
    """Represents a Tesla Energy Solar site.

    This class shouldn't be instantiated directly; it will be instantiated
    by :meth:`teslajsonpy.controller.generate_energysite_objects`.
    """

    def __init__(self, api, energysite, data) -> None:
        """Initialize SolarSite."""
        super().__init__(api, energysite, data)

    @property
    def grid_power(self) -> float:
        """Return grid power in Watts."""
        # Add check to see if site has power metering?
        return self._data["grid_power"]

    @property
    def load_power(self) -> float:
        """Return load power in Watts."""
        # Add check to see if site has power metering?
        return self._data["load_power"]

    @property
    def solar_power(self) -> float:
        """Return solar power in Watts."""
        return self._data["solar_power"]

    @property
    def solar_type(self) -> str:
        """Return type of solar (e.g. pv_panels or roof)."""
        return self._energysite.get("components").get("solar_type")


class PowerwallSite(EnergySite):
    """Represents a Tesla Energy Powerwall site.

    This class shouldn't be instantiated directly; it will be instantiated
    by :meth:`teslajsonpy.controller.generate_energysite_objects`.
    """

    def __init__(self, api, energysite, data) -> None:
        """Initialize PowerwallSite."""
        super().__init__(api, energysite, data)

    @property
    def battery_power(self) -> float:
        """Return battery power in Watts."""
        return self._data["battery_power"]

    @property
    def battery_reserve_percent(self) -> float:
        """Return battery reserve percentage."""
        return self._data["backup_reserve_percent"]

    @property
    def energy_left(self) -> float:
        """Return battery energy left in Watt hours."""
        return self._data["energy_left"]

    @property
    def grid_power(self) -> float:
        # Grid and load power are the same in SolarSite because of how we store
        # the data. It comes from two different endpoints but we stored in self._data
        return self._data["grid_power"]

    @property
    def grid_status(self) -> str:
        """Return grid status."""
        return self._data["grid_status"]

    @property
    def load_power(self) -> float:
        """Return load power in Watts."""
        return self._data["load_power"]

    @property
    def percentage_charged(self) -> float:
        """Return battery percentage charged."""
        return self._data["percentage_charged"]

    async def set_operation_mode(self, real_mode: str, value: int) -> None:
        """Set operation mode of Powerwall.

        Mode: "self_consumption", "backup", "autonomous"
        Value: 0-100
        """
        data = await self._api(
            "BATTERY_OPERATION_MODE",
            path_vars={"battery_id": self.id},
            default_real_mode=real_mode,
            backup_reserve_percent=int(value),
        )
        if data and data["response"]["result"] is True:
            self._data["default_real_mode"] = real_mode
            self._data["backup_reserve_percent"] = value


class SolarPowerwallSite(PowerwallSite, SolarSite):
    """Represents a Tesla Energy Solar site with Powerwall(s).

    This class shouldn't be instantiated directly; it will be instantiated
    by :meth:`teslajsonpy.controller.generate_energysite_objects`.
    """

    def __init__(self, api, energysite, data) -> None:
        """Initialize SolarPowerwallSite."""
        super().__init__(api, energysite, data)
