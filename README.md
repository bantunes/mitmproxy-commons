# mitmproxy-commons

Some sammple addons  for [mitmproxy](https://github.com/mitmproxy/mitmproxy).

## CustomDNSResolver

A simplistic dns resolver that allows mapping and address to specifig address

Adjust hosts in variable  `host_mappings` in init method

Excute the addon passing argument `-s CustomDNSResolver.py` to mitmproxy
Exemple: `mitmtweb -mode dns -s -s CustomDNSResolver.py`



