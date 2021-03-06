# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AccessLevel(str, Enum):

    none = "None"
    read = "Read"
    write = "Write"

class DiskCreateOption(str, Enum):
    """This enumerates the possible sources of a disk's creation.
    """

    empty = "Empty"
    attach = "Attach"
    from_image = "FromImage"
    import_enum = "Import"
    copy = "Copy"
    restore = "Restore"
    upload = "Upload"

class DiskState(str, Enum):
    """The state of the disk.
    """

    unattached = "Unattached"
    attached = "Attached"
    reserved = "Reserved"
    active_sas = "ActiveSAS"
    ready_to_upload = "ReadyToUpload"
    active_upload = "ActiveUpload"

class DiskStorageAccountTypes(str, Enum):
    """The sku name.
    """

    standard_lrs = "Standard_LRS"
    premium_lrs = "Premium_LRS"
    standard_ssd_lrs = "StandardSSD_LRS"
    ultra_ssd_lrs = "UltraSSD_LRS"

class HyperVGeneration(str, Enum):
    """The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """

    v1 = "V1"
    v2 = "V2"

class OperatingSystemTypes(str, Enum):
    """The Operating System type.
    """

    windows = "Windows"
    linux = "Linux"

class SnapshotStorageAccountTypes(str, Enum):
    """The sku name.
    """

    standard_lrs = "Standard_LRS"
    premium_lrs = "Premium_LRS"
    standard_zrs = "Standard_ZRS"
