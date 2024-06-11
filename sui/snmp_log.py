import time

from pysnmp.hlapi import (
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    getCmd,
)

def fetch_snmp_data(target, community, port, oid):
    # Fetch SNMP data from the target device
    iterator = getCmd(
        SnmpEngine(),  # SNMP engine
        CommunityData(community),  # Community data for authentication
        UdpTransportTarget((target, port)),  # Target device address and port
        ContextData(),  # Context data
        ObjectType(ObjectIdentity(oid)),  # Object type to fetch
    )
    errorIndication, errorStatus, varBinds = next(iterator)
    if errorIndication:
        print(f"Error: {errorIndication}")
        return None
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()}")
        return None
    else:
        for varBind in varBinds:
            return f"{varBind[0]} = {varBind[1]}"

def log_snmp_data(runtime, log_interval):
    # Log SNMP data for a specific runtime, creating a new log file every interval
    start_time = time.time()
    end_time = start_time + runtime
    log_file_index = 1
    log_file_name = f"snmp_logs_{log_file_index}.txt"
    while time.time() < end_time:
        current_time = time.time()
        if current_time - start_time >= log_interval * 60:
            log_file_index += 1
            log_file_name = f"snmp_logs_{log_file_index}.txt"
            start_time = current_time
        with open(log_file_name, "a") as file: 
            
            snmp_data = fetch_snmp_data(snmp_target, community_string, snmp_port, oid)
            if snmp_data:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                file.write(f"{timestamp} - {snmp_data}\n")
                file.flush()
        time.sleep(1)

if __name__ == "__main__":
    # Configuration
    snmp_target = "192.168.1.1"  # SNMP target device IP address
    community_string = "public"  # SNMP community string for authentication
    snmp_port = 161  # SNMP port number
    oid = "1.3.6.1.2.1.2.2.1.16"  # SNMP object identifier
    runtime = 3600  # 1 hour in seconds
    log_interval = 1  # 1 minutes

    # Start logging SNMP data
    log_snmp_data(runtime, log_interval)
