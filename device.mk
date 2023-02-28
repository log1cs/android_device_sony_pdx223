#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# NFC
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/nfc/libnfc-nxp-typef.conf:$(TARGET_COPY_OUT_VENDOR)/etc/libnfc-nxp-typef.conf

# Overlay
PRODUCT_PACKAGES += \
    FrameworkRes-PDX223-Overlay \
    SettingsProvider-PDX223-Overlay \
    SystemUIRes-PDX223-Overlay

DEVICE_PACKAGE_OVERLAYS += \
    $(LOCAL_PATH)/overlay-lineage

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Inherit from the common OEM chipset makefile.
$(call inherit-product, device/sony/sm8450-common/common.mk)

# Inherit from the proprietary files makefile.
$(call inherit-product, vendor/sony/pdx223/pdx223-vendor.mk)
