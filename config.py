# RFM69 Config Dictionary
#
# Ported to Micropython 2016 Ara Kourchians
#
# C code Author: Phil Crump (phildcrump@gmail.com)
# Copyright (C) 2014 Phil Crump
# Based on RF22.h
# Author: Mike McCauley (mikem@open.com.au)
# Copyright (C) 2011 Mike McCauley
from registers import registers

config = {
    "RFM69_REG_01_OPMODE" :      registers["RF_OPMODE_SEQUENCER_ON"] | registers["RF_OPMODE_LISTEN_OFF"] | registers["RFM69_MODE_RX"],
    "RFM69_REG_02_DATA_MODUL" :  registers["RF_DATAMODUL_DATAMODE_PACKET"] | registers["RF_DATAMODUL_MODULATIONTYPE_FSK"] | registers["RF_DATAMODUL_MODULATIONSHAPING_00"],
    "RFM69_REG_03_BITRATE_MSB" : 0x3E, #0x1A, # 2000 bps
    "RFM69_REG_04_BITRATE_LSB" : 0x80, #0x0B,
    "RFM69_REG_05_FDEV_MSB" :    0x00, # 12000 hz (24000 hz shift)
    "RFM69_REG_06_FDEV_LSB" :    0xC5, #0x52,
    "RFM69_REG_07_FRF_MSB" :     0x6C, #0xD9, # 869.5 MHz
    "RFM69_REG_08_FRF_MID" :     0x80, #0x60, # calculated: 0x80?
    "RFM69_REG_09_FRF_LSB" :     0x00, #0x12,
    "RFM69_REG_0B_AFC_CTRL" :    registers["RF_AFCLOWBETA_OFF"], # AFC Offset On
    "RFM69_REG_11_PA_LEVEL" : registers["RF_PALEVEL_PA0_OFF"] | registers["RF_PALEVEL_PA1_ON"] | registers["RF_PALEVEL_PA2_ON"] | 0x1f, # 50mW
    "RFM69_REG_12_PA_RAMP" : registers["RF_PARAMP_500"], # 500us PA ramp-up (1 bit)
    "RFM69_REG_13_OCP" :         registers["RF_OCP_ON"] | registers["RF_OCP_TRIM_95"],
    "RFM69_REG_18_LNA" :         registers["RF_LNA_ZIN_50"], # 50 ohm for matched antenna, 200 otherwise
    "RFM69_REG_19_RX_BW" :       registers["RF_RXBW_DCCFREQ_010"] | registers["RF_RXBW_MANT_16"] | registers["RF_RXBW_EXP_2"], # Rx Bandwidth: 128KHz
    "RFM69_REG_1E_AFC_FEI" :     registers["RF_AFCFEI_AFCAUTO_ON"] | registers["RF_AFCFEI_AFCAUTOCLEAR_ON"], # Automatic AFC on, clear after each packet
    "RFM69_REG_25_DIO_MAPPING1" : registers["RF_DIOMAPPING1_DIO0_01"],
    "RFM69_REG_26_DIO_MAPPING2" : registers["RF_DIOMAPPING2_CLKOUT_OFF"], # Switch off Clkout
    "RFM69_REG_2E_SYNC_CONFIG" : registers["RF_SYNC_ON"] | registers["RF_SYNC_FIFOFILL_AUTO"] | registers["RF_SYNC_SIZE_2"] | registers["RF_SYNC_TOL_0"],
    "RFM69_REG_2F_SYNCVALUE1" : 0x2D,
    "RFM69_REG_30_SYNCVALUE2" : 0xAA,
    "RFM69_REG_24_RSSI_VALUE" : 200,
    "RFM69_REG_37_PACKET_CONFIG1" : registers["RF_PACKET1_FORMAT_VARIABLE"] | registers["RF_PACKET1_DCFREE_OFF"] | registers["RF_PACKET1_CRC_ON"] | registers["RF_PACKET1_CRCAUTOCLEAR_ON"] | registers["RF_PACKET1_ADRSFILTERING_OFF"],
    "RFM69_REG_38_PAYLOAD_LENGTH" : registers["RFM69_FIFO_SIZE"], # Full FIFO size for rx packet
    "RFM69_REG_3C_FIFO_THRESHOLD" : registers["RF_FIFOTHRESH_TXSTART_FIFONOTEMPTY"] | 0x05, #TX on FIFO not empty
    "RFM69_REG_3D_PACKET_CONFIG2" : registers["RF_PACKET2_RXRESTARTDELAY_2BITS"] | registers["RF_PACKET2_AUTORXRESTART_ON"] | registers["RF_PACKET2_AES_OFF"], #RXRESTARTDELAY must match transmitter PA ramp-down time (bitrate dependent)
    "RFM69_REG_6F_TEST_DAGC" : registers["RF_DAGC_IMPROVED_LOWBETA0"] # run DAGC continuously in RX mode, recommended default for AfcLowBetaOn=0
}
