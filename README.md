Serval_signal_maps_generator
============================

Takes .trace files containing Serval Mesh Extender signal information and plot them as maps with Google Maps API v3. Uses Python, Bash, Jekyll, and Twitter Bootstrap.

How-to
======

1. Add your .trace files to the traces/ folder
2. Edit the generator.py *address_list_full* array to add your traces using [["Title", center latitude, center longitude, "path_to_file"],[..],..]
3. chmod +x generate_website.sh
4. ./generate_website.sh
