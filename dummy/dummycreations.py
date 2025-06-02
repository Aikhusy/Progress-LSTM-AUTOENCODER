import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed untuk reproducibility
np.random.seed(42)
random.seed(42)

def generate_system_monitoring_data(n_samples=1000, anomaly_ratio=0.05):
    """
    Generate synthetic system monitoring data with realistic patterns and anomalies
    """
    
    # Base timestamp
    start_time = datetime(2024, 11, 6, 8, 0, 0)
    
    data = []
    anomaly_indices = set(np.random.choice(n_samples, int(n_samples * anomaly_ratio), replace=False))
    
    for i in range(n_samples):
        # Time progression (irregular intervals like real monitoring)
        time_offset = timedelta(
            seconds=random.randint(10, 300),  # 10 seconds to 5 minutes
            microseconds=random.randint(0, 999999)
        )
        current_time = start_time + timedelta(seconds=i * 45) + time_offset
        
        is_anomaly = i in anomaly_indices
        
        if is_anomaly:
            # Generate anomalous data
            row = generate_anomaly_row(current_time)
        else:
            # Generate normal data
            row = generate_normal_row(current_time)
        
        data.append(row)
    
    return pd.DataFrame(data)

def generate_normal_row(timestamp):
    """Generate normal system metrics"""
    
    # Normal load averages (typically 0.0 - 0.8)
    fw_load_avg_1_min = round(np.random.normal(0.2, 0.15), 2)
    fw_load_avg_5_min = round(np.random.normal(0.22, 0.12), 2)
    fw_load_avg_15_min = round(np.random.normal(0.20, 0.10), 2)
    
    # Ensure load averages are non-negative
    fw_load_avg_1_min = max(0, fw_load_avg_1_min)
    fw_load_avg_5_min = max(0, fw_load_avg_5_min)
    fw_load_avg_15_min = max(0, fw_load_avg_15_min)
    
    # CPU usage (0-2% normal)
    fw_cpu_used = random.choice([0, 0, 0, 0, 1, 1, 2])  # Mostly 0, sometimes 1-2
    
    # Memory usage (around 7.9M with small variation)
    mem_used = int(np.random.normal(7914000, 5000))
    
    # Root filesystem usage (around 10.09M)
    root_used = int(np.random.normal(10093250, 100))
    
    # Log usage (around 10.3M with gradual increase)
    log_used = int(np.random.normal(10310000, 2000))
    
    # Firewall total allocation (around 647M)
    fw_total_alloc = int(np.random.normal(647000000, 500000))
    
    # Network packets (gradual increase over time)
    base_rx = 19100000
    base_tx = 1823000
    
    total_rx_packets = base_rx + random.randint(0, 50000)
    total_tx_packets = base_tx + random.randint(0, 1000)
    
    return {
        'fw_load_avg_1_min': f"{fw_load_avg_1_min:.2f}".replace('.', ','),
        'fw_load_avg_5_min': f"{fw_load_avg_5_min:.2f}".replace('.', ','),
        'fw_load_avg_15_min': f"{fw_load_avg_15_min:.2f}".replace('.', ','),
        'fw_cpu_used': fw_cpu_used,
        'mem_used': mem_used,
        'root_used': root_used,
        'log_used': log_used,
        'fw_total_alloc': fw_total_alloc,
        'total_rx_packets': total_rx_packets,
        'total_tx_packets': total_tx_packets,
        'created_at': timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    }

def generate_anomaly_row(timestamp):
    """Generate anomalous system metrics"""
    
    anomaly_type = random.choice([
        'high_load', 'high_cpu', 'memory_spike', 'disk_spike', 
        'network_spike', 'system_stress', 'resource_leak'
    ])
    
    if anomaly_type == 'high_load':
        # Abnormally high load averages
        fw_load_avg_1_min = round(np.random.uniform(2.0, 8.0), 2)
        fw_load_avg_5_min = round(np.random.uniform(1.5, 4.0), 2)
        fw_load_avg_15_min = round(np.random.uniform(1.0, 2.5), 2)
        fw_cpu_used = random.randint(50, 95)
        mem_used = int(np.random.normal(7914000, 5000))
        root_used = int(np.random.normal(10093250, 100))
        log_used = int(np.random.normal(10310000, 2000))
        fw_total_alloc = int(np.random.normal(647000000, 500000))
        total_rx_packets = 19100000 + random.randint(0, 50000)
        total_tx_packets = 1823000 + random.randint(0, 1000)
        
    elif anomaly_type == 'high_cpu':
        # Normal load but very high CPU
        fw_load_avg_1_min = round(np.random.normal(0.3, 0.1), 2)
        fw_load_avg_5_min = round(np.random.normal(0.25, 0.1), 2)
        fw_load_avg_15_min = round(np.random.normal(0.22, 0.08), 2)
        fw_cpu_used = random.randint(80, 100)
        mem_used = int(np.random.normal(7914000, 5000))
        root_used = int(np.random.normal(10093250, 100))
        log_used = int(np.random.normal(10310000, 2000))
        fw_total_alloc = int(np.random.normal(647000000, 500000))
        total_rx_packets = 19100000 + random.randint(0, 50000)
        total_tx_packets = 1823000 + random.randint(0, 1000)
        
    elif anomaly_type == 'memory_spike':
        # Memory usage spike
        fw_load_avg_1_min = round(np.random.normal(0.4, 0.2), 2)
        fw_load_avg_5_min = round(np.random.normal(0.35, 0.15), 2)
        fw_load_avg_15_min = round(np.random.normal(0.25, 0.1), 2)
        fw_cpu_used = random.randint(5, 25)
        mem_used = int(np.random.uniform(15000000, 25000000))  # 2-3x normal
        root_used = int(np.random.normal(10093250, 100))
        log_used = int(np.random.normal(10310000, 2000))
        fw_total_alloc = int(np.random.normal(647000000, 500000))
        total_rx_packets = 19100000 + random.randint(0, 50000)
        total_tx_packets = 1823000 + random.randint(0, 1000)
        
    elif anomaly_type == 'disk_spike':
        # Disk usage anomaly
        fw_load_avg_1_min = round(np.random.normal(0.8, 0.3), 2)
        fw_load_avg_5_min = round(np.random.normal(0.6, 0.2), 2)
        fw_load_avg_15_min = round(np.random.normal(0.4, 0.15), 2)
        fw_cpu_used = random.randint(15, 40)
        mem_used = int(np.random.normal(7914000, 5000))
        root_used = int(np.random.uniform(15000000, 20000000))  # Disk full
        log_used = int(np.random.uniform(20000000, 30000000))   # Log explosion
        fw_total_alloc = int(np.random.normal(647000000, 500000))
        total_rx_packets = 19100000 + random.randint(0, 50000)
        total_tx_packets = 1823000 + random.randint(0, 1000)
        
    elif anomaly_type == 'network_spike':
        # Network traffic anomaly
        fw_load_avg_1_min = round(np.random.normal(0.6, 0.2), 2)
        fw_load_avg_5_min = round(np.random.normal(0.5, 0.15), 2)
        fw_load_avg_15_min = round(np.random.normal(0.3, 0.1), 2)
        fw_cpu_used = random.randint(10, 30)
        mem_used = int(np.random.normal(8500000, 200000))
        root_used = int(np.random.normal(10093250, 100))
        log_used = int(np.random.normal(10310000, 2000))
        fw_total_alloc = int(np.random.uniform(800000000, 1200000000))  # High allocation
        total_rx_packets = random.randint(25000000, 40000000)  # Traffic spike
        total_tx_packets = random.randint(2500000, 4000000)
        
    elif anomaly_type == 'system_stress':
        # Overall system stress
        fw_load_avg_1_min = round(np.random.uniform(3.0, 6.0), 2)
        fw_load_avg_5_min = round(np.random.uniform(2.0, 4.0), 2)
        fw_load_avg_15_min = round(np.random.uniform(1.5, 3.0), 2)
        fw_cpu_used = random.randint(70, 95)
        mem_used = int(np.random.uniform(12000000, 18000000))
        root_used = int(np.random.uniform(12000000, 15000000))
        log_used = int(np.random.uniform(15000000, 25000000))
        fw_total_alloc = int(np.random.uniform(750000000, 950000000))
        total_rx_packets = random.randint(22000000, 35000000)
        total_tx_packets = random.randint(2200000, 3500000)
        
    else:  # resource_leak
        # Gradual resource leak pattern
        fw_load_avg_1_min = round(np.random.uniform(1.0, 2.5), 2)
        fw_load_avg_5_min = round(np.random.uniform(1.2, 2.8), 2)
        fw_load_avg_15_min = round(np.random.uniform(1.5, 3.2), 2)
        fw_cpu_used = random.randint(25, 60)
        mem_used = int(np.random.uniform(10000000, 14000000))
        root_used = int(np.random.normal(10093250, 100))
        log_used = int(np.random.normal(10310000, 2000))
        fw_total_alloc = int(np.random.uniform(680000000, 750000000))
        total_rx_packets = 19100000 + random.randint(0, 50000)
        total_tx_packets = 1823000 + random.randint(0, 1000)
    
    # Ensure non-negative values
    fw_load_avg_1_min = max(0, fw_load_avg_1_min)
    fw_load_avg_5_min = max(0, fw_load_avg_5_min)
    fw_load_avg_15_min = max(0, fw_load_avg_15_min)
    
    return {
        'fw_load_avg_1_min': f"{fw_load_avg_1_min:.2f}".replace('.', ','),
        'fw_load_avg_5_min': f"{fw_load_avg_5_min:.2f}".replace('.', ','),
        'fw_load_avg_15_min': f"{fw_load_avg_15_min:.2f}".replace('.', ','),
        'fw_cpu_used': fw_cpu_used,
        'mem_used': mem_used,
        'root_used': root_used,
        'log_used': log_used,
        'fw_total_alloc': fw_total_alloc,
        'total_rx_packets': total_rx_packets,
        'total_tx_packets': total_tx_packets,
        'created_at': timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    }

# Generate the dataset
print("🚀 Generating 1000 system monitoring records with ~5% anomalies...")
df = generate_system_monitoring_data(n_samples=1000, anomaly_ratio=0.05)

# Save to CSV with semicolon separator (like your original data)
output_file = 'system_monitoring_data_with_anomalies.csv'
df.to_csv(output_file, sep=';', index=False)

print(f"✅ Dataset generated successfully!")
print(f"📁 Saved as: {output_file}")
print(f"📊 Dataset shape: {df.shape}")
print(f"🎯 Anomalies: ~{int(1000 * 0.05)} records")

# Display sample data
print("\n📋 Sample of generated data:")
print(df.head(10).to_string(index=False))

print("\n🔍 Data statistics:")
print(f"Date range: {df['created_at'].min()} to {df['created_at'].max()}")
print(f"Load avg 1min range: {df['fw_load_avg_1_min'].min()} to {df['fw_load_avg_1_min'].max()}")
print(f"CPU usage range: {df['fw_cpu_used'].min()} to {df['fw_cpu_used'].max()}")
print(f"Memory usage range: {df['mem_used'].min():,} to {df['mem_used'].max():,}")

print("\n💡 Anomaly types included:")
print("• High load averages (system overload)")
print("• High CPU usage (processing spikes)")  
print("• Memory spikes (memory leaks)")
print("• Disk usage spikes (storage issues)")
print("• Network traffic spikes (DDoS/high traffic)")
print("• Overall system stress (multiple resources)")
print("• Resource leak patterns (gradual degradation)")