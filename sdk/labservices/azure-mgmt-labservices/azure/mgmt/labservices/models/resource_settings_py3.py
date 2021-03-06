# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceSettings(Model):
    """Represents resource specific settings.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The unique id of the resource setting
    :vartype id: str
    :param gallery_image_resource_id: The resource id of the gallery image
     used for creating the virtual machine
    :type gallery_image_resource_id: str
    :ivar image_name: The name of the image used to created the environment
     setting
    :vartype image_name: str
    :param size: The size of the virtual machine. Possible values include:
     'Basic', 'Standard', 'Performance'
    :type size: str or ~azure.mgmt.labservices.models.ManagedLabVmSize
    :ivar cores: The translated compute cores of the virtual machine
    :vartype cores: int
    :param reference_vm: Required. Details specific to Reference Vm
    :type reference_vm: ~azure.mgmt.labservices.models.ReferenceVm
    """

    _validation = {
        'id': {'readonly': True},
        'image_name': {'readonly': True},
        'cores': {'readonly': True},
        'reference_vm': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'gallery_image_resource_id': {'key': 'galleryImageResourceId', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'cores': {'key': 'cores', 'type': 'int'},
        'reference_vm': {'key': 'referenceVm', 'type': 'ReferenceVm'},
    }

    def __init__(self, *, reference_vm, gallery_image_resource_id: str=None, size=None, **kwargs) -> None:
        super(ResourceSettings, self).__init__(**kwargs)
        self.id = None
        self.gallery_image_resource_id = gallery_image_resource_id
        self.image_name = None
        self.size = size
        self.cores = None
        self.reference_vm = reference_vm
