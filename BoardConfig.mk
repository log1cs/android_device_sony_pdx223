#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Include the common OEM chipset BoardConfig.
include device/sony/sm8450-common/BoardConfigCommon.mk

DEVICE_PATH := device/sony/pdx223

# Kernel
TARGET_KERNEL_CONFIG += vendor/sony/pdx223.config

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop
TARGET_ODM_PROP += $(DEVICE_PATH)/odm.prop

# Include the proprietary files BoardConfig.
include vendor/sony/pdx223/BoardConfigVendor.mk
