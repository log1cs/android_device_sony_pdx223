#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Overlay
PRODUCT_PACKAGES += \
    FrameworkRes-PDX223-Overlay \
    SettingsProvider-PDX223-Overlay \
    SystemUIRes-PDX223-Overlay

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Inherit from the common OEM chipset makefile.
$(call inherit-product, device/sony/sm8450-common/common.mk)

# Inherit from the proprietary files makefile.
$(call inherit-product, vendor/sony/pdx223/pdx223-vendor.mk)
