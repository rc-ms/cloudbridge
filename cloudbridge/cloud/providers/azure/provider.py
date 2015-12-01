"""
Provider implementation based on Azure-SDK.
"""
from cloudbridge.cloud.base import BaseCloudProvider


class AzureCloudProvider(BaseCloudProvider):

    PROVIDER_ID = 'azure'

    def __init__(self, config):
        super(AzureCloudProvider, self).__init__(config)
