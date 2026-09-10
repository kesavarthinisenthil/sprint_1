class BaseConfig:
    """Base configuration class."""

class ConfigManager(BaseConfig):
    """Manage application configuration."""

    def __init__(self):
        """Initialize the configuration."""        
        self._config = {}

    def set(self, key: str, value: str) -> None:
            """Set a configuration value."""
            self._config[key] = value

    def get(self, key: str) -> str | None:
            """Get a configuration value."""
            return self._config.get(key)

    def get_config(self) -> dict:
        """Return all configuration values."""
        return self._config.copy()

    @property
    def configuration(self) -> dict:
        """Return the current configuration."""
        return self._config.copy()

    @classmethod
    def create_default(cls):
        """Create a ConfigManager with default settings."""
        config = cls()
        config.set("host", "localhost")
        return config