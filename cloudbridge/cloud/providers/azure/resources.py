"""
DataTypes used by this provider
"""
from cloudbridge.cloud.base.resources import BaseKeyPair


class AzureKeyPair(BaseKeyPair):

    def __init__(self, provider, cert, material=None):
        super(AzureKeyPair, self).__init__(provider)
        self._cert = cert
        self._material = material

    @property
    def id(self):
        """
        Return the id of this key pair.
        """
        return self._cert.thumbprint

    @property
    def name(self):
        """
        Return the name of this key pair.
        """
        return "%s %s " % (self._cert.thumbprint,
                           self._cert.thumbprint_algorithm)

    def delete(self):
        """
        Delete this KeyPair.

        :rtype: bool
        :return: True if successful, otherwise False.
        """
        return self.provider.sms.delete_service_certificate(
            self.provider.sms.service_name,
            self._cert.thumbprint_algorithm,
            self._cert.thumbprint)

    @property
    def material(self):
        """
        Unencrypted private key.

        :rtype: str
        :return: Unencrypted private key or ``None`` if not available.

        """
        return self._material
