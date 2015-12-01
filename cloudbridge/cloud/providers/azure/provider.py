"""
Provider implementation based on Azure-SDK.
"""
from cloudbridge.cloud.base import BaseCloudProvider


class AzureCloudProvider(BaseCloudProvider):

    PROVIDER_ID = 'azure'

    def __init__(self, config):
        super(AzureCloudProvider, self).__init__(config)

    @property
    def compute(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")

    @property
    def security(self):
        return self._security

    @property
    def block_store(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")

    @property
    def object_store(self):
        raise NotImplementedError(
            "AzureCloudProvider does not implement this service")
