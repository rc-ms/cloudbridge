"""
Provider implementation based on Azure-SDK.
"""
from cloudbridge.cloud.base import BaseCloudProvider
from cloudbridge.cloud.providers.azure.services import AzureSecurityService


class AzureCloudProvider(BaseCloudProvider):

    PROVIDER_ID = 'azure'

    def __init__(self, config):
        super(AzureCloudProvider, self).__init__(config)
        self._security = None

    @property
    def compute(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")

    @property
    def security(self):
        if not self._security:
            self._security = AzureSecurityService(self)
        return self._security

    @property
    def block_store(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")

    @property
    def object_store(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")
