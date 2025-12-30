<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python"> <img src="https://img.shields.io/badge/First%20Project-Yes!-green?style=for-the-badge" alt="First Project"> <img src="https://img.shields.io/badge/Status-Under%20Development-orange?style=for-the-badge" alt="Status"> </p>

## About
Wifirat is my first try on developing ethical-hacking tools

This proyect is focused on improving my Python skills through practical, hands-on implementation

Also to get a deeper understanding of penetration testing tools, network security, and proyect developing

⚠️ IMPORTANT: This tool is for _**EDUCATIONAL PURPOSES ONLY**_. **Only use on networks you own or have explicit permission to test.**


## TREE STRUCTURE
I know it might be too much but this is what i would like to have in my proyect:

wifipentest-toolkit/
│
├── core/
│   ├── __init__.py
│   ├── base_tool.py          # Base class for all tools
│   ├── interface_manager.py  # Handle network interfaces
│   └── logger.py            # Custom logging system
│
├── attacks/
│   ├── __init__.py
│   ├── common/              # Tools used by both WEP and WPA2
│   │   ├── __init__.py
│   │   ├── scanner.py      # AP/Client discovery
│   │   ├── monitor.py      # Monitor mode operations
│   │   ├── sniffer.py      # Packet capture/sniffing
│   │   └── deauth.py       # Deauthentication attacks
│   │
│   ├── wep/                 # WEP-specific attacks
│   │   ├── __init__.py
│   │   ├── arp_replay.py   # ARP request replay attack
│   │   ├── chopchop.py     # Chop-chop attack
│   │   ├── fragmentation.py # Fragmentation attack
│   │   ├── p0841.py        # P0841 attack
│   │   └── wep_cracker.py  # WEP cracking (aircrack-ng)
│   │
│   ├── wpa/                 # WPA/WPA2-specific attacks
│   │   ├── __init__.py
│   │   ├── handshake.py    # WPA handshake capture
│   │   ├── pmkid.py        # PMKID attack
│   │   ├── wps.py          # WPS attacks (Pixie Dust, Reaver)
│   │   └── wpa_cracker.py  # WPA cracking (hashcat, john)
│   │
│   └── reconnaissance/      # Reconnaissance tools
│       ├── __init__.py
│       ├── wardriving.py   # GPS-based wardriving
│       ├── kismet.py       # Kismet integration
│       └── recon.py        # General reconnaissance
│
├── post_exploitation/
│   ├── __init__.py
│   ├── ettercap.py         # ARP poisoning, MITM
│   ├── sslstrip.py         # SSL stripping attacks
│   ├── dns_spoof.py        # DNS spoofing
│   ├── credential_sniffer.py # Credential harvesting
│   ├── rogue_ap.py         # Evil Twin/rogue AP
│   └── packet_injection.py # Custom packet injection
│
├── cracking/
│   ├── __init__.py
│   ├── wordlist_manager.py # Wordlist management/generation
│   ├── hashcat_wrapper.py  # Hashcat integration
│   ├── aircrack_wrapper.py # Aircrack-ng integration
│   ├── john_wrapper.py     # John the Ripper integration
│   └── rainbow_table.py    # Rainbow table utilities
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py          # Common utilities
│   ├── validator.py        # Input validation
│   ├── output_formatter.py # Pretty output/display
│   ├── network_utils.py    # Network utilities
│   └── encryption_utils.py # Encryption/decryption helpers
│
├── config/
│   ├── __init__.py
│   ├── settings.py         # Configuration constants
│   ├── colors.py           # ANSI color codes
│   └── presets.py          # Attack presets/configs
│
├── tests/
│   ├── test_attacks/
│   ├── test_post_exploit/
│   └── test_utils.py
│
├── data/
│   ├── wordlists/
│   ├── captures/
│   ├── hashes/
│   └── logs/
│
├── reports/
│   ├── templates/
│   └── generator.py        # Report generation (PDF/HTML)
│
├── requirements.txt
├── setup.py
├── main.py                 # Main CLI interface
└── README.md
