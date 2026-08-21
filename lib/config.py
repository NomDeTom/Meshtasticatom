"""Simulation configuration.

Every table here that mirrors the firmware is pinned to 2.8.0 (version.properties), commit 51eadb7:
the region list, the region profiles, the modem presets and the frequency-slot calculation.
"""

from enum import Enum

# djb2, from hash() in src/mesh/RadioInterface.cpp. A device with no frequency slot configured
# picks one by hashing its primary channel's name, so this has to match the firmware bit for bit.
def djb2_hash(text):
    value = 5381
    for byte in text.encode():
        value = ((value << 5) + value + byte) & 0xFFFFFFFF
    return value


# Preset display names from src/DisplayFormatters.cpp. These strings are what gets hashed, so a
# rename upstream moves every default frequency in the region.
MODEM_PRESET_DISPLAY_NAMES = {
    "SHORT_TURBO": "ShortTurbo",
    "SHORT_SLOW": "ShortSlow",
    "SHORT_FAST": "ShortFast",
    "MEDIUM_SLOW": "MediumSlow",
    "MEDIUM_FAST": "MediumFast",
    "MEDIUM_TURBO": "MediumTurbo",
    "LONG_SLOW": "LongSlow",
    "LONG_FAST": "LongFast",
    "LONG_TURBO": "LongTurbo",
    "LONG_MODERATE": "LongMod",
    "LITE_FAST": "LiteFast",
    "LITE_SLOW": "LiteSlow",
    "NARROW_FAST": "NarrowFast",
    "NARROW_SLOW": "NarrowSlow",
    "TINY_FAST": "TinyFast",
    "TINY_SLOW": "TinySlow",
}


class Config:

    class ROUTER_TYPE(Enum):
        MANAGED_FLOOD = 'MANAGED_FLOOD'

    def __init__(self):
        self.MODEL = 5  # Path loss model to use - see docs/radio_model.md, or lib.phy.PATH_LOSS_MODELS

        self.XSIZE = 15000  # horizontal size of the area to simulate in m
        self.YSIZE = 15000  # vertical size of the area to simulate in m
        self.OX = 0.0  # origin x-coordinate
        self.OY = 0.0  # origin y-coordinate
        self.MINDIST = 10  # minimum distance between each node in the area in m

        self.GL = 0  # antenna gain of each node in dBi
        self.HM = 1.0  # height of each node in m

        ### Meshtastic specific ###
        self.hopLimit = 3  # default 3
        self.router = False  # set role of each node as router (True) or normal client (False)
        # Total sends including the first, from NextHopRouter.h - the firmware carries two
        # figures, not one: NUM_RELIABLE_RETX for a reliable broadcast and
        # NUM_RELIABLE_UNICAST_ATTEMPTS for an acknowledged unicast from the originator.
        self.RELIABLE_BROADCAST_ATTEMPTS = 3
        self.RELIABLE_UNICAST_ATTEMPTS = 5
        ### End of Meshtastic specific ###

        self.ONE_SECOND_INTERVAL = 1000
        self.TEN_SECONDS_INTERVAL = self.ONE_SECOND_INTERVAL * 10
        self.ONE_MIN_INTERVAL = self.TEN_SECONDS_INTERVAL * 6
        self.ONE_HR_INTERVAL = self.ONE_MIN_INTERVAL * 60

        ### Discrete-event specific ###
        self.ENABLE_CONNECTIVITY_MAP = True # use the connectivity map optimization
        self.CONNECTIVITY_MAP_RSSI_MARGIN = 8

        self.MODEM_PRESET = "LONG_FAST"  # LoRa modem preset to use (default LONG_FAST matches firmware)
        self.PERIOD = 100 * self.ONE_SECOND_INTERVAL  # mean period of generating a new message with exponential distribution in ms
        self.PACKETLENGTH = 40  # payload in bytes
        self.SIMTIME = 30 * self.ONE_MIN_INTERVAL  # duration of one simulation in ms
        # Long-run share of time a foreign, non-Meshtastic transmitter holds a node's channel, in
        # [0, 1]. One control: the interferer both defers this node's CAD and jams frames arriving
        # at it, because those are the same occupancy seen from the two ends. It used to be two -
        # an ungated draw for CAD and COLLISION_DUE_TO_INTERFERENCE for reception - which made a
        # channel that was busy enough to wait for but never busy enough to break anything.
        self.INTERFERENCE_LEVEL = 0.05
        # Mean length of one busy stretch. None derives it from a full frame on the configured
        # preset, a foreign LoRa packet being the likeliest occupant of a LoRa channel.
        self.INTERFERENCE_MEAN_BUSY_MS = None
        self.CAPTURE_COLLISION_MODEL_ENABLED = False
        self.COLLISION_CAPTURE_THRESHOLD_DB = 6.0
        self.COLLISION_PAYLOAD_OVERLAP_LOSS_FRACTION = 0.15
        self.DMs = False  # Set True for sending DMs (with random destination), False for broadcasts

        #################################################
        ####### DYNAMIC CODING RATE #####################
        #################################################
        # Off by default; no released firmware has this. See docs/configuration.md.
        self.DCR_ENABLED = False
        self.DCR_MIN_CR = 5
        self.DCR_MAX_CR = 8
        self.DCR_USER_MIN_CR = 5
        # A mesh-behaviour rail on non-urgent CR8 traffic, not a regulatory one.
        self.DCR_CR8_AIRTIME_LIMIT_PERCENT = 10.0
        # Local channel-pressure thresholds, deliberately not regulatory limits.
        self.DCR_IDLE_UTIL_PERCENT = 2.0
        self.DCR_BUSY_UTIL_PERCENT = 7.0
        self.DCR_CONGESTED_UTIL_PERCENT = 17.5
        self.DCR_BUSY_QUEUE_DEPTH = 3
        self.DCR_CONGESTED_QUEUE_DEPTH = 6

        #################################################
        ####### DYNAMIC TX POWER ########################
        #################################################
        # Off by default, and only ever lowers power: PTX stays the ceiling.
        # No released firmware has this either. See docs/configuration.md.
        self.DTP_ENABLED = False
        self.DTP_MAX_POWER_DROP_DB = 12
        self.DTP_POWER_STEP_DB = 3
        self.DTP_MIN_TX_POWER_DBM = None
        self.DTP_STRONG_LINK_MARGIN_DB = 20.0
        self.DTP_VERY_STRONG_LINK_MARGIN_DB = 24.0
        # Region profiles bundle a preset list with the regulatory parameters regions share.
        # From RegionProfile in src/mesh/MeshRadio.h; spacing and padding are Hz here, MHz there.
        self.REGION_PROFILES = {
            "STD": {
                "presets": ("LONG_FAST", "LONG_SLOW", "MEDIUM_SLOW", "MEDIUM_FAST", "SHORT_SLOW",
                            "SHORT_FAST", "LONG_MODERATE", "SHORT_TURBO", "LONG_TURBO", "MEDIUM_TURBO"),
                "spacing": 0.0, "padding": 0.0, "audio_permitted": True, "licensed_only": False
            },
            "EU868": {
                "presets": ("LONG_FAST", "LONG_SLOW", "MEDIUM_SLOW", "MEDIUM_FAST", "SHORT_SLOW",
                            "SHORT_FAST", "LONG_MODERATE"),
                "spacing": 0.0, "padding": 0.0, "audio_permitted": False, "licensed_only": False
            },
            "UNDEF": {
                "presets": ("LONG_FAST",),
                "spacing": 0.0, "padding": 0.0, "audio_permitted": True, "licensed_only": False
            },
            "LITE": {
                "presets": ("LITE_FAST", "LITE_SLOW"),
                "spacing": 400e3, "padding": 37.5e3, "audio_permitted": False, "licensed_only": False
            },
            "NARROW": {
                "presets": ("NARROW_FAST", "NARROW_SLOW"),
                "spacing": 0.0, "padding": 10.4e3, "audio_permitted": True, "licensed_only": False
            },
            # Ham 20 kHz: 15.6 kHz of bandwidth padded out to the channel it has to sit in.
            "HAM_20KHZ": {
                "presets": ("TINY_FAST", "TINY_SLOW"),
                "spacing": 0.0, "padding": 2.2e3, "audio_permitted": False, "licensed_only": True
            },
            # Ham 100 kHz: 62.5 kHz padded the same way.
            "HAM_100KHZ": {
                "presets": ("NARROW_FAST", "NARROW_SLOW"),
                "spacing": 0.0, "padding": 18.75e3, "audio_permitted": False, "licensed_only": True
            }
        }

        # from firmware RegionInfo regions[] in src/mesh/RadioInterface.cpp, at this file's pin
        self.regions = {
            "US": {
                "freq_start": 902.0e6,
                "freq_end": 928.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "EU_433": {
                "freq_start": 433.0e6,
                "freq_end": 434.0e6,
                "duty_cycle": 10,
                "power_limit": 10,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "EU_868": {
                "freq_start": 869.4e6,
                "freq_end": 869.65e6,
                "duty_cycle": 10,
                "power_limit": 27,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "EU868",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "EU_866": {
                "freq_start": 865.6e6,
                "freq_end": 867.6e6,
                "duty_cycle": 2.5,
                "power_limit": 27,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "LITE",
                "default_preset": "LITE_FAST",
                "override_slot": 0
            },
            "EU_N_868": {
                "freq_start": 869.4e6,
                "freq_end": 869.65e6,
                "duty_cycle": 10,
                "power_limit": 27,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "NARROW",
                "default_preset": "NARROW_SLOW",
                "override_slot": 1
            },
            "CN": {
                "freq_start": 470.0e6,
                "freq_end": 510.0e6,
                "duty_cycle": 100,
                "power_limit": 19,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "JP": {
                "freq_start": 920.5e6,
                "freq_end": 923.5e6,
                "duty_cycle": 100,
                "power_limit": 13,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "ANZ": {
                "freq_start": 915.0e6,
                "freq_end": 928.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "ANZ_433": {
                "freq_start": 433.05e6,
                "freq_end": 434.79e6,
                "duty_cycle": 100,
                "power_limit": 14,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "RU": {
                "freq_start": 868.7e6,
                "freq_end": 869.2e6,
                "duty_cycle": 100,
                "power_limit": 20,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "KR": {
                "freq_start": 920.0e6,
                "freq_end": 923.0e6,
                "duty_cycle": 100,
                "power_limit": 23,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "TW": {
                "freq_start": 920.0e6,
                "freq_end": 925.0e6,
                "duty_cycle": 100,
                "power_limit": 27,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "IN": {
                "freq_start": 865.0e6,
                "freq_end": 867.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "NZ_865": {
                "freq_start": 864.0e6,
                "freq_end": 868.0e6,
                "duty_cycle": 100,
                "power_limit": 36,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "TH": {
                "freq_start": 920.0e6,
                "freq_end": 925.0e6,
                "duty_cycle": 10,
                "power_limit": 27,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "UA_433": {
                "freq_start": 433.0e6,
                "freq_end": 434.7e6,
                "duty_cycle": 10,
                "power_limit": 10,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "MY_433": {
                "freq_start": 433.0e6,
                "freq_end": 435.0e6,
                "duty_cycle": 100,
                "power_limit": 20,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "MY_919": {
                "freq_start": 919.0e6,
                "freq_end": 924.0e6,
                "duty_cycle": 100,
                "power_limit": 27,
                "frequency_switching": True,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "SG_923": {
                "freq_start": 917.0e6,
                "freq_end": 925.0e6,
                "duty_cycle": 100,
                "power_limit": 20,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "PH_433": {
                "freq_start": 433.0e6,
                "freq_end": 434.7e6,
                "duty_cycle": 100,
                "power_limit": 10,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "PH_868": {
                "freq_start": 868.0e6,
                "freq_end": 869.4e6,
                "duty_cycle": 100,
                "power_limit": 14,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "PH_915": {
                "freq_start": 915.0e6,
                "freq_end": 918.0e6,
                "duty_cycle": 100,
                "power_limit": 24,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "KZ_433": {
                "freq_start": 433.075e6,
                "freq_end": 434.775e6,
                "duty_cycle": 100,
                "power_limit": 10,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "KZ_863": {
                "freq_start": 863.0e6,
                "freq_end": 868.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "NP_865": {
                "freq_start": 865.0e6,
                "freq_end": 868.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "BR_902": {
                "freq_start": 902.0e6,
                "freq_end": 907.5e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "ITU1_2M": {
                "freq_start": 144.0e6,
                "freq_end": 146.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "HAM_20KHZ",
                "default_preset": "TINY_FAST",
                "override_slot": 26
            },
            "ITU2_2M": {
                "freq_start": 144.0e6,
                "freq_end": 148.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "HAM_20KHZ",
                "default_preset": "TINY_FAST",
                "override_slot": 51
            },
            "ITU3_2M": {
                "freq_start": 144.0e6,
                "freq_end": 148.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "HAM_20KHZ",
                "default_preset": "TINY_FAST",
                "override_slot": 33
            },
            "ITU2_125CM": {
                "freq_start": 220.0e6,
                "freq_end": 225.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "HAM_100KHZ",
                "default_preset": "NARROW_SLOW",
                "override_slot": 37
            },
            "ITU1_70CM": {
                "freq_start": 430.0e6,
                "freq_end": 440.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "HAM_100KHZ",
                "default_preset": "NARROW_SLOW",
                "override_slot": 37
            },
            "ITU2_70CM": {
                "freq_start": 420.0e6,
                "freq_end": 450.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "HAM_100KHZ",
                "default_preset": "NARROW_SLOW",
                "override_slot": 137
            },
            "ITU3_70CM": {
                "freq_start": 430.0e6,
                "freq_end": 450.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "HAM_100KHZ",
                "default_preset": "NARROW_SLOW",
                "override_slot": 37
            },
            "LORA_24": {
                "freq_start": 2400.0e6,
                "freq_end": 2483.5e6,
                "duty_cycle": 100,
                "power_limit": 10,
                "frequency_switching": False,
                "wide_lora": True,
                "profile": "STD",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            },
            "UNSET": {
                "freq_start": 902.0e6,
                "freq_end": 928.0e6,
                "duty_cycle": 100,
                "power_limit": 30,
                "frequency_switching": False,
                "wide_lora": False,
                "profile": "UNDEF",
                "default_preset": "LONG_FAST",
                "override_slot": 0
            }
        }

        self.REGION = self.regions["US"]  # Select a different region here
        # Frequency slot, 1-based as in the firmware's loraConfig.channel_num. 0 means unset, which
        # takes the region's default slot the same way a device with no slot configured does.
        self.CHANNEL_NUM = 0

        self.GUI_ENABLED = True # whether to update/save the Tk/Matplotlib node-placement graph during CLI simulation
        self.PLOT = True # whether to plot the time schedule of packets after the simulation
        ### End of discrete-event specific ###

        ### PHY parameters (normally no change needed) ###
        self.PTX = self.REGION["power_limit"]

        # From firmware modemPresetToParams() in src/mesh/MeshRadio.h, at this file's pin. Sensitivity
        # is kTB + 6 dB NF at the SF's demod limit, CAD 3 dB below; bandwidth in Hz, not kHz.
        self.MODEM_PRESETS = {
            "SHORT_TURBO": {
                "bw": 500e3,
                "cr": 5,
                "sf": 7,
                "sensitivity": -118.5,
                "cad_threshold": -121.5
            },
            "SHORT_FAST": {
                "bw": 250e3,
                "cr": 5,
                "sf": 7,
                "sensitivity": -121.5,
                "cad_threshold": -124.5
            },
            "SHORT_SLOW": {
                "bw": 250e3,
                "cr": 5,
                "sf": 8,
                "sensitivity": -124.0,
                "cad_threshold": -127.0
            },
            "MEDIUM_FAST": {
                "bw": 250e3,
                "cr": 5,
                "sf": 9,
                "sensitivity": -126.5,
                "cad_threshold": -129.5
            },
            "MEDIUM_SLOW": {
                "bw": 250e3,
                "cr": 5,
                "sf": 10,
                "sensitivity": -129.0,
                "cad_threshold": -132.0
            },
            "LONG_TURBO": {
                "bw": 500e3,
                "cr": 8,
                "sf": 11,
                "sensitivity": -128.5,
                "cad_threshold": -131.5
            },
            "LONG_FAST": {
                "bw": 250e3,
                "cr": 5,
                "sf": 11,
                "sensitivity": -131.5,
                "cad_threshold": -134.5
            },
            "LONG_MODERATE": {
                "bw": 125e3,
                "cr": 8,
                "sf": 11,
                "sensitivity": -134.5,
                "cad_threshold": -137.5
            },
            "LONG_SLOW": {
                "bw": 125e3,
                "cr": 8,
                "sf": 12,
                "sensitivity": -137.0,
                "cad_threshold": -140.0
            },
            # Retired from the firmware; kept because archived runs used it.
            "VERY_LONG_SLOW": {
                "bw": 62.5e3,
                "sf": 12,
                "cr": 8,
                "sensitivity": -140.0,
                "cad_threshold": -143.0
            },
            "MEDIUM_TURBO": {
                "bw": 500e3,
                "cr": 5,
                "sf": 9,
                "sensitivity": -123.51,
                "cad_threshold": -126.51
            },
            # LITE_FAST is the EU_866 default; the LITE pair is that region's whole preset list.
            "LITE_FAST": {
                "bw": 125e3,
                "cr": 5,
                "sf": 9,
                "sensitivity": -129.53,
                "cad_threshold": -132.53
            },
            "LITE_SLOW": {
                "bw": 125e3,
                "cr": 5,
                "sf": 10,
                "sensitivity": -132.03,
                "cad_threshold": -135.03
            },
            # NARROW_SLOW is the EU_N_868 default and the ITU 100 kHz ham default.
            "NARROW_FAST": {
                "bw": 62.5e3,
                "cr": 6,
                "sf": 7,
                "sensitivity": -127.54,
                "cad_threshold": -130.54
            },
            "NARROW_SLOW": {
                "bw": 62.5e3,
                "cr": 6,
                "sf": 8,
                "sensitivity": -130.04,
                "cad_threshold": -133.04
            },
            # 15.6 kHz, for the ITU 20 kHz ham profile only.
            "TINY_FAST": {
                "bw": 15.6e3,
                "cr": 5,
                "sf": 7,
                "sensitivity": -133.57,
                "cad_threshold": -136.57
            },
            "TINY_SLOW": {
                "bw": 15.6e3,
                "cr": 6,
                "sf": 8,
                "sensitivity": -136.07,
                "cad_threshold": -139.07
            }
        }

        self.FREQ = self.frequency()
        self.HEADERLENGTH = 16  # number of Meshtastic header bytes
        self.ACKLENGTH = 2  # ACK payload in bytes
        # The *median* noise floor. A real one is not the thermal floor and does not hold still:
        # it is a distribution with a median well above kTB+NF and several decibels of spread,
        # varying by site and by hour. NOISE_SIGMA_DB gives it that spread, correlated over
        # NOISE_TAU_MSEC so the band drifts rather than flickering per packet, and clamped below by
        # kTB. Zero reproduces a constant floor exactly, which is the default so no existing result
        # moves until a scenario asks for the variation.
        #
        # None derives it from the preset's own bandwidth. It was one constant of -119.25 dBm for
        # bandwidths spanning 15.6 kHz to 500 kHz - a 15 dB range in thermal noise - and that
        # constant implies a 0.8 dB noise figure at 250 kHz, so it was a figure back-derived from
        # the sensitivity table rather than a band. A scenario that measured its own floor sets it
        # explicitly and overrides this.
        self._noise_level = None
        self.NOISE_SIGMA_DB = 0.0
        self.NOISE_TAU_MSEC = 60_000.0
        self.GAMMA = 2.08  # PHY parameter
        self.D0 = 40.0  # PHY parameter
        self.LPLD0 = 127.41  # PHY parameter
        # Optional calibration knobs; the defaults are plain simulator behaviour.
        # A packaged preset can tighten them - see docs/configuration.md.
        self.PATH_LOSS_DISTANCE_FLOOR_M = 0.001
        self.REPORTED_SNR_MIN_DB = None
        self.REPORTED_SNR_MAX_DB = None
        self.LINK_CALIBRATION_MODEL_ENABLED = False
        self.LINK_CALIBRATION_COEFFICIENTS = {}
        self.LINK_CALIBRATION_SNR_MIN_DB = None
        self.LINK_CALIBRATION_SNR_MAX_DB = None
        # How far the fit has support: past its longest observed link a linear model answers
        # confidently and wrongly, so beyond this the raw budget answers instead. None means no
        # envelope is known, which is not the same as the fit being valid everywhere.
        self.LINK_CALIBRATION_MAX_M = None
        self.NPREAM = 16   # number of preamble symbols from RadioInterface.h
        ### End of PHY parameters ###

        #################################################
        ####### TERRAIN OBSTRUCTION MODEL ###############
        #################################################
        # Off by default; TERRAIN_GRID holds a grid sampled from SRTM HGT tiles.
        self.TERRAIN_ENABLED = False
        self.TERRAIN_GRID = None
        # What Point.z means: height above local ground, or absolute altitude.
        self.NODE_Z_REFERENCE = "ground"
        self.GEO_ORIGIN_LAT = None
        self.GEO_ORIGIN_LON = None
        self.TERRAIN_PROFILE_SAMPLES = 24
        self.TERRAIN_FRESNEL_CLEARANCE = 0.6
        # The radio-planning 4/3 earth-radius approximation, as an earth-bulge term.
        self.TERRAIN_EFFECTIVE_EARTH_RADIUS_MULTIPLIER = 4.0 / 3.0
        self.TERRAIN_MIN_ANTENNA_HEIGHT_M = 1.5
        self.TERRAIN_MAX_LOSS_DB = 35.0

        #################################################
        ####### LAND-COVER CLUTTER MODEL ################
        #################################################
        # Excess loss from buildings and land use, separate from terrain: a hill can be
        # visible while low urban fabric still blocks the link. docs/configuration.md.
        self.CLUTTER_ENABLED = False
        self.CLUTTER_GRID_FILE = None
        self.CLUTTER_PROFILE_SAMPLES = 16
        self.CLUTTER_URBAN_LOSS_DB_PER_KM = 4.0
        self.CLUTTER_SUBURBAN_LOSS_DB_PER_KM = 2.0
        self.CLUTTER_FOREST_LOSS_DB_PER_KM = 2.5
        self.CLUTTER_OPEN_LOSS_DB_PER_KM = 0.2
        self.CLUTTER_WATER_LOSS_DB_PER_KM = 0.0
        self.CLUTTER_URBAN_ENDPOINT_LOSS_DB = 3.0
        self.CLUTTER_HIGH_VANTAGE_ELEVATION_M = 120.0
        self.CLUTTER_HIGH_VANTAGE_LOSS_FACTOR = 0.35
        self.CLUTTER_COASTAL_PATH_LOSS_FACTOR = 0.25
        self.CLUTTER_COASTAL_SAMPLE_FRACTION = 0.55
        self.CLUTTER_MAX_LOSS_DB = 25.0

        #################################################
        ####### EMPIRICAL PAYLOAD LOSS MODEL ############
        #################################################
        # Off by default. Sensitivity still gates whether a packet is heard at all;
        # this only adds a CR-dependent success probability after it.
        self.PHY_LOSS_MODEL_ENABLED = False
        self.PHY_LOSS_MODEL_NAME = "snr_payload_v1"
        # Where the payload-loss curve's half-way point sits, as an offset from the modem's own
        # demodulation limit for the spreading factor in use. It was an absolute SNR per coding
        # rate - -17.0 dB for 4/5 and so on - but a curve's position is set by the spreading
        # factor, which moves the limit by 12.5 dB across the presets, while the coding rate only
        # modulates it. So the curve sat 10 dB clear of the edge on SHORT_TURBO and right on it at
        # LONG_FAST: the model was nearly inert on the fast presets and severe on the slow ones,
        # and a preset sweep with --phy-loss-model measured that rather than the presets.
        #
        # These offsets reproduce the old absolute figures exactly at LONG_FAST, which is what they
        # were tuned on (SF11 needs -17.5 dB, so -17.0 is +0.5 dB above the limit).
        self.PHY_LOSS_P50_OFFSET_DB_BY_CR = {
            5: 0.5,
            6: -0.3,
            7: -1.1,
            8: -1.9,
        }
        self.PHY_LOSS_SNR_TRANSITION_DB = 1.4
        self.PHY_LOSS_REFERENCE_PACKET_BYTES = 40
        self.PHY_LOSS_LONG_PACKET_PENALTY_DB_PER_100B = 0.8
        self.PHY_LOSS_MIN_SUCCESS_PROB = 0.02
        self.PHY_LOSS_MAX_SUCCESS_PROB = 0.995

        # Misc
        self.SEED = 44  # random seed to use
        # End of misc

        # Initializers
        self.NR_NODES = None
        # End of initializers

        ############################
        ####### ROUTER TYPE ########
        ############################
        # Overridable by a batchSim scenario or loraMesh's second positional argument.
        self.SELECTED_ROUTER_TYPE = self.ROUTER_TYPE.MANAGED_FLOOD

        #####################################################
        ####### ASYMMETRIC LINK SIMULATION VARIABLES ########
        #####################################################
        # Shadowing on the path, reciprocal because the channel is, plus a per-node radio offset
        # per direction, which is where real link asymmetry comes from. A hearing B still does not
        # imply B hearing A, but for the reason it does in the field.
        self.MODEL_ASYMMETRIC_LINKS = True
        self.MODEL_SHADOWING_MEAN = 0
        # Measured log-normal shadowing in outdoor UHF links runs 6-10 dB. This was 2 dB applied
        # per direction, which made the mesh graph a near-perfect disc graph: the phenomena that
        # depend on connectivity being lucky - one long link holding two clusters together, an
        # isolated pocket, a route that works on Tuesday and not Wednesday - were absent by
        # construction, and every reach distribution came out narrower than the real thing. A
        # literature default, not a measurement of anywhere.
        self.MODEL_SHADOWING_STDDEV = 6
        # Transmit power tolerance, antenna variation and receiver noise figure, per node per
        # direction.
        self.MODEL_RADIO_ASYMMETRY_STDDEV = 2

        #################################################
        ####### MOVING NODE SIMULATION VARIABLES ########
        #################################################
        self.MOVEMENT_ENABLED = True
        # The average number of meters a human walks in a minute
        self.WALKING_METERS_PER_MIN = 96
        # The average number of meters a human bikes in a minute
        self.BIKING_METERS_PER_MIN = 390
        # The average number of meters a human drives in a minute
        self.DRIVING_METERS_PER_MIN = 1500
        # The % of nodes that end up mobile in the simulation 0.4 = ~40%
        self.APPROX_RATIO_NODES_MOVING = 0.3
        # The % of mobile nodes that have GPS enabled 0.5 = 50%
        self.APPROX_RATIO_OF_NODES_MOVING_W_GPS_ENABLED = 0.3

        # 100 meters
        self.SMART_POSITION_DISTANCE_THRESHOLD = 100
        # 30s minimum time in firmware
        self.SMART_POSITION_DISTANCE_MIN_TIME = 30 * self.ONE_SECOND_INTERVAL
        # This mirrors the firmware's approach to monitoring channel utilization: six 10 s buckets
        # of audible air for channel utilisation, sixty 1-minute buckets of our own transmissions
        # for the TX figure a duty cycle binds against. Two windows, as AirTime has.
        self.CHANNEL_UTILIZATION_PERIODS = 6
        self.UTILIZATION_TX_PERIODS = 60

        # AirTime::isTxAllowedChannelUtil, from src/airtime.h's hard-coded members. A device
        # declines to originate periodic traffic when the channel is this busy, and that gate is
        # the mesh's main self-regulation: without it a congestion sweep measures a network that
        # keeps offering the same load however busy the air gets. Relays and ACKs are not gated,
        # because the firmware puts the check in the modules that originate rather than in Router.
        self.CHANNEL_UTIL_TX_LIMIT_PERCENT = 40
        self.CHANNEL_UTIL_POLITE_TX_LIMIT_PERCENT = 25
        self.CHANNEL_UTIL_TX_GATE_ENABLED = True
        # PositionModule returns RUNONCE_INTERVAL when the gate is shut, so it retries on that
        # cadence. 5000 ms, from PositionModule.cpp.
        self.CHANNEL_UTIL_TX_RETRY_MSEC = 5000
        # Polite is the common case: PositionModule, DeviceTelemetry and the rest pass polite=true
        # for every role but TRACKER and SENSOR. NodeInfoModule is the impolite one.
        self.CHANNEL_UTIL_TX_GATE_POLITE = True

        # PacketHistory's capacity, from mesh-pb-constants.h: max(MAX_NUM_NODES * 2, 100), which is
        # 240 on the nRF52840 and generic ESP32 builds. It is bounded by size and evicts the oldest
        # slot; there is no time expiry, and the simulator kept an unbounded dict, so a node here
        # suppressed a duplicate of a message it heard an hour ago where a device would have
        # forgotten it.
        self.PACKET_HISTORY_MAX = 240

    @property
    def current_preset(self):
        """Returns the currently selected modem preset configuration"""
        return self.MODEM_PRESETS[self.MODEM_PRESET]

    @property
    def region_profile(self):
        """The preset list and regulatory parameters this region draws on."""
        return self.REGION_PROFILES[self.REGION["profile"]]

    def supports_preset(self, preset=None):
        return (preset or self.MODEM_PRESET) in self.region_profile["presets"]

    def freq_slot_width(self, preset=None):
        """Channel pitch: the occupied bandwidth plus this profile's padding and inter-slot gap."""
        profile = self.region_profile
        bw = self.MODEM_PRESETS[preset or self.MODEM_PRESET]["bw"]
        return profile["spacing"] + 2 * profile["padding"] + bw

    def num_freq_slots(self, preset=None):
        span = self.REGION["freq_end"] - self.REGION["freq_start"] + self.region_profile["spacing"]
        return int(round(span / self.freq_slot_width(preset)))

    def default_channel_num(self, preset=None):
        """The 0-based slot a device picks when the operator has not chosen one.

        A region override wins; otherwise it is the hash of the preset's display name.
        """
        preset = preset or self.MODEM_PRESET
        slots = self.num_freq_slots(preset)
        if slots <= 0:
            return 0
        override = self.REGION["override_slot"]
        if override > 0:
            return override - 1
        name = MODEM_PRESET_DISPLAY_NAMES.get(preset, "Invalid")
        return djb2_hash(name) % slots

    def frequency(self, channel_num=None, preset=None):
        """Centre frequency in Hz, from RadioInterface::applyModemConfig.

        `channel_num` is 1-based like the firmware's; 0 or None takes the region default.
        """
        preset = preset or self.MODEM_PRESET
        if not self.supports_preset(preset):
            raise ValueError(
                f"{preset} is not a legal preset in region {self.REGION['profile']}: "
                f"{', '.join(self.region_profile['presets'])}"
            )
        slots = self.num_freq_slots(preset)
        requested = self.CHANNEL_NUM if channel_num is None else channel_num
        if requested > slots:
            raise ValueError(
                f"channel number {requested} invalid for this region, max is {slots}"
            )
        slot = self.default_channel_num(preset) if requested == 0 else requested - 1
        profile = self.region_profile
        bw = self.MODEM_PRESETS[preset]["bw"]
        return (
            self.REGION["freq_start"]
            + bw / 2
            + profile["padding"]
            + slot * self.freq_slot_width(preset)
        )

    @property
    def NOISE_LEVEL(self):
        """Median noise floor in dBm: the scenario's own figure, or kTB+NF for this bandwidth.

        Deriving it keeps the SNR scale consistent across presets. With one constant, the SNR at
        each preset's own sensitivity ranged from +0.75 dB to -6.5 dB against the modem's actual
        requirement, so the payload-loss curve sat in a different place for every preset and a
        preset sweep with --phy-loss-model was confounded by it.
        """
        if self._noise_level is not None:
            return self._noise_level
        from lib.phy import thermal_noise_floor

        return thermal_noise_floor(self.current_preset["bw"])

    @NOISE_LEVEL.setter
    def NOISE_LEVEL(self, value):
        self._noise_level = None if value is None else float(value)

    @property
    def INTERFERENCE_LEVEL(self):
        """Probability the channel is already busy with non-Meshtastic traffic, in [0, 1]."""
        return self._interference_level

    @INTERFERENCE_LEVEL.setter
    def INTERFERENCE_LEVEL(self, value):
        value = float(value)
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"INTERFERENCE_LEVEL must be a probability in [0, 1], got {value}")
        self._interference_level = value

    # Function that needs to be run to ensure the router dependent variables change appropriately
    def update_router_dependencies(self):
        # A new router type overrides its dependent values here - hop limit, say - by
        # testing self.SELECTED_ROUTER_TYPE and assigning them.
        return

# single module-level config for all users to reference unambiguously
CONFIG = Config()
