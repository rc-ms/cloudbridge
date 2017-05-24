from azure_test.helpers import ProviderTestBase


class AzureSubnetServiceTestCase(ProviderTestBase):
    def test_azure_subnet_service_list(self):
        subnets = self.provider.network.subnets.list()
        self.assertIsNotNone(subnets)
        for subnet in subnets:
            print(subnet.name)
            print(subnet.id)
            print(subnet.cidr_block)
            print("network_id" + subnet.network_id)

    def test_azure_subnet_service_list_filter_network_id(self):
        network_id = '/subscriptions/7904d702-e01c-4826-8519-f5a25c866a96/' \
                     'resourceGroups/CloudBridge-Azure/providers/' \
                     'Microsoft.Network/virtualNetworks/CloudBridgeNet'
        subnets = self.provider.network.subnets.list(network_id)
        self.assertIsNotNone(subnets)
        for subnet in subnets:
            print(subnet.name)
            print(subnet.id)
            print(subnet.cidr_block)
            print("network_id" + subnet.network_id)

    def test_azure_subnet_service_list_filter_network_object(self):
        network_id = '/subscriptions/7904d702-e01c-4826-8519-f5a25c866a96/' \
                     'resourceGroups/CloudBridge-Azure/providers/' \
                     'Microsoft.Network/virtualNetworks/CloudBridgeNet'
        network = self.provider.network.get(network_id)
        subnets = self.provider.network.subnets.list(network)
        self.assertIsNotNone(subnets)
        for subnet in subnets:
            print(subnet.name)
            print(subnet.id)
            print(subnet.cidr_block)
            print("network_id" + subnet.network_id)

    def test_azure_subnet_service_get(self):
        subnet_id = '/subscriptions/7904d702-e01c-4826-8519-f5a25c866a96/' \
                    'resourceGroups/CloudBridge-Azure/providers/' \
                    'Microsoft.Network/virtualNetworks/' \
                    'CloudBridgeNet/subnets/MySN1'
        subnet = self.provider.network.subnets.get(subnet_id)
        self.assertIsNotNone(subnet)
        if subnet:
            print("Subnet found")
            print(subnet.id)
            print(subnet.name)
            print(subnet.cidr_block)
            print("network_id" + subnet.network_id)

    def test_azure_subnet_service_get_invalid_subnet(self):
        subnet_id = '/subscriptions/7904d702-e01c-4826-8519-f5a25c866a96/' \
                    'resourceGroups/CloudBridge-Azure/providers/' \
                    'Microsoft.Network/virtualNetworks/' \
                    'CloudBridgeNet/subnets/MySN'
        subnet = self.provider.network.subnets.get(subnet_id)
        self.assertIsNone(subnet)