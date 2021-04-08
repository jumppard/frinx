def get_extraxted_data_from_bdi(bdis):
    # todo, not necessary for now ...
    pass


def get_extraxted_data_from_loopback(loopbacks):
    # todo, not necessary for now ...
    pass


def get_extracted_data_from_port_channel(port_channels):
    result = []
    flag = 'Port-channel'
    for item in port_channels:
        name = flag + str(item['name'])
        description = item['description'] if 'description' in item else None  # description is optional
        max_frame_size = int(item['mtu']) if 'mtu' in item else None  # max_frame_size is optional
        config = item
        port_channel_id = None
        result.append({'name': name, 'description': description, 'max_frame_size': max_frame_size, 'config': config, 'port_channel_id': port_channel_id})

    return result


def get_extraxted_data_from_ten_gigabit_ethernet(ten_gigabit_ethernets):
    result = []
    flag = 'TenGigabitEthernet'
    for item in ten_gigabit_ethernets:
        name = flag + str(item['name'])
        description = item['description'] if 'description' in item else None  # description is optional
        max_frame_size = int(item['mtu']) if 'mtu' in item else None  # max_frame_size is optional
        config = item
        port_channel_id = item['Cisco-IOS-XE-ethernet:channel-group']['number'] if (('Cisco-IOS-XE-ethernet:channel-group' in item) and ('number' in item['Cisco-IOS-XE-ethernet:channel-group'])) else None  # port_channel_id is optional
        result.append({'name': name, 'description': description, 'max_frame_size': max_frame_size, 'config': config,
                       'port_channel_id': port_channel_id})

    return result


def get_extraxted_data_from_gigabit_ethernet(gigabit_ethernets):
    result = []
    flag = 'GigabitEthernet'
    for item in gigabit_ethernets:
        name = flag + str(item['name'])
        description = item['description'] if 'description' in item else None  # description is optional
        max_frame_size = int(item['mtu']) if 'mtu' in item else None  # max_frame_size is optional
        config = item
        port_channel_id = item['Cisco-IOS-XE-ethernet:channel-group']['number'] if (('Cisco-IOS-XE-ethernet:channel-group' in item) and ('number' in item['Cisco-IOS-XE-ethernet:channel-group'])) else None  # port_channel_id is optional
        result.append({'name': name, 'description': description, 'max_frame_size': max_frame_size, 'config': config,
                       'port_channel_id': port_channel_id})

    return result
